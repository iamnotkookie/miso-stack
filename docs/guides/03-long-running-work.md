# Guide 3: Run larger work without losing control

A long task needs more than a long prompt. It needs a clear end condition, explicit ownership, and evidence that survives the session.

MisoStack uses a local plan and decision trail for this work. The plan records dependencies and state. The trail records why a decision changed. The harness performs the work.

## Define the end condition

Use a result you can observe. “Improve the parser” is too broad. “Accept the new input format while preserving all existing examples” gives the agent a checkable target.

```text
Use miso to migrate the parser to the new input format.
Preserve existing examples. Split the work into verified units.
Keep a plan and evidence so another session can resume it.
```

The agent should inspect the current system before estimating the work. A risky assumption belongs in an early experiment.

## Give tasks a proof method

For repeated implementation and checks, give the run explicit limits:

```text
Use miso to implement the approved parser spec in a bounded loop.
Stop after five iterations or 20 minutes, whichever comes first.
Keep state and evidence under .miso/parser-loop/.
Complete only when every acceptance check passes.
```

Miso selects `miso-loop` and uses a plan when tasks have dependencies. Without supplied limits, the loop defaults to ten iterations and 30 minutes of active work. Failed attempts consume iterations. Two consecutive attempts without progress or new evidence stop the run as blocked.

The loop saves the task, checks, consumed limits, evidence, next action, and status in `loop.json`. A limit or blocker is not completion. A completion phrase alone cannot prove that the work passed.

To resume, ask `Use miso to resume the loop in .miso/parser-loop/.` The agent checks the current files and keeps the consumed limits. Give a new limit explicitly if the previous run exhausted its budget. To stop, say `Cancel this loop and preserve its evidence.`

This loop runs in the active agent session. MisoStack does not install an automatic continuation hook or daemon. If the host ends the session, resume from its saved state. For scheduled work, use a separately authorized automation.

Each task needs an outcome and a way to verify it. The task owner must know what result to return.

```sh
python3 plugins/miso-stack/scripts/miso.py plan init .miso/parser-migration/plan.json --goal "Verify a parser migration"
```

This creates a starter plan. Edit its tasks and verification method before execution. The starter deliberately cannot be claimed until its generic instruction is replaced.

```sh
python3 plugins/miso-stack/scripts/miso.py plan check .miso/parser-migration/plan.json
python3 plugins/miso-stack/scripts/miso.py plan next .miso/parser-migration/plan.json
```

The checker rejects cycles and missing dependencies. It also checks accepted evidence. If a proof file changes after completion, the plan becomes invalid until the result is deliberately reconciled.

## Separate coordination from execution

The helper does not launch agents. It is a task ledger. The coordinator uses the current harness's worker tools when they are available and permitted.

Use `miso-swarm` for independent coverage or research. Use `miso-design` to compare candidate interfaces. Any parallel work needs separate writable outputs and a lead that checks the results.

If the host has no worker tool, run the tasks serially. Report that difference. Do not create a repository merely to obtain worktrees.

## Keep a decision trail

Record decisions that change the approach. Include the failed experiment when it explains the next choice.

```text
Use miso-trail to record why the second parser design was rejected.
Link the input that caused the failure and the observed output.
```

Avoid a transcript of every command. A useful entry says what changed, why, what evidence supports it, and what happened.

## Handle blockers without repeating them

Mark a blocked task with its missing prerequisite. Continue independent ready tasks. Retry only after the prerequisite changes or a new experiment can distinguish the cause.

An unavailable service stays unverified. It does not become complete because local tests pass. A request to work unattended does not authorize deployment, data deletion, force-pushes, or messages.

## Resume from current state

For session pickup, compare the handoff with the files and running processes. Check whether another worker still owns the task. Then continue from the first ready action.

When pausing, preserve evidence and identify the next command. Stop only owned processes. The next session should not need to reconstruct a missing baseline.

## Check the integrated result

Completed tasks can still interact badly. Run the final acceptance journey on the combined result. Report that proof separately from task-level checks.

See the [plan contract](../../plugins/miso-stack/skills/miso/references/plan.md) for the file format and the [CLI reference](../reference/cli.md) for state transitions.
