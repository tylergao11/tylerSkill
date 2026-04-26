# Protocol Routing

Use this table to decide which protocol to load for a situation.

| Situation | Load | Required Output |
| --- | --- | --- |
| Delegating to a specialist | `context-packets.md` | `Specialist Context Packet`, `Task Brief` |
| Same-role specialist may already exist | `context-packets.md` | `Agent Reuse Decision`, optional `Context Refresh` |
| Specialist output needs user-facing interpretation or approval | `main-agent-decision-review.md` | `Main Agent Specialist Review`, `User Decision Brief` |
| Role context may bias tests, implementation, refactor, or art review | `agent-context-isolation.md` | `Context Isolation Packet`, `Leakage Block` |
| Installing globally or vendoring into a game project | `installation.md` | Install command, consumer init command |
| Publishing, vendoring, or evaluating cross-agent compatibility | `compatibility-registry.md` | `Skill Registry Record` |
| Specialist response may advance workflow | `response-contract.md` | `Agent Turn Result` |
| Specialist says "completed", "fixed", or "next step" without evidence | `response-contract.md` | `Invalid Response Notice` |
| Any agent claims completed, fixed, passed, ready, verified, or shippable | `completion-trust-boundary.md` | `Completion Audit Report` |
| Task is stuck or cannot complete | `blocker-recovery.md` | `Blocker Report`, then `Recovery Decision` |
| Bug has many hypotheses | `debug-bisection.md` | `Diagnostic Test`, `Bisection Choice` |
| True-device diagnostics or pre-embedded logs are needed | `preflight-debug-capture.md` | `Debug Observability Plan`, `Debug Capture Digest` |
| Development architecture or readability is in question | `role-development.md` | `Engineering Plan`, `Pattern Fit Check` |
| Strong online game needs dedicated client runtime owner | `role-client-development.md` | `Client Architecture Plan`, `Client/Server Contract Review` |
| Strong online game needs authoritative backend owner | `role-server-development.md` | `Server Architecture Plan`, `Authoritative Gameplay Contract` |
| Strong online game server architecture is being planned | `strong-online-server-governance.md` | `Strong Online Server Readiness Plan` |
| Login, session, room join, reconnect, player return, replay, settlement, or disconnection behavior is needed | `reconnect-session-governance.md` | `Reconnect and Session Plan` |
| Development work needs pre-code design validation, impact analysis, or completion risk review | `development-daily-tools.md` | Tool output plus `Regression Check Plan` or `Agent Turn Result` |
| Game feature touches two or more layers, cloud, reward, auth, payment, save data, leaderboard, ads, economy, or anti-cheat | `multi-layer-feature-gate.md` | `Multi-Layer Pre-Code Gate` |
| Code seems over-abstracted | `role-development.md` | `Over-Abstraction Block` |
| Visual, motion, audio, or asset work is needed | `role-art.md` | `Art Asset Delivery`, `Art Review` |
| Art rejects an implementation | `role-art.md` | `Experience Veto Brief` |
| Testing strategy, numeric balance, or release risk is needed | `role-testing.md` | `Risk Map`, `Test Case Plan`, `Release Confidence` |
| Completion evidence, skipped gates, false confidence, or self-check depth is in question | `role-audit.md` | `Completion Audit Report` |
| A change may break nearby behavior | `regression-iteration.md` | `Impact Scope`, `Regression Check Plan` |
| Art/dev revision loop repeats | `regression-iteration.md` | `Revision Budget`, `Iteration Decision`, `Acceptance Lock` |
| Project docs, screenshots, recordings, or evidence need management | `project-assets-governance.md` | `Evidence Note`, `Document Sweep`, `Decision Basis` |
| Code may become a reusable module | `reusable-modules.md` | `Module Contract`, `Anti-Coupling Review` |
| Changed files may cross model/controller/view/service/config/test layers | `layer-map-governance.md` | `Layer Placement Review` |
| Workflow failure should improve the skill | `evolution.md` | `Skill Improvement Note`, `Evolution Filter` |
| GitHub issues, PRs, CI, CodeQL, Dependabot, CODEOWNERS, releases, or repository protections matter | `github-governance.md` | `GitHub Setup Check`, PR gate evidence, CI gate evidence |
| GitHub/CI/production incident or hotfix work | `production-operations.md` | `Production Operation Plan`, `Incident Report` |
| Destructive, privileged, cloud, data, or deployment action | `permission-environment.md` | `Permission Gate`, `Environment Declaration` |
| Release, rollback, or post-release validation | `release-rollback.md` | `Release Plan`, `Rollback Plan` |
| User data, rewards, auth, payment, privacy, or anti-cheat boundary | `data-privacy-trust-boundary.md` | `Trust Boundary Review`, `Data Handling Review` |
| Art/audio/source/license question | `asset-provenance.md` | `Asset Provenance Record` |
| Dependency, SDK, asset, license, commercial rights, or package budget risk | `dependency-asset-audit.md` | `Dependency Asset Audit Result` |
| Skill/runtime version, budgets, or loaded protocol tracking | `runtime-versioning-budget.md` | `Runtime Version Record`, `Budget Declaration` |

## Routing Rules

- Load the smallest protocol that handles the current situation.
- Prefer a reference file over the full draft.
- When multiple protocols apply, load the one that controls state transition
  first, then load role-specific detail.
