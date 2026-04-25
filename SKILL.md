---
name: agent-collaboration-os
description: A portable Agent Collaboration Operating System workflow for coordinating a main agent, development agent, art/audio agent, and testing agent across game projects or other production work. Use when planning, building, reviewing, or shipping work that benefits from role-based multi-agent collaboration, dual-mode execution, standardized task briefs, quality gates, context packets, and handoff protocols.
---

# Agent Collaboration OS

Use this skill to run a portable multi-agent collaboration workflow.

The short file is the operating-system kernel. Load detailed protocols from
`references/` only when the current task needs them.

## File Encoding

All project documentation, skill files, reference files, templates, and generated
workflow notes must be read and written as UTF-8. This project uses Chinese text;
using the wrong encoding can corrupt formatting and content.

Use precise English for agent-facing Markdown such as `SKILL.md`, `references/`,
`templates/`, `profiles/`, and `modules/`. Use Chinese where practical for
user-facing Markdown such as repository usage guides.

## Core Principles

- **Main Agent owns orchestration**: user dialogue, decomposition, decisions, conflict resolution, and final synthesis.
- **Development Agent owns engineering**: client, server/cloud, architecture, implementation, build, performance, and maintainability.
- **Art Agent owns experience intent**: visuals, UI/UX, motion, audio, asset specs, sensory polish, and experience review.
- **Testing Agent owns quality risk**: test strategy, code review, numeric validation, observability, regression, and release confidence.
- **Explain before producing**: important work follows `Rationale -> Plan -> Output -> Review -> Acceptance`.
- **Use acceptance and risk as the driver**: tests first for deterministic logic, acceptance first for experiential work, risk map first for high-risk systems.
- **Progress claims do not advance state**: automation advances only through valid structured results.
- **Blocked is a state, not an ending**: every blocker must include evidence, fallback options, and a recommended recovery path.
- **Small is allowed, silent shrink is not**: scoped-down delivery requires explicit approval and recorded tradeoffs.
- **The skill must evolve**: recurring failures become skill improvement notes.

## Reuse Architecture

This skill is a workflow kernel, not a fixed game template.

Use this layering:

```text
Agent OS Workflow -> Game Architecture Profile -> Reusable Capability Modules -> Optional Game Template
```

- **Agent OS Workflow**: stable collaboration, decision, evidence, and quality protocols.
- **Game Architecture Profile**: project type guidance such as casual mini game, mid-core game, realtime multiplayer, or custom.
- **Reusable Capability Modules**: portable tools such as debug capture, config validation, asset manifest checks, cloud boundaries, reward trace, or numeric simulation.
- **Game Template**: optional and only justified after repeated projects share the same gameplay shell.

Prefer reusing workflow and capability modules before reusing a whole game shell.

## Operating Modes

### Lightweight Mode

Default for small, exploratory, or low-risk work.

- Main Agent handles most work directly.
- Specialist roles are invoked only when their expertise changes the outcome.
- Keep artifacts short but still structured when they affect state.

### Production Team Mode

Use when the user asks for strict process, high quality, full review, or complex production.

Trigger phrases may include:

- "进入制作组模式"
- "全流程审查"
- "严格模式"
- "用完整 agent 流程"

Production Team Mode requires:

- Task briefs before specialist work
- Role-specific rationale and plans
- Context packets for each specialist
- Quality gates before delivery
- Final synthesis with decisions, risks, and verification status

## Default Workflow

1. Intake: clarify goal, audience, success criteria, constraints, current context, risk, and mode.
2. Decomposition: Main Agent explains why the selected task split is correct.
3. Context Packet: Main Agent sends each specialist only the context needed for that role.
4. Specialist Work: roles return structured, state-bearing responses.
5. Integration: Main Agent merges outputs and resolves conflicts.
6. Quality Gate: use the smallest gate that fits the risk.
7. Delivery: summarize what changed, what was verified, remaining risks, and next owner.
8. Evolution: record process failures or reusable discoveries as skill improvement notes.

