# Use Miso for everyday work

Start with `miso` and describe the result you want. It selects the supporting skills. You do not need to remember their names.

Install [MisoStack](install.md), then start a fresh agent session in your project. Send the examples below in the agent's chat, not your shell.

## Can I type /miso?

The shortcut depends on your coding agent:

| Agent | Start a task | Another way |
| --- | --- | --- |
| Codex | `$miso explain how this project works` | Open `/skills` and select the Miso entry. |
| Claude Code | `/miso-stack:miso explain how this project works` | Use the plugin entry in slash-command completion. |
| Grok Build | `/miso explain how this project works` | Open `/skills` to inspect available skills. |
| OpenCode | `Use miso to explain how this project works.` | Ask it to load the `miso` skill explicitly. |

For any supported agent, you can write:

```text
Use miso to explain how this project works. Keep this pass read-only.
```

Codex documents `$skill` invocation and its `/skills` picker. Claude Code gives plugin skills a namespace. Grok Build exposes user-invocable skills as slash commands. OpenCode loads skills through its skill tool; MisoStack does not install a separate OpenCode `/miso` command.

Sources: [Codex skills](https://learn.chatgpt.com/docs/build-skills), [Codex commands](https://learn.chatgpt.com/docs/developer-commands?surface=cli), [Claude Code skills](https://code.claude.com/docs/en/skills), [Grok Build skills](https://docs.x.ai/build/features/skills-plugins-marketplaces), [OpenCode skills](https://opencode.ai/docs/skills/) and [commands](https://opencode.ai/docs/commands/).

## Give it a task, a constraint, and a check

A useful request tells Miso what you want, what must stay true, and how to check success:

```text
Use miso to add CSV export to the reports page.
Preserve the current filters and column order.
Export an empty report and a report with data, then inspect both files.
```

You can omit checks when you do not know what to run. Ask Miso to identify them from the project. Include error output, file paths, or a concrete example when available.

Miso should inspect the relevant code, choose a procedure, complete the requested work, and report the observed result. For substantial changes, expect tests and a check of the actual user path. A browser task can require screenshots; a CLI task usually needs commands and outputs.

## Choose how far it should go

These are separate requests. Use the step you need; a small fix does not need all four.

### Understand before changing

```text
Use miso to explain how report exports work and why they run in a worker.
Trace the code and available history. Label any inferred reasons.
Do not change files.
```

Expect an explanation with code references and clear limits on what the history establishes.

### Turn an idea into reviewable work

```text
Use miso to turn our export discussion into a local spec and separate tickets.
Keep the decisions we already made. Include acceptance checks and dependencies.
Stop before implementation or publication.
```

Expect a spec under `specs/` and ticket files under `tasks/`, unless the project defines other locations. Review their outcomes and scope before requesting implementation.

### Build and verify

```text
Use miso to implement the approved export spec in specs/report-export.md.
Verify each acceptance condition and update the relevant documentation.
Show what ran and what remains unverified.
```

Expect changes you can inspect and proof tied to the acceptance conditions. If an environment is unavailable, the result should say which checks could not run.

### Review independently of editing

```text
Use miso to review the current diff against specs/report-export.md.
Check correctness, affected callers, and missing verification.
Report findings with file references. Review only; do not edit.
```

Review the findings, then request the fixes you want. A review request does not authorize implementation.

## Prompts for common tasks

| What you need | Send this |
| --- | --- |
| Diagnose a bug | `Use miso to reproduce this failure and identify its cause. Stop before fixing it.` |
| Fix a bug | `Use miso to fix this failure. Reproduce it first, then rerun the same case after the fix.` |
| Test a design | `Use miso to compare two designs for this API. Prototype the uncertain parts. Recommend one and stop before production implementation.` |
| Measure performance | `Use miso to improve this slow query. Capture a baseline and repeat the same workload after the change.` |
| Resolve conflicts | `Use miso to resolve this rebase's conflicts. Preserve the intent of both changes and run the affected tests. Leave the rebase paused for review.` |
| Explain a result | `Use miso to explain that decision in plain English, with one concrete example.` |
| Improve documentation | `Use miso to improve this README. Check its commands and write in Simplified Technical English.` |
| Build app controls | `Use miso to create verification tools for this app. Reuse existing tooling, map the features, and prove one complete user journey.` |
| Resume work | `Use miso to resume tasks/report-export. Read the saved decisions, check the current files, and continue the next ready task.` |
| Tend the codebase | `Use miso to inspect recent changes for repeated helpers and growing lint suppressions. Report confirmed patterns without editing.` |
| Enforce architecture | `Use miso to prevent UI modules from importing storage internals. Add an executable check and prove it rejects a forbidden import.` |
| Run a bounded loop | `Use miso to implement this spec in at most five iterations and 20 minutes. Keep resumable state and stop only with verified completion or an explicit limit or blocker.` |
| Cancel a loop | `Cancel this loop and preserve its files and evidence.` |

For a new task or session, name `miso` again. Within a task, continue normally: “explain that tradeoff,” “fix the first finding,” or “stop after the spec.” A fresh session needs file paths or saved context to resume reliably.

## Know what the names mean

**MisoStack** is the package. **miso** is the skill that selects the workflow. Names such as `miso-debug` and `miso-review` are supporting skills. Direct invocation is optional; use the [catalog](../reference/catalog.md) when you want one specific procedure.

`miso-stack install` is a terminal command for setup. It does not start an engineering task. The package uses your agent's model and tools; it does not provide model access itself.

## If Miso does not load

Start a fresh session after installation or updates. Check that the Miso entry appears in the host's skill list. Use the exact entry shown if multiple installed sources share a name.

Then ask:

```text
Load the miso skill and tell me which SKILL.md you read.
Do not change the project.
```

Inspect the tool trace when available. If the skill is absent, run `miso-stack install` in your terminal and select that agent. See [troubleshooting](troubleshoot.md) for broken links, cached plugins, and reference permissions.

Try the [first verified change tutorial](../tutorials/first-verified-change.md) for a complete task in a disposable folder.
