# Security Registry Data Model v1.0 — Independent Review Notes
**Document ID:** QP-PM-SR-REVIEW-001  
**Review date:** 2026-11-27 (Asia/Singapore)  
**Scope:** Review of [QP-DE-SRDM-001](24_SECURITY_REGISTRY_DATA_MODEL_V1_0.md) against approved [QP-APR-007](21_OD_DECISION_APPROVAL_RECORD.md), [QP-APR-008](23_ROLE_PERMISSION_APPROVAL_RECORD.md), [architecture v1.1](12_SYSTEM_ARCHITECTURE_SECURITY_DESIGN_V1_1.md), and [readiness v1.0](17_DEVELOPMENT_READINESS_IMPLEMENTATION_PLAN_V1_0.md).  
**Disposition:** **REVISE / CONDITIONAL DESIGN REVIEW — NOT APPROVED**. This is a review, not Product Owner approval, Security sign-off, PostgreSQL DDL, or Development GO.

## A. Baseline confirmation
- QP-APR-007 approved seven **business/data policy decisions**, subject to independent verification and implementation gating.
- QP-APR-008 approved the **role, scope, capability, disclosure and provisioning policy direction**, subject to separate identity/DB authorization review.
- QP-DE-SRDM-001 is a **15-object proposal** for persisting the approved policy. It has **no recorded independent approval**.
- Authorization must be rechecked at every request and before returning protected evidence. Audit/history is not an authorization source.

## B. Review of proposed six SR decisions
| ID | Candidate | PM review | Formal decision still needed |
|---|---|---|---|
| SR-D01 | Separate security schema with 15 logical objects | **Support concept, conditional**: isolate policy from retail facts. The 15-object footprint increases implementation/test cost and needs a complexity justification. | Approve full 15-object design or an explicitly verified simplification without reducing controls. |
| SR-D02 | Versioned roles/principal states and explicit M08 base grants | **Recommend retain.** Non-additive M05/M07 and M08 base restrictions must be checked at both provision and runtime. | Verify no privilege expansion through multi-role union, expiration, or future-effective grants. |
| SR-D03 | Immutable full snapshots, independent reviews, atomic activation | **Recommend retain, conditional.** Checksum is not equivalent to proof of trusted reviewer identity. | Specify secure bootstrap, reviewer authentication, collision/serialization rules and who can activate. |
| SR-D04 | Deny-first, temporal grants and validity windows | **Recommend retain.** Use current policy time, not historical reporting time. | Formalize policy resolution across concurrent revocation and in-flight queries. |
| SR-D05 | Emergency suspension, controlled release and sanitized audit | **Recommend retain, conditional.** Cannot guarantee recall of an already transmitted result. | Define session invalidation, cancellation semantics, retention, audit reader separation. |
| SR-D06 | Synthetic fixtures SR-01–32 | **Recommend retain.** Tests are specifications; nothing has been run. | Assign independent reviewers and expected outcomes; include credential/pool isolation tests. |

