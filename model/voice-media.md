# Voice and Media Domain

## Separation
A business Interaction is distinct from signaling and media resources.

```text
Interaction
  → Voice Session
      → Call Leg(s)
          → signaling identifiers
      → Media Session(s)
          → Media Stream(s)
```

## Call leg
CallLeg represents one technical signaling leg with direction, endpoint references, lifecycle timestamps, termination reason and typed external IDs such as SIP Call-ID or carrier ID.

## Media
MediaSession owns negotiated/active media relationships. MediaStream describes audio/video direction, codec/payload metadata and quality observations. Recording is a separate governed domain referencing media/session/segment identities.

## State
Conceptual voice states include Initiating, Progressing, Ringing, Answered, Held, Terminating, Ended and Failed. B2BUA platforms can have different state on separate legs at the same instant.

## Termination
Preserve protocol cause and normalized business termination reason separately. Mapping SIP/Q.850/provider causes to canonical outcomes is versioned adapter logic.
