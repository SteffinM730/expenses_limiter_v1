# Feature Specification: Database Migration

**Feature Branch**: No branch was created; no specification hook is configured.

**Created**: 2026-10-21

**Status**: Draft

**Input**: User description: "database migration" in the stated Kotlin-to-Go modernization context.

## User Scenarios & Testing *(mandatory)*

<!--
  IMPORTANT: User stories should be PRIORITIZED as user journeys ordered by importance.
  Each user story/journey must be INDEPENDENTLY TESTABLE - meaning if you implement just ONE of them,
  you should still have a viable MVP (Minimum Viable Product) that delivers value.

  Assign priorities (P1, P2, P3, etc.) to each story, where P1 is the most critical.
  Think of each story as a standalone slice of functionality that can be:
  - Developed independently
  - Tested independently
  - Deployed independently
  - Demonstrated to users independently
-->

### User Story 1 - Define the documented source scope (Priority: P1)

An operator can identify the persisted source records and fields covered by this migration from the legacy estate's documented data model, so that the migration does not silently omit documented data.

**Why this priority**: The documented source schema is the only available evidence of persisted data. It establishes the smallest evidence-backed migration scope.

**Independent Test**: Review the migration inventory against the documented source model and confirm that it names `ExpenseEntity` and `TagEntity` and every field listed for them.

**Acceptance Scenarios**:

1. **Given** the documented source model, **When** the operator prepares the migration inventory, **Then** it includes `ExpenseEntity` with `id`, `amount`, `currency`, `title`, `date`, `notes`, `createdAt`, and `modifiedAt`.
2. **Given** the documented source model, **When** the operator prepares the migration inventory, **Then** it includes `TagEntity` with `id` and `name`.

---

### User Story 2 - Approve a field-level migration mapping (Priority: P2)

An operator can review and approve how every documented source field is represented in the destination before data movement begins.

**Why this priority**: A mapping makes preservation checks possible while avoiding an unsupported assumption about the destination schema.

**Independent Test**: Inspect the approved mapping and verify that it contains one disposition for each of the ten documented source fields.

**Acceptance Scenarios**:

1. **Given** an approved destination schema, **When** the operator reviews the mapping, **Then** every documented source field has a destination field or an explicit, approved disposition.
2. **Given** the source field types documented by the estate, **When** the mapping is approved, **Then** it records the treatment of `Long`, `Float`, `Currency`, `String`, and `LocalDate` values.

---

### User Story 3 - Verify recorded migration outcomes (Priority: P3)

An operator can determine the outcome for each source record processed by the migration and investigate records that did not reach the destination.

**Why this priority**: Outcome visibility is necessary to demonstrate that the approved source scope was handled, including exceptions.

**Independent Test**: Process a known set of source records and compare the recorded outcomes with that set; every record must have exactly one recorded outcome.

**Acceptance Scenarios**:

1. **Given** a source record in the approved scope, **When** it is processed, **Then** its outcome is recorded as migrated, skipped, or rejected with a reason.
2. **Given** records marked skipped or rejected, **When** the operator reviews the results, **Then** the records and their reasons are available for resolution before completion is accepted.

---

[Add more user stories as needed, each with an assigned priority]

### Edge Cases

- A documented `ExpenseEntity` or `TagEntity` field has no compatible destination field.
- A source record cannot be read or cannot be written to the selected destination.
- A record's outcome is unknown because processing stops before it is recorded.
- Values of the documented types `Currency` or `LocalDate` need a destination representation that has not been approved.
- The source model documents no relationship between `ExpenseEntity` and `TagEntity`; the migration must not invent one without approved evidence.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The migration scope MUST include the two source tables documented by the legacy estate: `ExpenseEntity` and `TagEntity`.
- **FR-002**: For `ExpenseEntity`, the migration inventory and mapping MUST account for `id` (`Long`), `amount` (`Float`), `currency` (`Currency`), `title` (`String`), `date` (`LocalDate`), `notes` (`String`), `createdAt` (`Long`), and `modifiedAt` (`Long`).
- **FR-003**: For `TagEntity`, the migration inventory and mapping MUST account for `id` (`Long`) and `name` (`String`).
- **FR-004**: Before processing data, the migration MUST provide an approved disposition for every documented source field: a destination field or an explicit recorded exclusion.
- **FR-005**: The migration MUST record exactly one outcome—migrated, skipped, or rejected—for each source record it processes; skipped and rejected outcomes MUST include a reason.
- **FR-006**: Completion MUST include a reconciliation that compares the number of source records processed with the number of recorded outcomes, and reports any difference.
- **FR-007**: The destination datastore and destination schema are [NEEDS CLARIFICATION: What datastore and schema will receive `ExpenseEntity` and `TagEntity` data?]
- **FR-008**: The migration's identifier policy is [NEEDS CLARIFICATION: Must each source `id` be preserved in the destination, or may the destination assign new identifiers with an approved cross-reference?]
- **FR-009**: The operational handling of records that cannot be processed is [NEEDS CLARIFICATION: Should the migration stop on the first rejected record, continue and report all rejections, or use another approved policy?]

### Key Entities

- **ExpenseEntity**: Documented source table with `id`, `amount`, `currency`, `title`, `date`, `notes`, `createdAt`, and `modifiedAt`. The legacy documentation assigns the types listed in FR-002.
- **TagEntity**: Documented source table with `id` and `name`. The legacy documentation assigns both fields the `Long` and `String` types respectively.
- **Migration outcome**: The recorded result for one processed source record: migrated, skipped, or rejected, with a reason for a skipped or rejected outcome.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: The approved migration inventory accounts for 2 documented source tables and 10 documented source fields before processing begins.
- **SC-002**: 100% of source records processed by the migration have exactly one recorded outcome.
- **SC-003**: The reconciliation reports a difference of 0 between processed source records and recorded outcomes, or identifies every differing record for operator review.
- **SC-004**: 100% of skipped and rejected records have a recorded reason available to the operator.
- **SC-005**: An operator can determine the approved disposition of each of the 10 documented source fields without consulting implementation details.

## Assumptions

- The frozen legacy documentation is the sole evidence source for this candidate; it declares 2 source tables and does not document their relationship, a destination datastore, or a migration process.
- This candidate is limited to the documented source data: `ExpenseEntity` and `TagEntity` and their listed fields. It does not claim that no other persisted data exists outside the available documentation.
- The operator will provide the destination schema, identifier policy, and rejected-record policy required by FR-007 through FR-009 before planning or implementation.
