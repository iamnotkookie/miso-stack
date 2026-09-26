# Troubleshoot MisoStack

## The skill is absent

Run the package check. Then inspect the host's discovered skills. A plugin install can be valid while a running session still has an old catalog. Start a fresh session.

For shared links, run `links` in dry-run mode and inspect the reported targets. A moved source tree leaves broken links. Repair only links that belong to MisoStack.

## A name collides

The link helper stops instead of replacing an existing skill. Inspect both definitions. Keep the existing skill until you choose how to resolve the name. The `miso-` prefix avoids common names such as `teach` and `tdd`.

## Codex does not run the hook

Plugin hooks need native trust review. Inspect `/hooks` in a new Codex session. Explicitly invoking `miso` does not require the reminder. Do not edit trust storage to force execution.

## Grok does not inject startup context

The documented Grok Build SessionStart event ignores stdout. Use `miso` by name. A successful hook process is not proof that its output entered context.

## A worker tool is missing

Use the serial fallback. Report it. Do not invent a tool name, model, subagent type, or cloud host. Check the actual session tools before editing a host map.

## OpenCode loads the skill but cannot read its references

Check for an `external_directory` rejection. The skill loader can read SKILL.md while the general file reader still needs permission for adjacent references. Grant project-scoped read access to the MisoStack paths through the native permission flow. Headless evaluation fixtures include this narrow allowance.

If `opencode debug skill` produces incomplete JSON when captured through a pipe, redirect stdout directly to a file and parse that file. This was observed with the installed OpenCode build; it is not a MisoStack parsing failure.

## A headless Grok command is cancelled

Inspect the permission result. Compound shell syntax can need an interactive decision even when its first command is allowed. Use simple commands or a local capture driver. The evaluation runner uses Grok's native `auto` review with the workspace sandbox and bounded command allowances. It does not disable safety checks. A cancelled command is not evidence that the user cancelled the task.

## A task cannot finish

Run `plan check`. Confirm the task is running under your owner ID, dependencies are done, and the proof file is nonempty. Keep proof beneath the plan directory. A changed evidence hash invalidates accepted proof. Re-run the relevant verification and update the plan deliberately.

## A command receipt fails

Read its status, exit code, and stderr. A timeout is a failed observation. Increase the limit only when the command is expected to take longer, and keep it bounded. Use a new receipt path so earlier evidence remains available.

## A model call cannot start

Check the host's normal login and provider setup. MisoStack does not select a substitute model or change credentials. Mark the runtime check unverified and retain the exact non-secret error.
