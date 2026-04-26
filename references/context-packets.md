# Context Packets

Use this protocol to keep specialist agents focused and prevent context overload.

## Core Rule

Main Agent keeps global context. Specialist agents receive bounded context packets
for their role, task, and decision point.

Do not send full history by default. Send only context that changes the specialist's
work or acceptance criteria.

Use this memory split:

```text
Raw Trace -> Project Memory -> Skill Evolution
```

- **Raw Trace**: chat history, temporary screenshots, failed attempts, logs,
  drafts, and old feedback. Archive it; do not load by default.
- **Project Memory**: short current truth for this project. Load and slice it
  when assigning work.
- **Skill Evolution**: reusable protocols promoted from repeated or general
  lessons. Do not store project-specific facts here.

Core distinction:

```text
Skill = reusable protocols
Project Memory = active project truth
Evidence Archive = proof and history
Raw Chat = not a source of truth unless summarized
```

## Context Budget Rule

A context item is included only if it changes the specialist's decision, output,
risk handling, or acceptance criteria.

Before adding context, ask:

- Would this change the role's output?
- Is it still current?
- Is it within this role's responsibility?
- Has it already been replaced by a shorter active decision?
- Is the source reliable enough for the decision being made?

## Specialist Agent Lifecycle

Before creating or spawning a specialist agent, Main Agent must perform an
agent reuse check.

Reuse an existing same-role specialist when:

- The role is the same.
- The task lane is still active or related.
- The existing agent has useful context that should not be fragmented.
- The agent is not blocked by stale assumptions, bad context, or a closed task.

Create a new specialist only when:

- No same-role agent exists.
- The existing same-role agent is closed, unavailable, or context-polluted.
- Isolation requires a fresh reviewer who has not seen biased information.
- Parallel work is genuinely independent and write scopes or review scopes do
  not overlap.

If Main Agent accidentally creates a duplicate same-role agent, it must close the duplicate, record which agent remains authoritative, and continue the lane with a Context Refresh.

## Agent Reuse Decision

Use this before delegation when any same-role specialist may already exist:

```markdown
## Agent Reuse Decision

Role Needed:
Existing Same-Role Agents:
Reuse Decision: Reuse Existing | Create New | Close Duplicate
Authoritative Agent:
Reason:
Context Refresh Needed: Yes | No
Isolation Risk:
Next Action:
```

## Explicit User-Requested Specialist Lane

When the user explicitly asks for a role to participate, that role becomes an
active specialist lane until the user closes it, the lane returns `Completed`
with accepted evidence, or Main Agent records a protocol-level exemption.

This applies especially to Testing Agent and Audit Agent.

Main Agent must not replace requested specialist participation with automated
test output. Automated test output is evidence, not Testing Agent participation.

For every substantial change after a requested specialist lane is active, Main
Agent must either:

- Send a `Context Refresh` to the existing same-role agent and obtain a fresh
  role output.
- Record why the change does not affect that lane.
- Ask the user whether to close the lane.

Use this ledger when specialist participation affects workflow trust:

```markdown
## Specialist Participation Ledger

Task ID:
Requested Specialist Roles:
Active Specialist Lanes:
Testing Agent Participation: Present | Not Needed | Missing
Audit Agent Participation: Present | Not Needed | Missing
Automated Evidence:
Specialist Outputs:
Exemptions:
Next Required Specialist Action:
```

## Working Context Pack

Main Agent maintains this across the whole project:

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

Update it after major decisions, blockers, scope changes, acceptance locks,
release decisions, and skill evolution notes.

## Project Memory

Use this as the compact source of current project truth:

```markdown
## Project Memory

Status: Active
Last Updated:
Active Decisions:
Accepted Assumptions:
Current Architecture:
Art Direction:
Testing Bar:
Known Risks:
Open Questions:
Do Not Repeat:
Source Documents:
```

Project Memory should stay short. If it grows too long, split by domain and keep
only the active slice in specialist packets.

## Specialist Context Packet

Use this when assigning work to a responsibility agent:

```markdown
## Specialist Context Packet

Role:
Task ID:
Context Version:
Source Documents:
Last Updated:
Goal:
Mode:
Relevant Decisions:
Relevant Constraints:
Inputs and Artifacts:
Acceptance Criteria:
Known Risks:
Out of Scope:
Dependencies:
Required Output Format:
```

## Context Diet Rules

Include:

- User goal and success criteria
- Current accepted decisions
- Constraints that affect the role
- Artifacts the role must inspect or produce
- Risks the role must handle
- Output format and state transition requirements

Exclude unless needed:

- Long chat history
- Rejected alternatives
- Other roles' unrelated reasoning
- Stale assumptions
- Full codebase summaries
- Old review comments already resolved

## Role-Specific Context

### Development Agent

Include engineering constraints, current architecture, relevant files/modules,
platform limits, art specs that affect implementation, testability requirements,
and regression hotspots.

Do not include unrelated aesthetic debate unless it changes implementation.

### Client Development Agent

Include player-facing behavior, UI/HUD requirements, input model, rendering and
asset constraints, local state limits, performance budget, accepted server
contract, and desync/reconnect risks.

Do not include private server implementation details unless they affect the
client contract or debugging evidence.

### Server Development Agent

Include authority model, room/match requirements, network model, persistence
needs, trust boundary, security risks, reconnect needs, scaling assumptions,
client contract needs, and server-side test requirements.

For strong online games, include enough context for
`Strong Online Server Readiness Plan`: game type, expected concurrency, match or
room model, economy/reward/ranking risk, anti-cheat expectation, operations
constraints, and what the user does not understand well enough to review.

For reconnect work, include identity proof assumptions, session token policy,
room retention rules, recovery mode, sequence/request ID policy, settlement
safety requirements, and client UX contract needs.

Do not include visual polish debate unless it changes authoritative timing,
payloads, or server performance.

### Art Agent

Include experience goal, audience, style decisions, platform/resource constraints,
current implementation screenshots or previews, asset requirements, and acceptance
criteria.

Do not include unrelated code details unless they constrain format, timing,
performance, package size, or platform support.

### Testing Agent

Include original requirement, accepted scope, engineering plan, art acceptance
criteria, change summary, impact scope, known risks, and required release bar.

Do not include speculative implementation ideas that were rejected unless they
explain a current risk.

### Audit Agent

Include the exact claim being audited, the source response, acceptance criteria,
artifacts, validation evidence, loaded protocols, tool outputs, known limits, and
the decision that would advance if the audit accepts the claim.

Do not include unrelated conversation history, persuasive summaries, or the
audited agent's self-confidence unless they are part of the claim being audited.

## Context Refresh

When a task lasts multiple turns, Main Agent should refresh the specialist packet
instead of appending raw history.

```markdown
## Context Refresh

Task ID:
What Changed:
Still True:
No Longer Relevant:
New Constraints:
Next Required Output:
```

## Context Overflow Handling

If a specialist seems confused, repeats stale decisions, or ignores constraints:

1. Stop the lane.
2. Issue a Context Refresh.
3. Ask for a new Agent Turn Result.
4. Record a Skill Improvement Note if the same confusion recurs.
