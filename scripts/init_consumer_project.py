import argparse
from pathlib import Path


DIRECTORIES = [
    "docs/project-notes",
    "docs/handoffs",
    "docs/reviews",
    "docs/decisions",
    "docs/archive",
    "evidence/screenshots",
    "evidence/recordings",
    "evidence/logs",
    "evidence/test-results",
    "evidence/performance",
    "evidence/references",
]


PROJECT_MEMORY = """Status: Active
Owner:
Last Updated:
Supersedes:
Superseded By:
Use For: Current project truth for Agent Collaboration OS.
Do Not Use For: Historical raw trace or superseded decisions.

# Project Memory

## Active Decisions

## Accepted Assumptions

## Current Architecture

## Art Direction

## Testing Bar

## Known Risks

## Open Questions

## Do Not Repeat

## Source Documents
"""


def write_if_missing(path, content):
    if path.exists():
        return False
    path.write_text(content, encoding="utf-8", newline="\n")
    return True


def init_project(root):
    created = []
    for directory in DIRECTORIES:
        path = root / directory
        path.mkdir(parents=True, exist_ok=True)
        keep = path / ".gitkeep"
        if write_if_missing(keep, ""):
            created.append(str(keep.relative_to(root)))

    memory = root / "docs" / "project-notes" / "project-memory.md"
    if write_if_missing(memory, PROJECT_MEMORY):
        created.append(str(memory.relative_to(root)))

    return created


def main():
    parser = argparse.ArgumentParser(
        description="Initialize Agent Collaboration OS folders in a consumer project."
    )
    parser.add_argument("project_dir", help="Path to the consumer game project.")
    args = parser.parse_args()

    root = Path(args.project_dir).resolve()
    root.mkdir(parents=True, exist_ok=True)
    created = init_project(root)

    print(f"Initialized consumer project at: {root}")
    if created:
        print("Created:")
        for item in created:
            print(f"- {item}")
    else:
        print("No new files created; structure already existed.")


if __name__ == "__main__":
    main()
