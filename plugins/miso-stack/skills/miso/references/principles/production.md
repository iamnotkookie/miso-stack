# Production

**Apply when:** A change touches writes, fan-out, stores, or spend.

**Rule:** Bound the work and make the effect single.

**Why:** Unbounded work and repeated effects fail in production, not in a test.

- A retried write, payment, or export does not double the effect.
- Fan-out, exports, queries, and token use have a budget. Unbounded work is a defect.
- The dependency graph is data: lockfile, manifest, or call graph. Blast radius comes from that graph.
- A pipeline has stages with contracts. Retrieve, rank, and present do not share one function.
- One store owns a fact. Caches say they are derived.
- Defense in depth: validation, authorization, and limits stack.
- Cost is a design input. Name queries, egress, retained data, and model spend.
