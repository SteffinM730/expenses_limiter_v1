---

description: "Task list for the evidence-bounded database-migration feature"
---

# Tasks: Database Migration

**Input**: Design documents from `/specs/003-database-migration/`

**Prerequisites**: [plan.md](./plan.md) and [spec.md](./spec.md). The plan's pre-Phase-0 Constitution Check is currently **ERROR**. These tasks deliberately do not select a Go implementation, source extractor, destination datastore, schema, or execution procedure. The operator decisions identified in Phase 2 are blocking prerequisites for any such work.

**Tests**: No automated-test tasks are included. The specification does not request a TDD approach, and the plan establishes that an executable migration and its test environment cannot be designed before the required approvals. The per-story independent validation criteria below are documentation/review checks from the specification, not substitutes for the constitution-required migration and characterization tests once an execution design is approved.

**Organization**: Tasks are grouped by user story so the evidence inventory, approved field mapping, and migration-outcome design can each be reviewed independently after the blocking decisions are recorded.

## Phase 1: Setup (Evidence and Decision Records)

**Purpose**: Create the controlled records needed to preserve the frozen-evidence boundary and to capture approvals without inventing missing migration details.

- [x] T001 Create a decision register for the unresolved destination, identifier, rejection-handling, source-extraction, and Go-architecture decisions in specs/003-database-migration/migration-decision-log.md
- [ ] T002 [P] Create an evidence-boundary record that cites the documented `ExpenseEntity` and `TagEntity` source paths and states unavailable source-database semantics in specs/003-database-migration/research.md
- [ ] T003 [P] Update the documentation artifact manifest and gate status for the decision register, research record, data model, outcome contract, and operator procedure in specs/003-database-migration/plan.md

---

## Phase 2: Foundational (Approval Gate)

**Purpose**: Record the approvals that the specification and Constitution Check require before defining or executing a migration.

**⚠️ CRITICAL**: No user-story implementation work may begin until every task in this phase is complete and the Constitution Check is re-evaluated as passing or governed by an approved exception.

- [ ] T004 Record the operator-approved destination datastore, destination schema or DDL, credential-handling model, target runtime, and target platform in specs/003-database-migration/migration-decision-log.md
- [ ] T005 Record the operator-approved source-ID preservation or cross-reference policy and stop/continue/retry handling for rejected records in specs/003-database-migration/migration-decision-log.md
- [ ] T006 Record the source database location, schema-version history, Room converter or encoding details for `Currency` and `LocalDate`, nullability/default/constraint/index semantics, and any approved `ExpenseEntity`–`TagEntity` relationship evidence in specs/003-database-migration/migration-decision-log.md
- [ ] T007 [P] Record an approved Go-target architecture amendment or exception and its validation requirements in .specify/memory/constitution.md
- [ ] T008 Reconcile the approved decisions with FR-007 through FR-009 and the Constitution Check, removing only resolved clarification markers and updating the gate result in specs/003-database-migration/spec.md

**Checkpoint**: The evidence and governing approvals are complete; a destination-specific migration design can be created without guessing.

---

## Phase 3: User Story 1 - Define the documented source scope (Priority: P1) 🎯 MVP

**Goal**: Give the operator a complete, evidence-backed inventory of the two documented source entities and all ten documented fields.

**Independent Test**: Review the source inventory and confirm it names `ExpenseEntity` with `id`, `amount`, `currency`, `title`, `date`, `notes`, `createdAt`, and `modifiedAt`, plus `TagEntity` with `id` and `name`.

- [ ] T009 [US1] Create the source-scope inventory for `ExpenseEntity` and `TagEntity`, including every documented field, type, and frozen source path, in specs/003-database-migration/data-model.md
- [ ] T010 [US1] Add the User Story 1 inventory-review result that verifies two entities and ten fields against the frozen evidence in specs/003-database-migration/data-model.md

**Checkpoint**: The documented source scope is complete and independently reviewable; no undocumented relationship or physical-schema property has been inferred.

---

## Phase 4: User Story 2 - Approve a field-level migration mapping (Priority: P2)

**Goal**: Give the operator one approved destination field or explicit approved exclusion for each documented source field before movement begins.

**Independent Test**: Inspect the mapping and confirm it has exactly one approved disposition for each of the ten source fields, including the recorded treatment of `Long`, `Float`, `Currency`, `String`, and `LocalDate`.

