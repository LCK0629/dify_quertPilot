# QueryPilot AI — Development Readiness & Implementation Plan v1.0

**Document ID:** QP-PM-DRIP-001  
**Version:** 1.0 — FOR APPROVAL  
**Prepared:** 26 November 2026 (Asia/Singapore)  
**Accountable owner:** Senior Technical Project Manager  
**Contributors/reviewers:** Solution Architect, Security Architect, Database Engineer / Data Architect, Business Analyst  
**Approver:** Project Owner  
**Implementation gate:** **NO-GO / NOT AUTHORIZED**  
**Proposed GitHub location:** `docs/phase-1/17_DEVELOPMENT_READINESS_IMPLEMENTATION_PLAN_V1_0.md` (not committed)

> **Decision boundary.** Approval of *this plan* would authorize the planning baseline and closure work only. It must **not** be interpreted as permission to write DDL, generate/publish datasets, implement an API, connect Dify to data, deploy, or declare tests passed. A separate signed Development GO record is mandatory.

## 1. Executive decision brief

**Overall finding: NOT DEVELOPMENT-READY.** Five MVP product decisions, the M01–M09 metric baseline, conceptual data model and physical database design have been approved as design baselines. System Architecture & Security Design v1.1 is **approved with conditions** under QP-APR-005. The consolidated PRD v1.0 has not received full sign-off. OD-01–OD-07, role/capability permissions, security-registry persistence, nonforgeable database scope binding, deployment/AI choices and evidence gates remain unresolved.

The approved solution direction is a **modular FastAPI monolith** that owns authentication, fine-grained authorization, deterministic SQL compilation, execution, result verification and evidence. **Dify is an optional replaceable intent adapter**, not a source of authority. React supplies a shared chatbot for authorized Owner, Manager, Analyst and Staff audiences; PostgreSQL holds fictional NovaMart retail data and governed analytics. The LLM cannot execute SQL or confer rights.

### 1.1 Baseline register and approval interpretation

| Ref | Baseline / evidence | Interpretation as of 26 Nov 2026 | Next action |
|---|---|---|---|
| PD-01–05 | Five MVP product decisions; `11_PRODUCT_DECISION_RECORD.md` | **Approved direction** (not full PRD) | Carry into PRD v1.1 |
| QP-BA-BMD-001 | Business Metric Dictionary M01–M09 / MR-01–10 | **Approved business baseline**, subject to independent BA validation and OD resolutions | BA reconfirm edge fixtures and matrix |
| QP-APR-003 | `14_CONCEPTUAL_ERD_DATA_MODEL_V1_0.md` | **Approved conceptual design baseline** | Do not alter grain without change control |
| QP-APR-004 | `15_PHYSICAL_DATABASE_DESIGN_V1_0.md` | **Approved physical design baseline with implementation conditions** | Security and BA gate |
| QP-APR-005 | `13_ARCHITECTURE_APPROVAL_RECORD.md` / architecture v1.1 | **Approved with conditions** | Close identity, permissions, DB scope and adapter ADRs |
| PRD-1 | `09_PRD_V1_0_DRAFT.md` | **Draft; not signed off in full** | Reconcile and obtain written approval |
| OD-01–07 | Architecture §13 and DB approval record | **All open; no silent closure** | Seven signed dispositions |
| RESEARCH | `01_RESEARCH_AND_USER_VALIDATION.md` | Desk research prepared; hands-on tests and user validation outstanding | Gather evidence or explicit risk acceptance |
| EVAL | `05_EVALUATION_AND_TEST_PLAN.md`, `07_TEST_SCENARIO_CATALOG.md` | Test specifications only; **not executed** | Freeze benchmark, fixtures and scoring |
| GATE | This document | **FOR APPROVAL** | Separate GO/NO-GO decision after all P0 evidence |

*Source-of-truth rule:* Use later dated approval **records** to interpret approval; do not silently relabel older review candidates. GitHub technical summaries are not guaranteed to be byte-identical to earlier Word review candidates.

## 2. PRD-to-design consistency review

Use the revised PRD as a **single implementable contract**, with linked metric/permission/response schemas. No item below constitutes an unapproved alteration of the business baseline.

