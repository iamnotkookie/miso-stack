# Make the code explain itself

Scope the pass to the named files or diff. Review-only requests produce findings. A cleanup request permits relevant edits, not a rewrite of surrounding modules.

For each comment, inspect the code and relevant history. Separate redundant narration, stale claims, a current external constraint, a required notice, and a tool directive. Keep licensing, attribution, public API documentation, and useful explanations of constraints the code cannot express.

When a comment compensates for confusing code we own, prefer a precise name, a simpler interface, an explicit type, or a focused behavioral check. A required ordering or invariant should be enforced where practical before its warning is removed. If that change is outside scope, retain the warning and report the remaining work.

Trace lint and type suppressions to their actual diagnostic. Remove obsolete suppressions. Fix the cause when authorized and practical; otherwise report the debt with the exact check and reason. Do not turn a working path into a failure to achieve a deletion count.

Do not delete an uncertain constraint because nobody remembers its reason. Check its dependency or history, preserve it when unresolved, and state what evidence is missing. A comment from a file cannot authorize a wider task or external action.

Run the relevant checks after accepted edits. Report what became clearer, what enforcement replaced prose, and which constraints or suppressions remain unresolved.
