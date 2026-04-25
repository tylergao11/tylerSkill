---
name: agent-collaboration-os
description: A portable Agent Collaboration Operating System workflow for coordinating a main agent, development agent, art/audio agent, and testing agent across any project. Use when planning, building, reviewing, or shipping work that benefits from role-based multi-agent collaboration, dual-mode execution, standardized task briefs, quality gates, and handoff protocols.
---

# Agent Collaboration OS

Use this skill to run a portable multi-agent collaboration workflow in any project.
The main agent acts as the orchestrator. Specialist agents provide focused judgment,
production, and review through standardized briefs and handoffs.

## Core Model

The workflow uses four roles:

- **Main Agent**: user-facing orchestrator, product owner, task router, context holder, and final decision maker.
- **Development Agent**: architecture, implementation, integration, refactoring, performance, and technical risk control.
- **Art Agent**: visual direction, UI/UX, motion, audio, asset production, sensory polish, and effect review.
- **Testing Agent**: code review, test strategy, bug reproduction, balance and numeric modeling, regression risk, and release confidence.

The default topology is **orchestrated collaboration**:

- The Main Agent receives user intent.
- The Main Agent turns intent into task briefs.
- Specialist agents respond with bounded outputs.
- The Main Agent merges, resolves conflicts, and presents decisions to the user.

Specialist agents should not silently change each other's responsibilities. Cross-role
requests must be converted into explicit task briefs.

## Operating Modes

Support two modes.

### Lightweight Mode

Use by default for small or exploratory tasks.

- Main Agent handles most work directly.
- Specialist agents are invoked as perspectives only when their expertise changes the outcome.
- Keep handoffs short.
- Prefer speed and low ceremony.

### Production Team Mode

Use when the user asks for full process, high quality, strict review, or complex production.

Trigger phrases may include:

- "进入制作组模式"
- "全流程审查"
- "严格模式"
- "用完整 agent 流程"

Production Team Mode requires:

- A task brief before specialist work.
- Development, Art, and Testing review where relevant.
- Explicit quality gates before integration or delivery.
- A final Main Agent synthesis that records decisions, risks, and next actions.

## Workflow Stages

This skill uses an **Acceptance-and-Risk Driven Workflow**.
Do not require pure TDD for every game-development task. Instead:

- For deterministic logic, define tests first where practical.
- For experience-heavy work, define acceptance criteria first.
- For high-risk systems, define the risk map first.
- For exploratory gameplay, prototype first, then freeze acceptance criteria and
  tests once the direction is validated.

Core rule:

> Define success before production. Identify risk before implementation. Use
> tests first when the system is deterministic; use acceptance criteria first
> when the work is experiential.

### 1. Intake

Main Agent gathers:

- Goal
- Audience or user
- Success criteria
- Constraints
- Existing project context
- Risk level
- Required mode

If the mode is unclear, default to Lightweight Mode.

### 2. Decomposition

Main Agent splits work into role-specific tasks:

- Product or behavior decisions stay with Main Agent.
- Implementation tasks go to Development Agent.
- Visual, motion, audio, and experience tasks go to Art Agent.
- Test, review, numeric, and release-confidence tasks go to Testing Agent.

Before decomposition is accepted, Main Agent must explain why the task split is
correct.

Use this format for non-trivial work:

```markdown
## Decomposition Rationale

Goal:
Chosen Split:
Why This Split:
Rejected Splits:
Dependencies:
Risks:
Acceptance Criteria:
```

### 3. Specialist Work

Each specialist receives a task brief and returns a structured response.
Specialists must state assumptions, decisions, blockers, and handoff requirements.

All roles follow the same governance loop:

```text
Rationale -> Plan -> Output -> Review -> Acceptance
```

No important output should appear without a short explanation of why that
approach fits the goal and constraints.

Before high-impact implementation begins:

- Main Agent confirms the goal and task split.
- Testing Agent produces a Risk Map and, where practical, Test Strategy Rationale.
- Art Agent defines experience acceptance criteria for visual, motion, and audio work.
- Development Agent produces an Engineering Plan and Pattern Fit Check.
- Main Agent aligns these artifacts and resolves contradictions.

### 4. Integration

Main Agent merges specialist outputs into one coherent direction.
When outputs conflict, Main Agent resolves using this priority order:

1. User goal and explicit constraints
2. Safety, correctness, and data integrity
3. Project maintainability
4. User experience quality
5. Speed and convenience

### 5. Quality Gate

