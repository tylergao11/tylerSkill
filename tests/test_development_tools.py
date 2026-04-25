import unittest
from pathlib import Path

from scripts.design_packet_validator import validate_design_packet
from scripts.diff_risk_reviewer import review_diff_risk
from scripts.impact_analyzer import analyze_impact


VALID_PACKET = """## Engineering Plan

Goal: Add daily reward claim.
Project Type: WeChat mini game.
Chosen Architecture: MVC-style feature slice.
Why This Architecture: It keeps data, rules, and presentation separate.
Module Boundaries: reward data, reward controller, reward popup.
Data Flow: config -> controller -> state -> view.
State Ownership: reward state owns claim status.
Public Interfaces: claimReward(userId).
Risk Points: reward duplication and save failure.
Test Strategy: unit test claim rules and save failure.
Readability Rules: keep code direct and avoid generic managers.

## Pattern Fit Check

Problem Shape: One feature with clear data and UI boundaries.
Candidate Patterns: MVC, event bus, generic reward framework.
Selected Pattern: MVC.
Fit Reason: It is simple and readable for one feature.
Overengineering Risk: Generic reward framework would hide flow.
Underengineering Risk: Hard-coded UI state could break save flow.
Exit Criteria: Tests pass and reward popup reflects saved state.
"""


class DesignPacketValidatorTests(unittest.TestCase):
    def test_accepts_complete_high_impact_packet(self):
        result = validate_design_packet(VALID_PACKET, require_pattern_fit=True)

        self.assertTrue(result["ok"])
        self.assertEqual(result["errors"], [])

    def test_rejects_missing_engineering_plan_fields(self):
        result = validate_design_packet("## Engineering Plan\n\nGoal: Add reward.\n")

        self.assertFalse(result["ok"])
        self.assertTrue(
            any("Chosen Architecture" in error for error in result["errors"])
        )


class ImpactAnalyzerTests(unittest.TestCase):
    def test_classifies_config_and_state_as_high_risk(self):
        result = analyze_impact(["src/config/rewards.json", "src/game/state.ts"])

        self.assertEqual(result["risk_level"], "high")
        self.assertIn("configuration", result["categories"])
        self.assertIn("state", result["categories"])
        self.assertTrue(any("config schema" in item for item in result["regression_checks"]))


class DiffRiskReviewerTests(unittest.TestCase):
    def test_blocks_high_risk_diff_without_tests(self):
        result = review_diff_risk(["src/cloud/reward_api.ts"])

        self.assertTrue(result["blocked"])
        self.assertIn("src/cloud/reward_api.ts", result["risky_files"])

    def test_allows_high_risk_diff_with_test_change(self):
        result = review_diff_risk(
            ["src/cloud/reward_api.ts", "tests/reward_api.test.ts"]
        )

        self.assertFalse(result["blocked"])
        self.assertEqual(result["required_action"], "Proceed with stated validation.")


class DevelopmentToolGateDocumentationTests(unittest.TestCase):
    def test_agent_prompt_requires_tool_gate_evidence(self):
        repo = Path(__file__).resolve().parents[1]
        prompt = (repo / "templates" / "role-development-prompt.md").read_text(
            encoding="utf-8"
        )
        reference = (repo / "references" / "development-daily-tools.md").read_text(
            encoding="utf-8"
        )

        for required in (
            "Tool Gate",
            "Tool Evidence",
            "design_packet_validator.py",
            "impact_analyzer.py",
            "diff_risk_reviewer.py",
        ):
            self.assertIn(required, prompt)
            self.assertIn(required, reference)

    def test_eval_covers_skipping_development_tools(self):
        repo = Path(__file__).resolve().parents[1]
        eval_text = (repo / "evals" / "development-tool-gate.json").read_text(
            encoding="utf-8"
        )

        self.assertIn("development-daily-tools.md", eval_text)
        self.assertIn("mark completed without diff risk review", eval_text)


if __name__ == "__main__":
    unittest.main()
