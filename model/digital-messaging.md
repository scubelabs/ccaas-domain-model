# Digital Messaging Domain

Digital channels share interaction correlation but preserve native message semantics.

## Core model
Conversation contains Participants and Messages. Message contains sender, recipients where applicable, channel, created/sent/delivered/read timestamps, content references and delivery state. Attachment is a separately governed artifact.

## Asynchronous lifecycle
Unlike voice, an asynchronous conversation can remain open across long periods and agent assignments. Assignment/session state must not be used as the conversation lifecycle.

## Delivery
Model Submitted, AcceptedByProvider, Delivered, Read and Failed as distinct observations where the channel supports them. Provider receipts are external facts with source identifiers.

## Content
Message content and attachments can contain sensitive data. Store classification, retention and redaction references. Channel adapters retain provider-specific metadata without polluting the canonical Message model.

## Routing
A digital work item can consume fractional/multi-session agent capacity. Routing references channel-specific capacity rather than assuming voice-style exclusivity.
