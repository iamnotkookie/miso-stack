# grok-build tool map

Use the skill name or its discovered file. Grok Build exposes `spawn_subagent` with a prompt and description. The documented schema has no `subagent_type` or model field. Put role and scope in the prompt. Leave model selection to the host or configured project roles. Background results use `get_command_or_subagent_output`; call it only if exposed. `send_subagent_message` is optional. A child must not assume it can create grandchildren.

Use the shared links in `~/.agents/skills/`. `grok inspect --json` checks discovery. Grok's documented SessionStart event ignores stdout, so the shared-link installation does not depend on a startup injection. Invoke `miso` by name. Grok Build is not Grok Bot. Do not invent Cursor cloud agents, bot webhooks, or a bot UI.

This map guides capability discovery. The tools in the current session are authoritative.
