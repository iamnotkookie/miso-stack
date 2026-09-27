---
name: miso-tickets
description: "Splits an agreed spec or plan into small verifiable tickets with explicit blockers. Use for breaking work into issues or preparing a backlog, with local files or an authorized tracker."
license: MIT
---

# Split the work

Apply the shared rules and current host map in [miso](../miso/SKILL.md). When called from a workflow, continue that workflow without restarting routing.

Read the supplied specification, issue comments when accessible, and relevant project decisions. Reuse an existing approved breakdown. If intent is unresolved, use [miso-spec](../miso-spec/SKILL.md) first without inventing requirements.

1. Prefer a narrow working path through the necessary layers for each ticket. Each ticket should demonstrate an outcome independently and fit a fresh agent context. Add preparatory refactoring only when it removes a concrete blocker.
2. Give every ticket a stable local ID, title, expected behavior, scope exclusions, source requirements, acceptance checks, and explicit blocking IDs. Include enough context to start without this conversation. State test boundaries and relevant constraints, not a line-by-line implementation recipe.
3. Check that blockers exist, the graph has no cycles, and each edge represents a real prerequisite. Independent tickets stay independent. Check that the union covers the spec without adding work the user did not request.
4. For a broad migration that cannot keep each vertical slice working, describe the exception. Use an added compatible form, caller migration batches, and removal only after all callers move. If green intermediate commits are impossible, name the shared integration branch and final verification ticket. Do not silently promise independent delivery.
5. Write one file per ticket in the project's established directory, or `tasks/<topic>/` when none exists. Show the titles, outcomes, and blockers together for review. Honor an explicitly requested approval checkpoint; do not request redundant approval for already authorized local drafting.
6. Publish only when requested and through an approved project connector. Create blockers first, retain the mapping from local IDs to real issue IDs, and use native dependency links where supported. Report partial publication and reuse created issues on retry. Do not close or relabel a parent issue unless requested.

If tracker access is unavailable, the local tickets remain usable and are explicitly unpublished. Use [miso-plan](../miso-plan/SKILL.md) to execute the ready tickets only when implementation is requested.
