# Transfer and Conference Domain Semantics

## Transfer
A transfer is a relationship between interaction segments/participants, not merely a SIP REFER.

Types may include blind, consultative, queue transfer and external transfer.

A consult transfer can create overlapping segments:
```text
Customer ↔ Agent A
             └─ consult → Agent B
Customer on hold
Agent A ↔ Agent B
then
Customer ↔ Agent B
```

Preserve who initiated transfer, source/destination, timestamps, consult outcome and resulting participant/segment lineage.

## Conference
Conference adds simultaneous participants to a communication session. Joining/leaving creates participant/media intervals; do not flatten conference duration into each participant's talk time without defined semantics.

## Reporting
Transferred interactions create classic double-counting risk. Define interaction-level metrics separately from queue/agent segment metrics.
