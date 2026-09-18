# Knowledge and Integration Domains

## Knowledge
Core concepts include KnowledgeBase, Article, ArticleVersion, Category, Tag, Audience, ApprovalState and Recommendation.

Agent-assist recommendations reference the exact article/version shown so outcomes can be audited and relevance measured.

## Integrations
```text
Connector
 ├─ AuthenticationConfiguration
 ├─ Capability
 ├─ Mapping
 ├─ RateLimitPolicy
 └─ Health

ExternalReference
 ├─ system
 ├─ entity_type
 └─ external_id
```

CRM/customer records should be referenced through typed external identities rather than copied wholesale into every interaction.

## Webhooks
WebhookSubscription owns event filters, destination, secret reference, delivery policy and state. WebhookDelivery has a stable delivery ID, attempt count and outcome. Consumers should receive versioned event contracts and be able to deduplicate retries.

Secrets are references to secret-management systems, not values stored in domain events or ordinary configuration documents.
