# Skill Evolution Protocol

Use this when a workflow failure or reusable pattern should improve the skill.

## Core Rule

This skill is expected to evolve through real project use.

Skill evolution must be filtered. Do not promote every project detail into the
skill.

Use this split:

```text
Skill = reusable protocols
Project Memory = active project truth
Evidence Archive = proof and history
```

Only reusable workflow lessons belong in the skill.

## Skill Improvement Note

```markdown
## Skill Improvement Note

Observed Problem:
Where It Happened:
Current Rule:
Proposed Rule Change:
Why:
Risk:
```

Create a note when:

- An agent repeatedly gives invalid responses.
- A role boundary is unclear.
- A blocker pattern recurs.
- A quality gate misses a real issue.
- A process creates unnecessary friction.
- A new platform pattern should become reusable.

Main Agent should periodically convert accepted improvement notes into updates to
this skill, then remove or archive incorporated notes.

## Evolution Filter

Use this before changing the skill:

```markdown
## Evolution Filter

Observation:
Project-Specific or Reusable:
Seen Once or Repeated:
Would This Help Future Projects:
Does It Add Context Cost:
Should Update:
Target File:
```

Promote a note only when it helps future projects more than it increases context
or process cost.

## Evolution Decision

```markdown
## Evolution Decision

Improvement Note:
Decision: Reject | Keep as Project Memory | Add Reference Rule | Promote to Core Skill
Reason:
Context Cost:
Expected Benefit:
Target Location:
```

Decision meanings:

- **Reject**: not useful, already covered, or too costly.
- **Keep as Project Memory**: useful for this project only.
- **Add Reference Rule**: reusable but situational; place in a reference file.
- **Promote to Core Skill**: universal enough to appear in `Skill.md`.

## Evolution Cadence

Use three cadences:

- **Immediate Patch**: fix a clear protocol hole that is actively causing failure.
- **Project-End Review**: collect notes after a project phase and update references.
- **Pattern Promotion**: promote lessons repeated across projects into the core skill.

When in doubt, prefer Project Memory or a reference file over expanding the core
`Skill.md`.
