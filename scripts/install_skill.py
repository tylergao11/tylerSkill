import argparse
import os
import shutil
from dataclasses import dataclass
from pathlib import Path


SKILL_NAME = "agent-collaboration-os"
INCLUDE_DIRS = [
    ".github",
    "agents",
    "examples",
    "modules",
    "profiles",
    "references",
    "scripts",
    "templates",
    "tools",
]
INCLUDE_FILES = [
    "SKILL.md",
    "VERSION",
    "CHANGELOG.md",
    "skill-manifest.json",
]
EXCLUDE_NAMES = {
    ".git",
    ".superpowers",
    "__pycache__",
}
EXCLUDE_SUFFIXES = {
    ".pyc",
    ".pyo",
}


@dataclass(frozen=True)
class InstallItem:
    source: Path
    destination: Path


@dataclass(frozen=True)
class InstallPlan:
    repo: Path
    destination_root: Path
    skill_dir: Path
    items: list


def default_skills_dir():
    codex_home = os.environ.get("CODEX_HOME")
    if codex_home:
        return Path(codex_home) / "skills"
    return Path.home() / ".codex" / "skills"


def should_include(path):
    parts = set(path.parts)
    if parts & EXCLUDE_NAMES:
        return False
    if path.suffix in EXCLUDE_SUFFIXES:
        return False
    return True


def build_install_plan(repo, destination_root):
    repo = Path(repo).resolve()
    destination_root = Path(destination_root).resolve()
    skill_dir = destination_root / SKILL_NAME
    items = []

    for file_name in INCLUDE_FILES:
        source = repo / file_name
        if source.exists():
            items.append(InstallItem(source, skill_dir / file_name))

    for dir_name in INCLUDE_DIRS:
        source_dir = repo / dir_name
        if not source_dir.exists():
            continue
        for source in source_dir.rglob("*"):
            if source.is_dir() or not should_include(source.relative_to(repo)):
                continue
            items.append(InstallItem(source, skill_dir / source.relative_to(repo)))

    return InstallPlan(repo, destination_root, skill_dir, items)


def execute_install(plan, dry_run=False, force=False):
    if dry_run:
        return [f"{item.source} -> {item.destination}" for item in plan.items]

    if plan.skill_dir.exists() and force:
        shutil.rmtree(plan.skill_dir)
    plan.skill_dir.mkdir(parents=True, exist_ok=True)

    copied = []
    for item in plan.items:
        item.destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(item.source, item.destination)
        copied.append(str(item.destination))
    return copied


def main():
    parser = argparse.ArgumentParser(description="Install Agent Collaboration OS as a Codex skill.")
    parser.add_argument("--repo", default=Path(__file__).resolve().parents[1], help="Skill repository root.")
    parser.add_argument("--dest", default=default_skills_dir(), help="Destination skills directory.")
    parser.add_argument("--dry-run", action="store_true", help="Print planned files without copying.")
    parser.add_argument("--force", action="store_true", help="Replace existing installed skill directory.")
    args = parser.parse_args()

    plan = build_install_plan(Path(args.repo), Path(args.dest))
    results = execute_install(plan, dry_run=args.dry_run, force=args.force)
    action = "Would install" if args.dry_run else "Installed"
    print(f"{action} {len(results)} files to {plan.skill_dir}")
    for line in results:
        print(f"- {line}")


if __name__ == "__main__":
    main()
