import argparse
import json
import sys
from pathlib import Path


UNKNOWN_VALUES = {"", "unknown", "n/a", "none", None}


def _missing(value):
    if value is None:
        return True
    if isinstance(value, str):
        return value.strip().lower() in UNKNOWN_VALUES
    return False


def audit_manifest(manifest):
    issues = []

    for dependency in manifest.get("dependencies", []):
        name = dependency.get("name", "<unnamed dependency>")
        if _missing(dependency.get("license")):
            issues.append(
                {
                    "type": "dependency-license",
                    "target": name,
                    "message": "Dependency license is missing or unknown.",
                }
            )
        if _missing(dependency.get("source")):
            issues.append(
                {
                    "type": "dependency-source",
                    "target": name,
                    "message": "Dependency source is missing or unknown.",
                }
            )

    for asset in manifest.get("assets", []):
        path = asset.get("path", "<unnamed asset>")
        if _missing(asset.get("source")):
            issues.append(
                {
                    "type": "asset-source",
                    "target": path,
                    "message": "Asset source is missing or unknown.",
                }
            )
        if str(asset.get("commercial_use", "")).strip().lower() not in {"yes", "true", "allowed"}:
            issues.append(
                {
                    "type": "asset-commercial-use",
                    "target": path,
                    "message": "Asset commercial-use rights are not confirmed.",
                }
            )
        if _missing(asset.get("evidence")):
            issues.append(
                {
                    "type": "asset-evidence",
                    "target": path,
                    "message": "Asset evidence record is missing.",
                }
            )

    return {
        "ok": not issues,
        "issues": issues,
        "dependency_count": len(manifest.get("dependencies", [])),
        "asset_count": len(manifest.get("assets", [])),
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description="Audit dependency and asset provenance manifest.")
    parser.add_argument("manifest", help="Dependency/asset audit JSON manifest.")
    args = parser.parse_args(argv)

    try:
        manifest = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
        result = audit_manifest(manifest)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"dependency-asset-audit error: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
