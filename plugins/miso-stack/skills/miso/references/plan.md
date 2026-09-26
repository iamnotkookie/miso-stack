# Plan contract

Run the helper with `python3 <plugin-root>/scripts/miso.py`. The project root, not the installed plugin, owns plan state and proof.

```json
{
  "version": 1,
  "goal": "The CLI handles empty input",
  "tasks": [
    {
      "id": "fix-empty-input",
      "outcome": "Empty input returns a clear error",
      "depends_on": [],
      "verification": "Run the CLI with an empty list and inspect its status and message",
      "status": "pending",
      "owner": null,
      "evidence": []
    }
  ]
}
```

`plan init PATH --goal TEXT` creates a starter without replacing an existing file. Edit the tasks and concrete verification methods before starting.

`plan check PATH` checks structure, IDs, dependencies, cycles, state, and proof hashes. `plan next PATH` lists pending tasks whose dependencies are complete.

`plan start PATH ID --owner NAME` claims a pending task. `plan finish PATH ID --owner NAME --evidence FILE` accepts proof from that owner. Evidence paths are relative to the plan directory. Repeat `--evidence` for more files. Proof must stay inside that directory and cannot be empty. The helper hashes the file and detects later changes.

`plan block PATH ID --owner NAME --reason TEXT` records a blocker. `plan retry PATH ID --reason TEXT` returns a blocked task to pending after the prerequisite changes.

State changes use a file lock and atomic replacement on macOS and Linux. A hash binds the recorded proof bytes; it cannot establish that the proof supports the claim. The lead must inspect the artifact. The helper runs no workers and executes no verification string from the plan.