| ID | Gap / inconsistency | Required disposition before GO | Owner | Status |
|---|---|---|---|---|
| ALIGN-01 | PRD persona list omits the new multi-role Staff/Inventory Staff/System Admin behavior defined in architecture v1.1 | Revise users and journeys: one chatbot, explicit `chat.use`, separate capability/metric/store grants; no implicit Owner or Admin super-access | PM + BA + Security | OPEN |
| ALIGN-02 | PRD and research suggest exposing executed SQL; architecture v1.1 forbids returning raw SQL | Specify sanitized evidence: query template ID/hash, approved metric version, scope, dates, snapshot, `data_as_of`, and safe lineage; raw SQL only in protected developer audit where approved | PM + Security | OPEN |
| ALIGN-03 | PRD describes role scope broadly; physical interface accepts a scope argument that is **not** proof of authorization | Require protected principal-to-store binding at the database boundary; select and test a concrete mechanism before DDL/API code | Security + DB | BLOCKER |
| ALIGN-04 | PRD offers ranking/grouping by category/product; M05 counts and M07 AOV are non-additive or risky at certain grains | Approve metric × intent × dimension × filter matrix, aggregate grain and tie behavior under OD-06 | BA + DB | BLOCKER |
| ALIGN-05 | Derived M04/M07/M08/M09 values can reveal component metrics across roles | Sign off dependency and **disclosure** matrix; internal calculations do not imply permission to display gross/discount/refund bridge | Security + BA | BLOCKER |
| ALIGN-06 | PRD last-month diagnostic may be asked for a month absent from the Jan 2024–Oct 2026 demo data | Resolve last **real** completed Singapore calendar month; return `insufficient_data` rather than silently substituting latest dataset month | BA + PM | OPEN |
| ALIGN-07 | Incomplete/provisional snapshot and published late corrections may change an apparently fixed answer | Introduce coverage/finality/restatement contract, immutable snapshot identification and freshness message under OD-03/07 | BA + DB | BLOCKER |
| ALIGN-08 | Product decision D5 approved typed intents, not a specific Dify deployment/provider | Retain `IntentAdapter`; record Dify vs direct API benchmark, data egress and license ADR separately | Architect + AI | OPEN |
| ALIGN-09 | PRD evidence/privacy and auth flows do not yet fully define reauthorization of multi-turn follow-ups and evidence retrieval | Reauthorize **every** turn, retrieval and export; stale policy invalidates old access; avoid shared answer caches | Security + Backend | BLOCKER |
| ALIGN-10 | 'Profit this month' could be mistaken for net merchandise revenue | Explicitly unsupported: no verified COGS/cost data; never relabel M04 as profit. Staff may use chatbot for permitted unit/sales tasks | BA + PM | OPEN |
| ALIGN-11 | PRD KPI source contract and approved physical revision/snapshot design require exact shared date and version semantics | Freeze `[start,end)` SGT, cents arithmetic, historical store/category-at-sale, refund confirmation dates, `M04=M01-M02-M03`, and M07 before later refunds | BA + DB | CHECK |
| ALIGN-12 | P1 inventory/history, Chinese NLP and enterprise multi-tenant functions could creep into P0 | Keep inventory, persistent history, Chinese NL parsing, forecasting, causal claims, real PII and arbitrary SQL outside P0 | PM | CHECK |

**Required PRD sign-off package:** PRD v1.1 change matrix, user-role journeys, permission/dependency matrix, outcome/response schema, scope exclusions, freshness/finality labels, and explicit Product Owner acceptance. Existing approved metric arithmetic must be preserved, unless a documented change request is approved by the owning authority.

## 3. OD-01–OD-07: formal decisions and blocking register

**All statuses remain OPEN.** The actions below are recommended dispositions, not approvals. Each decision needs a written choice, rationale, authority, impacted documents, golden negative cases and a versioned decision record.

| ID | Decision / risk | PM recommended disposition | Responsible decision owner | Closure evidence / acceptance |
|---|---|---|---|---|
| **OD-01** | Completed-order **non-refund correction** after sale recognition may change amount, units and order count | Quarantine and preserve event history; do not silently rewrite completed sales or publish dependent affected analysis. Define whether any correction event type enters P0 | BA + Project Owner; DB review | Written correction policy, exception status, example with expected M01/M05/M06 effect, AT negative tests |
| **OD-02** | Header + line discount or allocation exceeds eligible sale amount | Reject affected publication and retain rejection evidence; never silently cap or redistribute beyond eligible gross | BA + Project Owner | Cent-level allocation examples, upper bounds, rejection and no-leakage integration tests |
| **OD-03** | When does provisional data become **FINAL**, and what is acceptable coverage? | Require expected feed/store/channel/date matrix, source reconciliation, watermarks and published finality; unknown/missing is not numeric zero | BA + Data Architect | Finality policy and definition of COMPLETE_ZERO / INCOMPLETE / UNKNOWN; controlled missing-feed tests |
| **OD-04** | Does a monetary refund reversal restore previously refundable units? | Monetary reversal **does not automatically restore returned quantity** in P0; use separate approved state transition if ever supported | BA + Project Owner | Unit-bound policy, partial-refund/reversal fixture and prefix-cap tests |
| **OD-05** | Immutable business versions and consistent as-of snapshot retrieval | Maintain stable identity keys, append-only revision tables, publication sequence, snapshot cutoff, reproducible historical lookups; validate implementation implications | Data Architect + Project Owner | Version-selection specification, late-arrival test, old-snapshot checksum stability |
| **OD-06** | Safe metric/dimension combinations, especially category/product AOV and order counts | Deny unapproved metric × function × dimension × scope combinations; restrict product/category AOV until documented grain and counting semantics prove safe | BA + Project Owner; Security review | Signed allowlist table, policy fixtures, unauthorized and misleading-slice rejection tests |
| **OD-07** | Freshness SLA, scheduled publication, late-data restatement disclosure | Proposed daily 06:00 Singapore refresh is a **candidate**, not approved. Every answer must show snapshot `data_as_of` and stale/late-restated state; define stale threshold and disclosure text | PM + BA + Project Owner | Freshness policy, UX labels, as-of/restatement tests and publication schedule decision |

