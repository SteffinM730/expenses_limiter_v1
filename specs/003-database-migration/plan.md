# Implementation Plan: Database Migration

**Branch**: `003-database-migration` | **Date**: 2026-10-23 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `specs/003-database-migration/spec.md`

## Summary

The proposed feature must preserve the documented data of `ExpenseEntity` and
`TagEntity` while rebuilding from Kotlin to Go. The frozen legacy evidence
defines only the two entities and their ten fields. It does not define a
destination datastore or schema, identifier treatment, record-failure policy,
or executable source-database semantics. Planning is therefore halted at the
pre-research Constitution Check: choosing any migration architecture or data
mapping would invent information that the specification explicitly reserves for
approval.

## Technical Context

**Language/Version**: Go; version **NEEDS CLARIFICATION**

**Primary Dependencies**: **NEEDS CLARIFICATION** — they depend on the approved
destination datastore and execution model.

**Storage**: Source evidence is limited to Room-named Kotlin entity paths.
Destination datastore and schema are **NEEDS CLARIFICATION**.

**Testing**: **NEEDS CLARIFICATION** — the legacy documents provide no runnable
tests, fixtures, parity cases, or test command. The constitution will require
migration and characterization coverage once the executable migration is
defined.

**Target Platform**: **NEEDS CLARIFICATION**

**Project Type**: **NEEDS CLARIFICATION** — a migration executable, service, or
embedded data-access change would expose materially different contracts.

**Performance Goals**: **NEEDS CLARIFICATION** — no data volume, outage window,
or throughput requirement is documented.

**Constraints**: The scope is restricted to documented source data:
`ExpenseEntity` (eight fields) and `TagEntity` (two fields). The constitution
prohibits data loss and destructive fallback. The frozen source documentation
does not establish table names, keys, nullability, defaults, constraints,
relations, version history, physical database, or value encodings.

**Scale/Scope**: Two documented source entities and ten documented fields;
record count and operational scale are **NEEDS CLARIFICATION**.

## Constitution Check

### Pre-Phase-0 Gate: ERROR — planning cannot proceed

| Constitution / specification requirement | Evidence | Gate result |
| --- | --- | --- |
| I. Behavior Preservation | `../../old/docs/overview.md` reports 0.0% execution-grounded coverage; no behavior, DB query, or migration mechanics are described. | **FAIL**: no source characterization or verification basis is available. |
| II. Spec Before Code | FR-007, FR-008, and FR-009 explicitly mark destination, identifier, and rejected-record policies as needing clarification before planning or implementation. | **FAIL**: none of the required approvals is present. |
| IV. Data Safety | The constitution requires an explicit migration and migration test for Room schema changes, with no destructive fallback. The legacy documents do not state source schema version, migration history, database location, or backup/export behavior. | **FAIL**: a safe migration/rollback strategy cannot be designed from the available evidence. |
| V. Target Architecture | The constitution names Kotlin architecture, while the declared operator goal is Kotlin to Go. No constitutional amendment or approved exception defines the Go target architecture. | **FAIL** for Go implementation planning; no Go design will be invented. |
| VIII. Simplicity | Selecting a datastore, driver, deployment model, or schema without evidence would add speculative design. | **PASS**: planning stops rather than adding it. |
| IX. Security & Privacy | `../../old/docs/security.md` could not search the estate; credentials, access control, and data-handling constraints are unknown. | **FAIL**: destination access and handling cannot be specified safely. |

**Required operator decisions before Phase 0 can begin**:

1. Destination datastore, its schema/DDL, connection and credential-handling
   model, and target runtime/platform.
2. Identifier policy: preserve each source `id`, or define an approved
   source-to-destination cross-reference.
3. Rejected-record policy: stop, continue, retry, or another defined policy;
   include the required recording and operator-resolution behavior.
4. Source-database details needed for safe extraction: physical database/file
   location, schema version history, Room converters/encodings for `Currency`
   and `LocalDate`, nullability/default/constraint/index semantics, and any
   `ExpenseEntity`–`TagEntity` relation.
5. An approved constitutional amendment or exception that governs the Go
   target architecture and its validation requirements.

No Phase 0 research or Phase 1 design artifacts were generated. Research can
establish what the frozen source documents say, but it cannot approve or infer
the five decisions above. Treating them as resolved would violate both the
feature specification and the constitution.

## Project Structure

### Documentation (this feature)

```text
specs/003-database-migration/
├── plan.md              # Gate result and prerequisite decisions
├── research.md          # Not created: Phase 0 is blocked
├── data-model.md        # Not created: Phase 1 is blocked
├── contracts/           # Not created: Phase 1 is blocked
├── quickstart.md        # Not created: Phase 1 is blocked
└── tasks.md             # Not created: planning has not passed its gate
```

### Source Code (repository root)

```text
# No source-code layout is selected.
# This workspace contains planning artifacts only; the frozen legacy estate is
# represented by ../../old/docs/ and must not be modified from this worktree.
```

**Structure Decision**: Deferred. A source layout must follow the approved Go
target architecture, target datastore, and execution model.

## Complexity Tracking

Not applicable. No implementation design has been accepted, and no complexity
exception is justified.
