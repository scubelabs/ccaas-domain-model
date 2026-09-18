# Observability and Correlation Model

## Correlation chain
```text
interaction_id
 ├─ trace_id
 ├─ carrier_call_id
 ├─ sip_call_id(s)
 ├─ media_session_id(s)
 ├─ routing_attempt_id(s)
 ├─ reservation_id(s)
 ├─ agent_session_id(s)
 ├─ recording_id(s)
 └─ external_reference(s)
```

Metrics answer aggregate behavior; logs provide diagnostic records; traces connect distributed operations. Voice additionally needs protocol/media evidence such as SIP ladders, RTP statistics and synthetic call outcomes.

Events/logs should include tenant-safe correlation identifiers without unnecessarily copying PII. Sensitive values should be masked/tokenized according to policy.

Define customer-capability SLIs separately: inbound admission, routing success/latency, agent event delivery, media establishment, established-media continuity, recording availability, transcription completion and reporting freshness. One aggregate platform uptime percentage hides failure modes.
