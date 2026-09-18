# Event Data Classification

Domain events should contain the minimum data required by consumers.

Suggested reference labels:
- PUBLIC
- INTERNAL
- CONFIDENTIAL
- PII
- HIGHLY_SENSITIVE
- REGULATED

These labels are illustrative and must be mapped to organizational policy.

Avoid placing raw recording media, transcript bodies, payment data, authentication secrets or unnecessary customer contact details directly in broadly distributed event envelopes. Prefer governed artifact identifiers and authorized retrieval.

Classification should influence topic/access policy, encryption, retention, logging/redaction, export controls and observability behavior.
