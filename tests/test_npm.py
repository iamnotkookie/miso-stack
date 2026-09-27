import errno
import fcntl
import json
import os
from pathlib import Path
import pty
import select
import shutil
import signal
import struct
import subprocess
import tempfile
import termios
import time
import unittest

from test_install import FAKE


ROOT = Path(__file__).resolve().parents[1]


def run_terminal(argv, cwd, environment, answer, capture=None, size=(24, 80)):
    """Drive the real npm lifecycle through a disposable terminal."""
    master, slave = pty.openpty()
    original_flags = termios.tcgetattr(slave)[3]
    fcntl.ioctl(slave, termios.TIOCSWINSZ, struct.pack("HHHH", *size, 0, 0))
    def attach_terminal():
        os.setsid()
        fcntl.ioctl(0, termios.TIOCSCTTY, 0)

    try:
        process = subprocess.Popen(argv, cwd=cwd, env=environment, stdin=slave,
                                   stdout=slave, stderr=slave, preexec_fn=attach_terminal)
    finally:
        os.close(slave)
    output = bytearray()
    sent = False
    ready_at = None
    deadline = time.monotonic() + 60
    try:
        while time.monotonic() < deadline:
            if select.select([master], [], [], 0.1)[0]:
                try:
                    chunk = os.read(master, 65536)
                except OSError as error:
                    if error.errno != errno.EIO:  # A closed PTY returns EIO on Linux.
                        raise
                    break
                if not chunk:
                    break
                output.extend(chunk)
                if ready_at is None and (b"Choose [1]" in output or b"Enter Install" in output):
                    ready_at = time.monotonic() + 0.35
            if not sent and ready_at is not None and time.monotonic() >= ready_at:
                if capture:
                    capture(output.decode(errors="replace"))
                keys = answer if isinstance(answer, bytes) else {"0": b"\x1b", "codex": b" \x1b[B \r"}[answer]
                if b"Choose [1]" in output and isinstance(answer, str):
                    keys = (answer + "\n").encode()
                os.write(master, keys)
                sent = True
            if process.poll() is not None:
                break
        status = process.wait(timeout=5)
        restored = termios.tcgetattr(master)[3]
        assert restored & (termios.ECHO | termios.ICANON) == original_flags & (termios.ECHO | termios.ICANON), "Terminal input mode was not restored"
        return status, output.decode(errors="replace")
    finally:
        if process.poll() is None:
            os.killpg(process.pid, signal.SIGKILL)
            process.wait()
        os.close(master)


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
                           "MISO_INSTALL_TEST_STATE": str(temp), "TERM": "xterm-256color"}
            environment.pop("CI", None)

            def run(argv, cwd=ROOT):
                result = subprocess.run(argv, cwd=cwd, env=environment, stdin=subprocess.DEVNULL,
                                        capture_output=True, text=True, timeout=60, start_new_session=True)
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
            install_command = ["npm", "install", "-g", str(archive), "--prefix", str(prefix),
                               "--cache", str(cache), "--offline",
                               "--no-audit", "--no-fund", "--allow-scripts=file:" + str(archive)]
            # npm matches local tarballs by resolved path, not their package name.
            # Permit only the artifact built by this test in the isolated install.
            # No terminal: npm completes without changing any harness settings.
            self.assertIn("Run miso-stack install", run([*install_command, "--foreground-scripts"], cwd=temp))
            self.assertFalse((temp / "calls.jsonl").exists())
            run(install_command, cwd=temp)
            self.assertFalse((temp / "calls.jsonl").exists())
            # Explicit script restrictions and CI still skip setup with a terminal.
            for command, env in [
                ([*install_command, "--ignore-scripts"], environment),
                (install_command, {**environment, "CI": "true"}),
                (["node", str(ROOT / "bin/postinstall.mjs")],
                 {**environment, "npm_config_global": "false"}),
            ]:
                code, output = run_terminal(command, temp, env, "0")
                self.assertEqual(code, 0, output)
                self.assertNotIn("Enter Install", output)
                self.assertFalse((temp / "calls.jsonl").exists())
            # Real terminal: cancelling the lifecycle prompt keeps settings intact.
            code, output = run_terminal(install_command, temp, environment, "0")
            self.assertEqual(code, 0, output)
            self.assertIn("All detected", output)
            self.assertIn("Space Toggle", output)
            self.assertIn("Cancelled", output)
            self.assertFalse((temp / "calls.jsonl").exists())
            code, output = run_terminal([*install_command, "--foreground-scripts"], temp, environment, "0")
            self.assertEqual(code, 0, output)
            self.assertIn("Cancelled", output)
            self.assertFalse((temp / "calls.jsonl").exists())
            # Choose Codex in the npm lifecycle, using its fake native CLI.
            code, output = run_terminal(install_command, temp, environment, "codex")
            self.assertEqual(code, 0, output)
            self.assertIn("Installed. Start a fresh session", output)
            cli = str(prefix / "bin/miso-stack")
            version = json.loads((ROOT / "package.json").read_text())["version"]
            self.assertEqual(run([cli, "--version"], cwd=temp).strip(), version)
            run([cli, "install", "codex", "--dry-run"], cwd=temp)
            self.assertTrue((temp / "codex.json").exists())
            run([cli, "install", "codex"], cwd=temp)
            installed_root = prefix / "lib/node_modules/miso-stack"
            self.assertEqual(Path(json.loads((temp / "codex.json").read_text())).resolve(), installed_root.resolve())
            run([cli, "install", "codex"], cwd=temp)
            calls = [json.loads(row) for row in (temp / "calls.jsonl").read_text().splitlines()]
            self.assertEqual(sum(row[1:4] == ["plugin", "marketplace", "add"] for row in calls), 1)
            self.assertIn(["codex", "plugin", "add", "miso-stack@miso-local"], calls)
            # Setup failure must leave a usable CLI and a recovery command.
            failed_environment = {**environment, "MISO_INSTALL_TEST_FAIL": "codex"}
            code, output = run_terminal(install_command, temp, failed_environment, "codex")
            self.assertEqual(code, 0, output)
            self.assertIn("simulated install failure", output)
            self.assertIn("Run miso-stack install to retry", output)
            self.assertEqual(run([cli, "--version"], cwd=temp).strip(), version)
            run(["python3", str(installed_root / "scripts/check_repository.py")], cwd=temp)


if __name__ == "__main__":
    unittest.main()
