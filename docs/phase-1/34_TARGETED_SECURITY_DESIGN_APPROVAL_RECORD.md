# Targeted Security Design — Project Owner Approval Record

**Record ID:** QP-DEC-SR-REVIEW-004  
**Date:** 2026-11-27 (Asia/Singapore)  
**Authority:** Project Owner  
**Disposition:** Five limited design decisions APPROVED  
**Registry:** NOT APPROVED | **Development:** NO-GO

## Exact baseline
Reviewed commit [6dbeb00d30e415ffdaf098f06bbe1ac097681a4e](https://github.com/LCK0629/dify_quertPilot/commit/6dbeb00d30e415ffdaf098f06bbe1ac097681a4e).
- [Document 32](https://github.com/LCK0629/dify_quertPilot/blob/6dbeb00d30e415ffdaf098f06bbe1ac097681a4e/docs/phase-1/32_SECURITY_REGISTRY_DATA_MODEL_V1_1.md), blob f3611418137e474c7f4d257f5575dcf9b5a174ea.
- [Document 26](https://github.com/LCK0629/dify_quertPilot/blob/6dbeb00d30e415ffdaf098f06bbe1ac097681a4e/docs/phase-1/26_POSTGRESQL_AUTHORIZATION_ADR_CANDIDATE.md), blob 5cb771204292f46e06a136a635a8fb17adbc73cc.
- [Document 33](33_SECURITY_REGISTRY_V1_1_LIMITED_DESIGN_APPROVAL_RECORD.md) remains controlling for SEL-01–04.

## Explicit Owner disposition
| Decision | Approved scope | Remaining conditions |
|---|---|---|
| SEC-T1 | Immutable binding and terminal retirement data-model design | AUTH-D02 server attestation, credential lifecycle operational contract and future tests remain pending |
| SEC-T2 | RFC 8785 JCS + SHA-256 integrity direction | Exact canonical manifest/golden vectors, authenticated reviewer evidence, trust rotation/recovery and approval/release linkage still require review |
| AUTH-D01 | Select PostgreSQL Authorization Option A for bounded synthetic MVP | Exact attacker/trust model and operational boundary remain subject to review; no approval of full ADR or residual risk |
| SEC-T3 | Single-process Gateway and fresh transaction direction | Writer exclusivity, direct DB boundary, shared handoff, crash/expiry semantics remain open; 250ms/1s/1s timing parameters provisional |
| SEC-T4 | Global Analytics Quarantine direction | Durable fail-closed state, restart, operator isolation and recovery design remain pending |

All unselected decisions remain pending. Registry Model A (16 objects) previously selected; PostgreSQL Authorization Option A now selected within stated limits. Neither selection constitutes final registry or database privilege approval.

## Remaining ADR closure — targeted design work only
- AUTH-D01 selection component approved; exact threat model remains open. AUTH-D02–07 remain unapproved.
- AUTH-D02: protected server/epoch attestation, verified session-to-login routing, secret provisioning/rotation and deprovisioning.
- AUTH-D03: exact routine signatures, return allowlist, ownership/privilege matrix, helper and RLS decision, deny direct base access.
- AUTH-D04: single process/writer exclusivity, fresh READ COMMITTED visibility, current wall clock, durable audit before bounded handoff, timeout/crash/restart, no external DB clients.
- AUTH-D05: explicit R01–04 residual-risk dispositions, with BA/Security review; no acceptance inferred.
- AUTH-D06: reconcile selected 16-object registry and exact authorization interfaces with database v1.1.
- AUTH-D07: QA/Security independent oracle and evidence contract, including targeted T1–T5 specifications; execution only after separate GO.
- Identity/session ADR (#3): verified authentication, session/CSRF, independent bootstrap, actual reviewer identity and capacity, manifest rotation/recovery, release and durable quarantine; no simulated dual usernames as proof of human independence.
- T5 BA/QA review remains pending. Preserve M01–M09, OD-01–07, QP-APR-008 and approved retail grain. No new suppression rules.
- SG-01–04, SR-D03–05 and final SR acceptance remain open; QP-APR-009 and QP-APR-DEV-GO-001 unissued.

Next action: complete the exact design contracts in existing Document 26, Document 32 and identity/session ADR under Issues #2/#3, then request separate Owner decisions. This record authorizes design review, not code, DDL, migrations, fixture generation, deployment, grants or executed tests. No security test pass claimed.
