# Local CLI reference

Run `python3 plugins/miso-stack/scripts/miso.py --help` from this repo. `bin/miso` is a shell wrapper for the same helper. Python 3.10+ and macOS or Linux are required. No third-party Python packages are required.

Commands return JSON on stdout. Operational errors return JSON on stderr with exit status 1. Argument syntax errors use argparse's help and exit status 2. Commands do not initialize Git, select models, send messages, or deploy.

| Command | Result |
| --- | --- |
| `catalog` | Skill and workflow inventory. |
| `check` | Frontmatter, names, descriptions, workflow references, and local skill links. |
| `doctor` | Package result and host binary paths; no runtime or login claim. |
| `links [--target DIR]` | Dry-run shared skill installation. |
| `links [--target DIR] --apply` | Create missing links; refuse collisions. |
| `plan init PATH --goal TEXT` | New starter plan; refuses overwrite. |
| `plan check PATH` | Validate structure, dependencies, states, and proof hashes. |
| `plan next PATH` | List ready pending tasks and blocked IDs. |
| `plan start PATH ID --owner NAME` | Atomically claim a ready task. |
| `plan finish PATH ID --owner NAME --evidence FILE` | Mark a running task complete with hashed proof. Repeat the evidence flag for more files. |
| `plan block PATH ID --owner NAME --reason TEXT` | Record a blocked task. |
| `plan retry PATH ID --reason TEXT` | Return a blocked task to pending. |
| `record [--timeout SECONDS] PATH -- PROGRAM ARGS` | Run the supplied command without a shell and write a new receipt. |
| `trail add PATH --decision TEXT --reason TEXT --evidence FILE --result TEXT` | Append a decision with a hash of existing evidence. |
| `trail show PATH` | Read the JSONL trail. |

## File behavior

Plans follow [the plan contract](../../plugins/miso-stack/skills/miso/references/plan.md). Proof paths are relative to the plan directory and cannot escape it through a symlink. Completed tasks require nonempty evidence. The tool checks file identity, not semantic truth.

Trail evidence is relative to the command's current directory. Trails retain that base path. Logs are local artifacts; do not include secrets or unrelated private data.

`record` captures the working directory, arguments, time, exit status, stdout, and stderr. Output is limited to 128 KiB per stream in the receipt and marked when truncated. The default timeout is 120 seconds; the maximum is 3600. Timeout stops the process group started for the command. A failed command still gets a receipt and makes the helper fail. Do not put credentials in arguments or output.

`record` runs the command you supply. It is not a sandbox and cannot make a destructive command safe. Use the harness sandbox and a disposable fixture for evaluations.

Shared links require this source tree to remain at its current location. Plugin caches may contain a snapshot of the files. Use host update commands and start a fresh session after changes.
