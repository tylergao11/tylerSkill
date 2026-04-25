# Blocker Recovery Protocol

Use this when a task stalls, fails, lacks tools, lacks permissions, or cannot
complete normally.

## Core Rule

Blocked is a valid state. Silent stagnation is not.

Every blocker must produce a recovery path, not just a stop sign.

## Blocker Report

```markdown
## Blocker Report

Role:
Task ID:
Blocker Type: Missing Input | Tool Failure | Capability Gap | Permission | Dependency | Ambiguous Requirement | Technical Constraint | External Service | Safety/Policy | Time Budget
Escalation Level: L1 | L2 | L3 | L4 | L5
What Is Blocked:
Attempted:
Evidence:
Needed To Unblock:
Fallback Options:
Recommended Option:
Impact If Delayed:
Owner To Resolve:
Review Deadline:
```

Escalation levels:

- **L1**: role can resolve internally.
- **L2**: Main Agent decision required.
- **L3**: user decision required.
- **L4**: external tool, permission, or human resource required.
- **L5**: project strategy or scope must change.

A blocker without attempted steps, evidence, fallback options, and a recommended
option is invalid.

## Recovery Decision

```markdown
## Recovery Decision

Blocked Task:
Chosen Path:
Reason:
Scope Impact:
Risk:
New Task Briefs:
Follow-up Check:
```

## Stall Check

```markdown
## Stall Check

Target Role:
Task ID:
Expected Output:
Last Valid State:
Elapsed Time or Turns:
Required Response: Agent Turn Result | Blocker Report | Partial Output
```

## Partial Output Report

```markdown
## Partial Output Report

Role:
Task ID:
Completed Parts:
Incomplete Parts:
Reason Incomplete:
Usable Artifacts:
Risks:
Recommended Next Step:
```

## Lane Management

Main Agent should maintain:

- **Blocked Lane**: work waiting on a blocker.
- **Active Lane**: work that can continue now.
- **Fallback Lane**: degraded or mocked path used to preserve momentum.

Use `Ready with Risk` only when unresolved risk is explicit, accepted, and does
not violate safety, data integrity, payment, privacy, or core release requirements.
