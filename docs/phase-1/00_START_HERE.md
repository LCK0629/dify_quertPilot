# QueryPilot AI — Phase 1 Planning Pack

**Current status:** 2026-11-27 | Phase 1 — Pre-Development / Decision Closure | **Development NO-GO**

QueryPilot AI is a secure retail-focused natural-language analytics workbench. The objective is authorized, reproducible analytics, not arbitrary generated SQL.

## Follow-up review — 2026-11-27

- [29 Formal Security Registry Security Review — For Approval](29_SECURITY_REGISTRY_SECURITY_REVIEW_FOR_APPROVAL.md) — v1.1 review direction Owner-approved (5/5 RV decisions); registry not approved.

- [25 Security Registry Independent Review](25_SECURITY_REGISTRY_REVIEW_NOTES.md) — SR-D01–D06 review findings and unresolved identity/approval controls; **not approved**.
- [26 PostgreSQL Authorization ADR Candidate](26_POSTGRESQL_AUTHORIZATION_ADR_CANDIDATE.md) — identity-binding alternatives, recommended test candidate and DBA-01–18 negatives; **not approved**.
- [27 Verified Status](27_STATUS_2026_11_27.md) — owner-approved OD/roles versus remaining authorization/PRD/research blockers.

No Development GO has been issued. These review files do not change approved metrics, business-model grains or role policy.

## Current controlling records

| Document | Status |
|---|---|
| [09 PRD v1.0 Draft](09_PRD_V1_0_DRAFT.md) | Full PRD not approved; reconcile in v1.1 |
| [11 Product Decision Record](11_PRODUCT_DECISION_RECORD.md) | Five MVP directions approved |
| [12 System Architecture & Security v1.1](12_SYSTEM_ARCHITECTURE_SECURITY_DESIGN_V1_1.md) / [13 Approval](13_ARCHITECTURE_APPROVAL_RECORD.md) | Conditionally approved |
| [14 Conceptual ERD](14_CONCEPTUAL_ERD_DATA_MODEL_V1_0.md) / [15 Physical Database Design](15_PHYSICAL_DATABASE_DESIGN_V1_0.md) / [16 Approval](16_DATABASE_DESIGN_APPROVAL_RECORD.md) | v1.0 design baselines approved, implementation conditions remain |
| [17 Development Readiness Plan](17_DEVELOPMENT_READINESS_IMPLEMENTATION_PLAN_V1_0.md) / [18 Approval](18_DEVELOPMENT_READINESS_APPROVAL_RECORD.md) | Planning baseline approved, not Development GO |
| [19 Business Metric Dictionary](19_BUSINESS_METRIC_DICTIONARY_V1_0_APPROVED.md) | DEC-BA-001 approved business baseline; OD policy details subsequently approved under QP-APR-007 |
| [20 OD Decision Resolution](20_OD_DECISION_RESOLUTION_V1_0.md) | All seven owner-approved; independent verification pending |
| [21 OD Approval Record](21_OD_DECISION_APPROVAL_RECORD.md) | QP-APR-007; 7/7 policy dispositions approved |
| [22 Role & Permission Matrix](22_ROLE_PERMISSION_MATRIX_V1_0.md) | Owner-approved design; independent verification pending; not deployed |
| [23 Role Permission Approval](23_ROLE_PERMISSION_APPROVAL_RECORD.md) | QP-APR-008; 6/6 design recommendations approved |
| [24 Security Registry Data Model](24_SECURITY_REGISTRY_DATA_MODEL_V1_0.md) | FOR APPROVAL; review findings in 29 require revision; not owner-approved |
| [29 Formal Security Review](29_SECURITY_REGISTRY_SECURITY_REVIEW_FOR_APPROVAL.md) | v1.1 REVIEW APPROVED (5/5); targeted registry revision pending; registry not approved |
| [Database Design v1.1 Change Proposal](DB_DESIGN_V1_1_CHANGE_PROPOSAL.md) | Proposed; not a replacement approved design |

Historical draft labels in original review candidates are preserved for traceability; later explicit approval records govern the scope of approval.

## Earlier planning and evaluation references

- [01 Research & User Validation](01_RESEARCH_AND_USER_VALIDATION.md)
- [02 PRD v0.1](02_PRD_V0_1.md)
- [03 Metrics & Data Design](03_METRICS_AND_DATA_DESIGN.md)
- [04 Architecture & Security ADRs](04_ARCHITECTURE_SECURITY_ADRS.md)
- [05 Evaluation & Test Plan](05_EVALUATION_AND_TEST_PLAN.md)
- [06 Roadmap & Backlog](06_ROADMAP_BACKLOG_GATE.md)
- [07 Test Scenario Catalog](07_TEST_SCENARIO_CATALOG.md)
- [10 Metric Definition Review](10_METRIC_DEFINITION_REVIEW.md)

