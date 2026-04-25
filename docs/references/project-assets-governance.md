# Project Assets Governance

Use this protocol when managing project documents, screenshots, recordings, logs,
evidence, decision references, archival, or cleanup.

## Core Rules

- Skill files define reusable workflow rules, not project-specific truth.
- Project documents define current project truth.
- Evidence files support claims, reviews, and decisions.
- Archived files are historical references, not default decision sources.
- No evidence, no durable decision memory.

Short-term judgment may move work forward. Durable decisions, acceptance, and
project memory should be tied to documents, evidence, structured reports, tests,
or reliable external references.

## Recommended Directory Structure

```text
docs/
├── Skill.md
├── references/
├── project-notes/
├── handoffs/
├── reviews/
├── decisions/
└── archive/

evidence/
├── screenshots/
├── recordings/
├── logs/
├── test-results/
├── performance/
└── references/
```

Use UTF-8 for all text files.

## Document Status Header

Important project documents should start with:

```markdown
Status: Draft | Active | Superseded | Archived | Rejected
Owner:
Last Updated:
Supersedes:
Superseded By:
Use For:
Do Not Use For:
```

Status meanings:

- **Draft**: still being discussed; do not treat as final.
- **Active**: current source of truth.
- **Superseded**: replaced by a newer document.
- **Archived**: retained for history only.
- **Rejected**: explicitly not a valid basis for future work.

## Evidence Naming

Use stable, sortable names:

```text
YYYYMMDD-role-task-target-version.ext
```

Examples:

```text
20260426-art-victory-popup-review-v001.png
20260426-test-reward-flow-lowend-v001.mp4
20260426-dev-cloud-save-error-log-v001.txt
```

## Evidence Note

Pair important screenshots, recordings, logs, or test outputs with a note:

```markdown
## Evidence Note

File:
Task ID:
Captured By:
What It Shows:
Related Decision:
Valid Until:
```

Evidence should state what it proves and what it does not prove.

## Decision Basis With References

When Main Agent makes a high-impact decision or synthesis, cite the basis:

```markdown
## Decision Basis

Decision:
Project Documents:
Skill Protocols:
Evidence:
Official References:
Agent Reports:
Assumptions:
Confidence: High | Medium | Low
```

Priority order:

1. Current active project documents
2. Reliable evidence and structured agent reports
3. Official platform, engine, API, or legal/compliance references
4. Skill protocols
5. Established practice
6. Agent judgment

## Document Sweep

Run this at phase boundaries, acceptance locks, release decisions, and after major
direction changes:

```markdown
## Document Sweep

Active Documents:
Archived Documents:
Superseded Decisions:
Reusable Evidence:
Discarded or Ignored:
Reason:
```

Sweep rules:

- Archive old art feedback after Acceptance Lock.
- Mark old architecture choices as Superseded when a new ADR replaces them.
- Keep failed experiments only if the conclusion is useful.
- Do not use outdated screenshots or recordings as current acceptance evidence.
- Keep logs and recordings that explain a release block or regression incident.

## Screenshot and Recording Lifecycle

Screenshots and recordings should have a lifecycle:

- **Capture**: name and store under `evidence/`.
- **Annotate**: add an Evidence Note when it affects a decision.
- **Use**: cite in reviews, release confidence, or decision basis.
- **Expire**: mark invalid when the UI, build, feature, or platform state changes.
- **Archive**: move old evidence out of active review paths.

## External References

When decisions depend on official docs, platform behavior, package limits,
security rules, payment, privacy, API support, or library maintenance, record:

- Source title
- URL or local path
- Access date
- What claim it supports
- Whether verification is still needed

Do not let unsourced web memory become durable project truth.
