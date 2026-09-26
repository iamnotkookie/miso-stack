# codex tool map

Use the skill loader when exposed; otherwise read the discovered SKILL.md path. Use the session's shell and patch tools. Codex runtimes can expose `spawn_agent` directly or through a collaboration namespace. Read the actual schema; do not copy Claude's `Agent` arguments. Use the matching wait, message, and close tools exposed by that runtime. If multi-agent support is unavailable or forbidden, stay serial. Omit model overrides by default.

The plugin uses `.codex-plugin/plugin.json` and default `hooks/hooks.json` discovery. Codex must trust plugin hooks through its own hook interface. Do not write trust settings to bypass that review. Explicit `miso` invocation works without hook trust. New sessions pick up installed skills; this active session does not reload itself automatically.

This map guides capability discovery. The tools in the current session are authoritative.
