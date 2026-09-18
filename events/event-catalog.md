# Canonical CCaaS Event Catalog

Events are past-tense facts. Commands such as `RouteInteraction` are not events.

## Interaction

- `interaction.created`
- `interaction.activated`
- `interaction.queued`
- `interaction.dequeued`
- `interaction.completed`
- `interaction.abandoned`
- `interaction.failed`

## Routing

- `routing.attempt.started`
- `routing.agent.reserved`
- `routing.agent.offer_sent`
- `routing.agent.offer_accepted`
- `routing.agent.offer_rejected`
- `routing.agent.offer_timed_out`
- `routing.reservation.released`
- `routing.attempt.completed`

## Agent

- `agent.session.started`
- `agent.presence.changed`
- `agent.routing_state.changed`
- `agent.capacity.changed`
- `agent.session.ended`

## Media / recording

- `media.session.started`
- `media.session.connected`
- `media.session.ended`
- `recording.started`
- `recording.paused`
- `recording.resumed`
- `recording.stopped`
- `recording.available`
- `recording.failed`
- `recording.deleted`

## Transcription / AI

- `transcription.started`
- `transcription.partial.produced`
- `transcription.completed`
- `transcription.failed`
- `conversation.summary.generated`
- `conversation.topic.detected`
- `agent_assist.suggestion.generated`

## Quality / coaching

- `quality.evaluation.created`
- `quality.evaluation.completed`
- `quality.calibration.completed`
- `quality.coaching.assigned`
- `quality.coaching.completed`

## WFM

- `wfm.forecast.published`
- `wfm.schedule.published`
- `wfm.activity.started`
- `wfm.activity.ended`
- `wfm.adherence.calculated`

## Survey

- `survey.invitation.sent`
- `survey.response.started`
- `survey.response.submitted`

## Event requirements

Every event contract should define producer, aggregate ID, schema version, event ID, occurrence time, tenant, correlation/causation, ordering expectations, PII classification, retention expectations and compatibility policy.

Consumers must assume at-least-once delivery unless the concrete transport contract proves otherwise and should implement deduplication/idempotency accordingly.
