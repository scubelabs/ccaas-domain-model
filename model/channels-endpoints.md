# Channels and Endpoints

## Canonical channel abstraction
The Interaction domain normalizes shared lifecycle concepts while channel contexts preserve channel-native semantics.

| Channel | Native concepts |
|---|---|
| Voice | call leg, SIP dialog, media session, DTMF |
| Chat | conversation, message, typing/read state |
| SMS/Messaging | address, message, delivery receipt |
| Email | thread, message, recipients, attachments |
| Social | platform identity, public/private message |
| Video | room/session, participant media tracks |

## Endpoint
An Endpoint represents a technical communication termination point: SIP UA, PSTN destination, WebRTC browser/device, messaging address or integration endpoint.

Do not force every channel into SIP-like call semantics. Shared concepts belong above the channel adapter; transport-specific metadata remains typed extension data.

## Channel capability
Capabilities such as synchronous/asynchronous, supports hold, transfer, conference, attachments, read receipts and concurrency should be modeled so routing and agent UX can reason about channels without hard-coded product assumptions.