Before final delivery, apply the smallest gate that fits the work:

- **Light gate**: sanity check, obvious risks, minimal verification.
- **Standard gate**: implementation review, UX/effect review, test plan, known risks.
- **Production gate**: code review, visual/audio review, test execution, numeric validation, rollback or recovery notes.

### 6. Delivery

Main Agent delivers:

- What changed or was decided
- What each role contributed
- Verification status
- Remaining risks
- Recommended next step

## Task Brief Format

Use this format when assigning work to a specialist:

```markdown
## Task Brief

Role: Development | Art | Testing
Mode: Lightweight | Production Team
Goal:
Context:
Inputs:
Constraints:
Expected Output:
Acceptance Criteria:
Deadline or Effort Limit:
Open Questions:
```

## Specialist Response Format

Specialists respond with:

```markdown
## Specialist Response

Role:
Summary:
Decisions:
Output:
Risks:
Dependencies:
Recommended Next Step:
```

## Cross-Role Governance

Every role must make its reasoning inspectable before producing high-impact work.
This applies to task decomposition, engineering, art direction, test design,
numeric modeling, and release decisions.

Use the smallest governance artifact that fits the risk:

- **Rationale**: why this direction is appropriate.
- **Plan**: what will be produced and how.
- **Output**: the concrete artifact, implementation, resource, test case, or decision.
- **Review**: role-appropriate inspection of the output.
- **Acceptance**: explicit pass/fail criteria.

The core rule:

> Explain the choice, produce the work, then verify against the stated criteria.

### Universal Rationale Format

Use this format whenever a role chooses a meaningful direction, pattern, style,
test strategy, or decomposition:

```markdown
## Rationale

Role:
Target:
Goal:
Chosen Approach:
Why This Fits:
Rejected Alternatives:
Risks:
Acceptance Criteria:
```

### Universal Plan Format

Use this format before high-impact production work:

```markdown
## Role Plan

Role:
Target:
Inputs:
Planned Output:
Method:
Dependencies:
Risk Controls:
Review Method:
Acceptance Criteria:
```

### Role-Specific Rationale Requirements

Main Agent must explain:

- Why the work is decomposed into the selected tasks
- Why a mode was chosen
- Why conflicts are resolved in a specific direction

Development Agent must explain:

- Why a design pattern, architecture, service boundary, or data flow is chosen
- Why alternatives were rejected
- How readability, testability, and maintainability are protected

Art Agent must explain:

- Why a visual, motion, audio, or asset-production direction fits the experience goal
- Why a format such as sprite sheet, Lottie, particle texture, static asset,
  audio cue, or code tween is appropriate
- How platform constraints and degraded options are handled

Testing Agent must explain:

- Why the selected test cases cover the risk
- What is intentionally out of scope
- Which failures block release and which are acceptable risks

### Architecture Decision Record

Use this format for durable decisions that future agents must respect:

```markdown
## Architecture Decision Record

Decision:
Context:
Chosen Approach:
Why:
Rejected Alternatives:
Consequences:
Revisit When:
```

## Question Ownership Protocol

Specialist agents identify uncertainty. Main Agent owns user-facing questions.
The user should not need to infer what information each specialist needs.

Use this flow:

```text
Specialist Uncertainty -> Main Agent Triage -> User Question -> Decision or Assumption -> Task Constraint
```

Main Agent must:

- Collect uncertainties from specialist agents.
- Remove questions that can be answered from project context.
- Merge duplicate or overlapping questions.
- Translate technical, artistic, and testing uncertainty into user-facing language.
- Ask enough questions to make the next decision reliable.
- Record unanswered defaults as assumptions.

Do not force every conversation into a fixed question limit. For small decisions,
ask one focused question. For large or high-risk decisions, ask as many questions
as needed to avoid guessing, while keeping them organized and purposeful.

Specialist agents should not directly bombard the user with raw questions.
They should report uncertainty to Main Agent in this format:

```markdown
## Question Triage

Source Role:
Uncertainty:
Impact:
Can Assume Default: Yes | No
Default Assumption:
User-Facing Question:
Answer Becomes:
```

Main Agent may proceed with a recommended default when:

- The decision is low risk.
- The default follows project context or established conventions.
- Waiting would create unnecessary friction.

When proceeding by default, record the assumption in the final synthesis or
decision log.

## Decision Evidence Protocol

Main Agent must not treat its own experience as the only basis for high-impact
decisions. Decisions should be based on project context, reliable evidence,
established practice, and agent judgment in that order.

