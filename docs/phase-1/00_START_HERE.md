# QueryPilot AI — Phase 1 Planning Pack

**Current status:** 2026-11-26 | Phase 1 — Pre-Development / Decision Closure | **Development NO-GO**

QueryPilot AI is a secure retail-focused natural-language analytics workbench. The objective is authorized, reproducible analytics, not arbitrary generated SQL.

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
| [24 Security Registry Data Model](24_SECURITY_REGISTRY_DATA_MODEL_V1_0.md) | FOR APPROVAL; current review task |
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
3. Review document 24 Security Registry Data Model (current task); then identity/session and nonforgeable PostgreSQL authorization ADRs.
4. Review consolidated database v1.1 amendments and Dify/direct adapter/provider decisions.
5. Reconcile PRD v1.1, evaluation contract, user/competitor research evidence or explicit risk acceptance, and all remaining PRE-01–PRE-10 conditions.
6. Obtain separate written Development GO (G-01–G-17). QP-APR-DEV-GO-001 is reserved, not issued.

## Guardrails and evidence

- Read-only, authorized, bounded database access; no unrestricted LLM SQL.
- Current permissions govern historical snapshot access; raw data and component disclosure require separate authorization.
- Numerical contributions are not proof of causality; unknown data is not zero.
- User interviews and hands-on competitor benchmarks are not evidenced as completed. Tests remain specifications, not executed results.
- No DDL, dataset generation, coding or deployment is authorized. This index does not approve any proposed rules or imply a working product.
