---
name: miso-merge
description: "Resolves an existing Git merge or rebase conflict by preserving the intent of both changes. Use for conflicted files or a stopped merge/rebase, not to start a new merge or publish code."
license: MIT
---

# Resolve a conflict

Apply the shared rules and current host map in [miso](../miso/SKILL.md). When called from a workflow, continue that workflow without restarting routing.

1. Inspect status, the current operation, unmerged index entries, and relevant history. Record unrelated staged and unstaged work. A request to resolve conflicts does not authorize starting a new merge, resetting work, or fetching from a remote.
2. For each conflict, read the common base and both sides, their callers, tests, commit messages, and available issue context. During a rebase, establish what each index stage represents; do not infer intent from the labels ours and theirs.
3. State the two intended behaviors. Resolve the affected files so both hold where compatible. Follow the user's stated migration goal when the intents conflict. Ask only if incompatible product decisions cannot be resolved from evidence. Do not invent a third behavior to make the markers disappear.
4. Preserve unrelated edits and comments that express live constraints. Regenerate generated files with their owner tool when practical. Never resolve every file with a blanket side selection. Do not stage all files.
5. Check unmerged index entries and accidental conflict markers, then run the existing relevant build, type, formatting, and behavior checks. A marker-free file can still be wrong. Compare the resolved behavior against both intended changes.
6. Stage only the resolved paths when the requested operation permits it. Continue and commit an in-progress merge or rebase only within the user's authority and project rules. Otherwise leave the verified resolution ready and identify the next command. Repeat for later rebase stops when continuation is authorized.

Do not abort, reset, force-push, or drop a commit without explicit authority. If resolution is blocked, retain the operation and report the specific decision or failed check. Completion means the requested Git operation and its resulting code are verified, or the exact unfinished step is stated.
