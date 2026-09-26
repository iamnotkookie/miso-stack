# Engineering principles

These concise rules interpret the pstack ideas for MisoStack. They are guidance for decisions, not 23 separate skills.

## laziness-protocol

**Choose the smallest complete change.** Remove unnecessary work and reuse a proven tool before inventing a layer.

## foundational-thinking

**Start with ownership and data.** Name the domain objects, state owners, and proof method before adding behavior.

## redesign-from-first-principles

**Reconsider the structure.** When a new requirement conflicts with the design, compare a simpler integrated shape with another workaround.

## attack-the-premise

**Question repeated failure.** When experiments fail for the same reason, test the shared assumption before another patch.

## subtract-before-you-add

**Remove dead weight.** Delete obsolete paths only within authorized scope, then build on the smaller design.

## minimize-reader-load

**Keep the path visible.** Reduce hidden state, needless indirection, and names that conceal ownership.

## outcome-oriented-execution

**Finish the intended migration.** Use temporary compatibility only with an explicit need and removal condition.

## experience-first

**Start with the user outcome.** Evaluate how the person calls, operates, and recovers the system before internal convenience.

## exhaust-the-design-space

**Compare consequential alternatives.** Use a few executable candidates when a choice has no reliable precedent.

## build-the-lever

**Build a reusable tool.** Turn repeated manual operations or proof steps into small inspectable commands.

## model-the-domain

**Represent the domain directly.** Use explicit states and types instead of flags whose combinations have unclear meanings.

## boundary-discipline

**Validate at boundaries.** Validate untrusted inputs and keep integration failures out of pure domain logic.

## type-system-discipline

**Make contracts checkable.** Use narrow types and validated construction. Do not suppress evidence of a bad model with casts.

## make-operations-idempotent

**Make retries safe.** Use stable identity and explicit state so a retry converges without repeating effects.

## migrate-callers-then-delete-legacy-apis

**Retire obsolete interfaces.** Move known callers, prove compatibility where required, then remove old code with authorization.

## separate-before-serializing-shared-state

**Separate writers.** Prefer separate state or one clear owner over competing writes and more locks.

## prove-it-works

**Prove the actual result.** Exercise the relevant artifact and user path. Do not replace runtime evidence with a claim.

## fix-root-causes

**Test the mechanism.** Reproduce the symptom and verify the cause before selecting a fix.

## sequence-verifiable-units

**Verify each unit.** Order changes so each unit has a useful, repeatable acceptance check.

## test-behavior-not-implementation

**Test the contract.** Check a known result through the caller-facing interface rather than restating source structure.

## guard-the-context-window

**Keep context relevant.** Search before reading broadly. Retain decisions and evidence pointers, not huge raw outputs.

## never-block-on-the-human

**Use granted autonomy.** Resolve observable facts with tools and continue reversible work. Keep explicit approval boundaries.

## encode-lessons-in-structure

**Prevent repeat failures.** Prefer a schema, test, lint, or better tool when it can enforce a recurring lesson.