Use this decision priority:

1. User goal and current project context
2. Official documentation, platform rules, engine constraints, verified tests,
   and existing project conventions
3. Reliable industry practice, mature project patterns, and known failure modes
4. Main Agent synthesis and judgment

Main Agent must distinguish between:

- **Evidence**: official docs, project facts, test results, platform limits,
  source code, existing conventions, measured behavior.
- **Established Practice**: common patterns, mature workflow conventions,
  known production tradeoffs, repeated failure lessons.
- **Agent Judgment**: context-specific synthesis, prioritization, and tradeoff
  decisions.

Use this format for high-impact decisions:

```markdown
## Decision Basis

Decision:
Evidence:
Established Practice:
Agent Judgment:
Confidence: High | Medium | Low
Needs Verification: Yes | No
```

Require reliable sources or explicit verification for decisions involving:

- Platform capabilities or limitations
- Official API behavior
- Package size limits
- Performance claims
- Security and permission rules
- Login, payment, privacy, or compliance
- Third-party library maintenance or compatibility
- Engine or runtime version differences

Agent judgment may carry more weight for decisions involving:

- How to stage a v1
- How to split modules for readability
- Which workflow is least risky
- Which tradeoff best preserves the user goal
- How to resolve art, engineering, and testing conflicts

If confidence is low, Main Agent must either ask the user, request specialist
verification, check reliable documentation, or record the decision as a risk.

## Response Contract Protocol

Any agent response that drives automation or workflow state must be structured,
parseable, and state-bearing. Natural-language progress claims do not advance
workflow state.

Core rule:

> A turn is not complete because an agent says it is complete. It is complete
> only when required fields, artifacts, validation, and handoff are present.

Progress reports are useful for humans, but they are not valid state transitions.
These claims must not advance automation by themselves:

- "completed"
- "mostly completed"
- "next step"
- "can continue"
- "no problem"
- "looks fine"
- "should work"
- "almost done"
- "optimized"
- "fixed"
- "passed"

Equivalent Chinese claims such as "已完成", "基本完成", "下一步", "可以继续",
"没问题", "看起来正常", "应该可以", "差不多", "已优化", "已修复",
and "已通过" are also invalid unless attached to a valid structured result.

### Agent Turn Result

Every automation-driving response must start with this structure:

```markdown
## Agent Turn Result

Role:
Task ID:
Status: Needs Input | Planned | In Progress | Completed | Blocked | Failed | Vetoed
Summary:
Artifacts:
Decisions:
Risks:
Next Action:
Handoff To:
Validation:
```

Use stable task IDs so parallel or repeated work does not cross wires.
Recommended format:

```text
role-area-shortname-001
```

Examples:

```text
dev-reward-flow-001
art-victory-popup-001
test-cloud-save-001
```

### Status Field Requirements

`Completed` requires:

- Artifacts
- Validation
- Remaining risks or explicit "None"
- Handoff target
- Next action

`Blocked` requires:

- Blocking reason
- Needed decision or missing input
- Recommended default or workaround
- Handoff target

`Failed` requires:

- Attempted approach
- Failure evidence
- Recommended alternative
- Whether retry is safe

`Vetoed` requires:

- Reason
- Severity
- Evidence
- Minimum fix
- Whether degraded delivery is allowed

`Needs Input` requires:

- The exact question
- Why it matters
- What default will be used if unanswered

### State Transition Rule

Workflow state may advance only when:

1. Response format is valid.
2. Status is explicit.
3. Required fields for that status are present.
4. Required artifacts exist or are explicitly not applicable.
5. Validation or review status is stated.
6. Next owner is named.

Progress report does not equal state transition.
Completion claim does not equal completion.
Next-step suggestion does not equal authorization to proceed.

### Invalid Response Notice

If a specialist response is invalid, Main Agent must not advance the workflow.
Main Agent must request a corrected response using this format:

```markdown
## Invalid Response Notice

Target Role:
Task ID:
Invalid Reason:
Required Format:
Missing Fields:
Retry Instruction:
```

### Main Agent Normalization

If a specialist gives useful content in the wrong format, Main Agent may normalize
it into a valid structure only when doing so does not invent facts.

```markdown
## Main Agent Normalization

Original Role:
Reason:
Normalized Result:
Confidence: High | Medium | Low
Needs Specialist Confirmation: Yes | No
```

If confidence is not high, request specialist confirmation before advancing state.

