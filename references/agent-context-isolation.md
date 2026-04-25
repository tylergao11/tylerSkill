# Agent Context Isolation

Use this protocol when roles must stay independent enough to avoid biased tests,
implementation leakage, stale context, or circular review.

## Core Rule

Give each role the context it needs to perform its responsibility, not the full
conversation or another role's private reasoning.

## Isolation Modes

| Mode | Use When | Rule |
| --- | --- | --- |
| Test First Isolation | Testing Agent defines tests or acceptance before implementation | Do not include Development Agent's implementation plan unless needed for risk review. |
| Implementation Isolation | Development Agent implements against requirements and accepted tests | Do not include hidden expected fixes or speculative test internals. |
| Refactor Isolation | Reviewer checks readability after behavior passes | Focus on structure, names, coupling, and module boundaries. |
| Art Review Isolation | Art Agent reviews experience output | Provide screenshots, recordings, specs, and constraints, not unrelated code debate. |

## Context Isolation Packet

```markdown
## Context Isolation Packet

Role:
Task ID:
Isolation Mode:
Allowed Context:
Withheld Context:
Reason:
Inputs:
Expected Output:
Validation:
```

## Leakage Block

```markdown
## Leakage Block

Role:
Leaked Context:
Why It Biases Work:
Required Refresh:
Next Action:
```

If a role appears to optimize for another role's expected answer instead of the
actual requirement, stop the lane and issue a fresh context packet.
