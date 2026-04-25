import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path


FORBIDDEN_PATTERNS = ("TO" + "DO", "T" + "BD", "FIX" + "ME")
REQUIRED_FILES = (
    "SKILL.md",
    "skill-manifest.json",
    "VERSION",
    "CHANGELOG.md",
    "agents/openai.yaml",
    ".github/CODEOWNERS",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/dependabot.yml",
    ".github/workflows/skill-ci.yml",
    ".github/workflows/codeql.yml",
    ".github/workflows/release.yml",
    ".github/rulesets/main-protection.json",
    ".github/repository-settings.md",
    "templates/task-brief.md",
    "templates/agent-turn-result.md",
    "templates/specialist-context-packet.md",
)
SKIP_DIRS = {".git", ".superpowers", "__pycache__"}
DISALLOWED_RUNTIME_DIRS = (
    "docs",
    "evidence",
)
RUNTIME_OUTPUT_PARTS = {
    "handoffs",
    "reviews",
    "decisions",
    "archive",
    "evidence",
    "screenshots",
    "recordings",
    "logs",
    "test-results",
}
RUNTIME_OUTPUT_FILENAMES = {
    "project-memory.md",
}


@dataclass
class ValidationResult:
    errors: list = field(default_factory=list)
    checked: list = field(default_factory=list)

    @property
    def ok(self):
        return not self.errors


def iter_text_files(repo):
    for path in repo.rglob("*"):
        if path.is_dir():
            continue
        if set(path.relative_to(repo).parts) & SKIP_DIRS:
            continue
        if path.suffix.lower() in {".pyc", ".pyo"}:
            continue
        yield path


def check_utf8(repo, result):
    for path in iter_text_files(repo):
        try:
            path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            result.errors.append(f"Non-UTF-8 file: {path.relative_to(repo)} ({exc})")


def parse_frontmatter(text):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    return text[4:end].strip()


def check_frontmatter(repo, result):
    skill = repo / "SKILL.md"
    if not skill.exists():
        result.errors.append("Missing SKILL.md")
        return
    result.checked.append("SKILL.md")
    text = skill.read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(text)
    if not frontmatter:
        result.errors.append("SKILL.md missing YAML frontmatter")
        return
    if not re.search(r"^name:\s*agent-collaboration-os\s*$", frontmatter, re.M):
        result.errors.append("SKILL.md frontmatter missing expected name")
    if not re.search(r"^description:\s*.+", frontmatter, re.M):
        result.errors.append("SKILL.md frontmatter missing description")


def check_required_files(repo, result):
    for relative in REQUIRED_FILES:
        result.checked.append(relative)
        if not (repo / relative).exists():
            result.errors.append(f"Missing required file: {relative}")


def check_skill_manifest(repo, result):
    path = repo / "skill-manifest.json"
    result.checked.append("skill-manifest.json")
    if not path.exists():
        return
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        result.errors.append(f"Invalid skill-manifest.json: {exc}")
        return

    version_path = repo / "VERSION"
    if not version_path.exists():
        return
    version = version_path.read_text(encoding="utf-8").strip()
    if manifest.get("version") != version:
        result.errors.append("skill-manifest.json version does not match VERSION")

    for key in ("protocols", "tools", "github_templates"):
        for item in manifest.get(key, []):
            result.checked.append(f"manifest:{item}")
            if not (repo / item).exists():
                result.errors.append(f"skill-manifest.json references missing item: {item}")


def check_no_runtime_outputs(repo, result):
    for directory in DISALLOWED_RUNTIME_DIRS:
        path = repo / directory
        result.checked.append(f"no-runtime:{directory}")
        if path.exists():
            result.errors.append(
                f"Runtime output directory must not live in skill repository: {directory}"
            )
    for path in iter_text_files(repo):
        relative = path.relative_to(repo)
        parts = {part.lower() for part in relative.parts}
        name = relative.name.lower()
        if parts & RUNTIME_OUTPUT_PARTS or name in RUNTIME_OUTPUT_FILENAMES:
            if relative.parts[0] not in {".git", ".superpowers"}:
                result.errors.append(
                    f"Runtime output path must not live in skill repository: {relative.as_posix()}"
                )


