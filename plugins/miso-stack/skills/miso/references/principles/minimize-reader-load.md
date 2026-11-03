# Minimize reader load

**Apply when:** You write or review code that a reader cannot follow without a tour.

**Rule:** Keep the path visible.

**Why:** A reader can hold only a few layers and hidden states at one time. Every extra one causes a defect later.

- Count the layers between the caller and the effect. Collapse a wrapper that has one caller.
- Reduce hidden state and shrink the scope of mutation.
- Rename anything whose name conceals its owner.
