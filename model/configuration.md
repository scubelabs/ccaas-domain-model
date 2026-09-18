# Configuration and Policy Domain

Configuration is versioned domain data, not an unstructured global key/value bag.

Examples: QueuePolicy, RoutingPolicy, RecordingPolicy, RetentionPolicy, FlowVersion, SkillDefinition, ChannelConfiguration, BusinessHours, HolidayCalendar and FeatureConfiguration.

## Lifecycle
Draft → Validated → Published → Superseded/Retired.

Published configuration has immutable version identity. Runtime components consume a version and expose which version governed a decision so incidents can reconstruct behavior.

## Scope
Configuration resolves through explicit scopes such as platform, tenant, business unit, queue or resource. Override precedence must be deterministic and inspectable.

## Safety
Validation should catch invalid references, cyclic flows, impossible capacity, missing dependencies and incompatible policy combinations before publication. Secret values remain external secret references.
