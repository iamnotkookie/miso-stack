import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "plugins/miso-stack/scripts/miso.py"


class ToolsTest(unittest.TestCase):
    def setUp(self):
        self.scratch = tempfile.TemporaryDirectory(prefix="miso-test-")
        self.addCleanup(self.scratch.cleanup)
        self.base = Path(self.scratch.name)

    def call(self, *args, expected=0):
        result = subprocess.run(
            [sys.executable, str(CLI), *map(str, args)],
            cwd=self.base, capture_output=True, text=True, timeout=20,
        )
        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        return json.loads(result.stdout if expected == 0 else result.stderr)

    def plan(self):
        path = self.base / "plan.json"
        data = {
            "version": 1, "goal": "Prove dependent execution",
            "tasks": [
                {"id": "build", "outcome": "An executable result", "depends_on": [],
                 "verification": "Run the result", "status": "pending", "owner": None, "evidence": []},
                {"id": "check", "outcome": "An integrated result", "depends_on": ["build"],
                 "verification": "Run the integration check", "status": "pending", "owner": None, "evidence": []},
            ],
        }
        path.write_text(json.dumps(data))
        return path

    def test_catalog_has_default_and_specialist_workflows(self):
        data = self.call("catalog")
        self.assertEqual(len(data["skills"]), 23)
        self.assertEqual(sum(row["default"] for row in data["workflows"]), 8)
        self.assertIn("documentation", [row["id"] for row in data["workflows"]])

    def test_dependencies_and_proof_gate_completion(self):
        path = self.plan()
        self.assertEqual([t["id"] for t in self.call("plan", "next", path)["ready"]], ["build"])
        self.call("plan", "start", path, "check", "--owner", "lead", expected=1)
        self.call("plan", "finish", path, "build", "--owner", "lead", "--evidence", "proof.txt", expected=1)
        self.call("plan", "start", path, "build", "--owner", "lead")
        proof = self.base / "proof.txt"
        proof.write_text("Observed result: 42\n")
        self.call("plan", "finish", path, "build", "--owner", "other", "--evidence", "proof.txt", expected=1)
        self.call("plan", "finish", path, "build", "--owner", "lead", "--evidence", "proof.txt")
        self.assertEqual([t["id"] for t in self.call("plan", "next", path)["ready"]], ["check"])
        proof.write_text("Changed after acceptance\n")
        self.call("plan", "check", path, expected=1)

    def test_reject_cycle_and_missing_dependency(self):
        path = self.plan()
        data = json.loads(path.read_text())
        data["tasks"][0]["depends_on"] = ["check"]
        path.write_text(json.dumps(data))
        self.call("plan", "check", path, expected=1)
        data["tasks"][0]["depends_on"] = ["missing"]
        path.write_text(json.dumps(data))
        self.call("plan", "check", path, expected=1)

    def test_reject_duplicate_id_and_invalid_status(self):
        path = self.plan()
        data = json.loads(path.read_text())
        data["tasks"][1]["id"] = "build"
        path.write_text(json.dumps(data))
        self.call("plan", "check", path, expected=1)
        data["tasks"][1]["id"] = "check"
        data["tasks"][0]["status"] = "looks-good"
        path.write_text(json.dumps(data))
        self.call("plan", "check", path, expected=1)

    def test_concurrent_claim_has_one_owner(self):
        path = self.plan()
        processes = [subprocess.Popen(
            [sys.executable, str(CLI), "plan", "start", str(path), "build", "--owner", name],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
        ) for name in ["alpha", "beta"]]
        for process in processes:
            process.communicate(timeout=15)
        self.assertEqual(sorted(p.returncode for p in processes), [0, 1])
        self.assertIn(json.loads(path.read_text())["tasks"][0]["owner"], ["alpha", "beta"])

    def test_proof_cannot_escape_plan_directory(self):
        path = self.plan()
        self.call("plan", "start", path, "build", "--owner", "lead")
        with tempfile.TemporaryDirectory() as outside:
            secret = Path(outside) / "outside.txt"
            secret.write_text("outside")
            (self.base / "escape.txt").symlink_to(secret)
            self.call("plan", "finish", path, "build", "--owner", "lead", "--evidence", "escape.txt", expected=1)
        self.assertEqual(json.loads(path.read_text())["tasks"][0]["status"], "running")

    def test_block_and_retry_preserve_dependency_gate(self):
        path = self.plan()
        self.call("plan", "start", path, "build", "--owner", "lead")
        self.call("plan", "block", path, "build", "--owner", "lead", "--reason", "Missing runtime")
        self.assertEqual(self.call("plan", "next", path)["ready"], [])
        self.call("plan", "retry", path, "build", "--reason", "Runtime restored")
        self.assertEqual([t["id"] for t in self.call("plan", "next", path)["ready"]], ["build"])

    def test_init_will_not_overwrite(self):
        path = self.base / "new.json"
        self.call("plan", "init", path, "--goal", "Build a demo")
        original = path.read_bytes()
        self.call("plan", "init", path, "--goal", "Replace it", expected=1)
        self.assertEqual(path.read_bytes(), original)

    def test_install_dry_run_and_collision_are_safe(self):
        dest = self.base / "skills"
        self.call("links", "--target", dest)
        self.assertFalse(dest.exists())
        dest.mkdir()
        (dest / "miso").mkdir()
        marker = dest / "miso/keep.txt"
        marker.write_text("user-owned")
        self.call("links", "--target", dest, "--apply", expected=1)
        self.assertEqual(marker.read_text(), "user-owned")
        self.assertEqual(len(list(dest.iterdir())), 1)

    def test_install_is_idempotent(self):
        dest = self.base / "skills"
        self.call("links", "--target", dest, "--apply")
        result = self.call("links", "--target", dest, "--apply")
        self.assertTrue(all(item["status"] == "linked" for item in result["skills"]))
        self.assertTrue((dest / "miso/SKILL.md").is_file())

    def test_record_preserves_literal_arguments_and_failure(self):
        target = self.base / "record.json"
        self.call("record", target, "--", sys.executable, "-c", "print('$(touch should-not-exist)')")
        record = json.loads(target.read_text())
        self.assertIn("$(touch", record["stdout"])
        self.assertFalse((self.base / "should-not-exist").exists())
        failed = self.base / "failed.json"
        self.call("record", failed, "--", sys.executable, "-c", "raise SystemExit(7)", expected=1)
        self.assertEqual(json.loads(failed.read_text())["exit_code"], 7)

    def test_record_timeout_and_existing_output(self):
        target = self.base / "timeout.json"
        self.call("record", "--timeout", "0.05", target, "--", sys.executable, "-c", "import time; time.sleep(2)", expected=1)
        self.assertEqual(json.loads(target.read_text())["status"], "timeout")
        self.call("record", target, "--", sys.executable, "-c", "print('replace')", expected=1)
        self.assertEqual(json.loads(target.read_text())["status"], "timeout")

    def test_missing_program_still_has_error_receipt(self):
        target = self.base / "missing-program.json"
        self.call("record", target, "--", "/no/such/miso-program", expected=1)
        data = json.loads(target.read_text())
        self.assertEqual(data["status"], "error")
        self.assertIn("No such file", data["stderr"])

    def test_trail_requires_real_evidence(self):
        log = self.base / "trail.jsonl"
        args = ["trail", "add", log, "--decision", "Use a queue", "--reason", "Writers collide", "--result", "Both messages retained"]
        self.call(*args, "--evidence", "missing.txt", expected=1)
        (self.base / "proof.txt").write_text("Observed two messages")
        self.call(*args, "--evidence", "proof.txt")
        self.assertEqual(len(self.call("trail", "show", log)["entries"]), 1)

    def test_malformed_json_has_actionable_error(self):
        path = self.base / "broken.json"
        path.write_text('{"tasks":')
        result = self.call("plan", "check", path, expected=1)
        self.assertIn("error", result)
        self.assertNotIn("Traceback", result["error"])


if __name__ == "__main__":
    unittest.main()
