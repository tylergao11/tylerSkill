# Dependency and Asset Audit

Use this protocol when dependencies, third-party packages, SDKs, generated
assets, purchased assets, fonts, audio, video, or package budget may affect
shipping risk.

## Core Rule

Do not ship dependencies or assets with unknown source, license, commercial
rights, or budget impact unless the risk is explicitly accepted.

## Audit Manifest

Consumer projects may provide a JSON manifest:

```json
{
  "dependencies": [
    {
      "name": "example-package",
      "version": "1.0.0",
      "license": "MIT",
      "source": "npm",
      "purpose": "runtime"
    }
  ],
  "assets": [
    {
      "path": "assets/reward.png",
      "source": "Generated",
      "license": "Project Owned",
      "commercial_use": "yes",
      "evidence": "docs/decisions/asset-record.md"
    }
  ]
}
```

## Audit Gate

Run `scripts/dependency_asset_audit.py` against the manifest before release or
when adding packages/assets.

Blocking issues:

- Missing dependency license.
- Missing asset source.
- Unknown commercial use rights.
- Missing evidence for shipped third-party or generated assets.

## Audit Result

```markdown
## Dependency Asset Audit Result

Manifest:
Blocked:
Issues:
Accepted Risks:
Required Fixes:
Next Action:
```
