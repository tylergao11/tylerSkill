# Agent Collaboration OS

This repository contains a portable multi-agent workflow skill for game and
software production, plus reusable diagnostic and production-support tools.

All text files must be UTF-8.

## Directory Map

```text
docs/
  Skill.md                         Skill entry point and protocol index
  references/                      Detailed protocols loaded on demand

scripts/                           Small project-agnostic CLI tools
tools/                             Larger reusable tools and future packages
examples/                          Example inputs, sessions, and workflow artifacts
templates/                         Copyable markdown/json templates
profiles/                          Game architecture profiles
modules/                           Reusable capability module specs
tests/                             Automated tests for scripts and tools
```

## Loading Model

`docs/Skill.md` is the short kernel. It should stay compact.

Detailed protocols live in `docs/references/` and are loaded only when needed.
This keeps the main agent and specialist agents from carrying unnecessary
context.

## Consumer Project Outputs

This repository is the Skill/tooling source, not a game project workspace.
When a game project uses this skill, that consumer project should create its own
runtime folders:

```text
game-project/
  docs/project-notes/
  docs/handoffs/
  docs/reviews/
  docs/decisions/
  docs/archive/
  evidence/screenshots/
  evidence/recordings/
  evidence/logs/
  evidence/test-results/
  evidence/performance/
  evidence/references/
```

Do not put temporary brainstorming sessions, cache files, or generated Python
bytecode into git. Large evidence files usually belong in the consumer project,
artifact storage, or release evidence archive, not this skill repository.

## Tooling Rule

Small single-file CLIs live in `scripts/`.

Tools that grow into reusable modules should move to `tools/<tool-name>/` with
their own README, tests, examples, and module contract.