## C. Findings requiring closure
| Finding | Severity | Why it matters | Required evidence / reviewer |
|---|---|---|---|
| SR-F01 — No verified database principal binding | **BLOCKER** | `principal_id`, SQL parameter, custom GUC or an app-asserted store list cannot independently prove the logged-in human's identity. | Security/DB sign DB-identity ADR, threat model and denial tests. |
| SR-F02 — Registry deployment complexity | High | 15 interdependent objects plus revision/approval/audit flows are substantial for a portfolio MVP. Simplifying without a proof can damage entitlement correctness; overbuilding delays delivery. | Architect/PM compare full registry against a minimal equivalent, preserving approved policy semantics. |
| SR-F03 — Identity-to-DB binding metadata | **BLOCKER** | Existing issuer/subject principal key does not specify how a DB-authenticated execution identity is securely mapped to a principal. | Security/DB select identity design, protected mapping lifecycle and credential rotation. No ad hoc shared impersonation. |
| SR-F04 — Bootstrap authority | **BLOCKER** | A policy cannot safely approve its own first reviewer or grant administrator. | Document out-of-band provisioner and recovery of initial signer identities. |
| SR-F05 — Atomic activation and revocation concurrency | High | A query may run while active policy changes, or a session may be suspended between SQL and response. | Define consistent policy generation, revocation check at result boundary, and in-flight cancellation/denial behavior. |
| SR-F06 — Inference and derived metrics | **BLOCKER** | M04, M07, M08/M09, sparse groups and differencing can reveal information despite field-level denials. | BA/Security test sanctioned output combinations and residual-risk policy; don't claim full inference resistance. |
| SR-F07 — Time and snapshot semantics | High | Historical business snapshots cannot restore obsolete access. | Pin business `snapshot_id` separately from *current* `policy_version` and revocation state; prove replay denial. |
| SR-F08 — Audit retention and recovery | Medium | Immutable audit rows without retention, access, back-up and cleanup rules may accumulate unbounded sensitive metadata. | Security/Operations decide retention, safe redaction, recovery authority and incident review role. |
| SR-F09 — Approval traceability across versions | High | Historical proposal is not approved policy simply because approval refers to related role matrix. | Sign checksum and exact version by Security and Owner; record separate registry approval `QP-APR-009` only after owner decision. |
| SR-F10 — Active-policy failure behavior | High | Missing active pointer, stale cache or partial multi-table writes could silently over-grant. | Fail closed, transactional version activation, no partial grants, mandatory SR-18–20/28 negative scenarios. |

## D. Cross-document consistency decisions
1. Keep **principal-wide explicit store scopes**, even for an Owner. Admin does not automatically receive `chat.use` or financial rights.
2. Keep `chat.use` as Stage 1; LLM-generated intent remains untrusted. Stage 2 checks metrics, capabilities, dependencies, scope, and allowed dimensions.
3. Keep **no raw SQL or row-level transaction data to end users**. Show reviewed query-template provenance and aggregate evidence only; reconcile PRD v1.1 accordingly.
4. Preserve OD-06 semantic restrictions, including product ranking M01–M04/M06 and M05/M07 limits. Refuse ambiguous or forbidden combinations instead of silently intersecting rights.
5. Design success/error response paths to suppress unauthorized information in logs, LLM context and UI, not only the numeric payload.
6. Registry internal audit identities/approval rights are distinct from human business role labels; System Admin cannot self-approve grants.

## E. Review deliverables before registry approval
- [ ] Exact 15-object schema count, fields, keys, version FKs and migration strategy accepted or justified simplification signed.
- [ ] Owner + independent Security approve six SR-D decisions with a checksum-linked review record.
- [ ] Identity/session threat model, bootstrap and revocation semantics signed separately.
- [ ] DB authorization ADR proves nonforgeable scope to a bounded trust model; `session_user` vs `current_user` behavior reviewed.
- [ ] Mandatory SR-01–32, RPM-01–28, DBSEC-01–12 negative test specifications mapped to owners and expected evidence.
- [ ] Explicit disclosure/inference residual risks accepted or mitigated.
- [ ] Full PRD v1.1 and physical DB v1.1 references reconciled, without rewriting approved M01–M09 or OD rules.

## F. Project Manager conclusion
**The security-registry design is structurally credible but is not yet an implementation-ready authorization system.** Recommend a conditional design review rather than blanket approval. No owner approval is inferred; no DDL, code, tests or deployment is authorized. The next technical deliverable is a PostgreSQL nonforgeable authorization ADR (proposal only).

## Authoritative references
- PostgreSQL 17 row security: https://www.postgresql.org/docs/17/ddl-rowsecurity.html
- PostgreSQL 17 role/session identity: https://www.postgresql.org/docs/17/functions-info.html
- PostgreSQL 17 SET ROLE: https://www.postgresql.org/docs/17/sql-set-role.html
- PostgreSQL 17 secure function design: https://www.postgresql.org/docs/17/sql-createfunction.html
