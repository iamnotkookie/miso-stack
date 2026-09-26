# opencode tool map

Use the `skill` tool with the discovered `miso` name. Read files with `read` and use the exposed `bash` and editing tools. Delegate through `task` only when present and permitted. Use an agent type that the running instance actually lists. Do not supply Claude or Grok parameters. Follow the host's configured agent model; do not add fixed IDs.

The shared links live in `~/.agents/skills/`. `opencode debug skill` lists discovered skills. Invoke `miso` by name. MisoStack does not install an OpenCode startup extension. Independent workers and parallel execution must be observed in this installation before reporting them as verified.

The host may require `external_directory` permission to read a linked skill's reference files. Use its native permission flow or an explicitly authorized project-local rule limited to MisoStack paths. Do not grant broad filesystem access or change global policy merely to suppress a prompt. In headless tests, prepare this narrow fixture permission before running the model.

This map guides capability discovery. The tools in the current session are authoritative.