def check_reference_links(repo, result):
    skill = repo / "SKILL.md"
    if not skill.exists():
        return
    text = skill.read_text(encoding="utf-8")
    refs = re.findall(r"references/[A-Za-z0-9_.-]+\.md", text)
    for ref in refs:
        result.checked.append(ref)
        if not (repo / ref).exists():
            result.errors.append(f"Missing referenced protocol: {ref}")


def check_protocol_routing(repo, result):
    routing = repo / "references" / "protocol-routing.md"
    if not routing.exists():
        result.errors.append("Missing references/protocol-routing.md")
        return
    result.checked.append("references/protocol-routing.md")
    text = routing.read_text(encoding="utf-8")
    refs = re.findall(r"`([A-Za-z0-9_.-]+\.md)`", text)
    for ref in refs:
        result.checked.append(f"routing:{ref}")
        if not (repo / "references" / ref).exists():
            result.errors.append(f"Protocol routing references missing file: {ref}")


def check_evals(repo, result):
    eval_dir = repo / "evals"
    if not eval_dir.exists():
        result.errors.append("Missing evals directory")
        return
    for eval_file in sorted(eval_dir.glob("*.json")):
        result.checked.append(str(eval_file.relative_to(repo)))
        try:
            data = json.loads(eval_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            result.errors.append(f"Invalid eval JSON {eval_file.relative_to(repo)}: {exc}")
            continue
        for key in ("name", "prompt", "expected_protocols", "expected_outputs", "must_not"):
            if key not in data:
                result.errors.append(f"Eval {eval_file.relative_to(repo)} missing key: {key}")
        for protocol in data.get("expected_protocols", []):
            result.checked.append(f"eval:{protocol}")
            if not (repo / "references" / protocol).exists():
                result.errors.append(
                    f"Eval {eval_file.relative_to(repo)} references missing protocol: {protocol}"
                )
        protocol_text = ""
        for protocol in data.get("expected_protocols", []):
            path = repo / "references" / protocol
            if path.exists():
                protocol_text += "\n" + path.read_text(encoding="utf-8")
        for output in data.get("expected_outputs", []):
            result.checked.append(f"eval-output:{output}")
            pattern = rf"^#+\s+{re.escape(output)}\s*$"
            if not re.search(pattern, protocol_text, re.MULTILINE) and output not in protocol_text:
                result.errors.append(
                    f"Eval {eval_file.relative_to(repo)} expects undefined output: {output}"
                )


def check_forbidden_placeholders(repo, result):
    for path in iter_text_files(repo):
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in FORBIDDEN_PATTERNS:
            if pattern.lower() in text.lower():
                result.errors.append(f"Forbidden placeholder {pattern} in {path.relative_to(repo)}")


def check_pycache_not_tracked(repo, result):
    completed = subprocess.run(
        ["git", "ls-files"],
        cwd=repo,
        text=True,
        capture_output=True,
        check=False,
    )
    if completed.returncode != 0:
        return
    for line in completed.stdout.splitlines():
        if "__pycache__" in line or line.endswith((".pyc", ".pyo")):
            result.errors.append(f"Tracked Python cache file: {line}")


def check_codeowners(repo, result):
    path = repo / ".github" / "CODEOWNERS"
    result.checked.append(".github/CODEOWNERS owners")
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    forbidden = (
        "@main-agent-owner",
        "@development-agent-owner",
        "@testing-agent-owner",
        "@OWNER_REPLACE_ME",
    )
    for item in forbidden:
        if item in text:
            result.errors.append(f"CODEOWNERS contains placeholder owner: {item}")


def check_github_governance(repo, result):
    skill_ci = repo / ".github" / "workflows" / "skill-ci.yml"
    if skill_ci.exists():
        text = skill_ci.read_text(encoding="utf-8")
        required = (
            "python -m unittest discover tests",
            "python scripts/validate_skill_repo.py",
            "python scripts/install_skill.py --dry-run",
        )
        for command in required:
            result.checked.append(f"github-ci:{command}")
            if command not in text:
                result.errors.append(f"Skill CI missing required command: {command}")

    codeql = repo / ".github" / "workflows" / "codeql.yml"
    if codeql.exists():
        text = codeql.read_text(encoding="utf-8")
        for needle in ("github/codeql-action/init@v3", "github/codeql-action/analyze@v3", "languages: python"):
            result.checked.append(f"codeql:{needle}")
            if needle not in text:
                result.errors.append(f"CodeQL workflow missing required entry: {needle}")

    release = repo / ".github" / "workflows" / "release.yml"
    if release.exists():
        text = release.read_text(encoding="utf-8")
        for needle in ('test "${GITHUB_REF_NAME}" = "v${VERSION_VALUE}"', 'grep -q "## ${VERSION_VALUE} " CHANGELOG.md'):
            result.checked.append(f"release:{needle}")
            if needle not in text:
                result.errors.append(f"Release workflow missing version gate: {needle}")

    ruleset = repo / ".github" / "rulesets" / "main-protection.json"
    if ruleset.exists():
        try:
            data = json.loads(ruleset.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            result.errors.append(f"Invalid ruleset JSON: {exc}")
            return
        result.checked.append("ruleset:enforcement")
        if data.get("enforcement") != "active":
            result.errors.append("Ruleset enforcement must be active")
        rules = data.get("rules", [])
        rule_types = {rule.get("type") for rule in rules}
        for required_type in ("pull_request", "required_status_checks", "deletion", "non_fast_forward"):
            result.checked.append(f"ruleset:{required_type}")
            if required_type not in rule_types:
                result.errors.append(f"Ruleset missing rule: {required_type}")
        pr = next((rule for rule in rules if rule.get("type") == "pull_request"), {})
        params = pr.get("parameters", {})
        for key in (
            "dismiss_stale_reviews_on_push",
            "require_code_owner_review",
            "require_last_push_approval",
            "required_review_thread_resolution",
        ):
            result.checked.append(f"ruleset-pr:{key}")
            if params.get(key) is not True:
                result.errors.append(f"Ruleset pull_request must enable: {key}")
        checks = next((rule for rule in rules if rule.get("type") == "required_status_checks"), {})
        contexts = {
            item.get("context")
            for item in checks.get("parameters", {}).get("required_status_checks", [])
        }
        for context in ("Validate skill repository", "Analyze Python"):
            result.checked.append(f"ruleset-check:{context}")
            if context not in contexts:
                result.errors.append(f"Ruleset missing required status check: {context}")


def run_unit_tests(repo, result):
    completed = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "tests"],
        cwd=repo,
        text=True,
        capture_output=True,
        check=False,
    )
    result.checked.append("unit tests")
    if completed.returncode != 0:
        result.errors.append("Unit tests failed:\n" + completed.stdout + completed.stderr)


def validate_repo(repo, run_tests=True):
    repo = Path(repo).resolve()
    result = ValidationResult()
    check_required_files(repo, result)
    check_skill_manifest(repo, result)
    check_no_runtime_outputs(repo, result)
    check_frontmatter(repo, result)
    check_reference_links(repo, result)
    check_protocol_routing(repo, result)
    check_evals(repo, result)
    check_utf8(repo, result)
    check_forbidden_placeholders(repo, result)
    check_pycache_not_tracked(repo, result)
    check_codeowners(repo, result)
    check_github_governance(repo, result)
    if run_tests:
        run_unit_tests(repo, result)
    return result


def main():
    parser = argparse.ArgumentParser(description="Validate the Agent Collaboration OS skill repository.")
    parser.add_argument("--repo", default=Path(__file__).resolve().parents[1])
    parser.add_argument("--skip-tests", action="store_true")
    args = parser.parse_args()

    result = validate_repo(Path(args.repo), run_tests=not args.skip_tests)
    print(f"Checked {len(result.checked)} items")
    if result.errors:
        print("Validation failed:")
        for error in result.errors:
            print(f"- {error}")
        return 1
    print("Validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
