# Make your first verified change

This tutorial uses a disposable Python command. You will observe a bug, ask `miso` to repair it, and check the result. No repository, external service, or credentials are needed for the sample app. Your coding harness still needs its normal model access.

## Create the sandbox

From the MisoStack directory, run:

```sh
python3 scripts/create_sandbox.py /tmp/miso-first-change
cd /tmp/miso-first-change
python3 calculator.py 2 3
```

The command prints `-1`. The documented operation is addition, so the expected result is `5`. The setup command refuses an existing target. Choose a new path for another run.

## Ask the agent to fix it

Start an installed harness in the sandbox and send:

```text
Use miso to fix calculator.py. Its documented operation is addition,
but input 2 3 returns -1. Reproduce the failure before editing.
Use the existing tests, verify the command itself, and save proof in evidence/.
Do not initialize Git or change files outside this sandbox.
```

The agent should read the bug-fix playbook and its harness map. It should run the failing command and tests before repairing the implementation. Review its tool trace rather than accepting its final sentence alone.

## Check the result yourself

```sh
python3 calculator.py 2 3
python3 calculator.py -2 3
python3 -m unittest discover -s tests
```

Expect `5`, then `1`, then passing tests. The negative input helps catch a repair that merely returns a constant. Read the saved evidence. It should identify the commands and show both the failure and the successful result.

The sandbox also contains an unrelated `KEEP.txt`. Its content must remain unchanged. No `.git` directory should exist.

## What this proves

The example tests a complete bug-fix path through a real CLI. It does not prove browser verification, concurrent workers, or safe production deployment. Use the [evaluation guide](../how-to/evaluate.md) for wider coverage.
