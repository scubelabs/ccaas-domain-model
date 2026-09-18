# Commands, Invariants and Event Semantics

## Commands vs events
Commands request intent: `QueueInteraction`, `ReserveAgent`, `StartRecording`, `CompleteEvaluation`. Events state facts: `interaction.queued`, `routing.agent.reserved`, `recording.started`.

A rejected command does not emit a success event.

## Command envelope
Recommended metadata includes command_id, command_type/version, tenant_id, aggregate_id, correlation_id, causation context, requested_at, actor/service principal and idempotency_key where required.

## Aggregate invariants
Examples:
- a terminal Interaction cannot be queued again without an explicitly modeled reopen/new interaction;
- a routing reservation cannot be assigned simultaneously to two interactions;
- a completed Evaluation preserves its form version;
- a RecordingSegment end cannot precede its start;
- a SurveyResponse references the version of the survey presented;
- a usage source event is not metered twice.

## Concurrency
Use an explicit strategy: aggregate version/optimistic concurrency, atomic compare-and-set, transactional uniqueness, leases or another mechanism appropriate to the store. Do not rely on read-then-write availability checks for exclusive resources.

## Delivery semantics
Assume duplicates and delayed/out-of-order delivery unless the actual infrastructure contract proves stronger. Event consumers should use event identity and domain versions where needed to reject stale projections.
