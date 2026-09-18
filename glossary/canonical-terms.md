# Canonical CCaaS Glossary

| Term | Canonical meaning |
|---|---|
| Interaction | Top-level tracked customer engagement for a business purpose |
| Conversation | Coherent communication thread within an interaction |
| Session | Channel-specific communication period |
| Segment | Bounded portion of a session created by participant/routing/technical changes |
| Participant | Customer, agent, bot, supervisor or external party |
| Queue | Routing construct holding/organizing eligible interactions |
| Routing Attempt | One idempotently identifiable attempt to match/deliver an interaction |
| Reservation | Temporary exclusive claim on agent/capacity for an interaction |
| Agent Presence | Whether an agent has an active platform/session presence |
| Routing State | Agent intent/eligibility state such as Ready/NotReady |
| Capacity | Channel-specific concurrency available/consumed by an agent |
| Recording | Governed media artifact associated with interaction/session/segments |
| Transcript | Versioned textual representation derived from media or real-time speech |
| Utterance | Time-bounded speaker-attributed unit of transcript |
| Evaluation | Quality assessment using a specific form version |
| Calibration | Process for aligning evaluator interpretation/scoring |
| Forecast | Versioned estimate of future workload |
| Schedule | Planned allocation of agent time to activities |
| Adherence | Comparison of actual activity with scheduled activity under defined rules |
| Survey | Versioned customer-feedback instrument |
| Metric | Versioned analytical definition with explicit population/formula/grain |
| Domain Event | Immutable statement that a domain-relevant fact occurred |
| Correlation ID | Identifier used to trace related work across distributed components |

## Naming rule

Product/vendor terminology can be mapped to these terms, but should not redefine them silently. Vendor mappings belong in explicit adapter/mapping documents.
