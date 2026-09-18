# Canonical API Resource Model

The domain model is not identical to an API, but stable resources can expose domain capabilities without leaking database tables.

## Candidate resources
```text
/tenants/{tenantId}
/customers/{customerId}
/interactions/{interactionId}
/interactions/{interactionId}/conversations
/interactions/{interactionId}/recordings
/interactions/{interactionId}/transcripts
/interactions/{interactionId}/evaluations
/queues/{queueId}
/agents/{agentId}
/routing-attempts/{attemptId}
/surveys/{surveyId}
/campaigns/{campaignId}
/wfm/schedules/{scheduleId}
```

## API principles
Use opaque stable IDs; explicit versioning/compatibility; pagination for collections; idempotency keys for retryable creates/commands; optimistic concurrency/version tokens for conflicting updates; typed error contracts; tenant-aware authorization; correlation IDs; no secrets in URLs; and sparse/controlled expansion rather than enormous object graphs.

## Commands
State transitions with business semantics can be action resources/commands rather than generic PATCH fields, for example reserve agent, change routing state, pause recording, publish schedule or complete evaluation.

## Read models
A supervisor interaction view may compose data from multiple bounded contexts. Treat it as a projection/read model, not evidence that one service owns all underlying data.
