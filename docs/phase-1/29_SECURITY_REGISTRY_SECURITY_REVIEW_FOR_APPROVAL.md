# Security Registry Security Review — For Approval

**Document ID:** QP-SEC-SR-REVIEW-001  
**Version:** 1.0 | **Date:** 2026-11-27 (Asia/Singapore)  
**Reviewing authority:** Security Architect (design review only)  
**Review collaborators:** Database Engineer / Data Architect; BA and Solution Architect for scoped cross-review  
**Decision authority:** Project Owner  
**Security disposition:** **REVISE AND RESUBMIT — SECURITY SIGN-OFF WITHHELD**  
**Owner disposition:** **PENDING — NO SR-D01–SR-D06 OWNER APPROVAL IN THIS DOCUMENT**  
**Development gate:** **NO-GO**; no DDL, migrations, implementation, deployed privilege grants, security tests, or claim of operational compliance.

## 1. Reviewed source-of-truth baseline

Reviewed GitHub main baseline at commit [d158691c8a2267e215b46c918beef5f5632734bc](https://github.com/LCK0629/dify_quertPilot/commit/d158691c8a2267e215b46c918beef5f5632734bc):

| Source | Exact blob SHA | Authority / status |
|---|---|---|
| [24 Security Registry Data Model v1.0](24_SECURITY_REGISTRY_DATA_MODEL_V1_0.md), QP-DE-SRDM-001 | 576c9a3b97ca6bb040e55a51c5c1391eaf9def21 | Candidate only, not approved |
| [25 PM Independent Review Notes](25_SECURITY_REGISTRY_REVIEW_NOTES.md), QP-PM-SR-REVIEW-001 | 2edfe7d617b8b73af4c2a3f6bdc4ee1c9d85d63d | Advisory review, not approval |
| [22 Role & Permission Matrix v1.0](22_ROLE_PERMISSION_MATRIX_V1_0.md) | b5bbe201146f7e3c85e46a73c7278d681bdf9291 | Design controlled by [QP-APR-008](23_ROLE_PERMISSION_APPROVAL_RECORD.md); not deployed |
| [23 Role Approval Record](23_ROLE_PERMISSION_APPROVAL_RECORD.md) | 809793a0f9cbf075f8ae431ef047cde66f13b80d | All six RPM design decisions owner-approved |
| [20 OD Decision Resolution](20_OD_DECISION_RESOLUTION_V1_0.md) / [21 QP-APR-007](21_OD_DECISION_APPROVAL_RECORD.md) | See linked record | Seven OD business/data policy decisions owner-approved |
| [26 PostgreSQL Authorization ADR Candidate](26_POSTGRESQL_AUTHORIZATION_ADR_CANDIDATE.md) | 5172c89c9cf745781d850e96d77acf8108283a3e | Option A recommended for review, not selected or approved |
| [28 Decision Closure Board](28_DECISION_CLOSURE_EXECUTION_BOARD.md) | 80d2a3b0bf9b291ba66cdaaf13fdd4c480701494 | Tracks PRE-04–PRE-10 gates |

Scope includes logical model, declared invariants, role consistency, identities, policy lifecycle, revocation, approvals, audit and negative test *specifications*. This is a document/architecture review. No source-code audit, running PostgreSQL system, infrastructure configuration, penetration test, fixture execution or external user research was available as proof. Hashes above identify reviewed GitHub blobs; they are **not** trusted runtime policy-signing signatures.

## 2. Executive verdict

**The separation of business analytics from access-control policy is supported. The current 15-object implementation candidate is not yet security-approvable.** High-level design is coherent, but the binding of an authenticated person to the effective DB principal remains unresolved; initial reviewer/activator authority is insufficiently specified; effective policy content protection is incomplete; and the concurrency/revocation contract cannot yet be independently verified.

**Recommendation:** Owner may **accept these review findings and request DB revisions** now. Do not record the registry itself as approved, activate an SR design, or issue QP-APR-009 until a revised exact version and independent reviews are presented. Development stays NO-GO even if a later *design* approval is given.

### Severity interpretation

- **BLOCKER / P0:** Cannot approve the security boundary or start implementation until design decisions and trust assumptions are resolved.
- **HIGH / P1:** Material risk of incorrect authorization or unbounded MVP complexity; must be resolved before registry design sign-off unless Owner explicitly documents a constrained, Security-endorsed alternative.
- **MEDIUM / P2:** Requires documented disposition and test/operational requirements before final Development GO.

## 3. Formal review of SR-D01–SR-D06

All entries below are **Security Architect recommendations**, not Project Owner decisions.

| Decision | Security review | Rationale and mandatory revision before sign-off |
|---|---|---|
| **SR-D01 — Separate schema + 15 objects** | **REVISE** | Separate protected security schema is desirable. Fifteen objects are defensible but not demonstrated as minimal. DB Engineer must deliver a control-by-object justification and an explicitly evaluated reduced alternative. Neither count nor physical shape is pre-approved. |
| **SR-D02 — Versioned principal/roles, M08 bases** | **SUPPORT CONDITIONALLY / REVISE** | Aligns with QP-APR-008, including common principal-wide stores, deny precedence and explicit M08 bases. Define immutable catalog semantics, full effective-union/time-bound validation, protected reviewer/service identities and failure on inconsistent grants. |
| **SR-D03 — Sealed snapshots, dual reviews, atomic activation** | **REVISE — P0** | Retain independent Security + Owner review, checksum and serialized activation, but prove trusted signer capacity independent of the reviewed registry; protect canonical policy references and define bootstrap, signing/rejection, conflict and rollback semantics. |
| **SR-D04 — Deny-first temporal grants** | **SUPPORT CONDITIONALLY / REVISE** | Correct principle, but specify trusted current time, inclusive/exclusive interval rules, future-effective transitions, policy/revocation generations and revalidation during a query. Historical business-as-of must never restore historical entitlements. |
| **SR-D05 — Emergency suspension/release and sanitized audit** | **REVISE — P0/P1** | Emergency suspension must take effect on committed revocation independent of policy publication. Define protected revoker, independent release authority, final-response gate, session invalidation, query cancellation/streaming policy, sanitization, retention and recovery. |
| **SR-D06 — Synthetic fixtures SR-01–32** | **SUPPORT AS TEST SPECIFICATIONS ONLY** | Existing scenarios are a useful baseline. Expand/trace to RPM-01–28 and DBA-01–18, plus specific reviewer-authenticity, catalog-tamper, credential/pool, race and audit-abuse cases. Assign test owner/oracle/evidence, without marking any test passed. |

### Role & Permission Matrix consistency verdict

**Policy direction: consistent, subject to the specific gaps below.** The candidate maintains the following QP-APR-008 constraints:

1. The six personas and constrained role templates are not carte-blanche grants; optional permissions require separately controlled templates. System Admin users.manage **does not** imply chat.use, finance, policy activation or audit.read.
2. Every analytics principal, including Owner, requires explicit store IDs. A role name cannot grant all stores; a newly created store is not auto-granted. An explicitly requested unauthorized store makes the *entire request* fail.
3. Multiple roles combine only within a **common principal-wide scope**; explicit DENY wins over ALLOW, including conflicts across roles. A requirement for independent per-role store scopes is rejected at provisioning, not silently flattened.
4. No direct arbitrary per-user metric grant is introduced. A valid analytic response requires chat.use, evidence.read, operation and metric permission, approved semantics and current store scope.
5. M08 requires compare + M08 + an approved base; staff optional M08 base remains **M06 only**; manager defaults apply **M04/M05/M06**. M05/M07 and exactly-three-of-M01–M04 inference controls require validation on the **effective union** across every valid-time segment. M09 and optional gross/refund bridge display remain gated by separate metric/capability grants.
6. No user-facing raw SQL, retail event rows, uncontrolled components, profit/inventory M10, credential values or arbitrary exports. OD-06 semantic bounds and current-policy access to historical snapshots remain unchanged.

**Important interpretive detail:** The approved three-of-four rule concerns *exactly three* of M01, M02, M03, M04 after effective union. It must not be accidentally rewritten as a blanket denial of all four where the approved Owner grant is intentionally complete. Neither this review nor the DB Engineer may change OD-06/RPM rules without formal upstream change control.

## 4. Security findings and required Database Engineer revisions

| Finding | Severity | Evidence / design gap | Mandatory revision / acceptance evidence |
|---|---|---|---|
| **SEC-SR-01 — Nonforgeable DB principal link missing** | **BLOCKER** | principals stores issuer+subject, not the protected mapping from authenticated session to DB execution identity. Document 26 identifies the gap. | Coordinate [Issue #2](https://github.com/LCK0629/dify_quertPilot/issues/2) and [#3](https://github.com/LCK0629/dify_quertPilot/issues/3); choose an explicit trust model and propose secured DB login binding or independently verified evidence. SQL parameters/GUCs cannot be trusted authority. |
| **SEC-SR-02 — Bootstrap and signer authority not independently rooted** | **BLOCKER** | policy_approvals references principal IDs and reviewer_capacity but does not itself establish who independently authenticated, authorized, or initially provisioned the signer. | Describe out-of-band initial trust anchor, signer/verifier/activator identities, independent Owner+Security authorization, non-self-review, beneficiary exclusion, credential rotation, loss/recovery and emergency authority. |
| **SEC-SR-03 — Snapshot/checksum covers insufficiently explicit semantic dependencies** | **HIGH** | Hash of canonical policy rows is proposed; stable roles, permissions, principal kind/identity, template definitions, referenced semantic/output contracts and referenced role matrix may affect meaning without a full protected immutability contract. | List hashed and independently immutable artifacts, encoding/canonicalization version, reference digest/allowed changes and verification points. Catalog and template meaning cannot mutate beneath approved snapshots. |
| **SEC-SR-04 — Activation/revocation concurrency and transport race** | **HIGH** | Serializing DB changes does not itself prove stale app sessions/caches or previously prepared SQL are safe. Already-transmitted results cannot be recalled. | Specify generation capture, expiry, concurrent transaction protocol, cache invalidation/fail-closed behavior, post-query and pre-evidence/narrative reauthorization, session invalidation, cancellation and explicit no-streaming P0 choice or alternative. |
| **SEC-SR-05 — Derived output/sparse-group inference** | **BLOCKER for unrestricted disclosure claim; HIGH for bounded synthetic MVP** | M04/M07/M08/M09, query differencing, sparse cells and combinations can reveal suppressed components or individual information. Three-of-four rule is not complete inference protection. | BA+Security define allowed output groups/filters, repeat-query and small-cohort scenarios, tests and restricted synthetic-only residual risk; deny where policy fails. No claim of full confidentiality or approval for real customer data. |
| **SEC-SR-06 — 15-object necessity and control equivalence unproven** | **HIGH** | Added catalogs, state versions, temporal rows and approval/activation/audit records increase transaction, key and negative-test surface. | DB Engineer provides object ownership, FK/integrity matrix, full-vs-minimal alternative, estimated MVP overhead and one-for-one preservation of mandatory controls. No approval of arbitrary reduction. |
| **SEC-SR-07 — Temporal/version integrity underspecified at enforcement point** | **HIGH** | Cross-version composite FKs are partly specified, but business snapshot/policy snapshot, grant interval, role state, active generation and revocation sequence may be read under inconsistent boundaries. | State trusted time source; half-open window [from, until); full-snapshot joins and stale-parent rejection; all-time-segment effective-set check; runtime fail-closed behavior if pointer, generation or registry reference is missing. |
| **SEC-SR-08 — Audit trust, retention and independent read access** | **MEDIUM** | Append-only grant_audit prohibits payload secrets but retention, separate AUDIT READER, tamper evidence, backup/recovery, correlation integrity and write-failure policy remain undecided. | Define sanitized event taxonomy, trusted actor binding, controlled read, integrity/recovery/retention limits and behavior if mandatory change audit fails. No raw question/amount/token/secret fields. |
| **SEC-SR-09 — Principal lifecycle and service boundaries** | **HIGH** | Exact issuer+subject uniqueness is good but issuer validation, token audience, identity continuity, service-to-human assignment prohibition and DB credential deprovisioning are external. | Identity ADR must cover verified issuer/subject, sessions, rotation, deactivate/reinstate, stale principals, service/migrator/ingest/publisher/analytics separation, and session/pool credential non-reuse. |
| **SEC-SR-10 — Privileged PostgreSQL function/role configuration** | **BLOCKER for actual independent DB authorization** | Option A in document 26 is only a candidate. PostgreSQL ownership, SECURITY DEFINER privilege, search_path, EXECUTE and RLS interactions have not been independently approved or proved. | Independent signed ADR: direct base-table read denied; no SET ROLE/SESSION AUTHORIZATION privilege escalation; safe definer owner/search_path; PUBLIC EXECUTE closed transactionally; no BYPASSRLS; parameter spoof and pooled-login denial plan. |
| **SEC-SR-11 — Narrative/evidence/metadata exfiltration surfaces** | **HIGH** | Checking numeric payload only is insufficient if response labels, evidence, errors, caches, logs or optional Dify egress expose unauthorized fields. | Define one output allowlist bound to current permission, reviewed aggregate provenance, safe error categories, minimal model egress, cache isolation and identical reauthorization on evidence/narrative paths. |
| **SEC-SR-12 — Test identifier and evidence-contract mismatch** | **MEDIUM** | Document 24 cites DBSEC-01–12, while ADR 26 defines DBA-01–18; scenario overlap and responsibilities are not reconciled. | Publish crosswalk of SR-01–32, RPM-01–28, DBSEC-01–12 (where defined), DBA-01–18, expected negative outcomes, responsible independent witness, and future evidence location. Do not assert passed tests. |

### Particularly important authorization example

An authenticated Sales Staff principal with chat.use, evidence.read, analytics.kpi, M06 and Store B scope may ask for units at Store B. Asking for M04 revenue or Store A must be denied. If the browser instead sends a fabricated Owner principal_id or Store A scope, **both FastAPI and the separately designed PostgreSQL boundary must reject expansion**. A role or scope string supplied by the LLM is not identity proof. This example changes no approved business rule.

## 5. Fifteen-object MVP assessment

**Count verified: 15 proposed logical objects**, in five groups:

| Group | Objects | Count | Required property |
|---|---|---:|---|
| Stable catalog | principals, roles, permissions | 3 | Identity/capability meaning; protected mutability |
| Versioned identity and entitlement state | principal_states, role_states, principal_role_assignments, role_permission_grants, principal_store_scopes, role_m08_base_grants | 6 | Explicit version, deny-first, non-overlapping temporal scope, M08 bases |
| Lifecycle and active policy | policy_versions, policy_approvals, policy_activations, active_policy | 4 | Sealed snapshots, independent dual approval, serialized activation |
| Emergency exception | revocation_events | 1 | Immediate deny independently of ordinary publication |
| Forensic record | grant_audit | 1 | Sanitized, append-only accountability |
| **Total** | | **15** | **Count alone does not establish adequacy or necessity** |

**Assessment:** 15 objects are *architecturally explicable*, but **not yet proportionate by demonstrated evidence** for a single-tenant, fictional retail MVP. The prior eight-object concept is not an acceptable shortcut unless missing policy-version, M08, activation, reviewer and revocation controls are restored by a formally equivalent alternative. The proposed per-principal DB-login mapping is **not** one of these 15 and must be represented explicitly, either as a protected additional object or a separately reviewed external mapping.

DB Engineer shall compare:

- **Alternative A — retain 15 + protected identity binding:** strongest conceptual separation/traceability; higher operational burden and more integrity paths.
- **Alternative B — reduced normalized design:** may consolidate low-risk catalog/state records or operational ledgers only if version FKs, immutable meaning, dual review, independent emergency deny, audit and effective rights remain fully equivalent. Provide a row-by-row capability-to-storage mapping, not a claimed table-count target.
- **Alternative C — earlier eight-object proposal as-is:** **not supported**, because cited omitted controls are mandatory under the approved policy direction.

**Security does not currently approve Alternative A or B.** Decision SR-D01 must document the chosen design and explicit equivalence/risk/cost analysis; an added protected DB-login mapping may legitimately make the final object count exceed 15.

## 6. Minimum defensible trust and access contract

A final design must specify an enforceable chain, not only entity tables:

1. A server-validated authentication source yields trusted issuer+subject and binds a current session; no human role or store authority originates in browser input, LLM output or database request parameters.
2. Protected binding maps the verified principal to the DB execution identity under the selected ADR; service identities remain separate from people and cannot inherit interactive business rights.
3. Current active policy generation, unexpired principal/role assignments, explicit store IDs and latest committed suspension state are resolved together. Missing/stale/inconsistent policy state **denies**.
4. FastAPI authorizes chat.use before invoking Dify/direct adapter. It then checks a typed, untrusted intent against approved operation/metric, M08 bases, M09 disclosure, OD-06 semantics, data-snapshot coverage/finality and exact requested store scope.
5. A constrained independent DB boundary repeats protected principal, metric, scope and output checks. It cannot accept caller-asserted principal/store/GUC as sole proof.
6. Before any numeric/evidence/narrative transmission, current grants, revocation, generation and expiry are rechecked; stale requests suppress output and are safely audited. Already-delivered bytes are explicitly out of revocation reach; control streaming/long-running queries accordingly.
7. Policy creation/approval/activation and emergency release are not performed through chat or System Admin users.manage. They require a trusted out-of-band operator/dual-review process.

## 7. Required DB Engineer revision package — no implementation

| Work item | Owner / reviewer | Required design artifact | Links |
|---|---|---|---|
| **DB-R01** | Database Engineer + Security | Revised registry v1.1 showing every object, primary/composite FK, immutability, status, audit and hash coverage; identity-binding relationship | [#1](https://github.com/LCK0629/dify_quertPilot/issues/1), [#5](https://github.com/LCK0629/dify_quertPilot/issues/5) |
| **DB-R02** | Database Engineer + Solution Architect + Security | Full 15-object vs reduced schema comparison with control-equivalence, operational complexity and migration-safe conceptual sequencing | #1, #5 |
| **DB-R03** | Security + DB + Backend | Nonforgeable PostgreSQL authorization ADR, trust/attacker model, role/owner privileges, DB-login mapping, connection isolation, no shared-assertion shortcut | [#2](https://github.com/LCK0629/dify_quertPilot/issues/2) |
| **DB-R04** | Security + Solution Architect + DB | Identity/session/bootstrap/dual-review/revocation/release ADR; emergency-control sequence and transport race | [#3](https://github.com/LCK0629/dify_quertPilot/issues/3) |
| **DB-R05** | BA + Security + DB | Approved-matrix mapping and inference/sparse-output risk register; verify M01–M09, OD-01–07 without changing them | #1, #4 |
| **DB-R06** | QA + DB + Security | Unified scenario traceability (SR/RPM/DBSEC/DBA), expected oracle, evidence format and independent witnesses | [#7](https://github.com/LCK0629/dify_quertPilot/issues/7) |

These are requested future **design deliverables**, not claims that Database Engineer has performed the work, been personally assigned via GitHub, or completed a technical review.

## 8. Acceptance criteria and evidence checklist

The Project Owner can request revisions or approve *a future exact revised design* after this evidence is reviewed. Every requirement below is a design-acceptance requirement unless explicitly marked future implementation evidence.

| Gate | Acceptance criterion | Reviewer / evidence |
|---|---|---|
| **SR-AC-01** | Exact revised file path, Git commit, blob SHA, version and decision list pinned; review findings resolved with links; prior 24/25 preserved as history | Security + Owner |
| **SR-AC-02** | Nonforgeable human/session-to-DB identity mechanism chosen and threat model signed, or registry approval explicitly held pending this blocker; no reliance on caller-supplied GUC/IDs | Security + DB; issue #2 |
| **SR-AC-03** | Independent initial bootstrap, signers, approval capacity, self-review/beneficiary exclusion, version checksum, reject and recovery process documented | Security + Owner; issue #3 |
| **SR-AC-04** | Snapshot canonicalization includes protected semantics/contract version; immutable catalog meaning, composite FKs, interval checks and effective rights evaluated across future changes | DB + Security |
| **SR-AC-05** | Atomic activation/revocation race policy, stale-generation failure, no old-policy replay, session/cancellation/streaming rules, pre-output recheck defined | Security + Backend |
| **SR-AC-06** | Exact approved RPM/OD grant and output semantics retained; no implicit all-store, admin finance, arbitrary profit, M08/M09 dependency bypass or 3-of-4/M05+M07 inference violation | BA + Security |
| **SR-AC-07** | 15-object alternative comparison (or equivalent reduced proposal) approved with identity-mapping footprint and ownership/complexity budget | DB + Security + Owner |
| **SR-AC-08** | Sanitized audit, independent audit reader, event integrity, retention/recovery, log/model egress boundaries and risk treatment specified | Security + Operations/PM |
| **SR-AC-09** | SR-01–32/RPM-01–28/DBA-01–18 scenario crosswalk plus additional negatives for bootstrap/catalog/pool/race, independent oracle and evidence owner | QA + Security + DB; specifications only |
| **SR-AC-10** | Explicit Project Owner disposition for each SR-D01–D06, separate independent Security/DB/BA sign-offs and recorded unresolved risk; no inferred approval from QP-APR-008 | Owner; issue #1 |
| **DEV-GO** | After separate design approval: execute permitted DB/security tests, review actual negative evidence and remaining PRE issues and issue QP-APR-DEV-GO-001 as an independent written decision | Future work only; **NO-GO now** |

**Suggested additional negative cases (not run):** signer credential compromised; reviewer who is also proposed beneficiary; double-activation race; policy checksum stable while permission catalog meaning mutates; principal loses scope while long query runs; suspend → unauthorized release → re-suspend; session pooling wrong DB login; DB definer PUBLIC EXECUTE/search_path escape; old cached narrative after suspension; sparse query differencing; audit writer failure during approval/activation; stale historical data snapshot plus active revoked user. Expect rejection/suppression and sanitized audit, not partial leakage.

## 9. Project Owner decision request

**Review item offered for approval now:** Accept Security Architect's **REVISE & RESUBMIT** finding and direct the Database Engineer to prepare the DB-R01–DB-R06 *design-only* package. This **does not approve** SR-D01–D06 or any PostgreSQL implementation choice.

**Future exact-registry decision:** After the revised registry and cross-reviewed ADRs are available, decide separately for each SR-D01–D06 (APPROVE / REQUEST CHANGES / REJECT); pin exact version/blob/digest and record approval as QP-APR-009 only after explicit Project Owner authorization. A conditional approval must identify exactly what is and is not authorized. Do not auto-close [Issue #1](https://github.com/LCK0629/dify_quertPilot/issues/1) based on this review.

**Current formal state:** SECURITY REVIEW COMPLETE; REGISTRY NOT APPROVED; OWNER RESPONSE PENDING; PRE-04 OPEN; PRE-05 AND PRE-06 BLOCKING; DEVELOPMENT NO-GO. Nothing here changes approved M01–M09, OD-01–07, QP-APR-008 or existing retail business data grain.

## 10. References

- [Registry candidate — Document 24](24_SECURITY_REGISTRY_DATA_MODEL_V1_0.md)
- [PM independent review — Document 25](25_SECURITY_REGISTRY_REVIEW_NOTES.md)
- [Approved Role Matrix — Document 22](22_ROLE_PERMISSION_MATRIX_V1_0.md) and [approval QP-APR-008 — Document 23](23_ROLE_PERMISSION_APPROVAL_RECORD.md)
- [PostgreSQL authorization candidate — Document 26](26_POSTGRESQL_AUTHORIZATION_ADR_CANDIDATE.md)
- [GitHub Issue #1](https://github.com/LCK0629/dify_quertPilot/issues/1), [#2](https://github.com/LCK0629/dify_quertPilot/issues/2), [#3](https://github.com/LCK0629/dify_quertPilot/issues/3), [#5](https://github.com/LCK0629/dify_quertPilot/issues/5)
- [PostgreSQL 17: CREATE FUNCTION / SECURITY DEFINER](https://www.postgresql.org/docs/17/sql-createfunction.html)
- [PostgreSQL 17: Row Security Policies](https://www.postgresql.org/docs/17/ddl-rowsecurity.html)
- [PostgreSQL 17: Session Information](https://www.postgresql.org/docs/17/functions-info.html)
