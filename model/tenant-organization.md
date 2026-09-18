# Tenant, Organization and Entitlement Domain

## Purpose
Defines the administrative boundary within which every CCaaS resource is owned and authorized.

## Core model
```mermaid
classDiagram
 class Tenant { +TenantId id +TenantState state }
 class BusinessUnit { +BusinessUnitId id +String name }
 class Site { +SiteId id +TimeZone timeZone }
 class Team { +TeamId id +String name }
 class User { +UserId id }
 class Entitlement { +String capability +Limit limit }
 Tenant "1" --> "*" BusinessUnit
 BusinessUnit "1" --> "*" Site
 BusinessUnit "1" --> "*" Team
 Tenant "1" --> "*" User
 Tenant "1" --> "*" Entitlement
```

## Invariants
Every tenant-owned aggregate carries a tenant boundary. Cross-tenant references are invalid unless a deliberately modeled platform-level relationship permits them. Business units, sites and teams are organizational structures, not authorization boundaries by assumption; authorization is explicit.

Entitlements describe enabled capabilities and limits such as channels, recording, WFM, QM, storage or concurrent usage. They should not be scattered as product-specific booleans across unrelated aggregates.

## Lifecycle
Tenant states can include Provisioning, Active, Suspended and Decommissioning. Decommissioning requires data-retention and legal-hold evaluation before destructive deletion.