## Required Formats

### Task Brief

```markdown
## Task Brief

Role:
Mode:
Task ID:
Goal:
Context Packet:
Inputs:
Constraints:
Expected Output:
Acceptance Criteria:
Deadline or Effort Limit:
Open Questions:
```

### Agent Turn Result

Any response that drives automation must start with:

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

Workflow state may advance only when the response is valid, the status is explicit,
required fields are present, artifacts are present or not applicable, validation is
stated, and the next owner is named.

## Protocol Index

Load only what is needed:

- `references/context-packets.md`: when delegating to any specialist or resuming long work.
- `references/installation.md`: when installing this skill globally or vendoring it into a consumer project.
- `references/protocol-routing.md`: when deciding which protocol to load for a situation.
- `references/response-contract.md`: when a role response may drive automation, completion, handoff, or state transition.
- `references/blocker-recovery.md`: when a task stalls, fails, lacks tools, lacks permissions, or cannot complete normally.
- `references/debug-bisection.md`: when a bug has many hypotheses, fixes have failed, or an agent wants to guess-and-change code.
- `references/preflight-debug-capture.md`: when designing pre-embedded debug capture, true-device diagnostics, observability plans, or trace-based evidence.
- `references/development-daily-tools.md`: when Development Agent needs design packet validation, impact analysis, or diff risk review during routine implementation.
- `references/reusable-modules.md`: when deciding whether code should become reusable, portable, or part of a long-term capability module.
- `references/role-development.md`: when planning or reviewing architecture, implementation, cloud/server work, readability, or game engineering.
- `references/role-art.md`: when handling visuals, UI/UX, motion, audio, assets, experience review, or art vetoes.
- `references/role-testing.md`: when designing tests, risk maps, code review, numeric balance, observability, release blocks, or release confidence.
- `references/regression-iteration.md`: when revisions loop, art/dev disagree repeatedly, or a change may break nearby systems.
- `references/project-assets-governance.md`: when managing project docs, screenshots, recordings, logs, evidence, decision references, archival, or cleanup.
- `references/production-operations.md`: when triaging production incidents, GitHub/CI fixes, releases, hotfixes, or rollback decisions.
- `references/permission-environment.md`: when an operation may mutate files, cloud state, production config, data, secrets, or deployment environments.
- `references/release-rollback.md`: when preparing release notes, versioned releases, rollback plans, or post-release checks.
- `references/data-privacy-trust-boundary.md`: when handling user data, cloud writes, rewards, auth, payments, privacy, or anti-cheat trust boundaries.
- `references/asset-provenance.md`: when creating, importing, reviewing, or shipping art/audio/assets with source or license concerns.
- `references/runtime-versioning-budget.md`: when tracking skill/runtime versions, loaded protocols, task budgets, package budgets, context budgets, or performance budgets.
- `references/evolution.md`: when a process failure or reusable workflow improvement should update the skill.

## Context Policy

Main Agent keeps the full working memory. Specialist agents receive bounded
context packets, not the whole project history.

Each specialist context packet must include:

- Task goal
- Relevant decisions
- Relevant constraints
- Inputs and artifacts
- Acceptance criteria
- Known risks
- Out-of-scope items
- Required output format

Do not overload specialist agents with unrelated debate history, other roles'
private reasoning, stale alternatives, or full project context unless needed.

## Decision Evidence

For high-impact decisions, distinguish:

- **Evidence**: official docs, project facts, tests, platform limits, source code, measured behavior.
- **Established Practice**: mature patterns, common tradeoffs, known failure modes.
- **Agent Judgment**: context-specific synthesis and prioritization.

Use reliable sources or explicit verification for platform capabilities, APIs,
package limits, performance claims, security, payment, privacy, third-party
library status, and engine/runtime differences.
