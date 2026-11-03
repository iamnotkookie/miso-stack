# Engineering principles

Each row names the moment a principle applies. When a row fits, read its leaf in full, then apply it. Cite a principle only when you read its leaf and it changed a choice.

## Before you write

| When | Principle |
| --- | --- |
| You are about to write the first logic of a subsystem or stateful feature. | [foundational-thinking](principles/foundational-thinking.md) |
| You write stateful logic, heavy branching, or a shape assumption that repeats across files. | [model-the-domain](principles/model-the-domain.md) |
| You make a product, interface, or scope tradeoff. | [experience-first](principles/experience-first.md) |
| A new requirement conflicts with the current design. | [redesign-from-first-principles](principles/redesign-from-first-principles.md) |
| A consequential choice has no reliable precedent. | [exhaust-the-design-space](principles/exhaust-the-design-space.md) |

## While you shape the change

| When | Principle |
| --- | --- |
| You size a diff, refactor, or want to add a layer, option, or helper. | [laziness-protocol](principles/laziness-protocol.md) |
| You order an addition, a refactor, or a rewrite. | [subtract-before-you-add](principles/subtract-before-you-add.md) |
| You write or review code that a reader cannot follow without a tour. | [minimize-reader-load](principles/minimize-reader-load.md) |
| You plan a rewrite or migration with phases. | [outcome-oriented-execution](principles/outcome-oriented-execution.md) |
| You would repeat an edit or a proof step by hand. | [build-the-lever](principles/build-the-lever.md) |
| A change makes the next change less local. | [structure](principles/structure.md) |

## At boundaries and shared state

| When | Principle |
| --- | --- |
| You add validation, error handling, or a framework adapter. | [boundary-discipline](principles/boundary-discipline.md) |
| You design a type or a signature in a typed language. | [type-system-discipline](principles/type-system-discipline.md) |
| A command, lifecycle step, or loop can run again after a crash or retry. | [make-operations-idempotent](principles/make-operations-idempotent.md) |
| A new internal API replaces an old one that still has callers. | [migrate-callers-then-delete-legacy-apis](principles/migrate-callers-then-delete-legacy-apis.md) |
| Two workers or processes could change one file, branch, key, or object at the same time. | [separate-before-serializing-shared-state](principles/separate-before-serializing-shared-state.md) |
| A change touches writes, fan-out, stores, or spend. | [production](principles/production.md) |
| You judge a trust boundary, a finding, or a skill or plugin before install. | [security](principles/security.md) |

## When you debug and verify

| When | Principle |
| --- | --- |
| You debug a symptom or feel tempted to add a guard. | [fix-root-causes](principles/fix-root-causes.md) |
| A second fix fails, two experiments fail the same way, or evidence conflicts with the request. | [attack-the-premise](principles/attack-the-premise.md) |
| You are about to say that a task is done. | [prove-it-works](principles/prove-it-works.md) |
| A test is being added, edited, or kept after a change. | [test-behavior-not-implementation](principles/test-behavior-not-implementation.md) |
| You do multi-step work, such as a sweep or a migration, or you order commits and pull requests. | [sequence-verifiable-units](principles/sequence-verifiable-units.md) |
| You take a measurement, or a measured result will shape a decision or a report. This includes evaluation scores. | [explain-the-number](principles/explain-the-number.md) |

## How you work

| When | Principle |
| --- | --- |
| You want to ask a question about reversible work. | [never-block-on-the-human](principles/never-block-on-the-human.md) |
| A task produces big tool results, you keep rereading files, or planning spans much of the repository. | [guard-the-context-window](principles/guard-the-context-window.md) |
| You give the same correction a second time, or a rule depends on someone remembering it. | [encode-lessons-in-structure](principles/encode-lessons-in-structure.md) |
| An agent writes, reviews, or configures the change. | [with-agents](principles/with-agents.md) |
| You hear, or start to write, one of the excuses below. | [refuse-these](principles/refuse-these.md) |
