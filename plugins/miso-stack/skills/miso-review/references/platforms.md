# Review a pull request or merge request

Use whichever access the session has: the host's GitHub or GitLab connector, the `gh` or `glab` CLI, or the public API for a public project. A self-hosted GitLab works the same way, so take the host from the URL. Report any access you do not have, and do not guess at what it would show.

## Read

Accept a pull request URL, a merge request URL, a branch, or a diff path. Record the tip SHA first. Then fetch the full diff, the base branch, the pipeline or check status with links, approvals, mergeability, and the existing discussions. Read the discussions after your first findings.

## Draft notes that can be posted

Give each inline note a file, a side, a line, and a body. Use the new line for added or unchanged code, and the old line for removed code. A renamed file needs both its old and new path. Notes can usually not be edited or deleted with the available tools, so check each one before you post.

## Publish, only when authorized

- Batch the inline notes into one review with one summary. On GitHub, create a pending review and submit it as a comment. On GitLab, add the draft notes and submit them together with the summary.
- Do not submit an approve or request-changes event unless publishing that verdict is authorized for this change or by a standing instruction. Pass the head SHA with it when the host accepts one.
- Post at most once per tip SHA. First look in the existing discussions for a summary that names this tip SHA. When one exists, post nothing and say so. Review again when the SHA changes.
- Do not post on a merged or closed change. Return the review in the reply.
- When the host rejects an anchor, report that the note did not post. Do not turn it into a general note.
- Send bodies with real line breaks. A typed backslash and `n` appears literally in the posted note.
- Do not assign reviewers, merge, or message the author.
