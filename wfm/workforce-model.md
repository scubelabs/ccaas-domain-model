# Workforce Management Detailed Model

## Forecast
ForecastSet contains versioned ForecastIntervals by queue/skill/channel. Each interval can contain volume, average handling assumptions and confidence/scenario metadata.

## Staffing
StaffingRequirement derives required capacity from forecast plus service objective and planning assumptions. Keep the derivation/version so planners can reproduce results.

## Scheduling
Schedule → AgentSchedule → Shift → ActivityInterval. Activities include productive channel work, break, meal, meeting, training, time off and organization-defined activities.

## Actuals
ActualActivityInterval is derived from authoritative operational events under a versioned mapping policy. Agent routing state alone may not fully describe activity.

## Adherence
Adherence compares planned and actual activity under rules/tolerances. Store the rule/version and interval evidence rather than only a percentage.

## Intraday
Intraday management compares actual demand/staffing with plan and can create reforecast or schedule adjustment proposals. Published changes are auditable versions.
