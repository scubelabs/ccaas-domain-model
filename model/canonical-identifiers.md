# Canonical Identifiers and Correlation

## Identity hierarchy

```text
tenant_id
  └─ customer_id
      └─ interaction_id
          ├─ conversation_id
          │   └─ session_id
          │       └─ segment_id / call_leg_id
          ├─ routing_attempt_id
          │   └─ reservation_id
          ├─ recording_id
          │   └─ recording_segment_id
          ├─ transcript_id
          ├─ evaluation_id
          └─ survey_invitation_id
```

These identifiers describe different entities and should not be aliases.

## External correlation

An interaction may also carry external references:

| Identifier | Source |
|---|---|
| carrier_call_id | carrier |
| sip_call_id | SIP dialog/leg |
| media_uuid | media platform |
| crm_activity_id | CRM |
| campaign_attempt_id | outbound |
| trace_id | observability |
| recording_provider_id | recording system |

Store external IDs as typed references with source/system metadata rather than adding an unbounded number of provider-specific columns to the Interaction aggregate.

## Correlation envelope

Events should carry a common envelope containing at least:

```json
{
  "event_id": "evt_...",
  "event_type": "interaction.queued",
  "event_version": 1,
  "occurred_at": "2026-09-18T00:00:00Z",
  "tenant_id": "tnt_...",
  "interaction_id": "int_...",
  "correlation_id": "cor_...",
  "causation_id": "evt_previous",
  "producer": "routing-service"
}
```

`event_id` supports deduplication. `correlation_id` groups a distributed workflow. `causation_id` describes which prior command/event caused this fact when known.

## Identifier properties

Canonical IDs should be globally unique within their defined scope, immutable, opaque to consumers, non-PII, safe for logs, and independent of database location.

Avoid encoding mutable business meaning such as queue, region, agent name or phone number into identifiers.