**Cross-dependencies:** OD-03 ↔ OD-07 control whether results are truthfully publishable; OD-01/02/04/05 govern event correctness and revisions; OD-06 controls authorization and semantic query safety. Treat these as **P0 gate blockers**, not post-launch polish. If a case is deliberately excluded from MVP, the signed exclusion must define quarantine/refusal behavior and tests; saying “defer” without containment does not close it.

## 4. Authorization and database security approval package

### 4.1 Shared chatbot with two-stage protection

```mermaid
flowchart TD
    U[Authenticated user / React chat] --> F[FastAPI session verification]
    F --> G1{Stage 1: chat.use?}
    G1 -->|No| X[Safe denial - no LLM or SQL]
    G1 -->|Yes| A[IntentAdapter: Dify or direct LLM]
    A --> I[Untrusted typed IntentCandidate]
    I --> G2{Stage 2: capability + metric + dependencies + store + snapshot?}
    G2 -->|No| Y[Denied / clarify / unsupported - no SQL]
    G2 -->|Yes| C[Reviewed deterministic SQL compiler]
    C --> DB[Restricted PostgreSQL authorization boundary]
    DB --> V[Coverage + exact-metric reconciliation]
    V --> R[Evidence-grounded response and visualization]
```

**Clarification of the two checks:** A principal without `chat.use` is denied *before* Dify. A principal with chatbot access but without a requested metric is denied **before SQL** after typed intent is identified; Dify may have been called. A narrowly defined deterministic prefilter can skip Dify for recognized unsupported or prohibited capabilities, but cannot replace Stage 2 authorization. Do not claim “Dify was not invoked” unless a request trace proves it.

### 4.2 Candidate roles and entitlements — NOT YET APPROVED

| Persona | Chat permission | Example P0 business access | Boundary |
|---|---|---|---|
| Business Owner | Explicit `chat.use` | Approved functions/M01–M09 and explicitly granted stores | Owner title does **not** imply all-store grant |
| Store Manager | Explicit `chat.use` | Authorized KPIs, rank/compare for assigned stores only | No cross-store aggregations |
| Sales Staff | Explicit `chat.use` | Potentially M06 sold units for assigned stores | No finance metrics or diagnose by default |
| Inventory Staff | If explicitly granted | Optional M06; inventory unavailable in P0 | No inventory answer or inference |
| Data Analyst | Explicit `chat.use` | Individually granted metric/function/store scope | Analyst title is not superuser |
| System Admin | Separate `users.manage` | Chat/analytics only if separately granted | Admin authority ≠ financial disclosure |
| Service identities | No interactive chat | Separate ingestion, publication, migration and analytics privileges | Not business users |

**Policy catalog (proposed):** `chat.use`, `analytics.kpi`, `analytics.rank`, `analytics.compare`, `analytics.diagnose`, `metric.M01.read`…`metric.M09.read`, `users.manage`, explicit store-scope associations, grant expiry and `policy_version`. Deny by default; capabilities may be enabled only after scope and dependency checks. For M04, an authorized net figure may be computed from M01–M03 without disclosing those three separately; a visible bridge exposing the components requires separate disclosure permission.

### 4.3 Security-registry data model — proposed extension, not approved DDL

| Logical object | Minimum fields / purpose | Constraint |
|---|---|---|
| `security_principals` | `principal_id`, external IdP subject, active state | Subject unique; no client-supplied principal ID trusted |
| `security_roles` | Role ID, label, active | Stable IDs; titles confer no automatic rights |
| `security_permissions` | Permission ID, capability/metric identifier, status | Allowlist; explicit taxonomy and version |
| `principal_role_assignments` | Principal, role, effective/expiry, grant source | Temporal and auditable; no orphan grants |
| `role_permission_grants` | Role, permission, granted/denied, policy version | Explicit override semantics to be approved |
| `principal_store_scopes` | Principal/role, store ID, effective/expiry | No wildcard without explicit owner permission policy |
| `security_policy_versions` | Version, active_from, signer, checksum | Immutable approval chain; avoid policy drift |
| `security_grant_audit` | Actor, before/after, purpose, time, request ID | Append-only, sanitized, access-controlled |

These objects belong to a **separate security authorization boundary**, not the retail metric fact model; precise schema placement and migration must be approved. Retain least-privilege separation between identity administration and business query execution.

### 4.4 Nonforgeable database scope binding — HARD BLOCKER

The approved physical proposal `analytics.merchandise_events(snapshot_id, authorized_scope, start_at, end_at)` **cannot safely trust `authorized_scope` merely because FastAPI supplied it**. A shared `qp_analytics` login alone does not represent each human principal within PostgreSQL.

A **Security Architecture Decision Record** must select and prove one of these, or an equivalent reviewed design:

