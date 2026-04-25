import json
import unittest
from pathlib import Path

from scripts.dependency_asset_audit import audit_manifest
from scripts.layer_map_validator import validate_layer_map


class LayerMapValidatorTests(unittest.TestCase):
    def test_detects_forbidden_cross_layer_change(self):
        config = {
            "layers": {
                "model": ["src/model/"],
                "view": ["src/view/"],
            },
            "forbidden": [
                {
                    "source": "view",
                    "target": "model",
                    "reason": "View changes must not rewrite model state directly.",
                }
            ],
        }

        result = validate_layer_map(
            config,
            ["src/view/reward_popup.ts", "src/model/reward_state.ts"],
        )

        self.assertFalse(result["ok"])
        self.assertEqual(len(result["violations"]), 1)

    def test_accepts_known_single_layer_change(self):
        config = {
            "layers": {
                "controller": ["src/controller/"],
                "test": ["tests/"],
            },
            "forbidden": [],
        }

        result = validate_layer_map(config, ["src/controller/reward.ts", "tests/reward.test.ts"])

        self.assertTrue(result["ok"])
        self.assertEqual(result["unknown"], [])


class DependencyAssetAuditTests(unittest.TestCase):
    def test_blocks_unknown_asset_rights(self):
        result = audit_manifest(
            {
                "dependencies": [
                    {
                        "name": "safe-lib",
                        "version": "1.0.0",
                        "license": "MIT",
                        "source": "npm",
                    }
                ],
                "assets": [
                    {
                        "path": "assets/reward.png",
                        "source": "Unknown",
                        "license": "Unknown",
                        "commercial_use": "unknown",
                    }
                ],
            }
        )

        self.assertFalse(result["ok"])
        self.assertTrue(any(issue["type"] == "asset-source" for issue in result["issues"]))

    def test_accepts_documented_dependency_and_asset(self):
        result = audit_manifest(
            {
                "dependencies": [
                    {
                        "name": "safe-lib",
                        "version": "1.0.0",
                        "license": "MIT",
                        "source": "npm",
                    }
                ],
                "assets": [
                    {
                        "path": "assets/reward.png",
                        "source": "Generated",
                        "license": "Project Owned",
                        "commercial_use": "yes",
                        "evidence": "docs/decisions/asset-record.md",
                    }
                ],
            }
        )

        self.assertTrue(result["ok"])


class SkillManifestTests(unittest.TestCase):
    def test_manifest_version_matches_version_file(self):
        repo = Path(__file__).resolve().parents[1]
        manifest = json.loads((repo / "skill-manifest.json").read_text(encoding="utf-8"))
        version = (repo / "VERSION").read_text(encoding="utf-8").strip()

        self.assertEqual(manifest["version"], version)

    def test_manifest_references_existing_resources(self):
        repo = Path(__file__).resolve().parents[1]
        manifest = json.loads((repo / "skill-manifest.json").read_text(encoding="utf-8"))

        for collection in ("protocols", "tools"):
            with self.subTest(collection=collection):
                for item in manifest[collection]:
                    self.assertTrue((repo / item).exists(), item)


if __name__ == "__main__":
    unittest.main()
