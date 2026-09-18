# Interaction Core Domain

## Definitions

**Interaction** — top-level customer engagement tracked by the platform for a business purpose.

**Conversation** — coherent communication thread within an interaction.

**Session** — channel-specific period of communication.

**Segment** — a bounded portion of a session associated with routing, participant or technical-leg changes.

**Participant** — customer, agent, bot, supervisor or external party taking part.

A transfer does not necessarily create a new Interaction. It commonly creates new segments and may create additional channel/technical sessions.

## Conceptual class model

```mermaid
classDiagram
  class Interaction {
    +InteractionId id
    +TenantId tenantId
    +InteractionState state
    +ChannelType initialChannel
    +Instant createdAt
    +Instant endedAt
  }
  class Conversation {
    +ConversationId id
    +InteractionId interactionId
  }
  class Session {
    +SessionId id
    +ChannelType channel
    +SessionState state
  }
  class Segment {
    +SegmentId id
    +SegmentType type
    +Instant startedAt
    +Instant endedAt
  }
  class Participant {
    +ParticipantId id
    +ParticipantType type
  }
  class Disposition {
    +DispositionCode code
    +String notes
  }

  Interaction "1" --> "1..*" Conversation
  Conversation "1" --> "1..*" Session
  Session "1" --> "1..*" Segment
  Conversation "1" --> "1..*" Participant
  Interaction "1" --> "0..*" Disposition
```

## Lifecycle

```mermaid
stateDiagram-v2
 [*] --> Created
 Created --> Active
 Active --> Queued
 Queued --> Active: routed
 Active --> Held
 Held --> Active
 Active --> Completed
 Queued --> Abandoned
 Active --> Failed
 Completed --> [*]
 Abandoned --> [*]
 Failed --> [*]
```

This is conceptual. Channel-specific state machines remain in their owning contexts.

## Timing semantics

Do not overload one duration. Reporting may need:

- offered_at
- queued_at
- routing_started_at
- agent_offered_at
- agent_answered_at
- media_connected_at
- hold intervals
- wrap_up_started_at / ended_at
- interaction_completed_at

Metrics such as speed of answer, handle time and queue time must declare which timestamps they use.
