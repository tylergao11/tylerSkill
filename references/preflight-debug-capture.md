# Preflight Debug Capture Protocol

Use this protocol when designing pre-embedded debug capture, true-device
diagnostics, observability plans, or trace-based evidence.

## Core Rule

Collect enough to diagnose, not enough to surveil.

Preflight debug capture should gather key boundary evidence during the first
true-device run so later debugging can eliminate hypotheses from evidence instead
of guessing.

## When To Use

Use for high-risk or hard-to-debug features involving:

- Rewards, currency, save data, leaderboard, ads, payment, or gacha/drop logic
- Cloud functions, API calls, auth, permissions, or database writes
- Scene lifecycle, resource loading, animation playback, audio, or performance
- Async state, retries, weak network, or true-device-only bugs

## Debug Observability Plan

Create this before implementing a high-risk feature:

```markdown
## Debug Observability Plan

Feature:
Critical Trace:
Events To Capture:
State Snapshots:
Cloud/API Signals:
Performance Signals:
Sensitive Fields:
Capture Budget:
How To Export:
```

Testing Agent should review whether the plan is sufficient to diagnose likely
failures. Development Agent decides how to implement the signals.

## Event Schema

Use UTF-8 JSON lines where possible.

```json
{
  "debug_session_id": "debug-20260426-001",
  "trace_id": "reward-claim-001",
  "task_id": "debug-reward-flow-001",
  "timestamp": 1770000000000,
  "type": "cloud.call.end",
  "scope": "reward",
  "build_id": "1.0.0+42",
  "device_id_hash": "redacted-hash",
  "data": {
    "function": "claimReward",
    "duration_ms": 312,
    "status": "ok"
  }
}
```

Required identifiers:

- `debug_session_id`: one true-device diagnostic run.
- `trace_id`: one user flow or business transaction.
- `task_id`: related debugging or workflow task.
- `build_id`: app version, build number, or commit.

## Recommended Capture Areas

Capture only what is needed for diagnosis:

- Runtime: platform, device model, OS, app/runtime version, screen/DPR, network.
- Build: app version, build number, commit, config version, asset manifest version.
- Scene lifecycle: launch, first screen, scene enter/exit, resource timing.
- User flow: key clicks, popups, reward claims, level start/end.
- State: key state transitions before/after critical actions.
- Cloud/API: request id, function/API name, start/end, status, error code, duration, retry.
- Assets: load success/failure, path, duration, decode/playback error.
- Performance: FPS samples, frame spikes, memory warnings where available.
- Errors: JS errors, promise rejections, cloud errors, asset errors, assertions.
- Evidence: screenshot, short recording, or UI state summary when triggered.

## Privacy Rules

Never capture or export:

- Plain openid or user id
- Phone number
- Payment details
- Precise location
- Tokens, session keys, secrets, cookies, or credentials
- User chat or free-form private input
- Unredacted personal identifiers

Allowed when useful:

- Hashed user/device id
- Error codes
- Status enums
- Timings
- Config versions
- Asset paths
- Trace ids

## Capture Budget

Define limits before capture:

```markdown
## Debug Capture Budget

Max Events:
Max Session Duration:
Max Screenshots:
Max Recording Duration:
Sampling Rate:
Upload Policy: Manual Export | On Failure | Never Auto Upload
Retention:
```

Debug capture must not materially change gameplay performance. If capture affects
behavior, record that as a testing risk.

## Debug Capture Digest

Do not make agents read large raw logs by default. Summarize first:

```markdown
## Debug Capture Digest

Session:
Build:
Device:
Critical Flow:
Observed Events:
Missing Expected Events:
Errors:
Performance Spikes:
Hypotheses Eliminated:
Hypotheses Remaining:
Recommended Next Probe:
Evidence Files:
```

The digest is the context packet. Raw logs remain evidence and are loaded only
when the digest is insufficient.

## Hypothesis Mapping

After capture, map observations to hypotheses:

```markdown
## Hypothesis Mapping

Observation:
Supports:
Eliminates:
Still Unknown:
Next Diagnostic Probe:
```

Use `references/debug-bisection.md` when remaining hypotheses are still broad.

## Retention Policy

Diagnostic data should not pile up indefinitely:

- Keep only the latest useful sessions locally.
- Archive evidence used in decisions.
- Delete raw sessions after their retention window.
- Mark evidence expired when build, UI, config, or platform state changes.
- Keep release-blocking evidence until the incident is resolved and reviewed.
