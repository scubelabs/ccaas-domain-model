# Idempotency, Ordering and Replay Contract

## Delivery assumption
The reference model assumes at-least-once delivery unless a concrete transport proves stronger. Duplicate delivery must not create duplicate business effects.

## Deduplication
Use `event_id` for event-processing deduplication. Use business idempotency keys for commands whose retries can repeat the same intent.

## Ordering
Global ordering is not assumed. Where aggregate ordering matters, `aggregate_version` provides a monotonic domain sequence. Consumers can reject stale versions, buffer gaps or reconcile from an authoritative read model according to their requirements.

## Replay
Replayed events retain original `event_id` and `occurred_at`; transport/replay metadata should not masquerade as business occurrence time.

## Poison events
Consumers need bounded retry, dead-letter/quarantine handling, diagnostics and replay after correction. Infinite immediate retries can turn one malformed event into an outage.