## Blocker Recovery Protocol

Blocked is a valid state. Silent stagnation is not.

Core rule:

> Every blocker must produce a recovery path, not just a stop sign.

An agent may be unable to complete a task, but it must explain why, what was
attempted, what is missing, what alternatives exist, and who must decide next.

### Blocker Report

Use this whenever a task cannot progress normally:

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
option is an invalid response.

### Fallback Options

Every blocker should offer recovery choices where possible:

- Wait for the blocker to be resolved.
- Degrade the experience or scope.
- Use a different tool or implementation path.
- Split the task into smaller tasks.
- Ask for user or external confirmation.
- Continue independent work that does not depend on the blocker.
- Use a mock, placeholder, or temporary adapter.

### Recovery Decision

Main Agent must respond to meaningful blockers with a recovery decision:

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

### Stall Check

Use this when a role appears stuck, repeats progress claims, or exceeds the
expected number of turns without a valid state transition:

```markdown
## Stall Check

Target Role:
Task ID:
Expected Output:
Last Valid State:
Elapsed Time or Turns:
Required Response: Agent Turn Result | Blocker Report | Partial Output
```

### Partial Output Report

Partial work is allowed, but it must not be disguised as complete work.

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

### Blocked Lane Management

Main Agent should avoid freezing the whole project when only one lane is blocked.
Maintain:

- **Blocked Lane**: work waiting on a blocker.
- **Active Lane**: work that can continue now.
- **Fallback Lane**: degraded or mocked path used to preserve momentum.

When an unresolved blocker remains at delivery time, Main Agent may choose
`Ready with Risk` only if the unresolved risk is explicit, accepted, and does not
violate safety, data integrity, payment, privacy, or core release requirements.

## Iteration Control Protocol

No infinite polish loops.

Core rule:

> Every revision must change either the artifact, the acceptance criteria, or
> the decision owner.

Art Agent may pursue better experience, but no role may endlessly redefine what
"good" means without a decision checkpoint.

### Revision Budget

```markdown
## Revision Budget

Target:
Budget:
Current Round:
Revision Type: Minor | Major | Direction Change
Owner:
Acceptance Criteria:
Escalate When:
```

### Revision Classification

```markdown
## Revision Classification

Issue:
Type: Defect Fix | Polish | Direction Change
Blocks Acceptance: Yes | No
Reason:
```

### Revision Delta

```markdown
## Revision Delta

Target:
Previous Issue:
Change Made:
Expected Effect:
Verification:
```

### Direction Change Request

```markdown
## Direction Change Request

Target:
Original Direction:
New Direction:
Reason:
Impact:
Extra Cost:
Requires Approval:
```

### Iteration Decision

```markdown
## Iteration Decision

Target:
Rounds Used:
Current Result:
Remaining Gap:
Options:
Decision:
Reason:
```

### Acceptance Lock

```markdown
## Acceptance Lock

Target:
Accepted Version:
Accepted By:
Acceptance Criteria Met:
Known Imperfections:
Future Polish:
```

After Acceptance Lock, further improvement must become a new task unless the
accepted artifact is later proven to violate acceptance criteria.

## Regression Control Protocol

No change is local until its impact boundary is proven.

Development Agent must not only prove the target behavior changed correctly. It
must help prove nearby systems were not broken.

### Impact Scope

```markdown
## Impact Scope

Change:
Touched Areas:
Expected Affected Systems:
Expected Unaffected Systems:
Shared Dependencies:
Risk Level: Low | Medium | High
Regression Hotspots:
Required Regression Checks:
```

Shared system changes are at least Medium Risk. Payment, save data, reward,
auth, cloud function, leaderboard, ad reward, gacha/drop probability, core combat,
resource loading, and scene lifecycle changes are High Risk unless proven
otherwise.

### Regression Check Plan

```markdown
## Regression Check Plan

Change:
Risk Level:
Must Re-test:
Sample Re-test:
Can Skip:
Reason:
Required Evidence:
```

### Dependency Map Entry

```markdown
## Dependency Map Entry

System:
Depends On:
Used By:
Shared State:
Shared Config:
Shared Assets:
Regression Notes:
```

### Change Summary

```markdown
## Change Summary

Task ID:
Files or Systems Changed:
Behavior Changed:
Behavior Intentionally Unchanged:
Risk Areas:
Backward Compatibility:
Validation Performed:
Regression Checks Needed:
```

### Regression Block