- **Option A — DB identity/RLS:** a verifiably principal- or tenant-bound database execution identity, RLS that cannot be bypassed by the query role, and a demonstrated session/connection-pool isolation lifecycle. Must prove arbitrary `SET ROLE`, custom GUC spoofing and privileged-owner paths cannot widen stores.
- **Option B — constrained database authorization routine:** a narrowly granted, reviewed database routine that resolves allowed stores from independently protected identity/grant context; caller-controlled store lists and plain principal parameters are **not** authoritative. Any signed token approach requires a separately protected issuer and verification, nonce/expiry/version checks, secret isolation, and explicit threat acceptance.

**Do not mistake a role name, session variable, arbitrary store-array argument, or read-only transaction for database authorization.** Until the choice and its bypass resistance are reviewed and tested, the DB interface and API are not implementation-ready.

**Minimum security controls:** OIDC/BFF or specifically approved local-demo identity, server-held session, CSRF/TLS/origin policy, `qp_analytics` non-owner/non-`BYPASSRLS`, no base-table read or DML grants, revoke PUBLIC routine privileges, fixed `search_path`, reviewed `SECURITY DEFINER` ownership, parameterized values, allowlisted identifiers, query timeout/row/date/concurrency caps, per-turn reauthorization, sanitized audit, restricted model egress, and no direct DB/Dify browser credentials.

## 5. Development roadmap and dependency graph

This is a **dependency-ordered forecast, not a scheduled start date**. Relative weeks begin only after written Development GO; pre-GO decision closure is unscheduled and does not include coding.

```mermaid
flowchart LR
    P[Gate 0: approve PRD, OD, auth, safety, evaluation] --> S1[S1: repo/CI/env]
    S1 --> S2[S2: PostgreSQL + snapshots + goldens]
    S2 --> S3[S3: secure FastAPI + governed SQL]
    S3 --> S4[S4: IntentAdapter + Dify evaluation]
    S3 --> S5[S5: React workbench]
    S4 --> S6[S6: integration + evaluation]
    S5 --> S6
    S6 --> S7[S7: deployment + portfolio evidence]
```

| Stage | Relative sequence / estimate | Key deliverables | Exit dependency |
|---|---|---|---|
| **G0 — Pre-development closure** | Before Week 1; duration unknown | Signed PRD v1.1, OD records, permissions + DB security ADR, AI/provider ADR, approved test contract and research disposition | **Separate written GO** |
| **S1 — Engineering foundation** | Week 1 (illustrative) | Proposed monorepo, CI, lint/test hooks, local Compose, secret policy, health checks | G0 |
| **S2 — Database first** | Weeks 2–3 | Versioned migrations, roles, synthetic fixtures, snapshot publishing, metric SQL, DB negative tests | S1 + DB ADR |
| **S3 — Governed backend** | Weeks 3–4 | Session auth, capability evaluator, immutable query templates, execution limits, evidence & audit API | S2 security and metric reference pass |
| **S4 — AI adapter** | Week 5 | Intent schema, direct baseline, Dify or direct adapter, strict parser, prompt-injection evaluation | S3 safe non-LLM baseline |
| **S5 — React workbench** | Weeks 5–6 | Shared chat, denied/clarify/insufficient states, KPI/charts, safe evidence, accessibility | Stable S3 response contract |
| **S6 — System verification** | Weeks 7–8 | 60 + 20 + 50 catalog runs, AT-01–26/RR-01–12, security review, usability and benchmark report | S2–S5 complete |
| **S7 — Demo/release hardening** | Week 9, conditional | Private deployment, tested backup restore, reproducible demo, docs, limitations | Signed Release GO |

*Estimates are planning assumptions for a small/portfolio implementation, not commitments or evidence that work has started. S4 and S5 may overlap only after S3 contracts are stable.*

## 6. Prioritized technical backlog

Statuses in this table are planning statuses; implementation tasks are **NOT AUTHORIZED** until G0. P0 tasks are release-critical. Owners represent roles, not assigned individuals.