- [ ] T011 [US2] Populate a field-level source-to-destination mapping or explicit approved exclusion for all ten documented fields, using the approved destination schema and identifier policy, in specs/003-database-migration/data-model.md
- [ ] T012 [US2] Record the mapping approval and the User Story 2 completeness review for `Long`, `Float`, `Currency`, `String`, and `LocalDate` values in specs/003-database-migration/data-model.md

**Checkpoint**: The field mapping is approved and independently reviewable before migration behavior is designed or data is processed.

---

## Phase 5: User Story 3 - Verify recorded migration outcomes (Priority: P3)

**Goal**: Define the approved record-outcome and reconciliation contract needed to account for every processed source record and investigate exceptions.

**Independent Test**: Using a known processed-record set, review the specified outcome ledger and reconciliation procedure to confirm every source record must have exactly one `migrated`, `skipped`, or `rejected` outcome and that skipped/rejected outcomes require a reason.

- [ ] T013 [US3] Define the approved per-record outcome contract with `migrated`, `skipped`, and `rejected` statuses, mandatory reasons for skipped/rejected records, and the approved source-record reference in specs/003-database-migration/contracts/migration-outcome.md
- [ ] T014 [US3] Define the reconciliation report that compares processed source-record references with recorded outcomes and identifies each difference for operator review in specs/003-database-migration/quickstart.md
- [ ] T015 [US3] Add the User Story 3 review procedure for one-and-only-one outcomes and exception-resolution visibility in specs/003-database-migration/quickstart.md

**Checkpoint**: The required outcome accounting is specified and independently reviewable; executable migration, ledger storage, and report generation remain deferred until the approved execution design is added to the plan.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Confirm traceability, safety constraints, and plan readiness across the completed documentation.

- [ ] T016 [P] Update the feature checklist to mark only actually resolved clarifications and to record the final documentation review in specs/003-database-migration/checklists/requirements.md
- [ ] T017 Re-run the Constitution Check against the approved decisions, inventory, mapping, and outcome contract; record remaining blockers or the next design phase in specs/003-database-migration/plan.md

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: Can begin immediately from the frozen documentation.
- **Foundational (Phase 2)**: T004–T006 depend on the decision register from T001; T007 is independent but all four approvals must be complete before T008. T008 blocks all user-story work.
- **User Story 1 (Phase 3)**: Begins after T008 and supplies the documented source inventory used by User Story 2.
- **User Story 2 (Phase 4)**: Begins after User Story 1; its mapping relies on the approved destination and identifier decisions plus the source inventory.
- **User Story 3 (Phase 5)**: Begins after User Story 2; the approved record reference and mapping are needed to define a reconciliation contract.
- **Polish (Phase 6)**: Follows the desired user-story phases.

### User Story Dependency Graph

```text
Setup (T001–T003)
        │
        ▼
Approval Gate (T004–T008)
        │
        ▼
US1: documented source inventory (T009–T010)
        │
        ▼
US2: approved field mapping (T011–T012)
        │
        ▼
US3: outcome and reconciliation contract (T013–T015)
        │
        ▼
Polish and readiness review (T016–T017)
```

### Parallel Opportunities

- T002 and T003 can proceed independently of the decision-register creation because they modify different files.
- T007 can proceed in parallel with T004–T006 only after the authorized amendment/exception decision is available; it modifies the Constitution while the other tasks modify the decision register.
- T016 can proceed alongside the final plan review once the associated documentation review is complete; it modifies the checklist rather than the plan.

## Parallel Example: Approval Gate

```text
Task: "Record the approved destination, schema, credentials, runtime, and platform in specs/003-database-migration/migration-decision-log.md"
Task: "Record the approved Go-target architecture amendment or exception in .specify/memory/constitution.md"
```

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1 and all Phase 2 approval-gate tasks.
2. Complete T009–T010 to deliver the complete source-scope inventory.
3. Stop and validate the User Story 1 review criterion before mapping any field or designing data movement.

### Incremental Delivery

1. Establish the controlled evidence and approval records.
2. Deliver the P1 source inventory and validate it independently.
3. Add the P2 approved field mapping and validate its ten dispositions.
4. Add the P3 outcome/reconciliation contract and validate its accounting rules.
5. Re-open implementation planning only after T017 confirms that the constitutional and specification gates allow it.

## Notes

- All tasks use the required checklist format with sequential IDs and exact file paths.
- `[P]` denotes work in a different file with no dependency on an incomplete task; it does not bypass required operator approvals.
- These tasks do not authorize source-data reads, data movement, schema changes, destructive fallbacks, or Go-code creation. Those actions require the approved decisions and a revised implementation plan.
