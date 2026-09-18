# Contract Test Plan

This repository contains reference schemas and fixtures; it does not claim an executed CI suite yet.

A future executable contract test suite should:
1. validate every example against the canonical envelope and event payload schema;
2. maintain known-invalid fixtures for missing IDs, malformed timestamps and illegal states;
3. test backward-compatible additions against previous consumers;
4. test duplicate delivery/idempotency behavior in reference consumers;
5. test out-of-order aggregate versions;
6. test replay semantics;
7. verify examples contain no real customer or credential data.

The distinction between documented contract and executed proof is deliberate.
