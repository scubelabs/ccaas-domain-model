# ADR-003 — Separate Operational and Analytical Models

**Status:** Accepted for the reference model

## Decision
Operational models optimize for real-time correctness and state transitions. Analytical models optimize for historical facts, dimensions, aggregation and reproducible metrics. They are connected through events/ETL/ELT contracts rather than sharing one schema as authoritative for both purposes.

## Rationale
Routing needs current agent capacity with strict concurrency behavior; reporting needs historical agent-state intervals and late corrections. These are related but different models.

## Consequences
Metric lineage and reconciliation are required. Analytical latency is explicit. Operational outages need not be caused by reporting workloads, and reporting can preserve historical truth as operational state changes.
