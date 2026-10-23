## Specification Analysis Report

| ID | Category | Severity | Location(s) | Summary | Recommendation |
|----|----------|----------|-------------|---------|----------------|
| C1 | Constitution Alignment | CRITICAL | plan.md:L20, L56-L61, L75-L76; tasks.md:L35, L126, L133; constitution.md:L33-L39, L81-L85 | The planned Go target conflicts with the constitution's mandatory Kotlin target architecture. T007 proposes changing the constitution but does not require its governance prerequisites: rationale, version bump, and migration note. | Resolve the Go/Kotlin conflict in a separate, approved constitution amendment or exception that includes the required governance record; then revise the plan and tasks against that approved rule. |
| C2 | Constitution Alignment | CRITICAL | plan.md:L28-L31, L56-L58; tasks.md:L12, L74-L78; constitution.md:L14-L17, L28-L31 | The plan acknowledges that no characterization or migration-test basis exists, while the task list explicitly contains no automated-test task. This leaves the constitution's “No test, no migration” and explicit Room-migration-test requirements without a task path before any executable migration work. | After source and destination details are approved, add characterization, migration, and data-preservation test tasks before implementation tasks; retain the gate until they are executable and passing. |
| U1 | Ambiguity | HIGH | spec.md:L91-L93, L115; plan.md:L20-L39, L63-L76; tasks.md:L32-L36 | FR-007 through FR-009 leave the destination schema, identifier policy, and rejected-record policy unresolved. They determine the executable design, but tasks only provide a place to record future operator decisions. | Obtain and record the required operator approvals, then replace only the corresponding clarification markers and regenerate the implementation design/tasks. Do not begin data movement from the current artifacts. |
| U2 | Underspecification | HIGH | spec.md:L56-L67, L75-L78; plan.md:L28-L31; tasks.md:L72-L78 | User Story 3 requires processing a known record set and verifying outcomes, but no source access method, destination/ledger storage, fixture, or executable test procedure is specified. The planned deliverables are documentation contracts only. | Once the approval gate passes, specify a non-destructive test dataset, outcome-ledger persistence, recovery behavior for an unrecorded outcome, and acceptance tests that exercise the story. |
| I1 | Inconsistency | MEDIUM | plan.md:L78-L94; tasks.md:L6, L20-L22, L48-L49, L74-L76 | The plan's project tree says `tasks.md` is “Not created,” although the analyzed `tasks.md` exists and schedules creation of the research, data-model, contract, and quickstart artifacts that the plan labels blocked/not created. | Update the plan's artifact manifest to distinguish artifacts that are absent now from planned, gated deliverables; state that `tasks.md` has been generated. |
| I2 | Inconsistency | MEDIUM | plan.md:L52, L63-L81; tasks.md:L10, L16-L38 | The plan says five decisions are required “before Phase 0,” but tasks call them “identified in Phase 2” and permit Phase 1 work immediately. This obscures whether the evidence/decision-record tasks are allowed while the pre-Phase-0 gate is failing. | Use one gate model and phase vocabulary across plan and tasks, explicitly marking which documentation tasks are permitted before approval and which actions remain blocked. |
| A1 | Ambiguity | LOW | spec.md:L71 | The unremoved template placeholder, “[Add more user stories as needed, each with an assigned priority],” is not an actionable requirement and makes the feature's story set appear incomplete. | Remove the template instruction or replace it with an explicit statement that the three listed stories are the complete evidence-bounded scope. |

### Coverage Summary Table

| Requirement Key | Has Task? | Task IDs | Notes |
|-----------------|-----------|----------|-------|
| FR-001 | Yes | T002, T009, T010 | Inventory evidence and review cover both documented entities. |
| FR-002 | Yes | T009, T011, T012 | Inventory and field mapping cover the eight `ExpenseEntity` fields. |
| FR-003 | Yes | T009, T011, T012 | Inventory and field mapping cover the two `TagEntity` fields. |
| FR-004 | Yes | T011, T012 | Mapping and approval record are planned after the approval gate. |
| FR-005 | Yes | T013, T015 | Outcome contract and review procedure cover statuses and reasons. |
| FR-006 | Yes | T014, T015 | Reconciliation report and review procedure are planned. |
| FR-007 | Yes | T001, T004, T008 | Coverage is a pending operator decision, not an executable datastore design. |
| FR-008 | Yes | T001, T005, T008 | Coverage is a pending operator decision, not an identifier implementation. |
| FR-009 | Yes | T001, T005, T008 | Coverage is a pending operator decision, not an operational failure policy. |
| SC-001 | Yes | T009, T010 | The inventory review verifies two entities and ten fields. |
| SC-002 | Yes | T013, T015 | The contract/review describe one outcome per processed record; no executable verification exists yet. |
| SC-003 | Yes | T014, T015 | The proposed report identifies differing records, contingent on the future record reference. |
| SC-004 | Yes | T013, T015 | The outcome contract requires reasons for skipped and rejected records. |
| SC-005 | Yes | T011, T012 | The planned mapping and approval record are the operator-facing disposition source. |

### Constitution Alignment Issues

- **C1**: The current Go plan conflicts with Principle V until a separately governed amendment or exception exists.
- **C2**: No task path satisfies Principles I and IV's characterization and migration-test obligations before executable migration work.

### Unmapped Tasks

- **T003** — plan-manifest/gate maintenance; cross-cutting administration rather than a direct requirement or story.
- **T007** — constitutional governance; not a feature requirement and currently incomplete as described in C1.
- **T016** — checklist maintenance; cross-cutting review work.
- **T017** — final constitution-gate review; cross-cutting governance work.

### Metrics

- Total Requirements: 14 (9 functional requirements, 5 buildable success criteria)
- Total Tasks: 17
- Coverage: 100% (14 of 14 requirements have at least one planned task)
- Ambiguity Count: 4
- Duplication Count: 0
- Critical Issues Count: 2

### Next Actions

- Resolve the CRITICAL constitution issues before `/speckit-implement`; the current approval gate must remain closed.
- Run `/speckit-clarify` to capture the decisions behind FR-007 through FR-009, then run `/speckit-plan` and `/speckit-tasks` after the approved constitutional amendment or exception is available.
- Correct the plan/task phase and artifact-manifest inconsistencies before relying on the task sequence.

Would you like me to suggest concrete remediation edits for the top 2 issues?
