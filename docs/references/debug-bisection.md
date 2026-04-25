# Hypothesis Bisection Debugger

Use this protocol and tool when a bug has many hypotheses, fixes have failed, or
an agent wants to guess-and-change code.

## Core Rule

Do not repair hypotheses one by one. Use diagnostic probes to shrink the
hypothesis space before changing production code.

Trigger this protocol when:

- There are five or more plausible hypotheses.
- Two fix attempts have failed.
- The symptom crosses multiple modules.
- The issue may involve state, async behavior, cloud calls, resources, config,
  performance, or environment differences.
- An agent proposes "try changing X" without evidence.

## Universal Fit

The tool is project-agnostic. It works with any language or framework because it
models debugging as:

```text
hypotheses + diagnostic probes + yes/no evidence -> smaller hypothesis set
```

Use it for code bugs, asset issues, performance problems, config problems,
cloud/API issues, CI failures, and environment differences.

## CLI

Recommend the next diagnostic probe:

```powershell
python scripts/debug_bisection.py recommend path\to\session.json
```

Apply a probe result:

```powershell
python scripts/debug_bisection.py apply path\to\session.json --probe P1 --result yes -o path\to\session.updated.json
```

All JSON files must be UTF-8.

## Session JSON

```json
{
  "bug": "Reward is shown but coins are not granted",
  "hypotheses": [
    { "id": "H1", "group": "ui", "statement": "Button handler did not fire" },
    { "id": "H2", "group": "cloud", "statement": "Cloud function failed" },
    { "id": "H3", "group": "database", "statement": "Database write was denied" }
  ],
  "probes": [
    {
      "id": "P1",
      "question": "Did the cloud function receive the request?",
      "eliminates_if_yes": ["H1"],
      "eliminates_if_no": ["H2", "H3"]
    }
  ]
}
```

## Diagnostic Test

Before using a probe, the agent must state:

```markdown
## Diagnostic Test

Question:
Hypotheses Split:
Probe:
Expected Result A:
Expected Result B:
Evidence Captured:
Result:
Eliminated Hypotheses:
Remaining Hypotheses:
```

## Bisection Choice

When multiple probes exist, prefer the one with the best worst-case reduction.

```markdown
## Bisection Choice

Candidate Probes:
Selected Probe:
Why Highest Information Gain:
Hypotheses It Can Eliminate:
Risk:
```

## Fix Attempt Budget

- Diagnostic probes are allowed before root cause is confirmed.
- Fix attempts without confirmed root cause are not allowed.
- After root cause is confirmed, attempt one focused fix.
- If three fixes fail, stop and trigger architecture review.

## Agent Usage Rules

Agents must:

- Group hypotheses by boundary before proposing probes.
- Prefer evidence-gathering probes over code changes.
- Record eliminated hypotheses.
- Keep remaining hypotheses visible.
- Avoid committing fixes until the root cause boundary is known.

Main Agent must reject a debug response that lists many possible causes but does
not propose a diagnostic split.
