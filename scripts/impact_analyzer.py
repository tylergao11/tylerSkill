import argparse
import json
import subprocess
import sys
from pathlib import Path


RISK_RULES = (
    ("cloud", ("cloud", "server", "api", "auth", "payment", "database")),
    ("configuration", ("config", "configs", "settings", "balance")),
    ("economy-domain", ("reward", "level", "economy", "gacha", "drop")),
    ("state", ("state", "store", "save", "model", "session")),
    ("presentation", ("view", "ui", "scene", "animation", "audio", "asset", "sprite")),
    ("tests", ("test", "tests", "spec", "__tests__")),
    ("tooling", ("package", "vite", "webpack", "tsconfig", "eslint", "script")),
)


def _normalize(path):
    return path.replace("\\", "/")


def _changed_files_from_git(repo, base):
    completed = subprocess.run(
        ["git", "diff", "--name-only", base],
        cwd=repo,
        text=True,
        capture_output=True,
        check=False,
    )
    if completed.returncode != 0:
        raise ValueError(completed.stderr.strip() or "git diff failed")
    return [line.strip() for line in completed.stdout.splitlines() if line.strip()]


def classify_file(path):
    lower = _normalize(path).lower()
    segments = [segment for segment in lower.split("/") if segment]
    tokens = set(segments)
    for segment in segments:
        stem = segment.rsplit(".", 1)[0]
        tokens.update(part for part in re_split_path_token(stem) if part)
    labels = []
    for label, needles in RISK_RULES:
        if label in {"configuration", "presentation", "state", "tests", "tooling"}:
            matched = any(needle in tokens for needle in needles)
        else:
            matched = any(needle in lower for needle in needles)
        if matched:
            labels.append(label)
    if not labels:
        labels.append("general")
    return labels


def re_split_path_token(value):
    token = ""
    for char in value:
        if char.isalnum():
            token += char.lower()
        else:
            if token:
                yield token
                token = ""
    if token:
        yield token


def analyze_impact(files):
    normalized = sorted({_normalize(item) for item in files if item})
    categories = {}
    for file_path in normalized:
        for label in classify_file(file_path):
            categories.setdefault(label, []).append(file_path)

    regression_checks = []
    if "cloud" in categories:
        regression_checks.append("Verify cloud/API permission, failure, retry, and trust-boundary behavior.")
    if "configuration" in categories:
        regression_checks.append("Validate config schema, numeric ranges, and representative balance cases.")
    if "economy-domain" in categories:
        regression_checks.append("Verify reward/economy outcomes, duplication protection, and player-facing state.")
    if "state" in categories:
        regression_checks.append("Run save/load, lifecycle, and state transition checks.")
    if "presentation" in categories:
        regression_checks.append("Run screenshot or true-device visual/audio smoke checks.")
    if "tooling" in categories:
        regression_checks.append("Run clean install/build commands in addition to focused tests.")
    if not regression_checks:
        regression_checks.append("Run focused tests for changed files and one nearby integration path.")

    return {
        "changed_files": normalized,
        "categories": categories,
        "risk_level": risk_level(categories, normalized),
        "regression_checks": regression_checks,
    }


def risk_level(categories, files):
    high_risk = {"cloud", "configuration", "state", "tooling", "economy-domain"}
    if high_risk & set(categories):
        return "high"
    if len(files) >= 5 or "presentation" in categories:
        return "medium"
    return "low"


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Analyze changed files and propose regression checks."
    )
    parser.add_argument("files", nargs="*", help="Files to analyze. If omitted, git diff is used.")
    parser.add_argument("--repo", default=".", help="Repository path for git diff mode.")
    parser.add_argument("--base", default="HEAD", help="Git diff base when files are omitted.")
    args = parser.parse_args(argv)

    try:
        files = args.files or _changed_files_from_git(Path(args.repo).resolve(), args.base)
        result = analyze_impact(files)
    except (OSError, ValueError) as exc:
        print(f"impact-analyzer error: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
