# Installation and Consumer Usage

Use this protocol when installing Agent Collaboration OS globally or vendoring it
into a consumer project.

## Global Codex Skill Install

Dry run:

```powershell
python scripts\install_skill.py --dry-run
```

Install to default Codex skills directory:

```powershell
python scripts\install_skill.py --force
```

Install to a custom skills directory:

```powershell
python scripts\install_skill.py --dest C:\path\to\skills --force
```

The installed skill directory is:

```text
agent-collaboration-os/
```

## Vendor or Submodule Usage

Consumer projects may pin this repository under:

```text
vendor/agent-collaboration-os/
```

The consumer project should record the vendor path and skill version in
`docs/project-notes/project-memory.md`.

## Initialize a Consumer Project

```powershell
python vendor\agent-collaboration-os\scripts\init_consumer_project.py . --profile casual-mini-game --vendor-path vendor\agent-collaboration-os --copy-templates
```

This creates project runtime folders such as:

- `docs/project-notes/`
- `docs/handoffs/`
- `docs/reviews/`
- `docs/decisions/`
- `evidence/`

Runtime evidence belongs in the consumer project, not in the skill repository.

## Verification

Run in the skill repository:

```powershell
python scripts\validate_skill_repo.py
python -m unittest discover tests
```
