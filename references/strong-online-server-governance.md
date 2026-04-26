# Strong Online Server Governance

Use this protocol before building server architecture for mahjong, MOBA, battle
royale, realtime action, ranked, economy, room, matchmaking, reconnect, replay,
anti-cheat, or other strong online games.

This protocol exists for users who understand the client but do not want to
personally enumerate server risks. Server Development Agent must surface the
whole server risk map before implementation.

## Required Output

```markdown
## Strong Online Server Readiness Plan

Game Type:
Server Language: Go
Client Language: TypeScript
Authority Model:
Client Trust Level:
Identity and Session:
Matchmaking and Room Lifecycle:
Reconnect and Session Plan:
State Sync Strategy:
Message Ordering and Idempotency:
Concurrency Model:
Data Consistency:
Persistence and Recovery:
Settlement and Reward Safety:
Anti-Cheat and Abuse Controls:
Rate Limits and Backpressure:
Protocol Versioning:
Observability and Audit Logs:
Replay or Dispute Review:
Deployment and Config:
Scaling and Capacity:
Failure Modes:
Operational Runbook:
Client Contract:
Testing Matrix:
Audit Requirements:
Implementation Allowed: Yes | No
Blocking Evidence:
```

## Minimum Server Risk Map

Server Development Agent must address these domains, even if the user does not
ask about them:

- Identity, login, session token, multi-login, and device/account binding.
- Matchmaking, room lifecycle, player readiness, start/end, and cleanup.
- Reconnect, player return, room retention, snapshot/replay recovery, and
  timeout behavior.
- Message sequence, duplicate requests, out-of-order messages, retries, and
  idempotency keys.
- Authoritative state ownership, state sync, prediction allowance, and desync
  recovery.
- Go goroutine ownership, room/match loops, locks, channels, backpressure,
  cancellation, and race detection.
- Persistence model, transaction boundaries, CAS/versioning, migration, backup,
  and disaster recovery.
- Settlement, rewards, inventory, ranking, payment-adjacent flows, and replay
  safety.
- Anti-cheat, abuse prevention, rate limits, suspicious event signals, and
  server-side validation.
- Observability, metrics, structured logs, replay/audit logs, alerting, and
  incident diagnosis.
- Protocol versioning, backward compatibility, forced upgrade, and client/server
  contract migration.
- Deployment config, environment separation, secret handling, rollout, rollback,
  and operational runbook.
- Capacity assumptions, load tests, cost risks, horizontal scaling assumptions,
  and degradation behavior.

## Implementation Gate

Server implementation may not begin for strong online games until:

1. `Strong Online Server Readiness Plan` is complete.
2. `Reconnect and Session Plan` is complete when players can disconnect or
   return.
3. `Go Concurrency Plan` is complete when goroutines, room loops, shared state,
   realtime sync, or background workers are involved.
4. `Data Consistency Plan` is complete when persistence, settlement, rewards,
   inventory, ranking, replay, or migrations are involved.
5. Client-facing request/response/event contracts are defined for TypeScript.
6. Testing Agent has provided test strategy for server authority, reconnect,
   consistency, and abuse cases.

## User-Safe Review Rule

If the user is not a server engineer, Main Agent should summarize the plan as:

- What the server owns.
- What the client is not allowed to decide.
- What can go wrong.
- What evidence will prove the server is safe enough to implement.

Do not require the user to understand Go internals before blocking unsafe server
work.
