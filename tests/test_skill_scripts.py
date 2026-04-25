import json
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.init_consumer_project import init_project
from scripts.install_skill import build_install_plan
from scripts.validate_skill_repo import validate_repo


class ConsumerProjectInitTests(unittest.TestCase):
    def test_initializes_profile_vendor_and_templates(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "game"
            vendor = Path(tmp) / "vendor" / "agent-os"

            created = init_project(
                root,
                profile="casual-mini-game",
                vendor_path=vendor,
                copy_templates=True,
            )

            self.assertTrue((root / "docs/project-notes/project-memory.md").exists())
            self.assertTrue((root / "docs/project-notes/architecture-profile.md").exists())
            self.assertTrue((root / "docs/project-notes/agent-os-vendor.md").exists())
            self.assertTrue((root / "templates/task-brief.md").exists())
            memory = (root / "docs/project-notes/project-memory.md").read_text(encoding="utf-8")
            self.assertIn("Skill Version:", memory)
            self.assertIn("casual-mini-game", memory)
            self.assertIn("docs/project-notes/project-memory.md", created)


class InstallSkillTests(unittest.TestCase):
    def test_build_install_plan_uses_standard_skill_files(self):
        repo = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as tmp:
            destination = Path(tmp) / "skills"
            plan = build_install_plan(repo, destination)

            relative_sources = {item.source.relative_to(repo).as_posix() for item in plan.items}
            self.assertIn("SKILL.md", relative_sources)
            self.assertIn("references/protocol-routing.md", relative_sources)
            self.assertIn("scripts/debug_bisection.py", relative_sources)
            self.assertNotIn("references/full-draft.md", relative_sources)
            self.assertEqual(plan.skill_dir, destination / "agent-collaboration-os")


class ValidateSkillRepoTests(unittest.TestCase):
    def copy_repo(self, repo, destination):
        ignore = shutil.ignore_patterns(".git", ".superpowers", "__pycache__", "docs")
        shutil.copytree(repo, destination, ignore=ignore)

    def test_current_repo_validates(self):
        repo = Path(__file__).resolve().parents[1]
        result = validate_repo(repo, run_tests=False)

        self.assertEqual(result.errors, [])
        self.assertIn("SKILL.md", result.checked)
        self.assertFalse((repo / "docs" / "Skill.md").exists())

    def test_detects_missing_reference_from_skill_index(self):
        repo = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as tmp:
            copy = Path(tmp) / "repo"
            self.copy_repo(repo, copy)
            skill = copy / "SKILL.md"
            skill.write_text(
                skill.read_text(encoding="utf-8")
                + "\n- `references/missing.md`: broken reference.\n",
                encoding="utf-8",
                newline="\n",
            )

            result = validate_repo(copy, run_tests=False)

            self.assertTrue(any("references/missing.md" in error for error in result.errors))

    def test_detects_eval_that_references_missing_protocol(self):
        repo = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as tmp:
            copy = Path(tmp) / "repo"
            self.copy_repo(repo, copy)
            eval_file = copy / "evals" / "bad.json"
            eval_file.write_text(
                json.dumps(
                    {
                        "name": "bad",
                        "prompt": "bad",
                        "expected_protocols": ["missing-protocol.md"],
                        "expected_outputs": ["Something"],
                        "must_not": [],
                    }
                ),
                encoding="utf-8",
                newline="\n",
            )

            result = validate_repo(copy, run_tests=False)

            self.assertTrue(any("missing-protocol.md" in error for error in result.errors))

    def test_detects_runtime_docs_in_skill_repository(self):
        repo = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as tmp:
            copy = Path(tmp) / "repo"
            self.copy_repo(repo, copy)
            runtime_docs = copy / "docs" / "handoffs"
            runtime_docs.mkdir(parents=True)
            (runtime_docs / "task.md").write_text("# Runtime Handoff\n", encoding="utf-8")

            result = validate_repo(copy, run_tests=False)

            self.assertTrue(any("docs" in error for error in result.errors))

    def test_detects_missing_github_ci_gate(self):
        repo = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as tmp:
            copy = Path(tmp) / "repo"
            self.copy_repo(repo, copy)
            (copy / ".github" / "workflows" / "skill-ci.yml").unlink()

            result = validate_repo(copy, run_tests=False)

            self.assertTrue(any("skill-ci.yml" in error for error in result.errors))

    def test_detects_placeholder_codeowners(self):
        repo = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as tmp:
            copy = Path(tmp) / "repo"
            self.copy_repo(repo, copy)
            (copy / ".github" / "CODEOWNERS").write_text(
                "* @main-agent-owner\n",
                encoding="utf-8",
                newline="\n",
            )

            result = validate_repo(copy, run_tests=False)

            self.assertTrue(any("placeholder owner" in error for error in result.errors))


if __name__ == "__main__":
    unittest.main()
