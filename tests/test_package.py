import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins/miso-stack"


class PackageTest(unittest.TestCase):
    def test_evaluator_isolates_input_and_reports_fixture_changes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            host = root / "codex"
            host.write_text("#!/usr/bin/env python3\nimport json, sys\nfrom pathlib import Path\nPath('unrequested.txt').write_text('mutation')\nprint(json.dumps({'inherited_input': sys.stdin.read()}))\n")
            host.chmod(0o755)
            output = root / "evaluation"
            command = [sys.executable, str(ROOT / "scripts/run_evaluation.py"),
                       "--harness", "codex", "--case", "smoke", "--output", str(output)]
            result = subprocess.run(command, input="parent orchestration text", capture_output=True,
                                    text=True, env={**os.environ, "PATH": str(root) + os.pathsep + os.environ["PATH"]})
            self.assertEqual(result.returncode, 0, result.stderr)
            trace = json.loads((output / "stdout.jsonl").read_text())
            self.assertEqual(trace["inherited_input"], "")
            run = json.loads((output / "run.json").read_text())
            self.assertEqual(run["fixture_changes"], {"added": ["unrequested.txt"], "removed": [], "changed": []})

    def test_relocated_package_keeps_references_and_hook_valid(self):
        with tempfile.TemporaryDirectory(prefix="miso path with spaces ") as directory:
            target = Path(directory) / "miso-stack"
            shutil.copytree(PLUGIN, target, ignore=shutil.ignore_patterns("__pycache__"))
            result = subprocess.run([sys.executable, str(target / "scripts/miso.py"), "check"], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            hook = subprocess.run([sys.executable, str(target / "scripts/session_start.py")], capture_output=True, text=True)
            data = json.loads(hook.stdout)["hookSpecificOutput"]
            self.assertEqual(data["hookEventName"], "SessionStart")
            self.assertIn(str(target / "skills/miso/SKILL.md"), data["additionalContext"])
            self.assertIn("grants no permissions", data["additionalContext"])

    def test_every_skill_has_a_behavioral_case(self):
        catalog = json.loads((PLUGIN / "catalog.json").read_text())
        cases = json.loads((ROOT / "evals/cases.json").read_text())["cases"]
        covered = {name for case in cases for name in case["skills"]}
        self.assertEqual({skill["name"] for skill in catalog["skills"]}, covered)

    def test_routing_cases_cover_every_supporting_skill(self):
        catalog = json.loads((PLUGIN / "catalog.json").read_text())
        cases = json.loads((ROOT / "evals/capability-routing.json").read_text())["cases"]
        self.assertEqual({skill["name"] for skill in catalog["skills"]} - {catalog["entry"]},
                         {case["skill"] for case in cases})
        self.assertEqual(len({case["id"] for case in cases}), len(cases))

    def test_package_rejects_a_router_that_omits_a_skill(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "plugin"
            shutil.copytree(PLUGIN, target, ignore=shutil.ignore_patterns("__pycache__"))
            router = target / "skills/miso/references/routing.md"
            router.write_text("\n".join(line for line in router.read_text().splitlines()
                                         if "../../miso-spec/SKILL.md" not in line))
            result = subprocess.run([sys.executable, str(target / "scripts/miso.py"), "check"], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("router does not reach every supporting skill", result.stderr)

    def package_check_after(self, edit):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "plugin"
            shutil.copytree(PLUGIN, target, ignore=shutil.ignore_patterns("__pycache__"))
            edit(target)
            return subprocess.run([sys.executable, str(target / "scripts/miso.py"), "check"], capture_output=True, text=True)

    def test_package_rejects_a_principle_without_a_trigger(self):
        def edit(target):
            leaf = target / "skills/miso/references/principles/prove-it-works.md"
            leaf.write_text(leaf.read_text().replace("**Apply when:**", "**Note:**"))
        result = self.package_check_after(edit)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("principles/prove-it-works.md: use a title", result.stderr)

    def test_package_rejects_a_principle_missing_from_the_index(self):
        def edit(target):
            leaf = target / "skills/miso/references/principles/new-idea.md"
            leaf.write_text("# New idea\n\n**Apply when:** Now.\n\n**Rule:** Do it.\n\n**Why:** Reason.\n\n- Act.\n")
        result = self.package_check_after(edit)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("new-idea.md has no row", result.stderr)

    def test_package_rejects_a_citation_of_the_principle_index(self):
        def edit(target):
            skill = target / "skills/miso-tdd/SKILL.md"
            skill.write_text(skill.read_text() + "\nSee [rules](../miso/references/principles.md).\n")
        result = self.package_check_after(edit)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("cites the principles index", result.stderr)

    def test_a_deleted_principle_breaks_its_citations(self):
        result = self.package_check_after(lambda target: (target / "skills/miso/references/principles/structure.md").unlink())
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("miso-tdd/SKILL.md", result.stderr)

    def test_package_rejects_a_playbook_without_a_reply(self):
        def edit(target):
            playbook = target / "skills/miso/playbooks/bug-fix.md"
            playbook.write_text(playbook.read_text().split("## Reply")[0])
        result = self.package_check_after(edit)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("playbooks/bug-fix.md: sections must be", result.stderr)

    def test_package_rejects_a_playbook_that_drifts_from_the_catalog(self):
        def edit(target):
            playbook = target / "skills/miso/playbooks/feature.md"
            playbook.write_text(playbook.read_text().replace("Use for: Add or change", "Use for: Change"))
        result = self.package_check_after(edit)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Use for differs from the catalog trigger", result.stderr)

    def test_package_rejects_a_playbook_whose_proof_drifts(self):
        def edit(target):
            catalog = target / "catalog.json"
            data = json.loads(catalog.read_text())
            next(row for row in data["workflows"] if row["id"] == "feature")["proof"] = "Something else."
            catalog.write_text(json.dumps(data))
        result = self.package_check_after(edit)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("playbooks/feature.md: Completion evidence differs", result.stderr)

    def test_package_rejects_an_empty_reply(self):
        def edit(target):
            playbook = target / "skills/miso/playbooks/bug-fix.md"
            playbook.write_text(playbook.read_text().split("## Reply")[0] + "## Reply\n\n")
        result = self.package_check_after(edit)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("playbooks/bug-fix.md: Reply must say", result.stderr)

    def test_package_rejects_an_orphaned_reference(self):
        result = self.package_check_after(lambda target: (target / "skills/miso-review/references/extra.md").write_text("# Extra\n"))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("references/extra.md: nothing links", result.stderr)

    def test_review_skill_names_both_change_types(self):
        catalog = json.loads((PLUGIN / "catalog.json").read_text())
        description = next(row["description"] for row in catalog["skills"] if row["name"] == "miso-review")
        for term in ["pull request", "merge request"]:
            self.assertIn(term, description)

    def test_review_fixture_diff_applies_to_the_fixture(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "fixture"
            subprocess.run([sys.executable, str(ROOT / "scripts/create_sandbox.py"), str(target)], capture_output=True, check=True)
            result = subprocess.run(["git", "apply", "--check", "changes/review.diff"], cwd=target, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)

    def test_package_rejects_a_long_dash_in_a_skill(self):
        def edit(target):
            skill = target / "skills/miso-tdd/SKILL.md"
            skill.write_text(skill.read_text() + "\nOne thought \u2014 another thought.\n")
        result = self.package_check_after(edit)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("has a long dash", result.stderr)

    def test_repository_check_rejects_stale_readme_counts(self):
        with tempfile.TemporaryDirectory() as directory:
            target = self.repository_check_copy(directory)
            catalog = json.loads((target / "plugins/miso-stack/catalog.json").read_text())
            current = f"{len(catalog['skills'])} skills"
            for stale in ["16 skills and 24 workflows", "1" + current + " and 24 workflows"]:
                with self.subTest(stale):
                    (target / "README.md").write_text(stale + "\n")
                    result = subprocess.run([sys.executable, str(target / "scripts/check_repository.py")], capture_output=True, text=True)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn("catalog counts", result.stdout)
    def overlap(self, upstream_text):
        with tempfile.TemporaryDirectory() as directory:
            (Path(directory) / "skill.md").write_text(upstream_text)
            return subprocess.run([sys.executable, str(ROOT / "scripts/check_overlap.py"), directory], capture_output=True, text=True)

    def test_overlap_check_finds_a_copied_sequence(self):
        result = self.overlap("Someone wrote: Use `miso` as the single entry point elsewhere.")
        self.assertEqual(result.returncode, 1)
        self.assertIn("miso/SKILL.md", result.stdout)

    def test_overlap_check_passes_on_unrelated_text(self):
        self.assertEqual(self.overlap("Zebra quartz vexing jumbo plaid fox nymph.").returncode, 0)

    def test_package_rejects_an_oversized_principle(self):
        def edit(target):
            leaf = target / "skills/miso/references/principles/structure.md"
            leaf.write_text(leaf.read_text() + "- " + "word " * 251 + "\n")
        result = self.package_check_after(edit)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("principles/structure.md: more than 250 words", result.stderr)

    def test_package_rejects_a_duplicate_principle_row(self):
        def edit(target):
            index = target / "skills/miso/references/principles.md"
            index.write_text(index.read_text() + "| Again. | [structure](principles/structure.md) |\n")
        result = self.package_check_after(edit)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("structure.md is listed twice", result.stderr)

    def grade(self, case, answer):
        with tempfile.TemporaryDirectory() as directory:
            trace = Path(directory) / "stdout.jsonl"
            event = {"type": "result", "result": "Here it is:\n```json\n" + json.dumps(answer) + "\n```"}
            trace.write_text("not json\n" + json.dumps({"prompt": "[{\"id\": \"1\"}]"}) + "\n" + json.dumps(event) + "\n")
            return subprocess.run([sys.executable, str(ROOT / "scripts/grade_routing.py"), "--case", case, str(trace)],
                                  capture_output=True, text=True)

    def test_routing_grader_accepts_correct_answers(self):
        cases = json.loads((ROOT / "evals/capability-routing.json").read_text())["cases"]
        answer = [{"id": row["id"], "skill": row["skill"], "mode": row["mode"]} for row in cases]
        result = self.grade("capability-routing", answer)
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertEqual(json.loads(result.stdout)["correct"], len(cases))

    def test_routing_grader_reports_a_wrong_or_missing_route(self):
        cases = json.loads((ROOT / "evals/routing.json").read_text())["cases"]
        answer = [{"id": row["id"], "workflow": row["expected_workflow"]} for row in cases[1:]]
        answer[0]["workflow"] = "wrong"
        result = self.grade("routing", answer)
        self.assertEqual(result.returncode, 1)
        graded = json.loads(result.stdout)
        self.assertEqual(graded["correct"], len(cases) - 2)
        self.assertEqual({miss["id"] for miss in graded["misses"]}, {cases[0]["id"], cases[1]["id"]})

    def test_routing_grader_fails_on_a_trace_with_no_answer(self):
        with tempfile.TemporaryDirectory() as directory:
            trace = Path(directory) / "stdout.jsonl"
            trace.write_text(json.dumps({"type": "result", "result": "I could not classify these."}) + "\n")
            result = subprocess.run([sys.executable, str(ROOT / "scripts/grade_routing.py"), "--case", "routing", str(trace)],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)

    def test_routing_grader_rejects_a_trace_that_touches_the_labels(self):
        cases = json.loads((ROOT / "evals/routing.json").read_text())["cases"]
        answer = [{"id": row["id"], "workflow": row["expected_workflow"]} for row in cases]
        with tempfile.TemporaryDirectory() as directory:
            trace = Path(directory) / "stdout.jsonl"
            trace.write_text(json.dumps({"tool": "Read", "input": "/repo/evals/routing.json"}) + "\n"
                             + json.dumps({"type": "result", "result": json.dumps(answer)}) + "\n")
            result = subprocess.run([sys.executable, str(ROOT / "scripts/grade_routing.py"), "--case", "routing", str(trace)],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertIn("could have read the labels", result.stderr)

    def repository_check_copy(self, directory):
        target = Path(directory) / "repo"
        for name in ["package.json", "plugins/miso-stack/catalog.json", "scripts/check_repository.py", ".claude-plugin/marketplace.json",
                     ".grok-plugin/marketplace.json", ".agents/plugins/marketplace.json",
                     "plugins/miso-stack/.claude-plugin/plugin.json", "plugins/miso-stack/.codex-plugin/plugin.json",
                     "plugins/miso-stack/.grok-plugin/plugin.json"]:
            (target / name).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(ROOT / name, target / name)
        catalog = json.loads((target / "plugins/miso-stack/catalog.json").read_text())
        (target / "README.md").write_text(f"{len(catalog['skills'])} skills and {len(catalog['workflows'])} workflows\n")
        return target

    def test_repository_check_accepts_matching_versions(self):
        with tempfile.TemporaryDirectory() as directory:
            target = self.repository_check_copy(directory)
            result = subprocess.run([sys.executable, str(target / "scripts/check_repository.py")], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout)

    def test_repository_check_rejects_version_drift(self):
        for name in ["plugins/miso-stack/.claude-plugin/plugin.json", ".claude-plugin/marketplace.json"]:
            with self.subTest(name), tempfile.TemporaryDirectory() as directory:
                target = self.repository_check_copy(directory)
                path = target / name
                data = json.loads(path.read_text())
                (data["plugins"][0] if "plugins" in data else data)["version"] = "0.0.1"
                path.write_text(json.dumps(data))
                result = subprocess.run([sys.executable, str(target / "scripts/check_repository.py")], capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(name, result.stdout)
                self.assertIn("package.json", result.stdout)

    def test_fixture_exposes_defect_and_preserves_existing_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "fixture"
            command = [sys.executable, str(ROOT / "scripts/create_sandbox.py"), str(target)]
            created = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(created.returncode, 0, created.stderr)
            result = subprocess.run([sys.executable, "calculator.py", "2", "3"], cwd=target, capture_output=True, text=True)
            self.assertEqual(result.stdout.strip(), "-1")
            original = (target / "KEEP.txt").read_bytes()
            repeated = subprocess.run(command, capture_output=True, text=True)
            self.assertNotEqual(repeated.returncode, 0)
            self.assertEqual((target / "KEEP.txt").read_bytes(), original)


if __name__ == "__main__":
    unittest.main()