| ID | Priority | Deliverable / acceptance summary | Depends on | Owner | State |
|---|---|---|---|---|---|
| PRE-01 | P0 | PRD v1.1 reconciliation; all ALIGN-01–12 disposed and signed | Existing PRD, architecture | PM/BA | OPEN |
| PRE-02 | P0 | Seven OD decisions signed with test fixtures and change impact | Existing DB & metric baselines | BA/DB/PO | OPEN |
| PRE-03 | P0 | Role × action × metric × dependency × store scope matrix; no implicit admin/owner grants | PRE-01 | Security/BA | OPEN |
| PRE-04 | P0 | Security-registry persistence/approval protocol and authorization ADR | PRE-03 | Security/DB | OPEN |
| PRE-05 | P0 | DB nonforgeable scope-binding prototype/spec and bypass threat review | PRE-04 | Security/DB | **BLOCKER** |
| PRE-06 | P0 | OIDC/demo identity, CSRF, session, data egress and secrets decisions | PRE-04 | Security/Architect | OPEN |
| PRE-07 | P0 | IntentAdapter / Dify vs direct provider ADR, licensing/egress/cost cap | PRE-01, PRE-06 | Architect/AI | OPEN |
| PRE-08 | P0 | Reference-fixture manifest, 60/20/50 rubric, AT/RR and thresholds approved | PRE-02, PRE-03 | BA/QA | OPEN |
| PRE-09 | P0 | 3–5 user interviews and 2 × 15-question trials OR explicit limitations/risk acceptance | Research plan | PM/PO | OPEN |
| PRE-10 | P0 | Readiness evidence index, security sign-off and explicit GO/NO-GO record | PRE-01–09 | PM/PO | NO-GO |
| ENG-01 | P0 | CI, lockfiles, Compose network isolation, sample env, no checked-in secrets | PRE-10 | DevOps/Backend | NOT AUTHORIZED |
| DB-01 | P0 | Migrations and restricted DB roles; permission/negative tests | ENG-01, PRE-05 | DB/Security | NOT AUTHORIZED |
| DB-02 | P0 | Deterministic synthetic 120k orders/300k lines; separate golden/invalid/temporal sets | DB-01, PRE-08 | DB | NOT AUTHORIZED |
| DB-03 | P0 | Immutable batch/snapshot/coverage; exact metric reconciliation M01–M09 | DB-02, OD-03/05/07 | DB/BA | NOT AUTHORIZED |
| API-01 | P0 | Secure session + two-stage authorization, per-turn revocation and audit | DB-01, PRE-03/05/06 | Backend/Security | NOT AUTHORIZED |
| API-02 | P0 | Typed intent validation, SQL template compiler, limits, safe errors/evidence | API-01, DB-03 | Backend | NOT AUTHORIZED |
| AI-01 | P0 | Deterministic B0 benchmark and bounded IntentAdapter with schema validation | API-02, PRE-07 | AI | NOT AUTHORIZED |
| UI-01 | P0 | React chatbot and six response states, scope-aware evidence & charts | API-02, PRE-01 | Frontend | NOT AUTHORIZED |
| QA-01 | P0 | Run reference, integration, 50 security and regression suites; preserve raw artifacts | DB-03, API-02, AI-01, UI-01 | QA/Security | NOT AUTHORIZED |
| OPS-01 | P0 | Private demo deployment, backup/restore, runbook, release gate | QA-01 | DevOps/PM | NOT AUTHORIZED |
| P1-01 | P1 | Inventory, persistence/history, Chinese NLP after separate evidence | Release GO/change review | Product/Eng | DEFERRED |

**Definition of Ready (DoR) for any implementation ticket:** approved source ADR/PRD version; documented negative and positive examples; accessible synthetic fixture and expected result; named reviewer; permission boundary; testable completion; no unresolved upstream P0 dependency. **Definition of Done (DoD):** reviewed PR, tests with linked artifacts, no privilege regressions, documentation/metric evidence updated, and relevant acceptance checks recorded.

## 7. Development milestones and sign-off

| Milestone | Exit evidence (not effort alone) | Gate owner |
|---|---|---|
| **M0 — Development GO** | Approved PRD, 7 OD dispositions, role policy/DB scope mechanism, architecture conditions, evaluation plan, risks, signed G0 checklist | PO + PM + Security |
| **M1 — Database reference foundation** | DDL/migrations, synthetic manifests, exact cents reference cases, no bad records published, AT/RR passing, old snapshot immutable | DB + BA |
| **M2 — Governed query service** | Correct allowlisted templates, denied store/metric queries leave no data or SQL execution, DB second-boundary enforcement proven | Backend + Security |
| **M3 — AI intent and explanations** | Approved schema; adapter reproducible; zero unapproved SQL; 60-question metrics measured with clean holdout | AI + BA |
| **M4 — Usable shared chat** | Authorized role journeys, charts/tables reconcile, denial/clarification/freshness and evidence accessible | Frontend + PM |
| **M5 — Validation complete** | 60/20/50 + AT/RR logs, independent golden answers, review of ≥30 narratives, latency and ≥5 users | QA + Security + PO |
| **M6 — Release GO** | Zero open critical/high security findings; validated backup restore; reproducible demo; documented limitations; signed deployment permission | PO + PM + Security |

## 8. Proposed GitHub repository structure and workflow

