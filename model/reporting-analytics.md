# Reporting and Analytics Domain

## Principle: metric definitions are data contracts

A dashboard label such as "Average Handle Time" is insufficient. A metric requires a canonical definition, grain, numerator/denominator or formula, included/excluded populations, timezone semantics and version.

## Analytical layers

```text
Operational domain events
       ↓
Normalized interaction events
       ↓
Facts / dimensions
       ↓
Semantic metrics
       ↓
Reports / dashboards / alerts
```

## Candidate facts

- InteractionFact
- SegmentFact
- QueueIntervalFact
- AgentInteractionFact
- AgentStateIntervalFact
- RoutingAttemptFact
- RecordingFact
- QualityEvaluationFact
- SurveyResponseFact
- ForecastIntervalFact
- AdherenceIntervalFact

## Candidate dimensions

Tenant, BusinessUnit, Team, Site, Queue, Skill, Agent, Channel, Direction, Disposition, Campaign, Time, CustomerSegment and Geography where lawful/appropriate.

## Example metric contract

```yaml
metric: average_speed_of_answer
version: 1
grain: queue_interval
population: answered_inbound_interactions
formula: sum(agent_answered_at - queued_at) / count(answered_interactions)
exclusions:
  - interactions_never_queued
timezone: event timestamps stored UTC; reporting bucket uses configured business timezone
owner: analytics-domain
```

The example is illustrative; organizations can define ASA differently. The important property is that the definition is explicit and versioned.

## Late and corrected events

Analytics must handle late-arriving events, corrections, duplicate events and historical dimension changes. Reports should not depend on exactly-once transport as a magical guarantee; consumers should be idempotent and reconciliation should be possible.

## Operational vs analytical truth

Operational state answers "what should the router do now?" Analytical state answers "what happened and how should it be measured?" They have different latency and consistency requirements and should not be forced into one data model.
