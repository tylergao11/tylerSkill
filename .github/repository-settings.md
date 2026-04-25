# GitHub Repository Settings

These settings cannot be fully enforced by repository files alone. Configure
them in GitHub settings or through the GitHub API after the repository is
created.

## Required Settings

- Enable branch protection or import `.github/rulesets/main-protection.json`.
- Require the `Skill CI` and `CodeQL` checks before merge.
- Require CODEOWNERS review for protected branches.
- Replace CODEOWNERS entries with valid GitHub users or teams for the repository.
- Enable secret scanning and push protection.
- Enable Dependabot alerts and security updates.
- Require approval for production GitHub environments.
- Disable force pushes and branch deletion on protected branches.

## Labels

Recommended labels:

```text
type:bug
type:feature
type:skill-evolution
role:main
role:development
role:art
role:testing
risk:high
needs:evidence
blocked
dependencies
github-actions
```

## Agent Rule

Agents may prepare settings files and instructions, but they must not claim
branch protection, secret scanning, or environment approvals are active until
GitHub reports them as enabled.
