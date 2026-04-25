import unittest

from scripts.debug_bisection import apply_probe_result, recommend_probe


class DebugBisectionTests(unittest.TestCase):
    def test_recommends_probe_with_best_worst_case_split(self):
        hypotheses = [
            {"id": "H1", "group": "ui"},
            {"id": "H2", "group": "client"},
            {"id": "H3", "group": "cloud"},
            {"id": "H4", "group": "database"},
        ]
        probes = [
            {
                "id": "P1",
                "question": "Did the cloud function receive the request?",
                "eliminates_if_yes": ["H1", "H2"],
                "eliminates_if_no": ["H3", "H4"],
            },
            {
                "id": "P2",
                "question": "Was the button handler called?",
                "eliminates_if_yes": ["H1"],
                "eliminates_if_no": ["H2", "H3", "H4"],
            },
        ]

        recommendation = recommend_probe(hypotheses, probes)

        self.assertEqual(recommendation["probe"]["id"], "P1")
        self.assertEqual(recommendation["worst_case_remaining"], 2)
        self.assertEqual(recommendation["best_case_eliminated"], 2)

    def test_ignores_already_eliminated_hypotheses_when_recommending(self):
        hypotheses = [
            {"id": "H1", "status": "eliminated"},
            {"id": "H2"},
            {"id": "H3"},
            {"id": "H4"},
        ]
        probes = [
            {
                "id": "P1",
                "question": "Does this separate active hypotheses?",
                "eliminates_if_yes": ["H2"],
                "eliminates_if_no": ["H3", "H4"],
            },
            {
                "id": "P2",
                "question": "Does this only touch eliminated hypotheses?",
                "eliminates_if_yes": ["H1"],
                "eliminates_if_no": [],
            },
        ]

        recommendation = recommend_probe(hypotheses, probes)

        self.assertEqual(recommendation["probe"]["id"], "P1")
        self.assertEqual(recommendation["active_hypotheses"], ["H2", "H3", "H4"])

    def test_applies_yes_result_and_marks_eliminated_hypotheses(self):
        session = {
            "hypotheses": [
                {"id": "H1", "statement": "UI handler did not fire"},
                {"id": "H2", "statement": "Cloud function failed"},
                {"id": "H3", "statement": "Database permission failed"},
            ],
            "probes": [
                {
                    "id": "P1",
                    "question": "Did cloud receive the request?",
                    "eliminates_if_yes": ["H1"],
                    "eliminates_if_no": ["H2", "H3"],
                }
            ],
        }

        updated = apply_probe_result(session, "P1", "yes")

        statuses = {item["id"]: item.get("status", "active") for item in updated["hypotheses"]}
        self.assertEqual(statuses["H1"], "eliminated")
        self.assertEqual(statuses["H2"], "active")
        self.assertEqual(statuses["H3"], "active")
        self.assertEqual(updated["diagnostic_history"][0]["result"], "yes")
        self.assertEqual(updated["diagnostic_history"][0]["eliminated"], ["H1"])

    def test_rejects_probe_that_does_not_split_any_active_hypotheses(self):
        hypotheses = [{"id": "H1"}, {"id": "H2"}]
        probes = [
            {
                "id": "P1",
                "question": "No information",
                "eliminates_if_yes": [],
                "eliminates_if_no": [],
            }
        ]

        with self.assertRaises(ValueError):
            recommend_probe(hypotheses, probes)


if __name__ == "__main__":
    unittest.main()
