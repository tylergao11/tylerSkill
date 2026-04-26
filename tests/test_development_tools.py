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

## Multi-Layer Pre-Code Gate

Feature: Daily reward claim.
Affected Layers: config, state, view, cloud.
Required Protocols: role-development, development-daily-tools, layer-map-governance, permission-environment, data-privacy-trust-boundary, role-testing, response-contract.
Engineering Plan: Present in this packet.
Pattern Fit Check: Present in this packet.
Layer Placement Review: config, state, view, and cloud files are separated.
Environment Declaration: development cloud environment, no production writes.
Permission Gate: no privileged production action.
Trust Boundary Review: client displays; cloud validates.
Test Strategy or Test Case Plan: config schema, state transition, cloud validation, UI smoke.
Implementation Allowed: Yes.
Blocking Evidence: None.
Next Owner: Development Agent.

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
        result = validate_design_packet(
            VALID_PACKET,
            require_pattern_fit=True,
            require_multi_layer=True,
        )

        self.assertTrue(result["ok"])
        self.assertEqual(result["errors"], [])

    def test_rejects_missing_engineering_plan_fields(self):
        result = validate_design_packet("## Engineering Plan\n\nGoal: Add reward.\n")

        self.assertFalse(result["ok"])
        self.assertTrue(
            any("Chosen Architecture" in error for error in result["errors"])
        )

    def test_rejects_missing_multi_layer_gate_section(self):
        packet = VALID_PACKET.replace(
            "## Multi-Layer Pre-Code Gate",
            "## Not The Multi-Layer Gate",
        )

        result = validate_design_packet(packet, require_multi_layer=True)

        self.assertFalse(result["ok"])
        self.assertTrue(
            any("Multi-Layer Pre-Code Gate" in error for error in result["errors"])
        )

    def test_rejects_missing_multi_layer_implementation_decision(self):
        packet = VALID_PACKET.replace("Implementation Allowed: Yes.\n", "")

        result = validate_design_packet(packet, require_multi_layer=True)

        self.assertFalse(result["ok"])
        self.assertTrue(
            any("Implementation Allowed" in error for error in result["errors"])
        )

    def test_rejects_missing_multi_layer_testing_evidence(self):
        packet = VALID_PACKET.replace(
            "Test Strategy or Test Case Plan: config schema, state transition, cloud validation, UI smoke.\n",
            "",
        )

        result = validate_design_packet(packet, require_multi_layer=True)

        self.assertFalse(result["ok"])
        self.assertTrue(
            any("Test Strategy or Test Case Plan" in error for error in result["errors"])
        )


