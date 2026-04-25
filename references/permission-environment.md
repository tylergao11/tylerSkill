# Permission and Environment Protocol

Use this when an operation may mutate files, cloud state, production config,
data, secrets, or deployment environments.

## Environment Declaration

```markdown
## Environment Declaration

Environment: Local | Dev | Test | Staging | Production
Allowed Operations:
Forbidden Operations:
Secrets Involved: Yes | No
Data Sensitivity:
Deployment Impact:
```

## Permission Gate

```markdown
## Permission Gate

Operation:
Environment:
Impact:
Reversibility: Reversible | Partially Reversible | Irreversible
Dry Run Available: Yes | No
Rollback Plan:
Required Approval:
```

Require confirmation before destructive, irreversible, production, data, secret,
deployment, payment, ads, or privacy operations.

Prefer dry runs, impact scopes, backups, and rollback plans before mutation.
