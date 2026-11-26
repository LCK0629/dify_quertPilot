# Role & Permission Matrix v1.0 — For Approval

**ID:** QP-SEC-RPM-001 | **Date:** 2026-11-26 | **Owner:** Security Architect | **Reviewers:** BA, DB Engineer, Solution Architect | **Approver:** Project Owner | **Status:** FOR APPROVAL | **Development:** NO-GO

## 1. Scope and controlling baseline
QP-APR-005, QP-APR-006, QP-APR-007, approved metric dictionary 19, approved semantic contracts 20 and proposed database amendment. One shared chatbot; English question interpretation P0. RBAC assigns capabilities; explicit principal store grants constrain data; current policy and semantic allowlist constrain every output. Role name never authenticates identity or grants all stores. No real PII. All grants below are proposals, not deployed access.

## 2. Proposed role templates
A = proposed template grant only when explicitly assigned, C = separately approved grant required, — = absent. Missing grants deny. Explicit deny overrides allow. No role inheritance. Each person requires active authenticated identity, active assignment, policy version and applicable scope.

| Capability | Owner | Store Manager | Sales Staff | Inventory Staff | Data Analyst | System Admin |
|---|---|---|---|---|---|---|
| chat.use | A | A | A | A | A | C |
| analytics.kpi | A | A | A | A | C | — |
| analytics.rank | A | A | — | — | C | — |
| analytics.compare | A | A | C | — | C | — |
| analytics.diagnose | A | C | — | — | C | — |
| evidence.read | A | A | A | A | C | — |
| users.manage | — | — | — | — | — | A |
| policy.manage | — | — | — | — | — | — |
| audit.read | — | — | — | — | — | — |

evidence.read permits only sanitized evidence for an authorized result; minimum evidence is inseparable from any successful analysis, so all analytics grants require evidence.read. Admin user management does not imply policy editing, grant activation, audit access or analytics. P0 grant changes via controlled operator workflow, not chatbot; separate security reviewer and owner approval, no self-grant, no browser role assertion. Analyst and additional capabilities use explicitly approved constrained role templates; do not infer direct grants from C. System Admin can receive a separate business role only through that workflow.

| Metric | Owner | Manager | Sales Staff | Inventory Staff | Analyst | Admin |
|---|---|---|---|---|---|---|
| M01 gross sales | A | C | — | — | C | — |
| M02 discounts | A | C | — | — | C | — |
| M03 signed refunds | A | C | — | — | C | — |
| M04 net revenue | A | A | — | — | C | — |
| M05 completed orders | A | A | — | — | C | — |
| M06 sold units | A | A | A | A | C | — |
| M07 AOV | A | C | — | — | C | — |
| M08 period change | A | A | C | — | C | — |
| M09 diagnostic contributions | A | C | — | — | C | — |

M08 requires an authorized base metric and compare capability. Staff optional M08 is restricted to M06 only. Manager proposed default M08 applies M04/M05/M06; additional base metrics require explicit grants. Manager diagnosis requires separate M09 and diagnose capability. Inventory staff can query sold units, not stock levels (M10 deferred). Profit unsupported for everyone. No user-facing raw SQL, row-level transactions, arbitrary export, inventory, cost or PII.

## 3. Scope and action semantics
- Explicit principal-specific store IDs for all analytics roles, including Owner. All-store owner means every store explicitly granted; new store not automatically included. Omitted scope = permitted stores with clear label, never company-wide unless all actual stores are granted. Explicit request for any unauthorized store denies the entire request; do not silently intersect. No scope or inactive identity fails closed.
- A principal with multiple roles may combine allowed capabilities only within the same explicit principal-wide store scope. This is a deliberate P0 simplification: all active business roles share the principal's store grants. Mixed role-specific store boundaries are not representable and must be refused at provisioning; if required, redesign registry before GO. Deny precedence applies across roles. No wildcard grants.
- Allow only approved OD-06 metric/function/dimension/filter combinations; product rank M01–M04/M06; M05 store rank only; M07 no rank or category/product grouping or filters; M08 compare only; M09 fixed store/category diagnosis only. Dates, channel, filters, rank limits and snapshot must match approved semantic contract. No unrestricted mixed dimensions or arbitrary expressions.
- Explicit scope words (all stores, named store) must be resolved as requested scope, never downgraded to omitted scope. Ambiguity requires clarification without listing unauthorized stores. Resolve only trusted identifiers; client, model and chat history cannot grant rights.
- Every turn and evidence retrieval rechecks current grants. Bind immutable policy version, principal, requested stores, metric, operation, allowed outputs and snapshot to approved execution plan. Abort on policy change or expiry before response. Historical business snapshots never revive old grants. No shared answer caches.

## 4. Derived calculations and disclosure
| Output | Required visible metric grants | Internal calculation only |
|---|---|---|
| M04 | M04 | M01/M02/M03, private exact reconciliation |
| M07 | M07 | M01/M02/M05, private numerator/denominator |
| M08 | M08 + authorized base | Same base in both matched periods; no unauthorized base values |
| M09 | M09 + M04 + diagnose | Store/category M04 deltas, full reconciliation |
| Gross-discount-refund bridge | M09 + M04 + M01 + M02 + M03 + diagnose | Private reconciliation; optional bridge omitted if not granted; explicit bridge request denied |

Internal computation must execute within protected metric-specific routines, never expose raw components to low-privilege caller or narrative adapter. Charts, labels, citations, totals, error text, metadata, logs and explanations use the same output policy.

