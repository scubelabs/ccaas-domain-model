# Event and Schema Compatibility Policy

## Versioning
Event type and major semantic version form a contract. Additive optional fields are preferred for compatible evolution. Removing fields, changing meaning, narrowing accepted values or changing units requires a new event/schema version.

## Consumer rules
Consumers must ignore unknown compatible fields unless their security model requires explicit allowlists. Consumers should not infer semantics from undocumented producer implementation details.

## Producer rules
A producer emits one documented version per event instance, preserves units/time semantics, does not reuse fields with new meanings and provides migration overlap when practical.

## Deprecation
Deprecation should identify replacement contract, producer migration date, consumer deadline and replay implications. Historical events retain their original schema identity.

## Testing
The repository validates current example envelopes and payloads plus selected known-invalid envelopes in CI. Compatibility across released versions, consumer idempotency and replay still require separate executable tests.