class ImpactAnalyzerTests(unittest.TestCase):
    def test_classifies_config_and_state_as_high_risk(self):
        result = analyze_impact(["src/config/rewards.json", "src/game/state.ts"])

        self.assertEqual(result["risk_level"], "high")
        self.assertIn("configuration", result["categories"])
        self.assertIn("state", result["categories"])
        self.assertTrue(any("config schema" in item for item in result["regression_checks"]))

    def test_reward_ui_is_not_misclassified_as_configuration(self):
        result = analyze_impact(["src/ui/RewardPanel.tsx", "cloud/functions/claimReward/index.ts"])

        self.assertIn("presentation", result["categories"])
        self.assertIn("cloud", result["categories"])
        self.assertIn("economy-domain", result["categories"])
        self.assertNotIn("configuration", result["categories"])


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
        self.assertIn("multi-layer-feature-gate.md", eval_text)
        self.assertIn("permission-environment.md", eval_text)
        self.assertIn("data-privacy-trust-boundary.md", eval_text)
        self.assertIn("Test Strategy Rationale", eval_text)

    def test_root_skill_required_formats_match_workflow_contracts(self):
        repo = Path(__file__).resolve().parents[1]
        skill = (repo / "SKILL.md").read_text(encoding="utf-8")

        for required in (
            "Required Protocols:",
            "Pre-Code Gates:",
            "Affected Layers:",
            "Trust Boundary:",
            "Implementation Permission:",
            "Tool Gate:",
            "Tool Evidence:",
            "Specialist Context Packet",
            "Isolation Mode:",
            "Allowed Context:",
            "Withheld Context:",
        ):
            self.assertIn(required, skill)

    def test_strong_online_games_have_client_server_role_split(self):
        repo = Path(__file__).resolve().parents[1]
        skill = (repo / "SKILL.md").read_text(encoding="utf-8")
        development = (repo / "references" / "role-development.md").read_text(
            encoding="utf-8"
        )
        client = (repo / "references" / "role-client-development.md").read_text(
            encoding="utf-8"
        )
        server = (repo / "references" / "role-server-development.md").read_text(
            encoding="utf-8"
        )
        prompt = (repo / "templates" / "role-development-prompt.md").read_text(
            encoding="utf-8"
        )

        for required in (
            "Client Development Agent owns client runtime",
            "Server Development Agent owns authoritative backend",
            "role-client-development.md",
            "role-server-development.md",
        ):
            self.assertIn(required, skill)

        for required in (
            "Development Role Split Decision",
            "Strong Online",
            "Client Development Agent Needed",
            "Server Development Agent Needed",
        ):
            self.assertIn(required, development)
            self.assertIn(required, prompt)

        for required in (
            "Client Architecture Plan",
            "Client/Server Contract Review",
            "Client Language: TypeScript",
            "Server Language: Go",
            "TypeScript Request Type",
            "client must not decide authoritative gameplay outcomes",
        ):
            self.assertIn(required, client)

        for required in (
            "Server Architecture Plan",
            "Strong Online Server Readiness Plan",
            "Server Language: Go",
            "Client Language: TypeScript",
            "Concurrency Model",
            "Data Model",
            "Go Concurrency Plan",
            "Data Consistency Plan",
            "Reconnect and Session Plan",
            "Authoritative Gameplay Contract",
            "TypeScript Request Type",
            "TypeScript Response/Event Type",
            "Do not mutate authoritative room state from arbitrary goroutines",
            "Mahjong",
            "MOBA",
            "Battle royale",
        ):
            self.assertIn(required, server)

    def test_eval_requires_server_agent_for_strong_online_games(self):
        repo = Path(__file__).resolve().parents[1]
        eval_text = (
            repo / "evals" / "strong-online-game-requires-server-agent.json"
        ).read_text(encoding="utf-8")

        self.assertIn("role-client-development.md", eval_text)
        self.assertIn("role-server-development.md", eval_text)
        self.assertIn("strong-online-server-governance.md", eval_text)
        self.assertIn("Strong Online Server Readiness Plan", eval_text)
        self.assertIn("Authoritative Gameplay Contract", eval_text)
        self.assertIn("Go Concurrency Plan", eval_text)
        self.assertIn("Data Consistency Plan", eval_text)
        self.assertIn("Reconnect and Session Plan", eval_text)
        self.assertIn("skip server authority model", eval_text)

    def test_strong_online_server_governance_covers_hidden_server_risks(self):
        repo = Path(__file__).resolve().parents[1]
        protocol = (repo / "references" / "strong-online-server-governance.md").read_text(
            encoding="utf-8"
        )
        server = (repo / "references" / "role-server-development.md").read_text(
            encoding="utf-8"
        )
        prompt = (repo / "templates" / "role-server-development-prompt.md").read_text(
            encoding="utf-8"
        )
        eval_text = (
            repo / "evals" / "strong-online-server-without-readiness-plan.json"
        ).read_text(encoding="utf-8")

        for required in (
            "Strong Online Server Readiness Plan",
            "Identity and Session",
            "Matchmaking and Room Lifecycle",
            "State Sync Strategy",
            "Message Ordering and Idempotency",
            "Anti-Cheat and Abuse Controls",
            "Observability and Audit Logs",
            "Deployment and Config",
            "Scaling and Capacity",
            "Operational Runbook",
            "Testing Matrix",
        ):
            self.assertIn(required, protocol)

        self.assertIn("strong-online-server-governance.md", server)
        self.assertIn("strong-online-server-governance.md", prompt)
        self.assertIn("wait for user to enumerate server risks", eval_text)

    def test_reconnect_session_governance_is_required_for_server_agent(self):
        repo = Path(__file__).resolve().parents[1]
        protocol = (repo / "references" / "reconnect-session-governance.md").read_text(
            encoding="utf-8"
        )
        server = (repo / "references" / "role-server-development.md").read_text(
            encoding="utf-8"
        )
        prompt = (repo / "templates" / "role-server-development-prompt.md").read_text(
            encoding="utf-8"
        )
        eval_text = (repo / "evals" / "reconnect-without-session-plan.json").read_text(
            encoding="utf-8"
        )

        for required in (
            "Reconnect and Session Plan",
            "Identity Proof",
            "Session Token",
            "Room Retention",
            "State Recovery Mode",
            "Duplicate Request Strategy",
            "Out-of-Order Message Strategy",
            "Reward and Settlement Safety",
        ):
            self.assertIn(required, protocol)

        self.assertIn("reconnect-session-governance.md", server)
        self.assertIn("reconnect-session-governance.md", prompt)
        self.assertIn("Reconnect and Session Plan", eval_text)
        self.assertIn("accept reconnect without identity proof", eval_text)


