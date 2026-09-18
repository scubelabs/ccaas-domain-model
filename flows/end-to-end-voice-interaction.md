# End-to-End Voice Interaction Domain Flow

```mermaid
sequenceDiagram
 participant C as Customer
 participant CH as Voice Channel
 participant I as Interaction Core
 participant IVR as IVR
 participant R as Routing
 participant A as Agent
 participant REC as Recording
 participant TX as Transcription
 participant Q as Quality
 participant AN as Analytics

 C->>CH: inbound call
 CH->>I: create interaction/session
 I->>IVR: start flow
 IVR->>I: context/intention collected
 I->>R: queue interaction
 R->>A: reserve + offer
 A-->>R: accept
 R->>I: agent assignment
 CH->>A: establish agent media
 CH->>REC: recording lifecycle
 I->>AN: lifecycle events
 REC->>TX: recording/media artifact
 TX->>Q: transcript available
 I->>Q: interaction eligible
 C-->>CH: disconnect
 CH->>I: session ended
 I->>AN: interaction completed
```

## Correlation
One `interaction_id` ties the business journey together while channel/media/routing/recording artifacts retain their own IDs. Transfer/conference can create additional participants, segments, call legs and recordings without destroying the parent identity.

## Failure semantics
If transcription fails after the call completes, the Interaction remains completed; transcription owns a failed/retryable processing state. If analytics is unavailable, real-time call processing should not become synchronously dependent on dashboard persistence. Bounded-context ownership makes such degradation explicit.
