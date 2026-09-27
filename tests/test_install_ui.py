import json
import os
from pathlib import Path
import sys
import unittest

from test_npm import run_terminal


ROOT = Path(__file__).resolve().parents[1]


class PickerTest(unittest.TestCase):
    def pick(self, keys, environment=None, size=(24, 80)):
        code = (f"import sys,json; sys.path.insert(0,{str(ROOT / 'scripts')!r}); "
                "from install_ui import choose; "
                "print('RESULT=' + json.dumps(choose(['codex','opencode'])))")
        status, output = run_terminal([sys.executable, "-c", code], ROOT,
                                      {**os.environ, "TERM": "xterm-256color", **(environment or {})}, keys, size=size)
        self.assertEqual(status, 0, output)
        marker = output.rsplit("RESULT=", 1)[1].splitlines()[0]
        return json.loads(marker), output

    def test_enter_accepts_recommended_selection(self):
        chosen, output = self.pick(b"\r")
        self.assertEqual(chosen, ["codex", "opencode"])
        self.assertIn("not found", output)

    def test_arrows_and_space_choose_subset_in_small_monochrome_terminal(self):
        chosen, output = self.pick(b" \x1b[B \r", {"NO_COLOR": "1"}, (18, 48))
        self.assertEqual(chosen, ["codex"])
        self.assertIn("Enter Install", output)

    def test_empty_selection_stays_open_and_escape_cancels(self):
        chosen, output = self.pick(b" \r\x1b")
        self.assertEqual(chosen, [])
        self.assertIn("Select at least one", output)

    def test_plain_terminal_accepts_names(self):
        chosen, output = self.pick("codex", {"TERM": "dumb"})
        self.assertEqual(chosen, ["codex"])
        self.assertNotIn("\x1b[?1049h", output)
