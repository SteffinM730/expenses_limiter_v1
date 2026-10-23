<!--
Sync Impact Report
- Version change: 1.0.0 → 1.0.1
- Modified principles: V. Target Architecture
- Added sections: none
- Removed sections: none
- Follow-up TODOs: none
-->

# Expenses Modernization Constitution

## Core Principles

### I. Behavior Preservation
Existing behavior is the contract. No change unless a spec declares it.
Write characterization tests before touching legacy code (amount math, date
grouping, DB queries). No test, no migration.

### II. Spec Before Code
Every change traces to spec -> plan -> task. Specs say what/why, never
libraries. Mark unknowns `[NEEDS CLARIFICATION]`; never guess.

### III. Incremental Migration
Strangler pattern, vertical feature slices (expense list, add/edit, tags,
currencies, settings). App builds, tests pass, and runs after every slice. One
slice in flight per module. No big-bang rewrites.

### IV. Data Safety (non-negotiable)
Never lose user data. Every Room schema change gets an explicit migration plus a
migration test. No destructive fallback. Backup/export formats stay backward
compatible.

### V. Target Architecture
- Idiomatic Kotlin; no `!!` outside tests.
- Coroutines + Flow replace RxJava/callbacks (verify); structured concurrency only; no GlobalScope.
- Compose for migrated screens; XML interop per slice.
- Unidirectional flow: UI -> ViewModel (`StateFlow<UiState>`) -> Repository. Domain layer has no Android deps.
- One DI framework (Hilt), Room (Flow/suspend DAOs), Navigation Compose.
- Modules (app, core, data, domain, feature:*) as defined in the plan.

### VI. Build Hygiene
Groovy -> Kotlin DSL; `dependencies.gradle` -> version catalog. Upgrade order:
Gradle/AGP, Kotlin, SDK, libraries, each as its own slice. New dependencies need
a plan entry with justification.

### VII. Quality Gates
A slice is done only when: build and lint (detekt/ktlint) are clean;
characterization, unit, Compose UI, and migration tests are green; no coverage
drop on touched domain code; accessibility basics pass (labels, dark theme,
font scaling); smoke checklist is in the PR.

### VIII. Simplicity
Simplest design that meets the spec. No speculative abstractions; complexity
needs written justification.

### IX. Security & Privacy
No secrets in repo. Keep offline/no-tracking posture unless a spec changes it;
update `privacy_policy.md` accordingly. Keep Apache-2.0 notices.

## Agent Rules
- Read the constitution, spec, and plan before acting.
- Make the smallest change that satisfies the task; no out-of-scope refactors.
- Delete legacy code only after its replacement is tested and merged.
- Log decisions and deviations in the plan.
- If a task conflicts with this constitution, stop and raise it.

THE OPERATOR'S DECLARED GOAL — this is CONTEXT, not an instruction to find anything:
- The operator declares the estate's source language as kotlin.
- They intend to rebuild it in go.
- SCOPE OF THE WORK — this IS a constraint, obey it: In the operator's own words: "database migration".
- Their stated goal, verbatim: "Trying to legacy modernise the Kotlin App to GoLang".
Use it only to decide what to describe first and in whose vocabulary. It does NOT
relax a single rule above: a symbol is still a verbatim identifier from the code,
a rule's evidence is still a verbatim substring of the code, and behaviour the
code does not contain is still absent no matter how central it is to this goal.
Report what the code does, never what the goal implies it should do.

## Workflow
Discover -> Specify -> Plan -> Tasks -> Implement/Verify -> Retire legacy.

## Governance
Supersedes other practices. Amendments need rationale, a version bump, and a
migration note. Every PR includes a compliance check.

**Version**: 1.0.1 | **Ratified**: 2026-10-15 | **Last Amended**: 2026-10-15