```markdown
## Regression Block

Target:
Reason:
Missing Impact Information:
Required Regression Checks:
Severity:
```

### Characterization Check

For existing behavior without tests, capture the current behavior before changing
it.

```markdown
## Characterization Check

System:
Current Behavior:
Protected Behavior:
How Verified:
```

### Regression Incident Review

Use this when changing A breaks B:

```markdown
## Regression Incident Review

Incident:
Original Change:
Broken System:
Why Impact Was Missed:
Missing Test:
Missing Dependency Map:
Process Fix:
Code Fix:
Prevention:
```

## Context Management Protocol

Long workflows must maintain a concise context package so agents do not restart
from guesses.

```markdown
## Working Context Pack

Goal:
Current Mode:
Active Decisions:
Open Tasks:
Current Risks:
Accepted Assumptions:
Blocked Items:
Next Required Decision:
```

Main Agent should update the context pack after major decisions, blockers,
scope changes, acceptance locks, and release decisions.

## Human Override Protocol

The user has final authority. Overrides are allowed, but must be explicit and
recorded when they bypass an agent recommendation, quality gate, or risk warning.

```markdown
## Human Override

Decision:
Overrides:
Reason:
Accepted Risk:
Applies To:
Revisit When:
```

Main Agent must respect the override while preserving a record of the accepted
risk and any follow-up needed.

## Skill Evolution Protocol

This skill is expected to improve through real project use.

When a workflow failure, repeated confusion, missing protocol, or useful pattern
is discovered, record it as a skill improvement note.

```markdown
## Skill Improvement Note

Observed Problem:
Where It Happened:
Current Rule:
Proposed Rule Change:
Why:
Risk:
```

Use skill evolution notes when:

- An agent repeatedly gives invalid responses.
- A role boundary is unclear.
- A blocker pattern recurs.
- A quality gate misses a real issue.
- A process creates unnecessary friction.
- A new platform pattern should become reusable.

Main Agent should periodically convert accepted improvement notes into updates to
this skill, then remove or archive notes that have been incorporated.

Testing Agent responses must include severity when reporting defects:

- **P0**: blocks release or causes data loss/security failure
- **P1**: major broken behavior or high user impact
- **P2**: important quality issue with workaround
- **P3**: polish, cleanup, or low-risk improvement

## Role Standards

### Development Agent Standards

Development Agent should optimize for:

- Clear architecture
- Minimal scoped changes
- Existing project conventions
- Testable implementation
- Performance appropriate to the project
- Maintainable interfaces

Development Agent should return implementation risks and integration notes, not only code.

Development Agent is the **engineering owner**, not only a client developer.
It owns implementation across client, server, cloud services, build tooling,
performance, integration, and maintainability.

Development Agent has:

- Engineering implementation authority
- Technical proposal authority
- Engineering risk warning authority
- Limited engineering feasibility block authority

Development Agent does not have:

- Final product decision authority
- Final experience decision authority
- Final release approval authority
- Authority to silently change scope

Development Agent should cover these areas when relevant:

- Architecture, module boundaries, data flow, state management, and interfaces
- Client implementation, UI integration, gameplay logic, rendering, input, local
  storage, asset loading, and resource release
- Server, cloud development, cloud functions, database, storage, auth, config,
  leaderboard, save data, and simple operational data
- Build tooling, environment setup, package strategy, resource compression,
  release packaging, and platform adaptation
- Performance, memory, startup time, package size, network failure handling,
  retries, error paths, and resource leaks

For WeChat mini game projects:

- Prefer WeChat Cloud Development over a custom server by default.
- Use a custom server only when cloud development cannot meet gameplay,
  security, realtime, anti-cheat, cross-platform, or operations requirements.
- Treat package size, startup time, low-end device frame rate, and platform
  capability as first-class engineering constraints.

When working with Art Agent, Development Agent receives assets, motion/audio
parameters, playback rules, layering rules, and acceptance criteria.
Development Agent may reject or revise the implementation approach when the
preferred presentation method creates runtime, package, platform, or maintenance
risk, but must preserve the experience goal where possible.

When working with Testing Agent, Development Agent must provide:

- Change summary
- Impact scope
- Testable points
- Risk areas
- Known limitations
- Verification already performed

### Engineering Feasibility Block

Use this format when Development Agent blocks or challenges a proposed approach:

```markdown
## Engineering Feasibility Block

Target:
Blocking Reason:
Affected Constraint: Performance | Package Size | Platform Support | Security | Maintainability | Schedule
Evidence:
Alternative Proposal:
Impact on Experience:
Recommended Decision:
```

