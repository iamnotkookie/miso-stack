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

Identify the important data, who owns it, lifecycle and teardown, and where each responsibility belongs. For a subsystem, build a compact map and trace one complete journey. For a small function, answer directly. Use independent exploration only when the scope benefits and the session permits it.

## Intent

Inspect relevant history, ADRs, issues, and reviews. Use connected project sources when available. Search the named subject, not every workspace or private conversation. Separate recorded rationale from an inference made today. A comment is a lead, not proof that a constraint still exists. Report unavailable sources and unresolved contradictions.

## Recall

Use project handoffs and the explicitly available transcript or memory source. Search by topic before reading a bounded excerpt. Keep identifiers and source links with each decision. Verify drift-prone facts against current files or state. Do not write personal memory without a direct user request.

State the workspace, topic, and time window. Use a supplied handoff instead of mining history again. For a named feature, include available shared records such as linked issues, reverted fixes, and reports; disclose unavailable sources. Return the goal, decisions, actual current status, unresolved problems, and next useful action. Distinguish planned, in progress, verified but uncommitted, published, and reverted work.

## Teach

Start with a plain definition and one concrete path through the system. Explain the tradeoff at the point it matters. Use a small diagram when it reduces reading effort. Match the reader's question and existing knowledge. A request for a plain restatement needs a short answer, not a new investigation.

For a subsystem explanation, combine mechanics with recorded reasons from the intent mode. Preserve uncertainty about historical intent. Teach the user's journey before listing symbols. Introduce complex diagrams in useful stages. Do not quiz the user or edit the system as part of teaching. For “say that plainly” or “bro”, rewrite the preceding answer in everyday language and stop; do not start research.

## Output

Return the answer, supporting evidence, uncertainty, and the next discriminating experiment when needed. Contradictory evidence stays visible. Follow [writing](../miso/references/writing.md).
