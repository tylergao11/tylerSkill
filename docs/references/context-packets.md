# Context Packets

Use this protocol to keep specialist agents focused and prevent context overload.

## Core Rule

Main Agent keeps global context. Specialist agents receive bounded context packets
for their role, task, and decision point.

Do not send full history by default. Send only context that changes the specialist's
work or acceptance criteria.

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

## Specialist Context Packet

Use this when assigning work to a responsibility agent:

```markdown
## Specialist Context Packet

Role:
Task ID:
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
