# Development Daily Tools

Use these tools as Development Agent gates. They exist so agents make placement,
impact, and completion decisions from explicit evidence instead of intuition.

## Mandatory Triggers

| Trigger | Required Tool | Blocking Rule |
| --- | --- | --- |
| Feature placement, architecture choice, cloud/server change, shared module change, or high-impact implementation | `design_packet_validator.py` | Do not implement until the packet passes. |
| Any code edit after changed paths are known | `impact_analyzer.py` | Do not finalize the plan until regression checks are listed. |
| Any completion claim after code changes | `diff_risk_reviewer.py` | Do not mark `Completed` while the tool reports blocked. |

If a required tool cannot run, return `Blocked` with the attempted command,
error output, and a fallback validation proposal.

## Tool Gate Output

Every Development Agent result that uses these tools must include:

```markdown
Tool Gate:
- design_packet_validator.py: Pass | Blocked | Not Required
- impact_analyzer.py: Pass | Blocked | Not Required
- diff_risk_reviewer.py: Pass | Blocked | Not Required
Tool Evidence:
- Command:
- Result:
- Follow-up:
```

`Not Required` must include a reason. It is invalid to omit a required tool and
replace it with a natural-language confidence statement.

## Design Packet Validator

Command:

```bash
python scripts/design_packet_validator.py docs/handoffs/dev-plan.md --require-pattern-fit
```

Use it when Development Agent has to explain where a feature belongs, what it
will touch, and how it will be tested before coding.

It blocks missing or empty `Engineering Plan` fields and can require
`Pattern Fit Check` for architecture-changing work.

Agent use:

1. Write the design packet into a handoff or review file.
2. Run the validator against that file.
3. If it fails, fix the packet or return `Needs Input`; do not start coding.

## Impact Analyzer

Command:

```bash
python scripts/impact_analyzer.py src/game/state.ts src/config/rewards.json
```

Use it to convert changed paths into risk categories and regression checks.
If no files are passed, it reads `git diff --name-only HEAD`.

Agent use:

1. Run it after deciding the likely files or after the first diff exists.
2. Copy the reported `risk_level` and `regression_checks` into the plan.
3. Use the checks to choose focused tests and manual/true-device verification.

## Regression Check Plan

Use the `impact_analyzer.py` result to populate the formal `Regression Check
Plan` from `regression-iteration.md` whenever changed paths are known.

## Diff Risk Reviewer

Command:

```bash
python scripts/diff_risk_reviewer.py --repo . --base HEAD
```

Use it before completion. It flags high-risk paths, large diffs, and missing
test changes so Development Agent must either add tests or cite existing
coverage.

Agent use:

1. Run it after implementation and before `Status: Completed`.
2. If it returns exit code `2`, treat the result as a block, not a warning.
3. Resolve by adding tests, citing existing tests with evidence, or returning
   `Blocked` with a recovery path.

## Agent Rule

Development Agent may not use these tools as decoration. If a tool reports a
block, the next turn must either fix the block or return `Blocked` with evidence
and a recovery path.
