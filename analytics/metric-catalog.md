# Canonical Metric Catalog Framework

This file defines semantic categories, not universal formulas. Organizations must version their exact definitions.

| Category | Example metrics | Required semantic decisions |
|---|---|---|
| Demand | offered interactions | entry point, retries, transfers |
| Queue | queued, abandoned, queue time | queue entry/exit rules |
| Service | service level, ASA | threshold, denominator, exclusions |
| Agent | handled, handle time, occupancy | segment vs interaction, ACW |
| Routing | attempt latency, conflicts | attempt boundaries |
| Media | setup, RTP quality | leg/session aggregation |
| Quality | evaluation score | form/version, weighting |
| WFM | adherence, conformance | schedule/activity mapping |
| Survey | response rate, CSAT/NPS/CES | eligibility, scale, population |
| AI | transcription coverage, assist acceptance | model/version, confidence |

## Anti-pattern
Do not create a column named `service_level` without preserving its threshold, population and formula version. Two dashboards can show the same label and calculate different numbers while both appear plausible.
