# Build a feature

Use for: Add or change user-visible behavior.

You own the design. Name the data shape before you write logic, and build the smallest path that a person can actually use.

## Procedure

1. State the user outcome, the inputs, the visible result, and the acceptance checks in your own words.
2. Read the current owners, conventions, and adjacent behavior. Resolve product ambiguity from the request. Ask only for a preference that no experiment can settle.
3. Name the data shape, its owner, and its organizing structure ([model-the-domain](../references/principles/model-the-domain.md)). Write the caller's example. When the change crosses a function boundary or adds an interface, use [miso-design](../../miso-design/SKILL.md) first.
4. Build a small complete path, including failure handling and boundary validation. Verify each unit before the next ([sequence-verifiable-units](../references/principles/sequence-verifiable-units.md)). Remove dead weight first when it is in scope.
5. Exercise the feature through its real surface, including one failure path. Check adjacent behavior and relevant security boundaries. A requested repository or skill audit uses [miso-audit](../../miso-audit/SKILL.md).
6. Update the feature map and documentation when behavior changes. Review the change in a fresh context when the host permits it.

## Supporting skills

[miso-research](../../miso-research/SKILL.md), [miso-design](../../miso-design/SKILL.md), [miso-verify](../../miso-verify/SKILL.md), [miso-review](../../miso-review/SKILL.md)

## Completion evidence

The acceptance journey runs on the real artifact, including a relevant failure path.

## Reply

Describe the result, the choices you made with their reasons, the proof you observed, and any decision still open. Use a table when you compare alternatives.
