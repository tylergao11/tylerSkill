# Development Daily Tools

Use these tools to keep Development Agent work readable, placed correctly, and
regression-aware during normal implementation.

## Tool Order

1. Run `design_packet_validator.py` before high-impact implementation.
2. Run `impact_analyzer.py` before editing or when planning regression checks.
3. Run `diff_risk_reviewer.py` before claiming completion.

## Design Packet Validator

Command:

```bash
python scripts/design_packet_validator.py docs/handoffs/dev-plan.md --require-pattern-fit
```

Use it when Development Agent has to explain where a feature belongs, what it
will touch, and how it will be tested before coding.

It blocks missing or empty `Engineering Plan` fields and can require
`Pattern Fit Check` for architecture-changing work.

## Impact Analyzer

Command:

```bash
python scripts/impact_analyzer.py src/game/state.ts src/config/rewards.json
```

Use it to convert changed paths into risk categories and regression checks.
If no files are passed, it reads `git diff --name-only HEAD`.

## Diff Risk Reviewer

Command:

```bash
python scripts/diff_risk_reviewer.py --repo . --base HEAD
```

Use it before completion. It flags high-risk paths, large diffs, and missing
test changes so Development Agent must either add tests or cite existing
coverage.

## Agent Rule

Development Agent may not use these tools as decoration. If a tool reports a
block, the next turn must either fix the block or return `Blocked` with evidence
and a recovery path.
