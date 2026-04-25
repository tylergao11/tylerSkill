# Completion Trust Boundary

Use this protocol when any agent claims work is completed, fixed, passing,
ready, verified, safe, shippable, or approved.

## Core Rule

An agent's completion claim is not evidence.

Completion is a trust-boundary crossing. It requires artifacts, verification
evidence, stated limits, and an audit decision when the work affects code,
release risk, production state, user data, cloud behavior, payment, rewards,
assets, or other agents' next actions.

## Constraint Ownership

Keep completion trust rules here. Other protocols should reference this file
instead of restating the full rule.

| Concern | Owner |
| --- | --- |
| Response shape and state transitions | `response-contract.md` |
| Completion evidence classes and audit decisions | `completion-trust-boundary.md` |
| Audit Agent authority and scope | `role-audit.md` |
| Role-specific required evidence | The relevant role protocol |
| Tool execution and machine-readable outputs | The relevant tool protocol |

## Evidence Classes

Classify every completion statement into exactly one evidence class:

| Class | Meaning | May Advance Workflow |
| --- | --- | --- |
| Verified | A real command, review, tool, screenshot, recording, log, or artifact was inspected and the result supports the claim. | Yes, if required protocols are satisfied. |
| Inferred | The claim follows from structure, reasoning, or static inspection but was not directly verified. | Only to planning or review, not release or final completion. |
| Unverified | The claim has no supporting evidence or the evidence is missing, stale, partial, or inaccessible. | No. |

## Completion Audit Trigger

Invoke Audit Agent when:

- A role returns `Status: Completed` for implementation, release, production, or multi-layer work.
- A response says "completed", "fixed", "passed", "ready", "verified",
  "已完成", "已修复", "已通过", or similar words.
- Main Agent claims project self-check, workflow completion, Git push/tag
  completion, release readiness, or production readiness.
- Tests pass but coverage is unclear.
- A self-check found new issues after an earlier completion claim.
- The same workflow needed more than one self-check round.
- Main Agent is about to tell the user that work is complete.

## Main Agent Claims

Main Agent completion summaries are auditable claims.

When Main Agent claims that self-check, verification, release preparation,
GitHub push/tag, production operation, or workflow completion is done, it must
include or trigger a Completion Audit Report.

Main Agent may report narrow facts without audit, such as "I ran command X and
it returned exit code 0." It must not turn those facts into broad completion
claims unless the evidence class and residual risk are stated.

## Completion Audit Report

`role-audit.md` and `templates/role-audit-prompt.md` should use this report
shape instead of redefining a different audit format.

```markdown
## Completion Audit Report

Task ID:
Claim Audited:
Claim Source:
Evidence Class: Verified | Inferred | Unverified
Evidence Reviewed:
Required Protocols Checked:
Missing Evidence:
Skipped or Weak Gates:
Residual Risks:
Workflow Decision: Accept | Downgrade to Partial | Block | Request More Evidence
Next Required Action:
```

## Audit Decision Rules

- `Accept` requires verified evidence for all acceptance-critical claims.
- `Downgrade to Partial` when useful work exists but the completion claim is too
  broad.
- `Block` when missing evidence could hide correctness, safety, data, release,
  production, or trust-boundary risk.
- `Request More Evidence` when a narrow command, review, screenshot, log, or
  tool run can close the gap.

## Completion Statement Shape

Main Agent final summaries should separate:

```markdown
Verified:
Inferred:
Unverified:
Residual Risk:
Audit Decision:
```

Do not merge inferred or unverified claims into verified language.

## Self-Check Escalation

When consecutive self-checks find new issues:

1. Stop saying the work is perfect or fully complete.
2. Produce a Completion Audit Report.
3. List unexamined dimensions.
4. Run the smallest next audit that can reduce meaningful risk.
5. Record a Skill Improvement Note if the failure came from the workflow.
