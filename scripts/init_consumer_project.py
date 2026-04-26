import argparse
import shutil
from pathlib import Path


DIRECTORIES = [
    "docs/project-notes",
    "docs/agent-os-upgrades",
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
    "evidence/references/agent-os",
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

Agent OS Runtime Record: docs/project-notes/agent-os-runtime.md
Skill Learning Log: docs/project-notes/skill-learning-log.md
Upgrade Packet Directory: docs/agent-os-upgrades/

## Active Decisions

## Accepted Assumptions

## Current Architecture

## Art Direction

## Testing Bar

## Known Risks

## Open Questions

## Do Not Repeat

## Source Documents

## Agent OS Growth

- Record workflow failures in `docs/project-notes/skill-learning-log.md`.
- Promote reusable lessons through `docs/agent-os-upgrades/<date-topic>/`.
- Do not write runtime notes into the installed or vendored skill path.
- A skill upgrade candidate needs evidence plus a proposed eval, test, or validator.
"""

AGENT_OS_RUNTIME = """Status: Active
Owner:
Last Updated:
Supersedes:
Superseded By:
Use For: Startup awareness for Agent Collaboration OS in this consumer project.
Do Not Use For: Project-specific feature requirements or raw evidence.

# Agent OS Runtime

Skill Version: {skill_version}
Architecture Profile: {profile}
Vendor Path: {vendor_path}

## Main Agent Startup Checklist

- Load `docs/project-notes/project-memory.md` before planning work.
- Load `docs/project-notes/architecture-profile.md` when it exists.
- Check whether this project has active entries in `docs/project-notes/skill-learning-log.md`.
- Check `docs/agent-os-upgrades/` for open upgrade packets before claiming workflow completion.
- Start with the profile's default protocol set. Do not load heavy protocols unless their trigger appears.
- Keep generated Markdown, evidence, logs, reviews, and handoffs in this project, not in the skill path.
- When a workflow failure repeats or generalizes, create a Project Learning Log Entry.
- When a lesson is reusable, create an Upgrade Packet with evidence and a proposed eval/test.

## Growth Paths

- Learning Log: `docs/project-notes/skill-learning-log.md`
- Upgrade Packets: `docs/agent-os-upgrades/<date-topic>/`
- Agent OS Evidence: `evidence/references/agent-os/`

## Upgrade Packet Minimum Contents

- `learning-note.md`
- `evidence.md`
- `proposed-rule.md`
- `proposed-eval.json` or `proposed-test.md`
- `target-files.md`
"""

SKILL_LEARNING_LOG = """Status: Active
Owner:
Last Updated:
Supersedes:
Superseded By:
Use For: Project-local observations that may improve Agent Collaboration OS.
Do Not Use For: Stable skill rules or project feature requirements.

# Skill Learning Log

Use this file to record real workflow failures and reusable lessons discovered
while running Agent Collaboration OS in this project.

Do not edit the installed or vendored skill directly from here. Convert reusable
lessons into upgrade packets under `docs/agent-os-upgrades/`.

## Project Learning Log Entry

Date:
Project:
Task ID:
Observed Agent Failure:
Impact:
Evidence:
Current Skill Rule:
Proposed Improvement:
Project-Specific Details:
Reusable Lesson:
Recommended Destination: Project Memory | Skill Reference | Core Skill | Tool | Eval/Test
Owner:
Status: Open | Accepted | Rejected | Promoted | Archived
"""

UPGRADE_PACKET_README = """Status: Active
Owner:
Last Updated:
Supersedes:
Superseded By:
Use For: Staging reusable Agent Collaboration OS upgrade candidates from this project.
Do Not Use For: Runtime feature notes, raw logs, or installed skill edits.

# Agent OS Upgrade Packets

Create one folder per candidate:

```text
docs/agent-os-upgrades/YYYYMMDD-short-topic/
```

Each packet should contain:

- `learning-note.md`: what failed and why it matters.
- `evidence.md`: links to logs, screenshots, reviews, tests, or agent outputs.
- `proposed-rule.md`: the smallest reusable rule or tool change.
- `proposed-eval.json` or `proposed-test.md`: how the skill will prevent repeat failure.
- `target-files.md`: likely files to update in the skill repository.

Main Agent should review this directory during phase reviews, release reviews,
and before claiming workflow completion.
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


def init_project(root, profile="lightweight", vendor_path=None, copy_templates=False):
    created = []
    for directory in DIRECTORIES:
        path = root / directory
        path.mkdir(parents=True, exist_ok=True)
        keep = path / ".gitkeep"
        if write_if_missing(keep, ""):
            created.append(rel_posix(keep, root))

    profile_name = profile or "lightweight"
    if vendor_path and not Path(vendor_path).is_absolute():
        vendor_path = root / vendor_path
    vendor_text = rel_posix(vendor_path, root) if vendor_path and vendor_path.is_relative_to(root) else (str(vendor_path) if vendor_path else "")
    memory = root / "docs" / "project-notes" / "project-memory.md"
    memory_text = PROJECT_MEMORY.format(
        skill_version=read_version(),
        profile=profile_name,
        vendor_path=vendor_text,
    )
    if write_if_missing(memory, memory_text):
        created.append(rel_posix(memory, root))

    runtime = root / "docs" / "project-notes" / "agent-os-runtime.md"
    runtime_text = AGENT_OS_RUNTIME.format(
        skill_version=read_version(),
        profile=profile_name,
        vendor_path=vendor_text,
    )
    if write_if_missing(runtime, runtime_text):
        created.append(rel_posix(runtime, root))

    learning_log = root / "docs" / "project-notes" / "skill-learning-log.md"
    if write_if_missing(learning_log, SKILL_LEARNING_LOG):
        created.append(rel_posix(learning_log, root))

    upgrade_readme = root / "docs" / "agent-os-upgrades" / "README.md"
    if write_if_missing(upgrade_readme, UPGRADE_PACKET_README):
        created.append(rel_posix(upgrade_readme, root))

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
    parser.add_argument("--profile", default="lightweight", help="Architecture profile name, defaults to lightweight.")
    parser.add_argument("--vendor-path", help="Path where this skill is vendored in the consumer project.")
    parser.add_argument("--copy-templates", action="store_true", help="Copy shared templates into the consumer project.")
    args = parser.parse_args()

    root = Path(args.project_dir).resolve()
    root.mkdir(parents=True, exist_ok=True)
    vendor_path = Path(args.vendor_path) if args.vendor_path else None
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
