import argparse
import shutil
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

Skill Version: {skill_version}
Architecture Profile: {profile}
Vendor Path: {vendor_path}

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


REPO_ROOT = Path(__file__).resolve().parents[1]


def read_version():
    version_file = REPO_ROOT / "VERSION"
    if version_file.exists():
        return version_file.read_text(encoding="utf-8").strip()
    return "unversioned"


def write_if_missing(path, content):
    if path.exists():
        return False
    path.write_text(content, encoding="utf-8", newline="\n")
    return True


def rel_posix(path, root):
    return path.relative_to(root).as_posix()


def copy_tree_files(source, destination):
    created = []
    if not source.exists():
        return created
    for item in source.rglob("*"):
        if item.is_dir():
            continue
        relative = item.relative_to(source)
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists():
            continue
        shutil.copy2(item, target)
        created.append(target)
    return created


def init_project(root, profile=None, vendor_path=None, copy_templates=False):
    created = []
    for directory in DIRECTORIES:
        path = root / directory
        path.mkdir(parents=True, exist_ok=True)
        keep = path / ".gitkeep"
        if write_if_missing(keep, ""):
            created.append(rel_posix(keep, root))

    profile_name = profile or "custom"
    vendor_text = str(vendor_path) if vendor_path else ""
    memory = root / "docs" / "project-notes" / "project-memory.md"
    memory_text = PROJECT_MEMORY.format(
        skill_version=read_version(),
        profile=profile_name,
        vendor_path=vendor_text,
    )
    if write_if_missing(memory, memory_text):
        created.append(rel_posix(memory, root))

    if profile:
        profile_source = REPO_ROOT / "profiles" / f"{profile}.md"
        if profile_source.exists():
            profile_target = root / "docs" / "project-notes" / "architecture-profile.md"
            if write_if_missing(profile_target, profile_source.read_text(encoding="utf-8")):
                created.append(rel_posix(profile_target, root))
        else:
            raise ValueError(f"Unknown profile: {profile}")

    if vendor_path:
        vendor_note = root / "docs" / "project-notes" / "agent-os-vendor.md"
        vendor_body = (
            "Status: Active\n"
            "Owner:\n"
            "Last Updated:\n"
            "Use For: Agent Collaboration OS vendor reference.\n"
            "Do Not Use For: Runtime project evidence.\n\n"
            "# Agent OS Vendor\n\n"
            f"Vendor Path: {vendor_path}\n"
            f"Skill Version: {read_version()}\n"
        )
        if write_if_missing(vendor_note, vendor_body):
            created.append(rel_posix(vendor_note, root))

    if copy_templates:
        template_created = copy_tree_files(REPO_ROOT / "templates", root / "templates")
        created.extend(rel_posix(Path(item), root) for item in template_created)

    return created


def main():
    parser = argparse.ArgumentParser(
        description="Initialize Agent Collaboration OS folders in a consumer project."
    )
    parser.add_argument("project_dir", help="Path to the consumer game project.")
    parser.add_argument("--profile", help="Architecture profile name, e.g. casual-mini-game.")
    parser.add_argument("--vendor-path", help="Path where this skill is vendored in the consumer project.")
    parser.add_argument("--copy-templates", action="store_true", help="Copy shared templates into the consumer project.")
    args = parser.parse_args()

    root = Path(args.project_dir).resolve()
    root.mkdir(parents=True, exist_ok=True)
    vendor_path = Path(args.vendor_path).resolve() if args.vendor_path else None
    created = init_project(
        root,
        profile=args.profile,
        vendor_path=vendor_path,
        copy_templates=args.copy_templates,
    )

    print(f"Initialized consumer project at: {root}")
    if created:
        print("Created:")
        for item in created:
            print(f"- {item}")
    else:
        print("No new files created; structure already existed.")


if __name__ == "__main__":
    main()
