import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
SPEC = importlib.util.spec_from_file_location("miso_installer", ROOT / "scripts/install.py")
INSTALLER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(INSTALLER)

FAKE = '''#!/usr/bin/env python3
import json, os, sys
from pathlib import Path
host = Path(sys.argv[0]).name
args = sys.argv[1:]
state = Path(os.environ["MISO_INSTALL_TEST_STATE"])
with (state / "calls.jsonl").open("a") as log:
    log.write(json.dumps([host, *args]) + "\\n")
record = state / (host + ".json")
if args == ["plugin", "marketplace", "list", "--json"]:
    source = json.loads(record.read_text()) if record.exists() else None
    rows = ([{"name": "miso-local", "root" if host == "codex" else "path": source}] if source else [])
    print(json.dumps({"marketplaces": rows} if host == "codex" else rows))
elif args[:3] == ["plugin", "marketplace", "add"]:
    record.write_text(json.dumps(args[3]))
elif os.environ.get("MISO_INSTALL_TEST_FAIL") == host:
    sys.stderr.write("simulated install failure")
    sys.exit(1)
else:
    print("installed")
'''


class InstallerTest(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory(prefix="miso installer ")
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.home = self.root / "user"
        self.home.mkdir()
        self.bin = self.root / "bin"
        self.bin.mkdir()
        for host in INSTALLER.HOSTS:
            binary = self.bin / host
            binary.write_text(FAKE)
            binary.chmod(0o755)
        self.environment = patch.dict(os.environ, {
            "PATH": str(self.bin) + os.pathsep + os.environ["PATH"],
            "MISO_INSTALL_TEST_STATE": str(self.root),
            "TERM": "dumb",
        })
        self.environment.start()
        self.addCleanup(self.environment.stop)
        self.home_patch = patch.object(Path, "home", return_value=self.home)
        self.home_patch.start()
        self.addCleanup(self.home_patch.stop)

    def invoke(self, names=(), dry_run=False):
        args = type("Args", (), {"harnesses": names, "dry_run": dry_run, "yes": True})()
        with contextlib.redirect_stdout(io.StringIO()):
            INSTALLER.install(args)

    def calls(self):
        path = self.root / "calls.jsonl"
        return [json.loads(line) for line in path.read_text().splitlines()] if path.exists() else []

    def test_detect_install_and_repeat_keep_links_and_marketplaces(self):
        self.invoke()
        target = self.home / ".agents/skills"
        self.assertEqual(len(list(target.glob("miso*/SKILL.md"))), 23)
        self.invoke()
        adds = [c for c in self.calls() if c[1:4] == ["plugin", "marketplace", "add"]]
        self.assertEqual(len(adds), 2)
        self.assertTrue((target / "miso").is_symlink())

    def test_preview_only_reads_and_creates_no_links(self):
        self.invoke(dry_run=True)
        self.assertTrue(all(c[1:] == ["plugin", "marketplace", "list", "--json"] for c in self.calls()))
        self.assertFalse((self.home / ".agents").exists())

    def test_marketplace_conflict_prevents_all_install_writes(self):
        (self.root / "claude.json").write_text(json.dumps(str(self.root / "other-source")))
        with self.assertRaisesRegex(ValueError, "another source"):
            self.invoke()
        self.assertTrue(all(c[2] == "marketplace" and c[3] == "list" for c in self.calls()))
        self.assertFalse((self.home / ".agents").exists())

    def test_skill_collision_prevents_plugin_changes(self):
        collision = self.home / ".agents/skills/miso"
        collision.mkdir(parents=True)
        with self.assertRaisesRegex(ValueError, "replaced"):
            self.invoke()
        self.assertEqual(self.calls(), [])
        self.assertFalse(collision.is_symlink())

    def test_native_failure_is_visible_and_stops_later_targets(self):
        with patch.dict(os.environ, {"MISO_INSTALL_TEST_FAIL": "codex"}):
            with self.assertRaisesRegex(ValueError, "simulated install failure"):
                self.invoke()
        self.assertFalse(any(c[0] == "claude" and c[2] == "install" for c in self.calls()))
        self.assertFalse((self.home / ".agents").exists())

    def test_selected_shared_host_does_not_touch_plugin_managers(self):
        self.invoke(["opencode"])
        self.assertEqual(self.calls(), [])
        self.assertTrue((self.home / ".agents/skills/miso").is_symlink())

    def test_missing_host_fails_before_side_effects(self):
        with patch.object(INSTALLER.shutil, "which", return_value=None):
            with self.assertRaisesRegex(ValueError, "not found"):
                self.invoke(["codex"])
        self.assertEqual(self.calls(), [])

    def choose(self, answers):
        args = type("Args", (), {"harnesses": [], "dry_run": False, "yes": False})()
        with patch.object(sys.stdin, "isatty", return_value=True), \
                patch.object(sys.stdout, "isatty", return_value=True), \
                patch("builtins.input", side_effect=answers):
            return INSTALLER.select_targets(args)

    def test_picker_default_selects_all_detected(self):
        self.assertEqual(self.choose([""]), list(INSTALLER.HOSTS))

    def test_picker_retries_invalid_and_accepts_multiple_choices(self):
        self.assertEqual(self.choose(["unknown", "2, opencode 2"]), ["codex", "opencode"])

    def test_picker_cancel_does_not_run_native_commands(self):
        args = type("Args", (), {"harnesses": [], "dry_run": False, "yes": False})()
        with patch.object(sys.stdin, "isatty", return_value=True), \
                patch.object(sys.stdout, "isatty", return_value=True), \
                patch("builtins.input", return_value="0"):
            INSTALLER.install(args)
        self.assertEqual(self.calls(), [])
        self.assertFalse((self.home / ".agents").exists())

    def test_headless_requires_explicit_targets_or_yes(self):
        args = type("Args", (), {"harnesses": [], "dry_run": False, "yes": False})()
        with patch.object(sys.stdin, "isatty", return_value=False):
            with self.assertRaisesRegex(ValueError, "--yes"):
                INSTALLER.install(args)
        self.assertEqual(self.calls(), [])

    def test_no_detected_harnesses_has_actionable_error(self):
        with patch.object(INSTALLER.shutil, "which", return_value=None):
            with self.assertRaisesRegex(ValueError, "No supported harness"):
                self.invoke()


if __name__ == "__main__":
    unittest.main()
