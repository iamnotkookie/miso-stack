# Grade the evidence

A risky-looking change is usually safe because of one thing. Name that thing, and climb these grades while the next one stays cheap. Report the grade you reached.

| Grade | What you have |
| --- | --- |
| Claimed | Someone said so. This alone proves nothing. |
| Located | You opened the `file:line`, or the dependency source at its pinned version. |
| Reasoned | You followed the failing path step by step and showed where it stops. |
| Ran | A short probe exercises the real code and would fail if the claim were false. |
| Observed | You saw the behavior in the running application. |

- Run probes in a scratch copy, never in the reviewed tree.
- A problem that needs some future change before it matters is not a finding.
- Say what an empty search covered. Do not invent a caller, an API, or a line number.
- Report confirmed risks, cleared risks, and unproven facts separately.
- When the main fact stays open, mark it `unproven` and name the check that would settle it.
- On a wide change, give a second reviewer the diff and the same question, without your answer. Keep a finding after you reproduce it.
