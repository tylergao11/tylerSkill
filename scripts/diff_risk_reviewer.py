import argparse
import json
import subprocess
import sys
from pathlib import Path


HIGH_RISK_KEYWORDS = (
    "auth",
    "payment",
    "cloud",
    "server",
    "database",
    "save",
    "reward",
    "economy",
    "config",
    "package",
)


def _git_changed_files(repo, base):
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


def review_diff_risk(files):
    normalized = sorted({item.replace("\\", "/") for item in files if item})
    risky_files = []
    for file_path in normalized:
        lower = file_path.lower()
        if any(keyword in lower for keyword in HIGH_RISK_KEYWORDS):
            risky_files.append(file_path)

    notes = []
    if risky_files:
        notes.append("High-risk paths changed; require focused tests and explicit regression notes.")
    if len(normalized) > 8:
        notes.append("Large file count; require impact summary before completion.")
    if not any(("test" in item.lower() or "spec" in item.lower()) for item in normalized):
        notes.append("No test files changed; explain existing coverage or add focused tests.")
    if not notes:
        notes.append("Diff appears low-risk; still require validation evidence before completion.")

    blocked = bool(risky_files) and not any(
        ("test" in item.lower() or "spec" in item.lower()) for item in normalized
    )
    return {
        "changed_files": normalized,
        "risky_files": risky_files,
        "blocked": blocked,
        "required_action": "Add or cite tests before completion." if blocked else "Proceed with stated validation.",
        "notes": notes,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Review changed file paths for completion risk before handoff."
    )
    parser.add_argument("files", nargs="*", help="Files to review. If omitted, git diff is used.")
    parser.add_argument("--repo", default=".", help="Repository path for git diff mode.")
    parser.add_argument("--base", default="HEAD", help="Git diff base when files are omitted.")
    args = parser.parse_args(argv)

    try:
        files = args.files or _git_changed_files(Path(args.repo).resolve(), args.base)
        result = review_diff_risk(files)
    except (OSError, ValueError) as exc:
        print(f"diff-risk-reviewer error: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not result["blocked"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
