# Conversation Intelligence and AI Domain

## Artifact pipeline
```text
Media/Audio → Speech Recognition → Transcript Version → Utterances
  → Intelligence Processing
      ├─ Topics / Entities / Intent
      ├─ Sentiment signals
      ├─ Summary / Action Items
      ├─ Compliance signals
      └─ Agent Assist suggestions
```

## Provenance
Every generated artifact references source artifact/version, model/provider identity, model/configuration version where available, generation time, language and confidence/quality metadata appropriate to the artifact.

## Human/AI boundary
Generated summaries, evaluations and recommendations are derived artifacts. Preserve whether a human accepted, edited, rejected or overrode them. Do not erase original machine output or represent it as human judgment.

## Streaming agent assist
Suggestion lifecycle can be Generated → Delivered → Viewed → Accepted/Used/Dismissed/Expired. This enables latency and usefulness measurement rather than counting generated suggestions as successful assistance.

## Governance
Model redaction, access, allowed-purpose policy, prompt/configuration version and audit references. Domain modeling alone does not establish correctness, fairness or regulatory compliance.
