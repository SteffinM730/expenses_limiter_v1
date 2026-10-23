"""Acceptance checks for the evidence-bounded database-migration work order.

These tests deliberately inspect only the documentation artifacts mandated by
specs/003-database-migration/tasks.md.  They must not be expanded to infer a
database engine, schema, source-reader, or Go implementation before an
operator has approved those choices.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[2]
FEATURE = REPOSITORY / "specs" / "003-database-migration"

SOURCE_FIELDS = {
    "ExpenseEntity": {
        "id": "Long",
        "amount": "Float",
        "currency": "Currency",
        "title": "String",
        "date": "LocalDate",
        "notes": "String",
        "createdAt": "Long",
        "modifiedAt": "Long",
    },
    "TagEntity": {"id": "Long", "name": "String"},
}

UNRESOLVED = re.compile(
    r"\b(?:needs\s+clarification|tbd|todo|pending|unknown|not\s+decided|"
    r"to\s+be\s+determined)\b",
    re.IGNORECASE,
)


class DocumentationAcceptanceTest(unittest.TestCase):
    maxDiff = None

    def document(self, relative_path: str) -> str:
        path = FEATURE / relative_path
        self.assertTrue(path.is_file(), f"Required work-order artifact is missing: {path}")
        return path.read_text(encoding="utf-8")

    def section(self, text: str, heading_pattern: str) -> str:
        """Return a Markdown heading section, excluding its following peer heading."""
        match = re.search(
            rf"^#{{1,6}}\s+[^\n]*{heading_pattern}[^\n]*$",
            text,
            re.IGNORECASE | re.MULTILINE,
        )
        self.assertIsNotNone(match, f"Missing required section matching: {heading_pattern}")
        following = re.search(r"^#{1,6}\s+", text[match.end() :], re.MULTILINE)
        end = match.end() + following.start() if following else len(text)
        return text[match.start() : end]

    def assert_resolved(self, text: str, description: str) -> None:
        unresolved = UNRESOLVED.search(text)
        self.assertIsNone(
            unresolved,
            f"{description} is not an approved, executable decision: {unresolved.group(0)!r}",
        )

    def assert_contains_terms(self, text: str, terms: list[str], description: str) -> None:
        missing = [term for term in terms if not re.search(re.escape(term), text, re.IGNORECASE)]
        self.assertFalse(missing, f"{description} is missing: {', '.join(missing)}")

    def test_approval_gate_records_all_operator_decisions(self) -> None:
        """T001/T004-T006: required choices are recorded, approved, and usable."""
        log = self.document("migration-decision-log.md")
        self.assertRegex(log, r"(?i)approved\s+(?:by|operator)")
        self.assertRegex(log, r"(?i)approved\s+(?:on|date)|date\s+approved")

        required_decisions = {
            "destination": ["datastore", "credential", "runtime", "platform"],
            "safe extraction": [
                "database location",
                "schema version",
                "Currency",
                "LocalDate",
                "nullability",
                "default",
                "constraint",
                "index",
                "relationship",
            ],
        }
        for decision, terms in required_decisions.items():
            with self.subTest(decision=decision):
                self.assert_contains_terms(log, terms, f"The {decision} decision")
                self.assertRegex(
                    log,
                    rf"(?is)(?:{terms[0]}).{{0,700}}\bapproved\b|"
                    rf"\bapproved\b.{{0,700}}(?:{terms[0]})",
                    f"The {decision} decision needs a current operator-approved entry, not only a note of the issue.",
                )

        self.assertRegex(log, r"(?i)\b(?:schema|ddl)\b")
        self.assertRegex(
            log,
            r"(?is)\b(?:source\s+)?id(?:entifier)?\b.{0,500}"
            r"(?:preserv|cross[ -]?reference)|(?:preserv|cross[ -]?reference).{0,500}"
            r"\b(?:source\s+)?id(?:entifier)?\b",
            "The log must select ID preservation or an approved source-to-destination cross-reference.",
        )
        self.assertRegex(
            log,
            r"(?is)\brejected\b.{0,500}\b(?:stop|continue|retry)\b|"
            r"\b(?:stop|continue|retry)\b.{0,500}\brejected\b",
            "The log must select a rejected-record policy (stop, continue, or retry).",
        )

    def test_evidence_boundary_cites_both_frozen_sources_and_unknown_semantics(self) -> None:
        """T002: research records evidence without fabricating physical DB details."""
        research = self.document("research.md")
        self.assert_contains_terms(
            research,
            [
                "ExpenseEntity.kt",
                "TagEntity.kt",
                "app/src/main/java/com/nominalista/expenses/data/room/entities",
                "source-database",
            ],
            "The evidence-boundary record",
        )
        self.assertRegex(
            research,
            r"(?is)(?:unavailable|not\s+documented|unknown).{0,300}"
            r"(?:table|key|nullability|default|constraint|index|relation|version|encoding)",
            "The research record must explicitly distinguish unavailable source-database semantics from evidence.",
        )
        self.assertRegex(
            research,
            r"(?is)(?:no|not).{0,80}(?:documented|approved).{0,100}"
            r"(?:relationship|relation).{0,160}(?:ExpenseEntity|TagEntity)",
            "The research record must not invent an ExpenseEntity–TagEntity relationship.",
        )

    def test_spec_and_plan_open_the_gate_only_after_recorded_approvals(self) -> None:
        """T008/T017: the specification and plan agree that the gate has passed."""
        spec = self.document("spec.md")
        plan = self.document("plan.md")

        for requirement in ("FR-007", "FR-008", "FR-009"):
            with self.subTest(requirement=requirement):
                line = re.search(rf"^.*{requirement}.*$", spec, re.IGNORECASE | re.MULTILINE)
                self.assertIsNotNone(line, f"{requirement} must remain traceable in the spec")
                self.assert_resolved(line.group(0), requirement)

        self.assertRegex(
            plan,
            r"(?im)^.*(?:constitution\s+check|approval\s+gate).*\b(?:pass|passed)\b.*$",
            "The plan must record a passing Constitution Check/approval gate.",
        )
        self.assert_contains_terms(
            plan,
            [
                "migration-decision-log.md",
                "research.md",
                "data-model.md",
                "migration-outcome.md",
                "quickstart.md",
            ],
            "The plan artifact manifest",
        )

    def test_go_architecture_exception_is_governed_and_validatable(self) -> None:
        """T007: a Go exception/amendment satisfies the constitution's governance rules."""
        constitution = (REPOSITORY / ".specify" / "memory" / "constitution.md")
        self.assertTrue(constitution.is_file(), "The governing constitution must remain present.")
        text = constitution.read_text(encoding="utf-8")
        go_rule = self.section(text, r"(?:go|exception|amendment)")

        self.assert_contains_terms(
            go_rule,
            ["Go", "architecture", "validation", "rationale", "migration note"],
            "The governed Go architecture amendment/exception",
        )
        self.assertRegex(text, r"(?im)^\*\*Version\*\*:\s*[0-9]+\.[0-9]+\.[0-9]+")
        self.assertRegex(
            text,
            r"(?im)^\*\*Last Amended\*\*:\s*\d{4}-\d{2}-\d{2}",
            "A governed amendment must update the constitution amendment record.",
        )

    def test_source_inventory_is_complete_and_does_not_create_a_relation(self) -> None:
        """T009/T010: exactly the frozen, documented source scope is reviewable."""
        model = self.document("data-model.md")
        inventory = self.section(model, r"(?:source.*(?:scope|inventory)|inventory)")
        self.assert_contains_terms(inventory, ["two", "ten", "review"], "The inventory review")

        for entity, fields in SOURCE_FIELDS.items():
            with self.subTest(entity=entity):
                self.assertIn(entity, inventory, f"Source inventory omits {entity}")
                for field, field_type in fields.items():
                    self.assertRegex(
                        inventory,
                        rf"(?is)\b{re.escape(field)}\b.{{0,180}}\b{re.escape(field_type)}\b",
                        f"Inventory omits {entity}.{field} or its documented {field_type} type.",
                    )

        self.assertRegex(
            inventory,
            r"(?is)(?:no|not)\s+(?:documented|approved).*?(?:relationship|relation).*?"
            r"(?:ExpenseEntity|TagEntity)",
            "The inventory must explicitly preserve the evidence boundary: no entity relation is invented.",
        )

    def test_mapping_gives_each_field_one_approved_non_placeholder_disposition(self) -> None:
        """T011/T012: every source field has one approved destination or exclusion."""
        model = self.document("data-model.md")
        mapping = self.section(model, r"(?:field.*mapping|mapping.*field)")
        self.assertRegex(mapping, r"(?i)approved")

        for entity, fields in SOURCE_FIELDS.items():
            for field, field_type in fields.items():
                source = f"{entity}.{field}"
                with self.subTest(source=source):
                    rows = re.findall(
                        rf"(?im)^\|[^\n]*\b{re.escape(source)}\b[^\n]*\|\s*$",
                        mapping,
                    )
                    self.assertEqual(
                        len(rows),
                        1,
                        f"{source} must have exactly one dedicated mapping-table disposition row; found {len(rows)}.",
                    )
                    row = rows[0]
                    self.assertRegex(row, rf"(?i)\b{re.escape(field_type)}\b")
                    self.assertRegex(
                        row,
                        r"(?i)(?:destination|exclude|exclusion|not\s+migrated)",
                        f"{source} needs a destination field or explicit exclusion.",
                    )
                    self.assertRegex(row, r"(?i)approved")

        self.assert_contains_terms(
            mapping,
            ["Long", "Float", "Currency", "String", "LocalDate"],
            "The mapping's documented type treatments",
        )

    def test_outcome_contract_accounts_for_one_result_per_processed_record(self) -> None:
        """T013: statuses, references, and exception reasons form a usable ledger contract."""
        contract = self.document("contracts/migration-outcome.md")
        self.assert_contains_terms(
            contract,
            ["source-record reference", "migrated", "skipped", "rejected"],
            "The outcome contract",
        )
        self.assertRegex(
            contract,
            r"(?is)(?:exactly\s+one|one\s+and\s+only\s+one).*?"
            r"(?:outcome|status).*?(?:processed|source).*?(?:record|reference)",
        )
        for status in ("skipped", "rejected"):
            with self.subTest(status=status):
                self.assertRegex(
                    contract,
                    rf"(?is)\b{status}\b.{{0,220}}\b(?:mandatory|required)\b.{{0,120}}\breason\b|"
                    rf"(?is)\b(?:mandatory|required)\b.{{0,120}}\breason\b.{{0,220}}\b{status}\b",
                )

    def test_reconciliation_procedure_identifies_each_difference_and_exposes_exceptions(self) -> None:
        """T014/T015: reconciliation compares references, not merely totals."""
        quickstart = self.document("quickstart.md")
        reconciliation = self.section(quickstart, r"reconciliation")
        self.assert_contains_terms(
            reconciliation,
            ["processed", "outcome", "source-record reference", "difference", "operator"],
            "The reconciliation procedure",
        )
        self.assertRegex(
            reconciliation,
            r"(?is)(?:compare|set\s+difference).*?(?:processed).*?(?:outcome)",
            "The procedure must compare the processed and outcome reference sets.",
        )
        self.assertRegex(
            reconciliation,
            r"(?is)(?:each|every).*?(?:differing|missing|extra).*?(?:record|reference)",
            "The procedure must identify every differing record, not only report a count.",
        )
        self.assertRegex(
            quickstart,
            r"(?is)(?:known|sample).*?(?:processed).*?(?:record|reference).*?"
            r"(?:exactly\s+one|one\s+and\s+only\s+one).*?(?:outcome|status)",
            "The review procedure must exercise a known processed-record set and one-outcome rule.",
        )
        self.assertRegex(
            quickstart,
            r"(?is)(?:skipped|rejected).*?reason.*?(?:resolution|resolve|operator)|"
            r"(?is)(?:resolution|resolve|operator).*?(?:skipped|rejected).*?reason",
            "The procedure must expose skipped/rejected records and their reasons for resolution.",
        )

    def test_requirements_checklist_records_completed_documentation_review(self) -> None:
        """T016: readiness evidence references the completed, reviewable artifacts."""
        checklist = self.document("checklists/requirements.md")
        self.assertNotRegex(
            checklist,
            r"(?im)^\s*-\s*\[\s\].*(?:clarification|migration|decision|mapping|outcome|reconciliation)",
            "The final checklist leaves a migration-readiness item unchecked.",
        )
        self.assert_contains_terms(
            checklist,
            ["migration-decision-log", "data-model", "migration-outcome", "quickstart", "review"],
            "The final documentation review checklist",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