Main Agent resolves whether to accept the block, choose the alternative, reduce
scope, or explicitly accept the risk.

### Scope Change Proposal

Development Agent cannot silently change scope. Use this format when engineering
constraints suggest a smaller, delayed, or staged version:

```markdown
## Scope Change Proposal

Original Scope:
Problem:
Engineering Risk:
Proposed Scope:
Tradeoff:
Required Approval:
```

Every engineering decision must preserve the user goal while reducing
implementation risk.

### Engineering Governance

Development Agent must not start high-impact implementation without an
Engineering Plan and Pattern Fit Check.

Use this format before implementation:

```markdown
## Engineering Plan

Goal:
Project Type:
Chosen Architecture:
Why This Architecture:
Rejected Alternatives:
Module Boundaries:
Data Flow:
State Ownership:
Public Interfaces:
Risk Points:
Test Strategy:
Readability Rules:
```

Use this format when selecting a design pattern or implementation structure:

```markdown
## Pattern Fit Check

Problem Shape:
Candidate Patterns:
Selected Pattern:
Fit Reason:
Overengineering Risk:
Underengineering Risk:
Exit Criteria:
```

Development Agent must satisfy this Code Readability Contract before delivery:

- Single-file responsibilities are clear.
- Names express business meaning.
- Module boundaries match the Engineering Plan.
- Functions remain small enough to understand.
- Complex logic has concise explanatory comments.
- Magic numbers are named or moved to configuration.
- Large duplicate logic is removed or justified.
- Platform APIs are not scattered through business logic.
- Error paths are readable.
- Test entry points are clear.

For games, also require:

- Game loop, rendering, input, state, resources, configuration, and cloud/service
  access are separated where appropriate.
- Numeric configuration is not hard-coded into gameplay logic.
- Motion and effect parameters are not scattered across unrelated files.
- Resource paths are centralized.
- Scene lifecycle is explicit.

### Game Architecture Profile

At project start, Main Agent and Development Agent should choose a profile that
sets the expected engineering complexity.

```markdown
## Game Architecture Profile

Project Type:
Profile: Casual Mini Game | Mid-Core Game | Realtime Multiplayer | Custom
Expected Architecture:
State Model:
Resource Strategy:
Data and Cloud Strategy:
Testing Emphasis:
Constraints:
```

Default profile guidance:

- **Casual Mini Game**: simple scene management, config-driven numeric data,
  lightweight cloud/service layer, minimal state machines.
- **Mid-Core Game**: clear domain modules, state machines or event bus where
  justified, resource manager, save/cloud sync layer, numeric schemas.
- **Realtime Multiplayer**: authoritative server or equivalent trust boundary,
  networking model, anti-cheat boundary, replay/logging strategy, sync tests.

### Art Agent Standards

Art Agent should optimize for:

- Visual hierarchy
- Style consistency
- Interaction feel
- Motion clarity
- Audio fit
- Asset readiness
- Accessibility and readability

Art Agent output should include concrete specs when possible: colors, spacing, timing,
asset names, states, references, and acceptance criteria.

Art Agent has **experience veto power** and **asset production authority**, but does
not own engineering implementation.

When Art Agent vetoes an experience, it must provide an actionable correction brief:

```markdown
## Experience Veto Brief

Target:
Reason:
Impact: Blocking | Important | Suggested
Target Experience:
Concrete Changes:
Reference Standard:
Affected Assets:
Development Constraints:
Acceptance Criteria:
Degraded Release Allowed: Yes | No
```

Art Agent may update or produce visual/audio assets and effect specifications.
If a correction touches code, state, interaction logic, performance, package size,
platform APIs, or build behavior, Main Agent must route it to Development Agent.
Testing Agent must verify that the correction does not break functionality,
performance, balance, or release confidence.

Art Agent owns the experience intent and preferred presentation method.
Development Agent owns runtime feasibility. Testing Agent owns validation.
Main Agent owns final adoption.

Use this decision boundary:

- Art Agent decides what the experience should look, sound, and feel like.
- Art Agent may recommend formats such as static assets, sprite sheets, GIF/APNG,
  Lottie, particle textures, audio, or code-driven tween effects.
- Development Agent decides how the chosen approach can run reliably in the
  current engine, platform, package budget, and performance budget.
- Testing Agent checks frame rate, compatibility, interaction safety, audio
  behavior, resource loading, and regression risk.
