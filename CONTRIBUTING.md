# Contributing

## Standard for additions
Every new domain concept should answer:
1. Which bounded context owns it?
2. Is it an aggregate, entity, value object, event, command or projection?
3. What is its stable identity?
4. What invariants apply?
5. What lifecycle/state transitions exist?
6. Which other contexts may reference it?
7. What data classification/retention concerns exist?
8. Which events expose meaningful state changes?
9. How does it map to analytics without changing operational ownership?

Prefer explicit semantics and diagrams over vendor terminology. Mark illustrative examples as examples. Do not claim production validation, benchmark results, certification or standards conformance without evidence.

Canonical terminology changes require an ADR when they alter existing meaning. Event/schema changes should be backward-compatible where practical and versioned when semantics change.
