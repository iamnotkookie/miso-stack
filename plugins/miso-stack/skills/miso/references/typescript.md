# TypeScript review

Model variants with discriminated unions where behavior differs. Parse external values from `unknown` with the repository's schema library. Keep optional fields for actual optionality. Use existing derived types when they express the contract.

Check `any`, assertions, non-null assertions, ignored errors, and lint suppressions against their runtime assumptions. Prefer narrowing and exhaustive handling. A cast is not validation. Keep a justified boundary assertion only when a checked invariant supports it.

Check lifecycle cleanup, rejected promises, cancellation, and state updates after teardown. Preserve public API and wire-format compatibility where required. Test through real caller-facing operations, including a failure case. Use structured diagnostics without secrets.
