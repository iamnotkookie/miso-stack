# Type system discipline

**Apply when:** You design a type or a signature in a typed language.

**Rule:** Make contracts checkable and invalid states unrepresentable.

**Why:** A compiler checks a type on every change. A comment is checked by nobody.

- Use narrow types and validated construction.
- Do not suppress evidence of a bad model with a cast. Fix the model.