class CompletionTrustBoundaryDocumentationTests(unittest.TestCase):
    def test_root_skill_defines_audit_agent_as_core_role(self):
        repo = Path(__file__).resolve().parents[1]
        skill = (repo / "SKILL.md").read_text(encoding="utf-8")

        for required in (
            "Audit Agent owns completion trust",
            "Agent completion is not evidence",
            "Audit Gate",
            "completion-trust-boundary.md",
            "role-audit.md",
        ):
            self.assertIn(required, skill)

    def test_completion_audit_protocol_and_prompt_exist(self):
        repo = Path(__file__).resolve().parents[1]
        protocol = (repo / "references" / "completion-trust-boundary.md").read_text(
            encoding="utf-8"
        )
        role = (repo / "references" / "role-audit.md").read_text(encoding="utf-8")
        prompt = (repo / "templates" / "role-audit-prompt.md").read_text(
            encoding="utf-8"
        )

        for required in (
            "Completion Audit Report",
            "Verified",
            "Inferred",
            "Unverified",
            "Workflow Decision",
            "Request More Evidence",
            "Main Agent completion summaries are auditable claims",
            "project self-check",
            "GitHub push/tag",
        ):
            self.assertIn(required, protocol)

        for required in (
            "completion-trust-boundary.md",
            "Completion Audit Report",
            "Tool Gate",
            "Tool Evidence",
        ):
            self.assertIn(required, role)
            self.assertIn(required, prompt)

        self.assertNotIn("Evidence Class: Verified | Inferred | Unverified", role)
        self.assertNotIn("Evidence Class: Verified | Inferred | Unverified", prompt)

    def test_completion_trust_rules_are_not_redefined_in_response_contract(self):
        repo = Path(__file__).resolve().parents[1]
        response_contract = (repo / "references" / "response-contract.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("completion-trust-boundary.md", response_contract)
        self.assertNotIn("## Evidence Classes", response_contract)
        self.assertNotIn("Evidence Class: Verified | Inferred | Unverified", response_contract)

    def test_eval_blocks_natural_language_completion_claims(self):
        repo = Path(__file__).resolve().parents[1]
        eval_text = (
            repo / "evals" / "completion-claim-without-audit.json"
        ).read_text(encoding="utf-8")

        self.assertIn("completion-trust-boundary.md", eval_text)
        self.assertIn("role-audit.md", eval_text)
        self.assertIn("Completion Audit Report", eval_text)
        self.assertIn("accept natural-language completion", eval_text)

    def test_eval_blocks_main_agent_self_check_claim_without_audit(self):
        repo = Path(__file__).resolve().parents[1]
        eval_text = (
            repo / "evals" / "main-agent-self-check-claim.json"
        ).read_text(encoding="utf-8")

        self.assertIn("completion-trust-boundary.md", eval_text)
        self.assertIn("role-audit.md", eval_text)
        self.assertIn("github-governance.md", eval_text)
        self.assertIn("Completion Audit Report", eval_text)
        self.assertIn("treat main agent self-check as proof", eval_text)

    def test_eval_blocks_release_confidence_without_evidence(self):
        repo = Path(__file__).resolve().parents[1]
        eval_text = (
            repo / "evals" / "release-confidence-without-evidence.json"
        ).read_text(encoding="utf-8")

        self.assertIn("role-testing.md", eval_text)
        self.assertIn("completion-trust-boundary.md", eval_text)
        self.assertIn("role-audit.md", eval_text)
        self.assertIn("Release Confidence", eval_text)
        self.assertIn("accept release confidence without evidence", eval_text)


if __name__ == "__main__":
    unittest.main()
