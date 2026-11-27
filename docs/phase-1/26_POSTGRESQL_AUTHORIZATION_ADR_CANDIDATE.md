# ADR Candidate — PostgreSQL Principal Binding and Restricted Analytics
**Document ID:** QP-SEC-ADR-DBAUTH-001  
**Version:** 0.1 **FOR REVIEW — NOT APPROVED**  
**Date:** 2026-11-27 (Asia/Singapore)  
**Owners:** Security Architect + Database Engineer; supporting Backend Architect / BA  
**Related decisions:** QP-APR-005 (architecture direction), QP-APR-007 (OD policies), QP-APR-008 (role policy); [registry proposal](24_SECURITY_REGISTRY_DATA_MODEL_V1_0.md) and [review](25_SECURITY_REGISTRY_REVIEW_NOTES.md).  
**Gate:** **Development NO-GO**. No login, role, DDL, SECURITY DEFINER function, migration or code has been created.

## 1. Decision question / security invariant

A shared `qp_analytics` DB login together with user-provided `authorized_scope`, `principal_id` or `SET app.principal` is **not** independent DB authorization. A caller controlling SQL arguments or session settings could impersonate another person if the DB treats those values as authority.

**Required invariant:** PostgreSQL must derive a nonforgeable execution identity under a stated trust model, resolve the **current** authorized principal-wide store scopes and metric/capability permissions from protected policy, and expose only fixed aggregate operations. A normal query caller cannot widen scope by changing SQL arguments, GUCs or role claims.

This must be backed by practical negative tests before any approval; merely describing it is insufficient.

## 2. Options considered

| Option | Mechanism | Benefits | Critical drawbacks | Review disposition |
|---|---|---|---|---|
| **A — Per-principal PostgreSQL login + bounded aggregate routines** | Distinct, least-privileged DB login for each synthetic human principal; DB maps protected `session_user` to registry principal; fixed reviewed SECURITY DEFINER aggregate routines independently check *current* policy and scope. | Clear DB-visible identity for small demo; no user-supplied principal/GUC trusted; normal SQL user cannot impersonate other DB login without credential. | Per-principal credentials and pool lifecycle; FastAPI credential routing is a high-value trust boundary; SECURITY DEFINER bugs are serious; not scalable as-is. | **RECOMMENDED FOR LIMITED MVP REVIEW ONLY** |
| **B — Shared restricted login + independently verified signed identity evidence** | DB validates short-lived cryptographic identity/capability proof issued by a **separate protected issuer**, not arbitrarily asserted by FastAPI. | Fewer DB credentials; potential scaling path. | Requires vetted verifier, key rotation/revocation, nonce/expiry and public-key operations; extra dependencies; cannot be considered secure without independent end-to-end proof. | **DEFER** unless A fails accepted requirements |
| **C — Shared login with scope/principal passed as SQL parameter or mutable custom GUC** | `WHERE store_id = ANY(:scope)` or `current_setting('app.principal')`. | Easiest to implement. | Caller-controlled assertion, not independent authority; if compiler/routing fails, DB cannot tell which human is authenticated. | **REJECT AS SOLE DB AUTHORIZATION** |

**No final option is approved.** The review recommendation is to independently assess A for the **small, fictional, offline-first** P0 environment; production architecture could differ.

## 3. Candidate A — bounded design proposal

### A. Identity and credential binding
1. FastAPI authenticates the current synthetic/verified human identity and checks `chat.use` **before** an LLM call.
2. On any authorized analytics request, FastAPI selects a DB connection credential from a **protected server-side mapping** of verified issuer+subject to a dedicated PostgreSQL login. Never accept a username, role, or connection string from browser/LLM.
3. Each database login is `LOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE NOREPLICATION NOBYPASSRLS`, no memberships permitting `SET ROLE` into any other human, owner, migrator, or definer role. Grant no base-table SELECT, CREATE, DML or DDL.
4. In PostgreSQL, a protected registry mapping `db_login_name -> principal_id` must be proposed, reviewed and provisioned separately; login names cannot be changed by browser requests. The current SRDM 15-object design does **not** yet specify this mapping, and must be amended or linked to a protected external identity mapping.
5. The DB derives the caller identity from `session_user` and confirms that principal is active, not suspended, has current policy/grants/role and explicit store scope. Do not derive it from `current_user` **inside SECURITY DEFINER** functions, as `current_user` becomes the function owner.
6. PostgreSQL 17 allows non-superusers to change their `current_user` only through allowed role memberships, while `session_user` ordinarily remains the connecting user. This is a **candidate property to test, not a blanket guarantee of system identity**.
7. A compromise of FastAPI or its credential vault could expose many demo principals; this design protects primarily against forged request/SQL parameters and cross-user privileges through normal restricted DB execution. Secret isolation, rotation, vault access and this residual risk require explicit sign-off.

