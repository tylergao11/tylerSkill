# Main Agent Decision Review

Use this protocol when specialist agents produce architecture diagrams, server
plans, art directions, testing reports, audit reports, release plans, or any
output that the user may not be able to judge directly.

Main Agent owns translation from specialist reasoning into user decisions.

## Core Rule

Do not pass specialist complexity directly to the user as if it were a decision.

Main Agent must explain what the output means, what the user needs to decide,
what risks remain, what questions must go back to specialists, and what evidence
will prove the decision is safe enough.

## Main Agent Specialist Review

```markdown
## Main Agent Specialist Review

Source Role:
Source Artifact:
What This Means:
User Decisions Needed:
Risks I See:
Questions For Specialist:
Testing Required:
Audit Required:
Recommendation:
Decision Options:
- Option:
  Pros:
  Cons:
  When To Choose:
```

## User Decision Brief

Use this shorter form when the user only needs to choose between options:

```markdown
## User Decision Brief

Decision Needed:
Recommended Choice:
Why:
Risk:
Alternative:
What Happens Next:
```

## Specialist Output Rules

Main Agent must review and translate:

- Server diagrams, authority models, reconnect/session plans, state sync plans,
  data consistency plans, anti-cheat plans, scaling plans, and operational
  runbooks.
- Art directions, style systems, animation/audio plans, asset format decisions,
  and experience vetoes.
- Development architecture, abstraction proposals, module boundaries, and
  client/server contracts.
- Testing risk maps, release confidence, numeric balance reviews, and release
  blocks.
- Audit reports, evidence gaps, completion claims, and residual risks.

## Server-Specific Translation

When the user lacks server expertise, summarize server plans as:

- What the server owns.
- What the client is not allowed to decide.
- What can go wrong.
- What the user must choose.
- What evidence will prove the server is safe enough to implement.

Do not require the user to understand Go internals, Redis, locks, channels,
packet ordering, CAS, or deployment details before blocking unsafe server work.

## Main Agent Anti-Pass-Through Rule

If a specialist output contains jargon, diagrams, tables, or implementation
details that affect product decisions, Main Agent must not simply say
"looks good" or paste it through. Produce `Main Agent Specialist Review` or
`User Decision Brief` first.