Inference policy proposal: treat permission as permission to learn the mathematical implications of permitted aggregate outputs, not guaranteed secrecy against all inference. To avoid obvious within-policy derivation of withheld monetary components, reject provisioning a partial set containing any three of M01–M04, because the fourth is exactly recoverable. Also reject provisioning M07 and M05 together unless M01 and M02 are both granted, because their product reveals pre-refund net sales and may enable component reconstruction across queries. Validate effective grants after combining roles and after changes. Reject inconsistent sets atomically; no silent expansion. This conservative MVP rule does not guarantee protection against external knowledge, cross-user collusion, differencing or sparse aggregate inference. No individual transaction drilldown; evaluate differencing and sparse-result risks before security approval/GO. If stronger confidentiality is required, redesign with query-history/threshold controls or narrower permissions. No real data deployment under this policy.

## 5. Two-stage enforcement
1. FastAPI verifies identity/session/CSRF and chat.use. No chat permission: 403, no adapter or business SQL.
2. Authorized chat: minimized question and generic approved catalog to IntentAdapter (Dify or direct, separately selected). No credentials, private values, hidden grant metadata or unrestricted tools.
3. Validate untrusted typed intent, semantic allowlist, capability, metric/dependency/output policy and exact scope. Unsupported profit/inventory returns 422; denied permitted-domain request returns 403; ambiguity clarifies. No business SQL for denied/unsupported/clarification outcomes. Deterministic prefilter may skip model only when safe; never assume model was not called.
4. Compile reviewed parameterized template. Independent DB authorization enforces principal, scope, metric and output boundary; shared login or caller-supplied scope not proof. Exact nonforgeable mechanism remains PRE-05 blocker.
5. Check snapshot compatibility, OD-03/07 coverage/finality and reconciliation. Incomplete required coverage returns insufficient_data; historical final snapshot explicit as-of only with current permission. Reauthorize immediately before response and audit sanitized outcome. Optional narrative uses only approved result fields and is verified; deterministic fallback.

## 6. Service identity separation
Migrator/owner: DDL only controlled deployment; no interactive chat. Ingest: staging writes only. Publisher: validated atomic publication only. Analytics gateway: bounded metric operations only, no base-table access, DML, role escalation or BYPASSRLS. Audit writer: append sanitized records; reader independently authorized. IdP/session and policy activation identities separate from analytics; no secrets in registry or model. Exact SQL GRANT, ownership, connection pool lifecycle and authentication design deferred to reviewed authorization ADR.

## 7. Acceptance specifications (not executed)
| ID | Synthetic scenario | Expected |
|---|---|---|
| RPM-01 | No chat grant | 403; zero adapter and business SQL |
| RPM-02 | Sales staff asks revenue | 403; zero business SQL; adapter may run |
| RPM-03 | Sales staff asks units in own store | Authorized M06 only if coverage valid |
| RPM-04 | Same staff asks another store | 403; no store data or metadata |
| RPM-05 | Manager A requests A+B, only A granted | Entire request denied |
| RPM-06 | Owner with A/B grants, newly created C | C excluded from omitted scope; explicit all-store request denied if C ungranted |
| RPM-07 | Manager M04 asks gross/refund bridge | Denied without component grants |
| RPM-08 | Owner asks profit or inventory | Unsupported; no business SQL |
| RPM-09 | M04 authorized product rank | Allowed with rank capability and valid coverage |
| RPM-10 | M07 product filter/rank | Unsupported regardless of role |
| RPM-11 | Analyst lacks M08 but has M04 | Growth denied |
| RPM-12 | Staff with M08 and compare asks M06 trend | Allowed; M04 trend denied |
| RPM-13 | Admin only asks revenue | Denied; user admin not analytics |
| RPM-14 | Role conflict explicit deny vs allow | Deny |
| RPM-15 | Three of M01–M04 granted across roles | Provisioning rejected atomically |
| RPM-16 | M05/M07 without M01/M02 | Provisioning rejected |
| RPM-17 | Mixed role-specific store requirements | Provisioning rejected pending redesigned scope |
| RPM-18 | Grant expires during query | Suppress result; audit; no narrative disclosure |
| RPM-19 | Old snapshot/evidence after revocation | Denied with current policy |
| RPM-20 | LLM injects role/store/SQL | Invalid/untrusted; no business SQL |
| RPM-21 | Client spoofs principal, policy or scope | Reject; no authority expansion |
| RPM-22 | Missing coverage in authorized scope | insufficient_data, no fabricated zero |
| RPM-23 | Units-only raw event or component request | Deny at API and DB |
| RPM-24 | Grant admin self-escalation attempt | Reject; audit |
| RPM-25 | Pooled connection inherited authority | No cross-principal leakage; DB ADR must demonstrate |
| RPM-26 | Inference via repeated aggregates or sparse cells | Evaluate residual risk; no claim of complete inference prevention |
| RPM-27 | Unapproved evidence fields or narrative components | Suppress; no leakage |
| RPM-28 | Missing policy version, expired scope, activation race | Fail closed |

Acceptance target: all defined authorization tests pass after separate Development GO; zero unauthorized disclosures in defined suite; no test results claimed now. BA validates semantic consistency, Security validates inference/role policy, DB validates independent enforcement.

## 8. Approval requests and remaining gates
Approve or revise (a) role templates and optional grants, (b) explicit principal-wide store scope and multi-role limitation, (c) deny precedence and controlled grant workflow, (d) derived-output and inference rules/residual demo risk, (e) evidence and service identity separation, (f) test specifications. Independent reviewers and Owner must record disposition. PRE-03 not closed by drafting this document. Registry v1.1, identity ADR, nonforgeable PostgreSQL enforcement, AI integration, full PRD and readiness gate remain separately pending. No implementation authorization.
