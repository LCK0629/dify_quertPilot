# Security Registry v1.1 — Limited Design Approval Record

**Record ID:** QP-DEC-SR-REVIEW-003  
**Date:** 2026-11-27 (Asia/Singapore)  
**Authority:** Project Owner  
**Disposition:** SEL-01–SEL-04 APPROVED (4/4), limited scope only  
**Registry:** NOT APPROVED | **Development:** NO-GO

## Exact decision baseline

[Document 32 — Security Registry Data Model v1.1](https://github.com/LCK0629/dify_quertPilot/blob/faec078f82a56e34aef8c33b09d6ec4082cf688f/docs/phase-1/32_SECURITY_REGISTRY_DATA_MODEL_V1_1.md), commit `faec078f82a56e34aef8c33b09d6ec4082cf688f`, blob `42a0e1acee3fca20faf00c59d30da82a18880575`; [independent Security review](https://github.com/LCK0629/dify_quertPilot/issues/1#issuecomment-7213623773). Read with controlling review framework [Document 31](31_SECURITY_REVIEW_V1_1_APPROVAL_RECORD.md).

The Project Owner explicitly approved SEL-01, SEL-02, SEL-03 and SEL-04, instructed recording the exact limited-scope disposition in GitHub, preserved M01–M09, OD-01–07 and RPM, and prohibited issuing QP-APR-009 or Development GO. All unselected decisions remain pending.

| ID | Owner-approved scope | Limits |
|---|---|---|
| SEL-01 | Select Model A — 16 logical storage objects | SR-D01 model selection only; final schema/keys and independent DB identity/privilege interfaces require review. Model B is not selected; no further comprehensive A/B comparison required unless material changes arise. |
| SEL-02 | Approve SR-D02 RBAC/M08 design direction | Approved RPM semantics unchanged; canonical integrity, effective union, binding/temporal invariants and independent verification remain required. |
| SEL-03 | Approve SR-D06 security test specification framework | Framework only; QA case oracles, coverage, witnesses and post-GO execution remain outstanding. No test pass inferred. |
| SEL-04 | Authorize targeted T1–T5 revisions and coordinated ADR closure | Design work and review only; no implicit approval of SR-D03–05, AUTH decisions or residual risks. |

## Targeted revisions authorized

| Item | Scope | Accountable roles |
|---|---|---|
| T1 | Immutable DB binding, typed BINDING_RETIRE reference and lifecycle, no reuse, exact cluster identity | DB Engineer |
| T2 | Single canonical serialization, approval/evidence and manifest lifecycle, digest and release linkage | Security + DB |
| T3 | Fresh policy visibility, real-time expiry, shared handoff serialization, direct DB return boundary, durable audit and timeout/crash handling | Security + Backend + DB |
| T4 | Emergency deny/quarantine on audit failure, recovery, audit order and retention | Security + DB |
| T5 | Approved policy mapping, output field allowlist, original test oracles and targeted negative/positive cases | BA + QA + Security |

Detailed requirements remain in the linked independent review; revise Document 32 and existing ADRs rather than duplicate a comprehensive planning pack. Role responsibilities do not establish named engineer assignments or completed work.

## Outstanding gates

- SR-D01 model selection accepted, final schema/interface sign-off pending; SR-D02 direction and SR-D06 framework accepted, remaining validation and exact design sign-off pending. SR-D03–05 pending.
- SEC-SR-01–12 and SR-AC-01–10 remain governed by the independent review dispositions; no blanket closure.
- AUTH-D01–07 and R01–04 remain individually unapproved. Selecting registry Model A does **not** select PostgreSQL authorization Option A.
- SG-01–04 remain open; PRE-04 Issue #1 remains open. Coordinate #2, #3, #4, #5 and #7. Separate independent Security/DB/BA/QA review and exact final registry disposition required.
- Preserve approved M01–M09, MR-01–10, OD-01–07, QP-APR-008 and retail data grain.
- QP-APR-009 and QP-APR-DEV-GO-001 remain unissued. No implementation code, DDL, migrations, fixture generation, live grants, deployment or implementation test execution authorized.

**Next:** targeted T1–T5 revision of existing design and ADR artifacts, followed by independent re-review of changed contracts. No new comprehensive planning document required.