## Decision closure sequence

1. OD-01–OD-07 owner dispositions recorded; complete independent BA/DB/Security verification.
2. Role & Permission Matrix owner-approved under QP-APR-008; independent verification pending.
3. Resolve findings in [29 Formal Security Review](29_SECURITY_REGISTRY_SECURITY_REVIEW_FOR_APPROVAL.md) against document 24 through a DB Engineer revision; identity/session and nonforgeable PostgreSQL authorization ADRs remain open.
4. Review consolidated database v1.1 amendments and Dify/direct adapter/provider decisions.
5. Reconcile PRD v1.1, evaluation contract, user/competitor research evidence or explicit risk acceptance, and all remaining PRE-01–PRE-10 conditions.
6. Obtain separate written Development GO (G-01–G-17). QP-APR-DEV-GO-001 is reserved, not issued.

## Guardrails and evidence

- Read-only, authorized, bounded database access; no unrestricted LLM SQL.
- Current permissions govern historical snapshot access; raw data and component disclosure require separate authorization.
- Numerical contributions are not proof of causality; unknown data is not zero.
- User interviews and hands-on competitor benchmarks are not evidenced as completed. Tests remain specifications, not executed results.
- No DDL, dataset generation, coding or deployment is authorized. This index does not approve any proposed rules or imply a working product.

## Historical Project Owner review disposition — 2026-11-27 (superseded for current review)

[Project Owner disposition — Document 30](30_SECURITY_REGISTRY_REVIEW_DISPOSITION_RECORD.md) records QP-DEC-SR-REVIEW-001: **REVISE & RESUBMIT accepted; design-only DB-R01–DB-R06 authorized.** SR-D01–SR-D06 remain unapproved. Issue #1 remains open pending revised registry v1.1 and independent review. QP-APR-009 and QP-APR-DEV-GO-001 remain unissued. **Development NO-GO.**


## Current Security Review v1.1 — 2026-11-27

[Document 31 — QP-DEC-SR-REVIEW-002](31_SECURITY_REVIEW_V1_1_APPROVAL_RECORD.md) records Project Owner approval of all five Document 29 v1.1 review decisions (RV-D01–RV-D05). The risk-based review framework and design-only DB-R01–DB-R06 revision scope are approved; SG-01–SG-04 remain open. SR-D01–SR-D06, exact DB identity/authorization choices and individual R01–R04 risk acceptances remain pending. Issue #1 remains open. QP-APR-009 and QP-APR-DEV-GO-001 are unissued. **Registry NOT APPROVED; Development NO-GO.**

Next deliverable: Security Registry Data Model v1.1 — For Approval. Independent Security/DB/BA review of the revised exact candidate precedes any separate registry approval. Approved business metrics, OD policies and role matrix remain unchanged. No implementation or tests executed.

## Registry v1.1 limited design disposition — 2026-11-27

[Document 33 — Limited Design Approval Record](33_SECURITY_REGISTRY_V1_1_LIMITED_DESIGN_APPROVAL_RECORD.md) (QP-DEC-SR-REVIEW-003) controls over earlier pending-selection statements: SEL-01–04 approved. Model A (16 logical objects) selected; SR-D02 direction and SR-D06 framework approved within limited scope; T1–T5 design revisions authorized. Final registry schema/interfaces, SR-D03–05, AUTH-D01–07, R01–04 and SG-01–04 remain outstanding. PRE-04 remains open. QP-APR-009 and Development GO remain unissued. Preserve approved business and RPM rules; no implementation or tests authorized.

## Controlling targeted design disposition — 2026-11-27

[Document 34 — Targeted Security Design Approval Record](34_TARGETED_SECURITY_DESIGN_APPROVAL_RECORD.md) (QP-DEC-SR-REVIEW-004) records Owner approval of SEC-T1, SEC-T2, AUTH-D01 (Option A selection only), SEC-T3 and SEC-T4 against exact reviewed commit 6dbeb00d30e415ffdaf098f06bbe1ac097681a4e. Earlier pending-selection statements are historical. Immutable binding/terminal retirement, JCS + SHA-256, per-principal restricted PostgreSQL logins, single-process gateway/fresh transaction and global analytics quarantine directions are accepted within limited scope. Exact attacker/trust model, credential/server attestation, routine privileges, handoff/writer exclusivity, durable quarantine/recovery, authenticated dual approvals, T5, AUTH-D02–07, R01–04 and SG-01–04 remain open. Timing parameters provisional. Final SR-D03–05 and registry/interface acceptance remain pending. No QP-APR-009 or Development GO; no implementation or tests authorized.
