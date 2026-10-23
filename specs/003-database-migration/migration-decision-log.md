# Migration Decision Register

**Feature**: Database Migration  
**Status**: Approval gate open — no migration design or data movement is authorized.

This register records the operator approvals required before an executable
migration can be designed. The frozen legacy documentation establishes only the
documented `ExpenseEntity` and `TagEntity` fields; it does not resolve any
decision below. An entry remains unresolved until the operator supplies the
requested approval and the applicable follow-on task records it.

| ID | Decision | Current status | Required operator approval | Basis / boundary | Follow-on task |
| --- | --- | --- | --- | --- | --- |
| D-001 | Destination datastore and execution environment | **Unresolved** | Name the destination datastore; provide its destination schema or DDL; define the connection and credential-handling model; and approve the target runtime and platform. | FR-007 is unresolved. The frozen documentation names no destination datastore, schema, credentials, or runtime. Do not select a datastore or schema from this register. | T004 |
| D-002 | Identifier policy | **Unresolved** | Approve either preservation of every source `id` or a source-to-destination cross-reference policy, including the approved cross-reference representation. | FR-008 is unresolved. The documented fields include `id` for `ExpenseEntity` and `TagEntity`; no identifier treatment is documented. | T005 |
| D-003 | Rejected-record handling | **Unresolved** | Approve the operational policy for records that cannot be processed: stop, continue and report all rejections, retry, or another defined policy. State the required recording and operator-resolution behavior. | FR-009 is unresolved. The future outcome contract must record one outcome per processed record and reasons for skipped or rejected records, but it does not choose the operational policy. | T005 |
| D-004 | Source extraction details | **Unresolved** | Provide the physical source database or file location, schema-version history, Room converter or encoding details for `Currency` and `LocalDate`, nullability/default/constraint/index semantics, and any evidence of an `ExpenseEntity`–`TagEntity` relationship. | The frozen data model documents entity field names, types, and Kotlin paths only. It does not document physical database semantics, encodings, or relationships. No source extraction method is selected. | T006 |
| D-005 | Go target architecture governance | **Unresolved** | Provide an approved constitutional amendment or exception for the Go target architecture, including its rationale, version bump, migration note, and validation requirements. | The declared modernization goal is Kotlin to Go, while Constitution Principle V specifies a Kotlin target architecture. No Go architecture is selected until the governance conflict is resolved. | T007 |

## Approval Record Rules

- Record the approver, approval date, decision detail, and supporting evidence
  when completing a follow-on task.
- Do not treat an unresolved entry as approval, and do not remove the
  clarification markers or reopen the Constitution Check until T008.
- This register does not authorize source-data reads, data movement, schema
  changes, destructive fallbacks, or Go-code creation.

## Evidence References

- [spec.md](./spec.md): FR-007 through FR-009 and the evidence-boundary
  assumptions.
- [plan.md](./plan.md): Constitution Check and its five required operator
  decisions.
- `../../old/docs/data_model.md`: the only documented persisted entities and
  fields.
- `.specify/memory/constitution.md`: data-safety, spec-before-code, and target
  architecture governance constraints.
