# ADR-001 — Interaction as the Cross-Domain Correlation Backbone

**Status:** Accepted for the reference model

## Context

Voice platforms often expose SIP Call-ID, media UUID, recording ID, queue ID and agent-leg IDs. Digital systems expose conversation/message IDs. WFM, quality, surveys and analytics introduce still more identifiers.

Using any transport/provider identifier as the universal business key couples the enterprise model to one channel or implementation.

## Decision

Define an implementation-neutral `interaction_id` as the top-level correlation identity for a customer engagement. Preserve subordinate domain identifiers rather than replacing them.

```text
interaction_id
  ├─ conversation_id
  ├─ session_id
  ├─ call_leg_id / sip_call_id
  ├─ routing_attempt_id
  ├─ recording_id
  ├─ transcript_id
  ├─ evaluation_id
  └─ survey_invitation_id
```

## Consequences

Positive: omnichannel correlation, provider independence, clearer analytics lineage, easier cross-domain APIs/events and better troubleshooting.

Tradeoff: correlation services/contracts must propagate the ID reliably; imported/legacy artifacts may require reconciliation; one interaction can legitimately map to many technical identifiers.

## Non-decision

This ADR does not require one physical database, one giant Interaction object or synchronous coupling between domains. Bounded contexts retain ownership of their aggregates.
