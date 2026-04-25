# Response Contract Protocol

Use this when a role response may drive automation, completion, handoff, or state
transition.

## Core Rule

Natural-language progress claims do not advance workflow state.

A turn is complete only when required fields, artifacts, validation, and handoff
are present.

Invalid standalone claims include "completed", "next step", "fixed", "passed",
"已完成", "下一步", "已修复", "已通过", and similar wording.

## Agent Turn Result

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
Tool Gate:
Tool Evidence:
```

## State Transition Rule

Workflow state may advance only when:

1. Response format is valid.
2. Status is explicit.
3. Required fields for that status are present.
4. Required artifacts exist or are explicitly not applicable.
5. Validation or review status is stated.
6. Next owner is named.

## Status Requirements

`Completed` requires artifacts, validation, remaining risks or `None`, handoff
target, and next action.

When a role-specific protocol requires tool evidence, `Tool Gate` and
`Tool Evidence` are required state-transition fields, not optional decoration.

For completion, release, production, or high-risk workflow transitions,
`Completed` is only format-valid until `completion-trust-boundary.md` classifies
the evidence and returns an audit decision.

`Validation` must be evidence-bearing. Use this shape when work is completed,
vetoed, blocked by quality, or release-relevant:

```markdown
Validation:
- Method:
- Command or Review Source:
- Result:
- Artifact Path:
- Reviewer:
- Limits:
```

`Artifacts: Not Applicable` requires a reason and Main Agent acceptance.

`Blocked` requires blocking reason, needed decision or missing input, recommended
default or workaround, and handoff target.

`Failed` requires attempted approach, failure evidence, recommended alternative,
and whether retry is safe.

`Vetoed` requires reason, severity, evidence, minimum fix, and whether degraded
delivery is allowed.

`Needs Input` requires the exact question, why it matters, and what default will
be used if unanswered.

## Invalid Response Notice

```markdown
## Invalid Response Notice

Target Role:
Task ID:
Invalid Reason:
Required Format:
Missing Fields:
Retry Instruction:
```

## Main Agent Normalization

Main Agent may normalize useful but malformed specialist content only when doing
so does not invent facts.

Main Agent must not normalize a malformed response into `Completed`, `Vetoed`,
`Release Confidence: Ready`, or any other workflow-advancing state unless the
source response already contains artifacts and validation evidence verbatim.
Otherwise require specialist confirmation.

```markdown
## Main Agent Normalization

Original Role:
Reason:
Normalized Result:
Confidence: High | Medium | Low
Needs Specialist Confirmation: Yes | No
```
