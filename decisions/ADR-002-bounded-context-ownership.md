# ADR-002 — Bounded Context Ownership over Shared Database Ownership

**Status:** Accepted for the reference model

## Context
CCaaS capabilities need shared identifiers and correlated views, but a single enterprise schema encourages direct cross-domain writes, hidden coupling and ambiguous authority.

## Decision
Each bounded context owns its aggregate semantics and mutation authority. Cross-context integration uses versioned APIs/events and stable identifiers. Composite UI/reporting views are projections.

## Consequences
Positive: clearer invariants, independent evolution, failure isolation and ownership. Tradeoffs: event/API contracts, eventual consistency and reconciliation become explicit engineering responsibilities.

This decision does not mandate microservices; multiple bounded contexts can be deployed together while preserving logical ownership.