### B. Database interface and privileges
- **No direct event stream exposed to business principals.** They may execute only a narrow list of reviewed routines corresponding to `kpi`, `rank`, `compare`, and `diagnose` operations, each returning approved aggregate types/evidence. Do **not** grant `analytics.merchandise_events` to ordinary callers.
- Use separate NOLOGIN ownership roles for raw business tables, registry, trusted aggregate routines and migration. Runtime login cannot own or modify trusted code or tables. Definer must not be superuser or `BYPASSRLS`, and should not own base tables that rely on RLS.
- Routines check policy/generation, explicit scope, capability, metric rights, derived disclosure dependencies, OD-06 dimension rules, snapshot `FINAL`/coverage, row limits and time bounds. A requested store outside scope **denies the whole query**, rather than silently intersecting.
- Routines accept typed values only (approved metric IDs, time range, bounded store filters, snapshot IDs). Identifiers and SQL shapes are developer-controlled, never taken from raw LLM SQL. A safe API compiler remains the first boundary, and database routines serve as the independent second.
- SECURITY DEFINER usage demands an explicit safe `search_path`, qualified objects, no unsafe dynamic SQL, a locked-down owner, and revocation of default `PUBLIC EXECUTE` **inside the same deployment transaction**. Review every callable helper and extension.
- RLS may supplement restricted routines; table owners, superusers and `BYPASSRLS` bypass ordinary policies, so FORCE RLS, view ownership, invoker/definer semantics and real privileges must be verified. **Do not assert that RLS alone makes a definer routine safe.**
- Avoid extending the frontend's query evidence with executable/raw SQL. Expose sanitized query template/hash, metric/version, snapshot/coverage, reporting period and approved scope only.

### C. Connection isolation and current-policy rechecks
- P0 demo preference: one authenticated DB session per principal/request or an **isolated pool per database login**. Do not share a pooled authenticated connection across principals; if a pool is introduced, audit checkout/return and ensure no session role/GUC/temp state leaks.
- Use read-only transactions, strict statement timeout, bounded result cardinality, maximum period and concurrency limits as **additional** controls, not authorization.
- Bind the evaluated `policy_generation`, `revocation_sequence`, `principal_id` and authorization expiry to query provenance. Recheck current policy and revocation before emitting evidence or invoking optional narrative model; permission expiry midway suppresses output.
- Clearly state the remaining race: an already-transmitted result cannot be recalled. Security review must decide whether in-flight cancellation/streaming is disabled in P0.
- Synthetic policy snapshot at query time may differ from historical business `data_snapshot`; business as-of never grants historical access rights.

## 4. End-to-end example: Sales Staff denied revenue

**User:** `demo_sales_b` is authenticated; has `chat.use`, `analytics.kpi`, `metric.M06.read`, `evidence.read`, and explicit Store B grant.

**Question:** “What was our net revenue last month?”

1. FastAPI validates `chat.use`; bounded LLM adapter may identify `M04`.
2. FastAPI Stage 2 sees no `metric.M04.read` and **denies before business SQL**; no unauthorized amount reaches model or browser.
3. If a malicious/buggy caller nevertheless invokes the restricted DB routine directly as `qp_demo_sales_b`, the routine independently resolves the authenticated login and denies M04. The caller cannot switch to another principal simply by providing `principal_id=owner` or `store_id=A`.
4. No raw revenue events, component bridges, stack traces or forbidden query patterns are disclosed.

**Other case:** System Admin with only `users.manage` lacks `chat.use` and is rejected at Stage 1 before Dify. Owner must have explicit store grants; role name alone never means all stores.

## 5. Required negative tests (specifications only)

