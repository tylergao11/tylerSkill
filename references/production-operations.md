# Production Operations

Use this for GitHub, CI, production incidents, hotfixes, release candidates, and
rollback decisions.

For GitHub repository gates, CI, CodeQL, Dependabot, CODEOWNERS, rulesets, and
release automation, also load `github-governance.md`.

## Core Rule

Agent may prepare production fixes, but production-impacting operations require
explicit permission gates.

## Production Operation Plan

```markdown
## Production Operation Plan

Incident or Task:
Environment:
Operation Level: Read Only | Fix Branch | PR | Merge | Release | Deploy | Rollback
Evidence:
Proposed Actions:
Risk:
Required Permissions:
Verification:
Rollback:
```

## Incident Report

```markdown
## Incident Report

Symptom:
Start Time:
Affected Users:
Systems:
Current Evidence:
Suspected Boundary:
Immediate Mitigation:
Owner:
Next Diagnostic Step:
```

## Allowed Without Production Confirmation

- Read issues, PRs, logs, CI results, and source code.
- Create local branches and patches.
- Run tests.
- Open a PR or draft fix.
- Prepare release and rollback notes.

## Requires Explicit Confirmation

- Merge to production branch.
- Trigger production deployment.
- Roll back production.
- Change production environment variables.
- Modify cloud database or production data.
- Delete user data, assets, builds, or releases.
- Change payment, ads, privacy, or permissions.
