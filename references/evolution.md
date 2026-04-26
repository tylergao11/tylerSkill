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

## Growth Loop

Use this loop during real projects. Do not try to perfect the skill by speculation
alone.

```text
Run Project -> Observe Failure -> Record Note -> Filter -> Patch Skill -> Add Eval/Test -> Version -> Reuse
```

Main Agent owns the loop. Testing Agent and Audit Agent may challenge whether a
lesson is real, reusable, and supported by enough evidence.

Every promoted skill change should include at least one of:

- A new or updated eval scenario.
- A regression test.
- A validator rule.
- A template or protocol check that prevents the same failure.

Do not promote a lesson to the skill when it only describes one project's
content, taste, file names, assets, or temporary team preference.

## Project Learning Log

During active project work, record raw lessons in the consumer project, not in
the skill directory.

Recommended path:

```text
docs/project-notes/skill-learning-log.md
```

Use this shape:

```markdown
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
```

The learning log is a staging area. It is not automatically part of the skill.

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
Required Eval or Test:
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
Required Eval or Test:
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

## Promotion Rules

- One-off project facts stay in Project Memory.
- Repeated agent failure patterns become Skill Improvement Notes.
- A promoted rule must be placed at the narrowest useful level: tool, template,
  reference protocol, or core skill.
- Core skill changes require stronger justification than reference changes.
- Any change that blocks, routes, or advances workflow state needs a matching
  eval or regression test.
- If a rule adds process cost, state what failure it prevents.
- If a rule cannot be verified, mark it experimental and keep it in Project
  Memory until real evidence exists.

## Growth Review

Run at phase boundaries, after serious blockers, and after release:

```markdown
## Growth Review

Project:
Phase:
Skill Version Used:
Failures Observed:
Rules That Helped:
Rules That Created Friction:
Missing Tooling:
Candidate Improvements:
Rejected Improvements:
Promotions:
Required Evals or Tests:
Next Skill Version:
```

The goal is compounding reliability, not a larger rulebook.
