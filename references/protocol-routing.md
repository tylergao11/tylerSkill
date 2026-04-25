# Protocol Routing

Use this table to decide which protocol to load for a situation.

| Situation | Load | Required Output |
| --- | --- | --- |
| Delegating to a specialist | `context-packets.md` | `Specialist Context Packet`, `Task Brief` |
| Installing globally or vendoring into a game project | `installation.md` | Install command, consumer init command |
| Specialist response may advance workflow | `response-contract.md` | `Agent Turn Result` |
| Specialist says "completed", "fixed", or "next step" without evidence | `response-contract.md` | `Invalid Response Notice` |
| Task is stuck or cannot complete | `blocker-recovery.md` | `Blocker Report`, then `Recovery Decision` |
| Bug has many hypotheses | `debug-bisection.md` | `Diagnostic Test`, `Bisection Choice` |
| True-device diagnostics or pre-embedded logs are needed | `preflight-debug-capture.md` | `Debug Observability Plan`, `Debug Capture Digest` |
| Development architecture or readability is in question | `role-development.md` | `Engineering Plan`, `Pattern Fit Check` |
| Development work needs pre-code design validation, impact analysis, or completion risk review | `development-daily-tools.md` | Tool output plus `Regression Check Plan` or `Agent Turn Result` |
| Code seems over-abstracted | `role-development.md` | `Over-Abstraction Block` |
| Visual, motion, audio, or asset work is needed | `role-art.md` | `Art Asset Delivery`, `Art Review` |
| Art rejects an implementation | `role-art.md` | `Experience Veto Brief` |
| Testing strategy, numeric balance, or release risk is needed | `role-testing.md` | `Risk Map`, `Test Case Plan`, `Release Confidence` |
| A change may break nearby behavior | `regression-iteration.md` | `Impact Scope`, `Regression Check Plan` |
| Art/dev revision loop repeats | `regression-iteration.md` | `Revision Budget`, `Iteration Decision`, `Acceptance Lock` |
| Project docs, screenshots, recordings, or evidence need management | `project-assets-governance.md` | `Evidence Note`, `Document Sweep`, `Decision Basis` |
| Code may become a reusable module | `reusable-modules.md` | `Module Contract`, `Anti-Coupling Review` |
| Workflow failure should improve the skill | `evolution.md` | `Skill Improvement Note`, `Evolution Filter` |
| GitHub/CI/production incident or hotfix work | `production-operations.md` | `Production Operation Plan`, `Incident Report` |
| Destructive, privileged, cloud, data, or deployment action | `permission-environment.md` | `Permission Gate`, `Environment Declaration` |
| Release, rollback, or post-release validation | `release-rollback.md` | `Release Plan`, `Rollback Plan` |
| User data, rewards, auth, payment, privacy, or anti-cheat boundary | `data-privacy-trust-boundary.md` | `Trust Boundary Review`, `Data Handling Review` |
| Art/audio/source/license question | `asset-provenance.md` | `Asset Provenance Record` |
| Skill/runtime version, budgets, or loaded protocol tracking | `runtime-versioning-budget.md` | `Runtime Version Record`, `Budget Declaration` |

## Routing Rules

- Load the smallest protocol that handles the current situation.
- Prefer a reference file over the full draft.
- When multiple protocols apply, load the one that controls state transition
  first, then load role-specific detail.
