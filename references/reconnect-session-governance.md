# Reconnect and Session Governance

Use this protocol for strong online games, room-based games, matchmaking games,
or any feature where disconnected players may return to an authoritative server
state.

Reconnect is not a UI convenience. It is a server authority, identity,
consistency, settlement, and anti-cheat boundary.

## Required Output

```markdown
## Reconnect and Session Plan

Identity Proof:
Session Token:
Device and Account Binding:
Multi-Login Policy:
Reconnect Window:
Room Retention:
State Recovery Mode: Snapshot | Event Replay | Snapshot + Replay
Snapshot Contents:
Event Replay Source:
Missed Message Strategy:
Duplicate Request Strategy:
Out-of-Order Message Strategy:
Client Sequence or Request ID:
Server Sequence or Version:
Timeout Behavior:
AI or Auto-Play Policy:
Forfeit or Kick Policy:
Reward and Settlement Safety:
Persistence and Idempotency:
Anti-Cheat Review:
Client UX Contract:
Server Test Cases:
```

## Server Rules

- Reconnect identity must be proven with server-issued session state, not client
  claims alone.
- The server decides whether a player may rejoin, spectate, auto-play, forfeit,
  or be kicked.
- Reconnect must define whether recovery uses snapshot, event replay, or both.
- Every reconnect-sensitive request needs duplicate and out-of-order handling.
- Settlement and rewards must remain idempotent across disconnect, retry, and
  reconnect.
- Room retention must have an explicit timeout and cleanup rule.
- Reconnect must not let the client overwrite authoritative room, match,
  inventory, reward, or settlement state.

## Game Defaults

Mahjong:

- Prefer snapshot plus event replay.
- Server retains room until settlement, timeout, or agreed dissolution.
- Disconnected players may auto-play by rule; settlement remains server-owned.

MOBA:

- Prefer latest authoritative state snapshot plus server tick/version.
- Disconnected players may pause only if game rules allow it; otherwise server
  continues simulation and client catches up.

Battle royale:

- Prefer latest authoritative state snapshot plus recent relevant events.
- Server continues match while disconnected; reconnect must not rewind other
  players or unsafe zone progression.
