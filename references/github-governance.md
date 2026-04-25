# GitHub Governance

Use this protocol when GitHub is the external quality gate for agent work:
issues, pull requests, CI, CodeQL, Dependabot, CODEOWNERS, releases, repository
rulesets, and security settings.

## Core Rule

Agents may prepare GitHub automation and pull requests, but they must not claim
GitHub protections are active until GitHub reports them as enabled.

Repository files can provide:

- GitHub Actions workflows.
- CodeQL workflow configuration.
- Dependabot configuration.
- CODEOWNERS review ownership.
- Pull request and issue templates.
- Release workflow.
- Ruleset templates and setup instructions.

GitHub settings must enable:

- Branch protection or repository rulesets.
- Secret scanning and push protection.
- Dependabot alerts and security updates.
- Protected environments and required approvals.

## Required Repository Files

```text
.github/workflows/skill-ci.yml
.github/workflows/codeql.yml
.github/workflows/release.yml
.github/dependabot.yml
.github/CODEOWNERS
.github/PULL_REQUEST_TEMPLATE.md
.github/ISSUE_TEMPLATE/
.github/rulesets/main-protection.json
.github/repository-settings.md
```

`CODEOWNERS` must contain valid GitHub users or teams for the current
repository. Placeholder owners are not a gate.

## PR Gate

Every agent-created pull request must include:

- Summary of changed behavior.
- Tool evidence.
- Tests and validation output.
- Risk and rollback notes.
- Whether `VERSION` and `CHANGELOG.md` changed.
- Whether runtime files were kept out of the skill path.

## CI Gate

Required checks for this skill repository:

```text
python -m unittest discover tests
python scripts/validate_skill_repo.py
python scripts/install_skill.py --dry-run
CodeQL
```

Do not merge when these checks fail. If a check cannot run, return `Blocked`
with the missing GitHub permission, failing job, or required setup step.

## Security Gate

For secrets, production credentials, cloud keys, payment, auth, or user data:

1. Confirm secret scanning and push protection status.
2. Keep secrets out of repository files and generated evidence.
3. Use GitHub environments or external secret stores for deployments.
4. Treat any detected secret as a production incident until rotated or proven safe.

## Release Gate

Release work requires:

- Version bump.
- Changelog entry.
- Passing CI.
- Tagged release, usually `vX.Y.Z`.
- Release artifact built from the install plan.
- Rollback plan from `release-rollback.md`.

## GitHub Setup Check

```markdown
## GitHub Setup Check

Repository:
Default Branch:
Required Checks:
Branch Protection or Ruleset:
CODEOWNERS Active:
Secret Scanning:
Dependabot:
CodeQL:
Release Workflow:
Missing Setup:
Next Action:
```
