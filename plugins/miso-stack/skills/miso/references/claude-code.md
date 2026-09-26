# claude-code tool map

Load skills with `Skill` when exposed, using the name shown by discovery. Plugin names may qualify the entry as `miso-stack:miso`. Use `Read`, `Bash`, and the available edit tools for local work. Delegate with `Agent` only when present. Use an available agent type, not `poteto-agent` or another plugin's private type. Omit the model field to use the configured default. Inspect actual wait and background-task tools before using them.

The plugin uses `.claude-plugin/plugin.json`. Its SessionStart hook is a small reminder to read `miso` for engineering work. It does not run edits or grant permissions. Follow the host's normal plugin trust and permission prompts.

This map guides capability discovery. The tools in the current session are authoritative.
