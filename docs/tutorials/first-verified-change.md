# Make your first verified change

This tutorial uses a disposable Python command. You will observe a bug, ask `miso` to repair it, and check the result. No repository, external service, or credentials are needed for the sample app. Your coding harness still needs its normal model access.

## Before you start

Install MisoStack with `npm install -g miso-stack` and select your coding agent. You need Python 3.10+, Node.js 18+, and a working agent login. This tutorial runs on macOS or Linux.

If npm blocks the setup script, run `miso-stack install` to open the picker.

The commands below go in your terminal. The task prompt goes in your agent's chat.

## Create the sandbox

Create a new temporary folder, then use the fixture included in the npm package:

```sh
miso_tutorial_dir=$(mktemp -d "${TMPDIR:-/tmp}/miso-tutorial.XXXXXX")
python3 "$(npm root -g)/miso-stack/scripts/create_sandbox.py" "$miso_tutorial_dir/project"
cd "$miso_tutorial_dir/project"
python3 calculator.py 2 3
```

The command prints `-1`. The documented operation is addition, so the expected result is `5`. Each run creates a new folder. You do not need to download the MisoStack repository.

If the setup script is missing, check `npm root -g` and confirm that `npm install -g miso-stack` succeeded. For a source checkout, use its `scripts/create_sandbox.py` instead.

## Ask the agent to fix it

Start your installed agent from this folder: `codex`, `claude`, `grok`, or `opencode`. Send:

```text
Use miso to fix calculator.py. Its documented operation is addition,
but input 2 3 returns -1. Reproduce the failure before editing.
Use the existing tests, verify the command itself, and save proof in evidence/.
Do not initialize Git or change files outside this sandbox.
```

The agent should read the bug-fix playbook and its harness map. It should run the failing command and tests before repairing the implementation. Review its tool trace rather than accepting its final sentence alone.

You can replace `Use miso to` with your agent's [invocation shortcut](../how-to/use-miso.md#can-i-type-miso). For example, Codex accepts `$miso fix calculator.py…`. Keep the task and constraints after the shortcut.

## Check the result yourself

```sh
python3 calculator.py 2 3
python3 calculator.py -2 3
python3 -m unittest discover -s tests
```

Expect `5`, then `1`, then passing tests. The negative input helps catch a repair that merely returns a constant. Read the saved evidence. It should identify the commands and show both the failure and the successful result.

The sandbox also contains an unrelated `KEEP.txt`. Its content must remain `This unrelated user file must remain unchanged.` No `.git` directory should exist. The `evidence/` folder belongs only to this disposable tutorial folder.

## What this proves

The example tests a complete bug-fix path through a real CLI. It does not prove browser verification, concurrent workers, or safe production deployment. Use the [evaluation guide](../how-to/evaluate.md) for wider coverage.
