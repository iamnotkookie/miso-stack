# Verify visual equivalence

Use for: Compare two UI implementations under matched conditions.

## Procedure

1. Define the surfaces, interactions, viewports, themes, data, and states to preserve.
2. Capture baseline screenshots and behavior under controlled fonts, scale, timing, and animation state.
3. Run the same state matrix against the candidate.
4. Compare screenshots and interactions. Separate rendering noise from a real difference.
5. Fix mismatches and repeat affected states. Do not update the baseline to hide a regression.
6. Report covered states, measured differences, accessibility checks, and anything unverified.

## Supporting skills

[miso-verify](../../miso-verify/SKILL.md), [miso-review](../../miso-review/SKILL.md)

## Completion evidence

The agreed state matrix matches the baseline within declared tolerances.
