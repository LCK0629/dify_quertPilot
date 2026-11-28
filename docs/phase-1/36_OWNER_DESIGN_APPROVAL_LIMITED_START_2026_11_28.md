# QueryPilot AI — Owner Design Approval and Limited Engineering Start

**Record ID:** QP-DEC-2026-11-28-001  
**Date:** 2026-11-28 (Asia/Singapore)  
**Decision authority:** Project Owner  
**Evidence:** In the active QueryPilot AI project conversation, the Owner instructed: **“全部批准并且开始”** (“Approve all and start”).  
**Controlling baseline:** GitHub `main` at `4b2bcd4cae8743942d52c92f14187c1da253a43c` immediately before recording this decision.

## 1. Exact design submissions covered

| Document | Exact blob SHA | Owner disposition |
|---|---|---|
| [26 — PostgreSQL Authorization ADR v1.0](26_POSTGRESQL_AUTHORIZATION_ADR_CANDIDATE.md) | `46619655da72c03149d8cfb8dbff04b5085cba9e` | **Owner approves its AUTH-D02–AUTH-D07 recommended design direction and AUTH-D01 trust assumptions**, subject to independent verification of the actual contracts |
| [35 — Identity, Session & Trusted Approval ADR v1.0](35_IDENTITY_SESSION_TRUSTED_APPROVAL_ADR_V1_0.md) | `330afc813db94f900b9d441ff6d64c03a38cad02` | **Owner approves ID-D01–ID-D07 proposed design direction and companion SR-D03–SR-D05 policy proposals**, subject to independent cross-review |
| [32 — Security Registry Data Model v1.1](32_SECURITY_REGISTRY_DATA_MODEL_V1_1.md) | `1d3437208708aba716bbfbf65ebbe1540b557bf4` | The **already selected** 16-object Model A remains the design baseline; targeted T1–T4 directions remain; T5 detailed oracles still require BA/QA review |
| [34 — Targeted Security Design Approval](34_TARGETED_SECURITY_DESIGN_APPROVAL_RECORD.md) | `b17b7c1cf6e3961bcbda00922d3212390d7e7d8f` | Existing earlier Owner approvals preserved (AUTH-D01 Option A, SEC-T1–T4) |

**Decision interpretation:** This is an explicit Owner-level approval of the **design recommendations currently submitted**, not a factual attestation that separate reviewers performed an independent review, credential handling is secure in a running system, or security tests passed. Timing constants in ADRs remain initial candidate values until measured. Nothing here changes M01–M09, MR-01–10, OD-01–07, approved RPM or the approved retail data grain.

## 2. Residual risks and acceptance boundaries

The Owner's general approval advances design planning for the **locally bounded, single-process, synthetic-only** MVP and the proposed mitigations for R01–R04:

- **R01:** Trusted gateway/credential-store compromise could defeat isolation; cannot call this zero-risk or production-grade.
- **R02:** Previously transmitted bytes cannot be recalled following revocation; no streaming or shared cached answers.
- **R03:** Statistical inference from approved aggregates remains possible; do not claim full protection for real data.
- **R04:** Privileged host/DB administrator tampering is outside the bounded demo trust model; auditable controls do not make it tamper-proof.

**Remaining required evidence:** Security Architect must document individual residual-risk statements with BA/DB/Backend review; Owner's broad instruction is not evidence that the risk mitigations were exercised or the controls independently tested. Release acceptance remains separate.

## 3. Limited start authorization — scope of work

The Owner also requested that work **start now**. To honor this without bypassing unresolved hard security prerequisites, begin **S1 Engineering Foundation in an isolated feature branch**:

**Allowed immediately:**
- Create project layout, FastAPI health endpoint, deterministic fail-closed analytics stub, local-only development setup documentation, unit tests/CI scaffolding, and GitHub branch review.
- Run offline **scaffold-only unit tests** that cannot access business data or external model services.
- Prepare independent design review comments and implementation plans for auth/identity/DB **without running migrations**.

**Not yet authorized as a general Development GO:**
- PostgreSQL DDL/migrations, real data generation/ingestion, user provisioning, DB authentication and privilege routines, SQL query execution endpoints, Dify/LLM tool integration, React business dashboards, public hosting or deploying production credentials.
- Claiming any independent Security/DB/BA/QA sign-offs or passing integration/security benchmarks without test evidence.

**Gate status:** `LIMITED S1 FOUNDATION START AUTHORIZED`; **Full Development GO / QP-APR-DEV-GO-001 NOT ISSUED**. This distinction is an explicit scope-limited record under the Owner's new instruction, not a retroactive claim that G-01–G-17 passed.

## 4. Pending tracked closure

1. Issues [#2](https://github.com/LCK0629/dify_quertPilot/issues/2) and [#3](https://github.com/LCK0629/dify_quertPilot/issues/3): independent DB/Backend/BA/QA review of exact ADR v1.0 interfaces and tests; Security to reconcile; no false signoffs.
2. [#1](https://github.com/LCK0629/dify_quertPilot/issues/1) and [#5](https://github.com/LCK0629/dify_quertPilot/issues/5): finalize 16-object Registry Model A and physical DB v1.1 consistency, with exact keys, grants, provenance and output contracts.
3. [#4](https://github.com/LCK0629/dify_quertPilot/issues/4): PRD v1.1 acceptance and T5 BA/QA review; [#6](https://github.com/LCK0629/dify_quertPilot/issues/6) Dify/direct ADR; [#8](https://github.com/LCK0629/dify_quertPilot/issues/8) research evidence or explicit limitations.
4. [#9](https://github.com/LCK0629/dify_quertPilot/issues/9): separate GO/NO-GO for implementation of trusted DB/data-access path and later release acceptance.

**Next evidence:** feature branch with code-free-of-data and reproducible local test results; do not merge security-critical changes without review.
