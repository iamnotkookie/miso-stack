---
name: miso-design
description: "Designs interfaces from usage and tests architectural choices with prototypes. Use when creating a subsystem, changing ownership, or comparing substantial designs."
license: MIT
---

# Design

Apply the shared rules and current host map in [miso](../miso/SKILL.md). When called directly, run this procedure after reading those rules. When called from a playbook, continue that playbook without restarting routing.

1. Establish the current behavior, owners, constraints, and target outcome with [research](../miso-research/SKILL.md).
2. Write a caller's example or a short tutorial before internal implementation details. State inputs, outputs, failure behavior, and state ownership.
3. Sketch types and public signatures. Make invalid states difficult to represent. Keep volatile integrations at explicit boundaries.
4. For a consequential choice, use [arena](../miso-arena/SKILL.md) to compare two or three independent designs against the same requirements. A routine change with a known pattern needs no competition.
5. Build a small executable probe for the riskiest assumption. Record the baseline, result, and tradeoff. Do not accept a diagram as runtime proof.
6. Select the simplest design that meets the observations. Honor any user review checkpoint. Otherwise proceed with reversible implementation.
7. Implement in small verified units. If callers need repeated workarounds, hidden state, or unsafe casts, revisit the sketch. Preserve the user's work when discarding your failed attempt.

Deliver the usage example, chosen interface, evidence, rejected alternatives, and unresolved limits. Read [principles](../miso/references/principles.md) for boundary, domain, and type rules.
