---
name: miso-spec
description: "Turns the conversation and repository evidence into a scoped specification with acceptance checks. Use when the user asks for a spec, requirements, or a written definition of what to build."
license: MIT
---

# Specify the work

Apply the shared rules and current host map in [miso](../miso/SKILL.md). When called from a workflow, continue that workflow without restarting routing.

Synthesize what is already known. Read relevant domain terms, interfaces, decisions, and prior work. Do not restart an interview or reopen settled decisions.

1. Identify the user's problem, expected outcome, agreed constraints, and explicit exclusions. Keep assumptions separate from decisions. Ask only for a missing fact that changes the contract; otherwise record a bounded open question.
2. Identify where a user or caller can observe success. Prefer existing public interfaces as test boundaries. Describe any missing test boundary and its cost. Use a small prototype only when it can resolve a consequential uncertainty within scope.
3. Write a local specification in the project's existing location. If none exists, use `specs/<topic>.md`. Include problem, intended behavior, acceptance criteria, agreed design decisions, verification, out of scope, and open questions. Include only useful scenarios, including failure and recovery where relevant.
4. Make each acceptance criterion observable: starting condition, action, expected result. Link decisions to their source. Preserve exact interfaces or a short proven type sketch where prose would lose the contract. Do not present a proposed design as an accepted decision.
5. Check that the spec agrees with the conversation and current code. Return a concise overview and the local path. Spec creation does not authorize implementation.

An issue tracker is optional. If the user explicitly requests publication and the project supplies an approved connector, publish the concrete spec using established labels and report its identifier. Without that authority or connector, leave a complete local artifact and say it is not published. Do not install another skill, invent tracker labels, or modify a parent issue to finish this task.
