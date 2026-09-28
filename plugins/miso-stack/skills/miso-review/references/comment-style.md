# Comment style

Notes are about the code. The author is not the subject.

Do not write "you" or "your". Ask, or drop the subject: "Can we rename this to `seconds_remaining`?" An order turns a reply into an argument.

A required note has three parts: the defect as a fact about the code, the reason (a principle, a style-guide rule, or an observed behavior), and a request. Add a short example only when the fix is unambiguous. Three examples is the maximum for one round.

Use [Conventional Comments](https://conventionalcomments.org/):

- `issue:` blocks. Incorrect behavior, a design defect, a missing test for new behavior, a drop in code health, or a production break.
- `suggestion:` does not block.
- `nit:` trivial. On a nearby untouched line, add `safe to ignore`.
- `praise:` name what was good and why. Skip it when nothing was good.
- `question:` does not block. An unresolved production risk is an `issue:`.

A pattern that shows up more than three times gets three examples and one request to fix the pattern.

`issue:` notes stay on lines the diff changes, unless the diff made an untouched line false.

## Summary on the change

Post one short summary before the chat reply when the user pointed at a pull request or merge request:

- Tip SHA and one-line intent.
- Verdict: `approve`, `request changes`, or `hold merge`. State that the review does not merge.
- Gates, each with a link and a status on that tip SHA. Unknown stays unknown.
- Blocking findings, or `none`.
- Nits only when any exist.
- One praise line when one was earned.
- Pointers to existing threads that already cover a shared finding.

Reply in an existing thread when the note agrees or disagrees with that thread. Open a new thread only for a new finding.