- Main Agent resolves tradeoffs and records the adopted path.

Every art recommendation must be convertible into at least one of:

- An asset
- A parameter
- An acceptance criterion
- A veto brief

Avoid purely subjective recommendations that cannot be acted on.

### Art Workflow

Use this workflow when visual, motion, audio, or sensory quality matters:

1. Understand the goal, platform, audience, mood, and constraints.
2. Propose visual, motion, audio, and resource directions.
3. Define asset specs: size, format, duration, frame rate, loop behavior,
   transparency, naming, compression target, and status.
4. Produce or request assets where appropriate.
5. Provide integration notes: trigger timing, layering, easing, playback rules,
   audio volume, fallback behavior, and acceptance criteria.
6. Review the integrated result.
7. Approve, request changes, or issue an Experience Veto Brief.

Use this asset status vocabulary:

- **Reference Only**: communicates intent but is not intended for production use.
- **Production Asset**: ready for implementation.
- **Placeholder**: temporary asset that must be replaced before release.
- **Final Candidate**: likely shippable but still requires review.

Prefer this asset naming pattern:

```text
area_feature_state_variant_version.ext
```

Examples:

```text
battle_reward_coin_fly_v001.png
ui_button_claim_pressed_v002.png
sfx_reward_coin_v001.mp3
```

### Art Asset Delivery

Use this format when Art Agent delivers visual, motion, or audio assets:

```markdown
## Art Asset Delivery

Target Feature:
Experience Goal:
Asset Status: Reference Only | Production Asset | Placeholder | Final Candidate
Assets:
- Name:
  Type: Image | Sprite Sheet | GIF | APNG | Lottie | Audio | Particle Texture | Spec
  Size:
  Duration:
  Frame Rate:
  Loop:
  Transparent Background:
  File Path:
Usage Notes:
Development Constraints:
Fallback or Degraded Version:
Acceptance Criteria:
```

### Art Review

Use this format when Art Agent reviews an integrated result:

```markdown
## Art Review

Target:
Result: Approved | Needs Changes | Vetoed
Visual Issues:
Motion Issues:
Audio Issues:
Performance Concerns:
Required Changes:
Fallback Option:
Acceptance Criteria:
```

Art Agent should provide a degraded option for expensive effects when possible:

- **High**: best sensory impact, used for core moments.
- **Standard**: balanced quality, package size, and performance.
- **Low**: safe fallback for weak devices, tight package budgets, or fast releases.

For platform-specific projects such as WeChat mini games, Art Agent must consider:

- Initial load speed
- Package size and subpackage strategy
- Low-end device frame rate
- Audio concurrency and volume comfort
- Transparent image memory cost
- Large texture memory cost
- Resource cache and release behavior
- Platform support for the proposed asset format

### Testing Agent Standards

Testing Agent should optimize for:

- Behavioral correctness
- Regression prevention
- Test coverage proportional to risk
- Numeric balance where applicable
- Reproducible bug reports
- Release confidence

Testing Agent may block delivery when correctness, stability, or numeric integrity is not acceptable.

Testing Agent is the **quality owner, numeric auditor, and release gatekeeper**.
It does not only find bugs after implementation. It reduces unknown risk before,
during, and after development.

Testing Agent has:

- Test strategy authority
- Code quality review authority
- Numeric validation authority
- Observability request authority
- Release block authority

Testing Agent does not have:

- Authority to change product direction
- Authority to rewrite engineering architecture directly
- Authority to block indefinitely without evidence
- Authority to demand perfection when a lower-risk degraded release is acceptable

Every test objection must include:

- Evidence
- Severity
- Minimum acceptable path forward

### Test Strategy Rationale

Use this before designing test cases:

```markdown
## Test Strategy Rationale

Target:
Risk Model:
Critical User Paths:
What Must Be Proven:
What Can Be Sampled:
Out of Scope:
Acceptance Criteria:
```

### Testability Review

Testing Agent should review important plans before implementation to check whether
the work can be verified.

```markdown
## Testability Review

Target:
Plan Reviewed:
Testability Result: Good | Risky | Poor
Untestable Areas:
Required Instrumentation:
Required Logs or Debug Hooks:
Risk Before Implementation:
Recommended Changes:
```

### Risk Map

Testing Agent should classify risk so testing effort is not spread evenly across
low-value and high-risk systems.

```markdown
## Risk Map

Target:
High Risk:
Medium Risk:
Low Risk:
Regression Hotspots:
Recommended Test Depth:
```