**Existing repository:** [`LCK0629/dify_quertPilot`](https://github.com/LCK0629/dify_quertPilot) (`main`). This is a **proposed future structure**, not a claim that these directories exist.

```text
QueryPilot-AI/                       # Existing repo name may remain dify_quertPilot
├── README.md
├── docs/
│   ├── phase-1/                   # existing design and approval records
│   │   └── 17_DEVELOPMENT_READINESS_IMPLEMENTATION_PLAN_V1_0.md  # proposed
│   ├── adr/                       # future approved technical decisions
│   ├── api/                       # response contracts and errors
│   └── runbooks/                  # deployment, operations, backup/restore
├── apps/
│   ├── api/                       # FastAPI modular monolith
│   │   ├── src/querypilot/{identity,policy,intent,metrics,compiler,executor,evidence,audit}/
│   │   └── tests/{unit,integration,security}/
│   └── web/                       # React + TypeScript
├── db/
│   ├── migrations/                # versioned SQL, only after GO
│   ├── fixtures/{golden,invalid,temporal}/
│   ├── generators/                # versioned synthetic NovaMart generator
│   └── tests/                     # reconciliation, permission, snapshot tests
├── ai/
│   ├── contracts/                 # typed intent schema
│   ├── adapters/                  # Dify/direct behind common interface
│   └── dify/                      # exportable workflows if ADR approves
├── evaluation/
│   ├── catalog/                   # 60 golden / 20 non-answer / 50 security
│   ├── references/                # independently reviewed expected outputs
│   └── reports/                   # real runs only; no fabricated metrics
├── infra/
│   ├── compose/                   # local private network, non-public DB
│   └── config/                    # example config without secrets
├── .github/workflows/            # CI, dependencies, secret/security scans
├── .env.example                   # placeholder keys only
└── .gitignore
```

**Branching and review:** protected `main`, short-lived `docs/...` or `feat/...`, small PRs tied to ticket IDs, CODEOWNERS for `db/`, `policy/`, `ai/` and security-sensitive modules, mandatory peer/security review for permission or SQL changes, signed release tag and artifact hashes. GitHub Actions should block merges on lint/unit/integration/negative tests as they become available. Keep real `.env`, credentials, raw secret-bearing logs and actual PII outside Git.

## 9. Development environment and implementation constraints

| Layer | Proposed environment | Acceptance / restriction |
|---|---|---|
| Source platform | GitHub; local VS Code + Git; Windows/WSL2 or compatible Linux/macOS | Reproducible setup in README |
| Runtime | Python (pin a supported 3.x minor after compatibility test); FastAPI; isolated virtual environment | Dependency lock and vulnerability review |
| Database | PostgreSQL **17.x proposed** by physical design, on private Docker network | Supported patched build; no exposed public DB port |
| Frontend | React + TypeScript, supported Node LTS | Lockfile, lint/typecheck, browser smoke tests |
| LLM | Dify self-host candidate or direct provider behind `IntentAdapter` | ADR, licensing, provider retention/egress, token and cost limits before use |
| Orchestration | Docker Compose for local-first demo | Only web/API exposed as intended; Dify admin/DB private |
| IdP/session | Proposed OIDC PKCE BFF or specifically approved isolated demo identity | Server-held session, expiry and CSRF protection; not browser trust |
| PostgreSQL credentials | Separate owner/migrator, ingest, publisher, restricted analytics, audit | Explicit grants and denial proofs; no `BYPASSRLS` analytics |
| Observability | Request/correlation IDs, metric/policy/snapshot version and safe query template ID | No secrets, unauthorized data or unsafe raw SQL in client/log |
| Toolchain | `pytest`, `httpx`, PostgreSQL integration, Playwright, Semgrep/Bandit, dependency/secret scans | Record versions and command outputs after GO |

**Proposed budget/performance guardrails (not measured):** SQL statement timeout 5 s, response ≤1,000 rows, query span ≤36 months, pool size 10, HTTP question ≤1,000 characters, capped LLM retries/tokens. Align all numbers in the security ADR and benchmark them on declared hardware before calling them production guarantees. Disable arbitrary schema browsing, external model tool execution, `SELECT *` from retail base tables, writes and background autonomous loops.

**Local setup after GO (illustrative commands, not an instruction to run now):** install pinned dependencies; prepare a non-secret `.env.example`; start private Compose services; run reviewed migrations with migrator role; generate fixed-seed synthetic fixtures; publish valid snapshot; run DB tests before API tests; start backend with restricted credential; run UI; execute structured security suite.

## 10. Testing strategy and acceptance criteria

All thresholds below are **proposed release criteria**, not actual results. Each result must reference a dataset manifest/version, source commit, test runner version, reviewer and timestamp. An LLM cannot certify its own output as reference truth.

| Test tier / ID | Minimum tests and proposed acceptance | Evidence owner |
|---|---|---|
| **T-01 Metric correctness** | **100%** of approved cent-precision reference assertions and reconciliation rules; `M04=M01−M02−M03` and decomposition sums exactly SGD 0.00 difference | BA/DB |
| **T-02 DB business integrity** | AT-01–26 and RR-01–12 all pass; duplicate, discount, refund and snapshot constraints; rejected records never published | DB/QA |
| **T-03 Supported NL analytics** | ≥**90%** correct end-to-end across 60 independently scored supported questions; correct metric, period, scope and number all required | AI/BA |
| **T-04 Clarification/out-of-scope** | 20 catalog cases individually reviewed; zero prohibited execution, no fabricated answers, correct documented outcome type | QA/BA |
| **T-05 Adversarial security** | **50/50** predefined cases with zero unauthorized DB retrieval, browser/model/log disclosure, or unsafe operation; add all role/permission negative cases | Security/QA |
| **T-06 Authorization defense-in-depth** | 100% approved fixture permutations (Owner/Manager/Analyst/Staff/Admin), forged store/role claims rejected, revocation enforced on next request, DB interface and direct base-table attempts denied | Security/DB |
| **T-07 Narratives and evidence** | ≥30 audited narratives with **zero unsupported numeric/causal claims**; **100%** success responses include permitted metric/snapshot/as-of/scope/limitations provenance | BA/QA |
| **T-08 UI and a11y** | KPI/chart/table numeric agreement; denied/clarify/unsupported/insufficient/error visible; keyboard and semantic accessibility checks pass | Frontend/QA |
| **T-09 User acceptance** | ≥5 qualified testers performing 3 predefined tasks each; ≥80% task success, review issues recorded | PM/BA |
| **T-10 Latency** | Provisional end-to-end p95 ≤**15 s** over ≥30 representative runs; DB monthly KPI p95 **<2 s** on stated local hardware; warm/cold and cost disclosed | Eng/QA |
| **T-11 Operational recovery** | One separate-environment restore verified; reproducible clean install, snapshots and logs; critical/high vulnerabilities remediated or gate NO-GO | DevOps/Security |

### 10.1 Mandatory negative scenarios

1. Sales Staff asks “What is our profit this month?” → **unsupported** for missing validated costs, no financial disclosure, no SQL; if only `chat.use` is approved, a constrained adapter may be consulted, but that does not grant data access.
2. Sales Staff asks “What is net merchandise revenue this month?” with no `metric.M04.read` → denied before SQL; no amount or indirect leakage.
3. Store Manager authorized for Store A asks “Show revenue from all stores” → denied or restricted with explicit, previously approved semantics; **never** silently include Store B.
4. Business Owner without a Store B grant asks for Store B → denied, despite owner role title.
5. User embeds `DELETE FROM retail.orders` or SQL-like command → no such SQL executes.
6. Dify returns a valid-looking JSON plan with ungranted store ID → Stage 2 denies it.
7. Category-ranked AOV without OD-06 signed allowlist → unsupported/denied; no misleading aggregation.
8. Prior-period baseline is 0 or negative → percentage change is `N/A`, not divide-by-zero or invented growth.
9. Requested real last month is not FINAL in the seeded dataset → `insufficient_data`; do not substitute an older month.
10. Late-arriving valid refund creates new snapshot; old snapshot results and hashes remain reproducible and a restatement is disclosed.
11. Permission revoked between chat turns → follow-up and evidence retrieval are re-authorized and denied if revoked.
12. Forced direct DB query with `qp_analytics` against `retail`, `ingest`, `governance` or bypass attempt → no unauthorized rows and no write privilege.

### 10.2 Testing pipeline / promotion rule

`static checks → unit → DB isolation/integrity → API/contract → integration → golden accuracy → 50 security → user/latency → release review`. Tests that rely on random generated labels without independently computed ground truth cannot count as metric accuracy proof. No security-bypass “demo mode” in a release candidate.

## 11. Development GO / NO-GO checklist

A checkmark requires an **actual linked approval record or test specification**, not a plausible recommendation. Currently **no Development GO is issued**.

| Gate | Mandatory approval / evidence | Responsible | At review |
|---|---|---|---|
| G-01 | Five MVP decisions traceable and scope unchanged | PO/PM | **MET** |
| G-02 | Final PRD v1.1 signed and ALIGN-01–12 resolved | PO/BA | **OPEN** |
| G-03 | M01–M09 baseline and independent BA fixture validation recorded | BA/PO | **PARTIAL** |
| G-04 | Conceptual ERD approval QP-APR-003 linked | PO/DB | **MET** |
| G-05 | Physical DB design approval QP-APR-004 linked; execution conditions identified | PO/DB | **MET (design only)** |
| G-06 | Architecture approval QP-APR-005 conditions closed | Security/Architect | **OPEN** |
| G-07 | OD-01 to OD-07 each explicitly closed or signed containment disposition | BA/DB/PO | **BLOCKER** |
| G-08 | Role × function × metric × dependency × store matrix approved | Security/BA/PO | **BLOCKER** |
| G-09 | DB nonforgeable scope-binding mechanism and privilege model approved | Security/DB/PO | **BLOCKER** |
| G-10 | Identity/session, policy-registry persistence, revocation and audit ADR signed | Security/Architect | **BLOCKER** |
| G-11 | Dify/direct adapter, provider egress, license and model retention ADR signed | Architect/PO | **OPEN** |
| G-12 | Data coverage, finality, freshness and restatement contract approved | BA/DB/PO | **BLOCKER** |
| G-13 | Evaluation rubric, independent reference approach, acceptance thresholds signed | QA/BA/PO | **OPEN** |
| G-14 | User/competitor research delivered, or limitation documented and risk accepted | PM/PO | **OPEN** |
| G-15 | Evidence/UI wireframes for denial, data gaps and charts reviewed | PM/UX/Security | **OPEN** |
| G-16 | Repo ownership, environment, secrets, cost and rollback plan agreed | PM/Architect | **OPEN** |
| G-17 | No open unmitigated critical P0 risk and written Development GO signed | PO + Security + PM | **NO-GO** |

**Gate logic:** `GO` only if G-01–G-17 are evidenced and every critical blocker is closed. `CONDITIONAL GO` is **not allowed for DDL/API/data access** while G-07/08/09/10/12 remain open. A future explicit *limited planning/spike authorization* may be recorded for non-production, non-data-access experiments, with scope and expiry; it is not implied here.

## 12. Risk management and change control

| Risk ID | Threat | Severity | Mitigation / escalation |
|---|---|---|---|
| R-01 | Correct SQL but wrong metric arithmetic/date/denominator | Critical | Business golden fixtures, BA review, exact cents and snapshot evidence |
| R-02 | Cross-store financial disclosure via scope spoofing or aggregate inference | Critical | Signed permission matrix, database scope boundary, zero-leak negative tests |
| R-03 | Dify prompt injection or vendor retention exposes data | High | Minimal metadata, bounded JSON, no SQL/tools, egress/retention ADR |
| R-04 | Nonfinal or restated data narrated as final | High | OD-03/07, coverage gate, exact snapshot/as-of disclosure |
| R-05 | Synthetic dataset too easy or inaccurate | High | Realistic fixed seed, independent goldens, invalid/temporal/holdout fixtures |
| R-06 | P1 scope creep compromises security and schedule | High | Signed P0/P1 exclusions, change control and DoR |
| R-07 | Heavy self-hosted Dify footprint/LLM costs | Medium | Adapter benchmark, cost caps, local/direct fallback decision (not automatic) |
| R-08 | Missing real user feedback leads to unsupported product claims | Medium | Interviews/trials or transparent owner risk acceptance |
| R-09 | Technical change silently invalidates previously approved designs | High | ADR + metric/data/PRD traceability; re-approval before merge |
| R-10 | Credential leakage or privilege drift in demo | Critical | Secret scanning, least privilege, session revocation, backup/restore evidence |

Change request fields: CR ID, affected approved artifact/version, reason, affected OD/metrics/permissions, data migration effect, security tests, rollback plan, reviewers, Project Owner authorization, and new version. **Never silently amend approved model grains or metric definitions via implementation PRs.**

## 13. Approval request and decision form

**Decision sought now:** Approval of **QP-PM-DRIP-001 as the planning and gate-control baseline** and instruction to close PRE-01–PRE-10. This request is **not** Development GO.

- [ ] **APPROVE PLAN** — adopt roadmap, governance, blocking register and acceptance approach; keep Development **NO-GO** until G-17.
- [ ] **APPROVE PLAN WITH CHANGES** — list specific corrections; keep Development **NO-GO**.
- [ ] **CHANGES REQUIRED — NOT APPROVED** — revise and resubmit.
- [ ] **REJECT / DEFER** — record rationale.

**Project Owner:** ________________________  
**Decision date/time (SGT):** ________________________  
**Decision reference:** ________________________  
**Conditions and due owners:** ________________________  
**Security Architect review:** ________________________  
**Database Engineer review:** ________________________  
**BA review:** ________________________

### Separate future authorization record — do not complete now

**Gate reference:** QP-APR-DEV-GO-001 (reserved, **not issued**).  
**Decision:** **NO-GO** as of this review.  
**Required evidence links:** G-01–G-17 signed artifact list, OD closures, authorization ADR and evaluation contract.  
**Authorized activities if and only if signed GO:** exact implementation scope, repositories/branches, start date, owners, conditions and review date.

## 14. GitHub source references (reviewed on 26 Nov 2026)

1. [Repository README and current approval summary](https://github.com/LCK0629/dify_quertPilot/blob/main/README.md)
2. [PRD v1.0 draft](https://github.com/LCK0629/dify_quertPilot/blob/main/docs/phase-1/09_PRD_V1_0_DRAFT.md)
3. [Product decision record](https://github.com/LCK0629/dify_quertPilot/blob/main/docs/phase-1/11_PRODUCT_DECISION_RECORD.md)
4. [Architecture & Security Design v1.1](https://github.com/LCK0629/dify_quertPilot/blob/main/docs/phase-1/12_SYSTEM_ARCHITECTURE_SECURITY_DESIGN_V1_1.md)
5. [Architecture approval QP-APR-005](https://github.com/LCK0629/dify_quertPilot/blob/main/docs/phase-1/13_ARCHITECTURE_APPROVAL_RECORD.md)
6. [Conceptual ERD and logical model](https://github.com/LCK0629/dify_quertPilot/blob/main/docs/phase-1/14_CONCEPTUAL_ERD_DATA_MODEL_V1_0.md)
7. [Physical Database Design](https://github.com/LCK0629/dify_quertPilot/blob/main/docs/phase-1/15_PHYSICAL_DATABASE_DESIGN_V1_0.md)
8. [Database design approval record QP-APR-003/004](https://github.com/LCK0629/dify_quertPilot/blob/main/docs/phase-1/16_DATABASE_DESIGN_APPROVAL_RECORD.md)
9. [Evaluation and Test Plan](https://github.com/LCK0629/dify_quertPilot/blob/main/docs/phase-1/05_EVALUATION_AND_TEST_PLAN.md)
10. [Scenario Catalog](https://github.com/LCK0629/dify_quertPilot/blob/main/docs/phase-1/07_TEST_SCENARIO_CATALOG.md)
11. [Research and Validation Plan](https://github.com/LCK0629/dify_quertPilot/blob/main/docs/phase-1/01_RESEARCH_AND_USER_VALIDATION.md)

**End of controlled review draft.** No implementation or test outcome is asserted in this document.