| ID | Scenario | Required outcome |
|---|---|---|
| DBA-01 | Restricted principal connects and queries `retail`, `ingest`, `governance` base tables | Permission denied |
| DBA-02 | Restricted login attempts DDL, INSERT/UPDATE/DELETE, function creation or unsafe extensions | Permission denied |
| DBA-03 | Restricted login attempts `SET ROLE` owner, another user, or function owner | Denied; no broader effective role |
| DBA-04 | Restricted login tries `SET SESSION AUTHORIZATION` to a different principal | Denied |
| DBA-05 | Forged SQL `principal_id`, `store_id`, claimed capability or GUC | Does not widen DB scope |
| DBA-06 | Direct SQL calls a metric routine lacking capability or base dependency | Denied with no amount |
| DBA-07 | Units-only staff requests M04 or raw underlying events | Denied; no bridge leakage |
| DBA-08 | Owner with only Stores A+B asks for Store C | Denied, no partial company-wide aggregate |
| DBA-09 | Definer routine has malicious `search_path`/temp-object shadowing attempt | No privilege escalation or data leak |
| DBA-10 | PUBLIC/unassigned role tries `EXECUTE` or schema CREATE | Denied |
| DBA-11 | Connection reused under wrong human identity; pool/credential cross-contamination | No cross-principal execution possible |
| DBA-12 | Policy revocation after SQL but before response or evidence read | Suppressed pending output; current policy required |
| DBA-13 | Sparse aggregates, differencing and repeated M04/M07/M08/M09 queries | Reviewed inference controls/accepted residual risk |
| DBA-14 | Old business snapshot or stale policy version replayed after revoke | Denied under current authorization |
| DBA-15 | SECURITY DEFINER owner/role inherits BYPASSRLS or base-table ownership accidentally | Privilege review fails; deployment blocked |
| DBA-16 | DB connector holds more privileged credentials than expected | Secret inventory fails; no GO |
| DBA-17 | Missing registry mapping or broken audit/active-policy pointer | Fail closed |
| DBA-18 | Attempt to use direct LLM/Dify DB credentials or a raw-SQL endpoint | Endpoint not available; no credentials exposed |

**Pass criteria:** Independent Security/DB reviewer witnesses real PostgreSQL 17 privilege checks with distinct test connections and raw evidence. No test result claimed in this document.

## 6. Unresolved sign-off decisions

| ID | Approval question | Responsible |
|---|---|---|
| AUTH-D01 | Select A/B/equivalent and the exact attacker/trust model | Security Architect + Project Owner |
| AUTH-D02 | Approve per-principal login lifecycle/mapping and operational credential boundary | Security + DB |
| AUTH-D03 | Approve routine signatures, protected ownership, invocation privileges, and RLS role matrix | Security + DB |
| AUTH-D04 | Approve connection pool policy, transaction isolation, policy/revocation race response | Backend + Security |
| AUTH-D05 | Approve residual sparse/inference/credential-store risk for synthetic MVP | BA + Security + Owner |
| AUTH-D06 | Approve integration with 15-object security registry or authorized simplification | DB + Security + Owner |
| AUTH-D07 | Approve actual negative-test protocol, expected outcomes and evidence | Security + QA |

## 7. Change impact and next step

This ADR deliberately **does not** change approved metrics M01–M09, OD-01–07, role matrix or v1.0 physical data grain. If Option A is approved, the Registry Data Model must add a protected DB-login binding or equivalent and database v1.1 must define roles, `EXECUTE` grants, ownership and safe routines. PRD v1.1 must align sanitized evidence and two-stage authorization. Dify/direct LLM selection remains a separate ADR.

**Decision status: PROPOSED — NO DEVELOPMENT GO.** Do not implement the proposed connection or SECURITY DEFINER design until separately reviewed and authorized.

## PostgreSQL 17 authoritative references
- Row Level Security: https://www.postgresql.org/docs/17/ddl-rowsecurity.html
- Identity and `session_user` vs `current_user`: https://www.postgresql.org/docs/17/functions-info.html
- `SET ROLE`: https://www.postgresql.org/docs/17/sql-set-role.html
- `SET SESSION AUTHORIZATION`: https://www.postgresql.org/docs/17/sql-set-session-authorization.html
- Safe `SECURITY DEFINER` functions: https://www.postgresql.org/docs/17/sql-createfunction.html


## Targeted coordination addendum — SEL-04 / T1–T4

Read [Document 33](33_SECURITY_REGISTRY_V1_1_LIMITED_DESIGN_APPROVAL_RECORD.md) and [Document 32 targeted revision](32_SECURITY_REGISTRY_DATA_MODEL_V1_1.md), sections T1 and targeted addendum. Registry Model A is selected; PostgreSQL Authorization Option A is NOT selected. DB-side recommendations for AUTH-D02/03/04: immutable binding rows, terminal BINDING_RETIRE events, verified deployment epoch and non-reused role identities, fresh dedicated READ COMMITTED gateway transactions, actual wall-clock expiry, network/credential restriction to trusted gateway, bounded shared authorization gate, durable audit before response enqueue, emergency global quarantine if suspension cannot commit. Exact operator/session trust, writer exclusivity, durable quarantine and transport implementation contract require independent Security/Backend design review. No direct external DB clients under this candidate; R01/R02/R04 remain pending. T1 design submitted, not independently accepted; T2–T4 coordinated proposals, not ADR closure. AUTH-D01–07 remain pending, no tests run, Development NO-GO.
