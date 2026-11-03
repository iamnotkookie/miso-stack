# Grade the evidence

A risky-looking change is usually safe because of one thing. Name that thing, and climb these grades while the next one stays cheap. Report the grade you reached.

| Grade | What you have |
| --- | --- |
| Claimed | Someone said so. This alone proves nothing. |
| Read | You opened the source, including a dependency at its pinned version, and followed the path. |
| Ran | You executed the real code or application and saw the result. |

- Run probes in a scratch copy, never in the reviewed tree.
- A problem that needs some future change before it matters is not a finding.
- Say what an empty search covered. Do not invent a caller, an API, or a line number.
- Report confirmed risks, cleared risks, and unproven facts separately.
- When the main fact stays open, mark it `unproven` and name the check that would settle it.
- On a wide change, give a second reviewer the diff and the same question, without your answer. Keep a finding after you reproduce it.
