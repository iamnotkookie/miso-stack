---
name: miso-research
description: "Traces behavior, decision history, and relevant prior work. Use when investigating how or why something works, recalling project context, or explaining a system."
license: MIT
---

# Research

Apply the shared rules and current host map in [miso](../miso/SKILL.md). When called directly, run this procedure after reading those rules. When called from a playbook, continue that playbook without restarting routing.

Start with the question and the decision the answer must support. Choose the relevant modes below. Keep read-only requests read-only.

## Mechanics

Follow one real input from the public entry point through state changes to its observable output. Read callers and error paths. Cite file locations. Run the smallest safe probe when the answer depends on runtime behavior. Distinguish the intended contract from observed behavior.

## Intent

Inspect relevant history, ADRs, issues, and reviews. Use connected project sources when available. Search the named subject, not every workspace or private conversation. Separate recorded rationale from an inference made today. A comment is a lead, not proof that a constraint still exists. Report unavailable sources and unresolved contradictions.

## Recall

Use project handoffs and the explicitly available transcript or memory source. Search by topic before reading a bounded excerpt. Keep identifiers and source links with each decision. Verify drift-prone facts against current files or state. Do not write personal memory without a direct user request.

## Teach

Start with a plain definition and one concrete path through the system. Explain the tradeoff at the point it matters. Use a small diagram when it reduces reading effort. Match the reader's question and existing knowledge. A request for a plain restatement needs a short answer, not a new investigation.

## Output

Return the answer, supporting evidence, uncertainty, and the next discriminating experiment when needed. Contradictory evidence stays visible. Follow [writing](../miso/references/writing.md).
