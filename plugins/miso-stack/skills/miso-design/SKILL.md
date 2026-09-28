---
name: miso-design
description: "Designs interfaces from usage and tests architectural choices with prototypes. Use when creating a subsystem, changing ownership, or comparing substantial designs."
license: MIT
---

# Design

Apply the shared rules and current host map in [miso](../miso/SKILL.md). When called directly, run this procedure after reading those rules. When called from a playbook, continue that playbook without restarting routing.

1. Establish the current behavior, owners, constraints, and target outcome with [research](../miso-research/SKILL.md).
2. Write a caller's example or a short tutorial before internal implementation details. State inputs, outputs, failure behavior, and state ownership.
3. Read [module design](references/modules.md). Sketch types and public signatures, plus error, ordering, ownership, and configuration contracts. Make invalid states difficult to represent. Keep volatile integrations at explicit boundaries.
4. For a consequential choice, compare two or three caller-facing designs against the same requirements. Use the same scenarios and rubric. A routine change with a known pattern needs no competition or extra workers.
5. Build a small executable probe for the riskiest assumption. Record the baseline, result, and tradeoff. Do not accept a diagram as runtime proof.
6. Select the simplest design that meets the observations. A design-only request ends with the interface, evidence, and tradeoffs. Honor any user review checkpoint. Proceed to implementation only when implementation is part of the authorized task.
7. When implementing, use small verified units. If callers need repeated workarounds, hidden state, or unsafe casts, revisit the sketch. Preserve the user's work when discarding your failed attempt.

Deliver the usage example, chosen interface, evidence, rejected alternatives, and unresolved limits. Read [principles](../miso/references/principles.md), including structure, production, and with-agents. Separate concerns, keep coupling loose, and hide detail behind the contract.

Make structural rules executable. Establish module ownership, allowed dependency directions, validated inputs, and state transitions. Put constraints in types, compiler settings, schemas, or focused checks when the task authorizes implementation. Prove a forbidden use fails and a supported use works. Use [miso-garden](../miso-garden/SKILL.md) for recurring drift across changes. Do not replace a working language or framework merely to improve its theoretical guarantees.