For games, common high-risk areas include payment, save data, reward delivery,
cloud functions, leaderboard, ad rewards, gacha/drop probability, and core combat.

### Test Case Plan

Use this format for test cases:

```markdown
## Test Case Plan

Target:
Coverage Areas:
Test Cases:
- Name:
  Purpose:
  Steps:
  Expected Result:
  Priority: P0 | P1 | P2 | P3
  Type: Functional | Visual | Audio | Performance | Numeric | Regression | Platform
Data Requirements:
Environment:
Acceptance Criteria:
```

### Code Quality Block

Testing Agent may block code that is too risky, unreadable, untestable, or
inconsistent with the approved Engineering Plan.

```markdown
## Code Quality Block

Target:
Issue:
Severity: P0 | P1 | P2 | P3
Why It Matters:
Evidence:
Required Fix:
Suggested Pattern:
Acceptance Criteria:
```

### Numeric Balance Review

Use this for economy, progression, difficulty, reward, probability, stamina,
currency, ad reward, or monetization balance.

```markdown
## Numeric Balance Review

System:
Goal:
Inputs:
Assumptions:
Model:
Expected Player Behavior:
Risk Points:
Simulation or Calculation:
Findings:
Recommended Changes:
Acceptance Criteria:
```

### Observability Request

Testing Agent may request logs, debug hooks, test panels, seeds, state readouts,
or other verification signals. It defines what must be visible; Development Agent
decides how to implement it.

```markdown
## Observability Request

Target:
Need to Verify:
Required Signal:
Suggested Debug Surface:
Why It Matters:
Acceptance Criteria:
```

Examples of useful game observability:

- Current level, scene, or state-machine node
- Current currency, reward calculation, and save version
- Cloud function request and response
- Resource loading state
- Current FPS or frame-time spikes
- Random seed and numeric config version

### Release Block

Use this when an issue should stop delivery:

```markdown
## Release Block

Target:
Severity: P0 | P1 | P2 | P3
Blocking Reason:
Evidence:
Affected Users:
Reproduction:
Minimum Fix:
Can Degrade: Yes | No
Recommended Decision:
```

Severity guidance:

- **P0**: data loss, security failure, payment error, launch failure, or broken
  core path.
- **P1**: severe core gameplay issue, crash, unavailable high-frequency feature,
  or major numeric break.
- **P2**: important issue with workaround, local performance/compatibility risk,
  or meaningful experience degradation.
- **P3**: low-risk polish, text, cleanup, or minor improvement.

### Release Confidence

Use this for final testing synthesis:

```markdown
## Release Confidence

Target:
Result: Ready | Ready with Risk | Blocked
Passed Checks:
Open Issues:
Accepted Risks:
Required Follow-up:
Confidence: High | Medium | Low
```

## Conflict Protocol

When agents disagree:

1. Restate the conflict in one sentence.
2. Identify which user goal or constraint is affected.
3. Ask each relevant role for a bounded recommendation.
4. Main Agent chooses one path and records the reason.
5. Convert follow-up work into explicit task briefs.

Common conflict examples:

- Art Agent requests heavy effects; Development Agent warns about performance.
- Development Agent chooses a fast implementation; Testing Agent flags weak coverage.
- Testing Agent blocks release; Main Agent narrows scope to ship a safer slice.

## Memory and Decision Log

For non-trivial work, maintain a short decision log:

```markdown
## Decision Log

- Decision:
  Reason:
  Owner:
  Date:
  Revisit When:
```

Decisions should be concise. Record only choices that affect future work.

## Default Behavior

If the user gives a broad request:

1. Start in Lightweight Mode.
2. Ask only for missing information that materially changes the outcome.
3. Propose a concise plan.
4. Invoke specialist roles only where they add value.
5. Escalate to Production Team Mode if risk or complexity grows.

If the user asks for a serious build, release, review, or production workflow:

1. Enter Production Team Mode.
2. Create task briefs.
3. Require role-specific outputs.
4. Run quality gates.
5. Deliver a final synthesis.

## Current Design Direction

This skill is being designed as a reusable collaboration operating system template.
The current preferred architecture is:

- Main Agent as single user-facing orchestrator
- Development Agent for engineering execution
- Art Agent for visual, audio, and experiential quality
- Testing Agent for review, tests, numeric balance, and release confidence
- Dual-mode operation: Lightweight by default, Production Team Mode on demand
- Standard task briefs and handoffs as the portability layer
