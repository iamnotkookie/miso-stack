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
