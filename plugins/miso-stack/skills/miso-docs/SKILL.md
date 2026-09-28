---
name: miso-docs
description: "Writes and verifies technical documentation in Simplified Technical English. Use for tutorials, how-to guides, references, explanations, READMEs, or documentation reviews."
license: MIT
---

# Documentation

Apply the shared rules and current host map in [miso](../miso/SKILL.md). When called directly, run this procedure after reading those rules. When called from a playbook, continue that playbook without restarting routing.

1. Identify the reader, their task, and their starting knowledge from the request and repository. A spec or a decision record states why. A comment that restates the code does not. Update the doc in the same change as the behavior.
2. Choose one document purpose. A tutorial teaches through a working example. A how-to solves a known task. A reference lists exact contracts. An explanation develops the reasons and tradeoffs. Split mixed purposes into linked pages.
3. Read the actual implementation and execute relevant commands before describing behavior. Distinguish supported behavior from a proposal.
4. Write the outcome first. Give prerequisites before steps. Use real paths and runnable commands. Explain the expected result and recovery for likely failures. Keep credentials out of examples.
5. Apply [the writing rules](../miso/references/writing.md): ASD-STE100, Simplicity, Brevity, Clarity, Humanity. Keep code identifiers exact. Use one term consistently for each concept.
6. Validate links, examples, names, flags, and stated defaults. Run a tutorial from its stated starting state in a sandbox. A document linter cannot prove that a procedure works.
7. Report what was executed and what remains unverified. Do not claim certified STE compliance from a prose review or a heuristic checker.

Deliver the document and evidence for its examples. Keep the main README short and link to details.

## Edit existing prose

For “unslop”, “make this clearer”, or “less AI”, preserve meaning, evidence, uncertainty, identifiers, and the writer's intended tone. Replace vague claims and ornate words with specific facts and plain verbs. Remove filler, repeated summaries, forced lists, inflated praise, and unnecessary formatting. Restore full sentences when compression makes the reader decode the text. Do not invent a source or remove an uncertainty qualifier merely to sound confident.

Return the edited text unless the user asks for an explanation of the edits. Ordinary prose cleanup needs no repository investigation. A request to simplify the previous answer routes to the plain-restatement mode in [miso-research](../miso-research/SKILL.md).
