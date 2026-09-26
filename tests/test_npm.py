import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

from test_install import FAKE


ROOT = Path(__file__).resolve().parents[1]


@unittest.skipUnless(shutil.which("npm") and shutil.which("node"), "npm and Node.js are required for package qualification")
class NpmPackageTest(unittest.TestCase):
    def test_packed_global_install_has_source_manifests_and_working_command(self):
        with tempfile.TemporaryDirectory(prefix="miso npm sandbox ") as directory:
            temp = Path(directory)
            cache = temp / "cache"
            prefix = temp / "prefix"
            fake_bin = temp / "fake-bin"
            fake_bin.mkdir()
            codex = fake_bin / "codex"
            codex.write_text(FAKE)
            codex.chmod(0o755)
            environment = {**os.environ, "PATH": str(fake_bin) + os.pathsep + os.environ["PATH"],
                           "MISO_INSTALL_TEST_STATE": str(temp)}

            def run(argv, cwd=ROOT):
                result = subprocess.run(argv, cwd=cwd, env=environment, stdin=subprocess.DEVNULL,
                                        capture_output=True, text=True, timeout=60)
                self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
                return result.stdout

            packed = json.loads(run(["npm", "pack", "--json", "--ignore-scripts", "--offline",
                                     "--cache", str(cache), "--pack-destination", str(temp)]))[0]
            names = {row["path"] for row in packed["files"]}
            required = {".agents/plugins/marketplace.json", ".claude-plugin/marketplace.json",
                        "plugins/miso-stack/skills/miso/SKILL.md", "bin/miso-stack.mjs", "scripts/install.py"}
            self.assertTrue(required <= names)
            self.assertFalse(any(name.startswith("evidence/") or "__pycache__" in name or name.endswith(".pyc") for name in names))
            archive = temp / packed["filename"]
            run(["npm", "install", "-g", str(archive), "--prefix", str(prefix), "--cache", str(cache),
                 "--offline", "--ignore-scripts", "--no-audit", "--no-fund"], cwd=temp)
            cli = str(prefix / "bin/miso-stack")
            version = json.loads((ROOT / "package.json").read_text())["version"]
            self.assertEqual(run([cli, "--version"], cwd=temp).strip(), version)
            run([cli, "install", "codex", "--dry-run"], cwd=temp)
            self.assertFalse((temp / "codex.json").exists())
            run([cli, "install", "codex"], cwd=temp)
            installed_root = prefix / "lib/node_modules/miso-stack"
            self.assertEqual(Path(json.loads((temp / "codex.json").read_text())).resolve(), installed_root.resolve())
            run([cli, "install", "codex"], cwd=temp)
            calls = [json.loads(row) for row in (temp / "calls.jsonl").read_text().splitlines()]
            self.assertEqual(sum(row[1:4] == ["plugin", "marketplace", "add"] for row in calls), 1)
            self.assertIn(["codex", "plugin", "add", "miso-stack@miso-local"], calls)
            run(["python3", str(installed_root / "scripts/check_repository.py")], cwd=temp)


if __name__ == "__main__":
    unittest.main()
