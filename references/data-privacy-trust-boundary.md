# Data Privacy and Trust Boundary

Use this when handling user data, cloud writes, rewards, auth, payments, privacy,
or anti-cheat boundaries.

## Core Rules

- Client is not trusted for authoritative rewards, payments, leaderboard writes,
  or anti-cheat-sensitive state.
- Do not log secrets, tokens, session keys, plain user identifiers, payment
  details, private inputs, or precise location.
- Prefer cloud/server validation for high-value writes.

## Data Handling Review

```markdown
## Data Handling Review

Data:
Purpose:
Storage:
Read Access:
Write Access:
Retention:
Sensitive Fields:
Redaction:
User Impact:
```

## Trust Boundary Review

```markdown
## Trust Boundary Review

Feature:
Client-Owned State:
Server/Cloud-Owned State:
Authoritative Writes:
Validation Rules:
Abuse Cases:
Required Tests:
```
