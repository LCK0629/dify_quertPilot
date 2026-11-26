# QueryPilot AI — Business Metric Dictionary v1.0 (Approved)

## Approval record — controlling disposition

- Decision: DEC-BA-001; Project Owner approval recorded 2026-11-24; published 2026-11-26.
- M01–M09 and MR-01–MR-10: approved as business-policy baseline v1.0. D-01–D-10: BA recommended options accepted; specifically use dated signed refund compensation for D-05.
- T01–T11: approved as specification, not executed. M10 remains deferred.
- D-03 correction treatment and D-10 freshness threshold still require concrete implementation specifications, as the approved recommendations themselves require. No numerical threshold or correction arithmetic is invented by this publication.
- This approval supersedes draft status markers and blank reviewer fields in the historical review text below. It does not independently authorize development or supersede later separately recorded approvals.

---

## Original review candidate (English extraction; historical status markers retained for traceability)

# QueryPilot AI

## Business Metric Dictionary v1.0 — For Approval

**Document ID:** QP-BA-BMD-001  
**Version:** 1.0 — proposed contracts
**Prepared:** 24 November 2026  
**Owner:** Business Analyst
**Approver:** Project Owner (business policy); Finance/Accounting reviewer recommended before any production usage  
**Overall status:** **FOR APPROVAL — NOT SIGNED OFF**  
**Phase gate:** **NO-GO for implementation** until separately approved PRD, data model, architecture and security decisions.

> **Decision boundary** The project owner approved five MVP-level directions on 23 November 2026: fictional NovaMart in SGD/Asia-Singapore; event-date net merchandise revenue with confirmed refunds recognized on confirmation date; sales KPI/ranking/comparison/limited numerical decline diagnosis/charts/evidence; English-first; and LLM intent extraction followed by controlled backend SQL. That approval **does not automatically approve the detailed metric contracts below**, the ERD, the architecture, or any development gate.

---

## 1. Purpose, scope and requested decision

**Purpose** Make every retail KPI reproducible, safe to query, and auditable before defining physical PostgreSQL tables or implementing AI workflows. A metric contract specifies *what is counted*, *when*, *for whom*, and *how it is checked*.

**In scope** M01–M09: merchandise sales, discounts, refunds, net merchandise revenue, orders, units, AOV, period growth and category change contribution. The reporting context is fictional **NovaMart**, **SGD**, and **Asia/Singapore**. Sales and refunds are separate business events. Metric output is numerical reporting, not statutory financial statements.

**Out of scope** M10 Low Stock (P1), profit/margin without verified cost, taxes/shipping revenue, forecasting, causal inference, ad hoc customer PII, unrestricted generated SQL, unrestricted cross-store views, and physical DDL.

**Approval required** Review nine metric contracts (M01–M09), ten cross-cutting rules (MR-01–MR-10), eleven reference tests (T01–T11), and the explicit open decisions in Section 8. The recommendation is *conditional approval only after all critical open rules are resolved and independently checked*.

### 1.1 Decision/status legend

| Label| Meaning|
|---|---|
| **A — Direction approved** | MVP-level policy agreed in prior review; not blanket contract approval|
| **P — Proposed; review now** | BA-recommended interpretation; requires approval|
| **B — Blocking open issue** | Unresolved issue that can change numeric results; no metric sign-off before resolution|
| **O — Out of scope** | Excluded from this dictionary|

### 1.2 Reporting invariants

- All monetary outputs are **SGD merchandise-only**; taxes, delivery charges, tips, gift-card top-ups and processing fees are excluded unless explicitly covered by a later version.
- A sale is recognized only once, at the **completion event**; a refund is recognized only once, at its **confirmation event**.
- All event timestamps represent instants (`timestamptz` concept); date filters use **Singapore local** time with a half-open range **[start, end)**.
- Every aggregation is performed **after authorization scope filtering** and **after event de-duplication**.
- Monetary sums use exact decimal/integer cents and round **only for display**.
- Null/unknown data must not be fabricated as zero; incomplete periods must be explicitly flagged.

---

## 2. Canonical fact contracts

**Proposed logical model**

| Fact / Source | One row means| Required business keys and dates| Guardrail|
|---|---|---|---|
| **Completed sale line** (`order_lines` + `orders`) | One original sold merchandise line, recognized once| `order_id`, `line_id`, `store_id`, `product_id`, `quantity`, `unit_list_price`, `allocated_discount`, `completed_at` | `status=completed`; no fan-out by refund join |
| **Confirmed refund event** (`refund_lines`) | One posted/confirmed refund for an original sale line| `refund_event_id`, `original_line_id`, `merchandise_refund_amount`, `confirmed_refund_at`, `status` | Unique event; link to original sale; refunds exclude shipping/tax |
| **Compensating refund adjustment** (proposed) | A separately auditable reversal of a previously confirmed refund| `adjustment_event_id`, `original_refund_event_id`, `adjustment_at`, `amount`, `reason` | **B**: final policy requires approval (MR-05) |
| **Product dimension at sale** (proposed) | Original category/product attribution preserved for historical comparability| `product_id`, `category_at_sale`, `store_at_sale` | **B**: historical mapping policy requires approval (MR-06) |

**Safe logical event view** `fact_merchandise_events` is a proposed contract, not an implemented table or view. It contains stable `event_id`, `event_type`, `event_at`, `store_id`, `product_id`, `category_id`, `gross_sales_amount`, `discount_amount`, `signed_refund_amount`, and `net_revenue_effect`. Original completed sales and all posted refund-related events must be combined **without joining refund rows back into sales amounts**.

**Event arithmetic** `net_revenue_effect = gross_sales_amount − discount_amount − signed_refund_amount`. A refund reversal, **if approved**, has negative `signed_refund_amount`, and thus increases net revenue on its adjustment date.

---

## 3. Business metric register

| ID | Business label| Exact definition| Time basis| Unit| Status |
|---|---|---|---|---|---|
| **M01** | Gross Merchandise Sales| `SUM(completed_line.quantity × unit_list_price)` | `completed_at` | SGD | P |
| **M02** | Booked Merchandise Discounts| `SUM(allocated_discount)` on completed sale lines | `completed_at` | SGD | **B: allocation** |
| **M03** | Net Confirmed Merchandise Refunds| `SUM(signed_refund_amount)` from confirmed refund events and approved reversals | `confirmed_refund_at` / adjustment date | SGD | **B: reversals** |
| **M04** | Net Merchandise Revenue| `M01 − M02 − M03` over SAME reporting period and authorized scope | Event dates | SGD | A at high level; P details |
| **M05** | Completed Order Count| `COUNT(DISTINCT order_id)` from completed orders | `completed_at` | orders | P |
| **M06** | Sold Units| `SUM(completed_line.quantity)` | `completed_at` | units | P |
| **M07** | AOV — after discounts, before refunds| `(M01 − M02) / M05`, only when `M05 > 0` | Completed-order cohort | SGD/order | P |
| **M08** | Period-over-period Change| `Δ = current − prior`; `% = Δ / prior ×100` only when `prior > 0` | Like-for-like periods | SGD / % / units | P |
| **M09** | Category Net Revenue Change Contribution| `Δ_category = M04(category,current) − M04(category,prior)` | Event dates and original category | SGD; optional % | **B: attribution** |

**Metric catalog control** Each metric must have a stable ID, definition version, display label (English + Chinese), unit, source grain, filter rules, supported dimensions, rounding/display rule, owner, approval status and effective version. The LLM may **select** approved metrics, not redefine them. / LLM ，。

### 3.1 M01 — Gross Merchandise Sales

- **Business question** What is the list-price value of merchandise in completed orders during the period?
- **Include** Each eligible completed merchandise sale line exactly once, `quantity × unit_list_price` before discounts; original store/channel and product identifiers.
- **Exclude** Pending/cancelled orders, tax, shipping, gifts with no separately sold merchandise value, refunds, discounts as deductions.
- **Grain, date, aggregation** Complete sale line; `completed_at` in reporting timezone; additive across distinct store/category/product partitions if each line belongs to exactly one partition.
- **Acceptance** M01 is nonnegative; across authorized stores `Σ M01(store) = M01(total)`; two refund events against one line do not duplicate its original M01.

### 3.2 M02 — Booked Merchandise Discounts

- **Definition** The effective monetary discount allocated to completed merchandise sale lines **at order completion**. Positive amounts; no discount is recognized for uncompleted/cancelled orders.
- **Sources** Explicit line discount preferred. **B:** If a promotion is stored only at the order level, allocate it once by pre-discount merchandise line value; use exact cents, largest fractional remainder and deterministic `line_id` tie-break; do not allocate to tax or shipping.
- **Constraints** `0 ≤ allocated_discount ≤ line_gross` and sum of allocated merchandise discounts equals the eligible order-level merchandise discount.
- **Acceptance** Discounts total and allocations reconcile to the cent; same input and line IDs produce the same output; prevent counting both an order header discount and its allocated line descendants.

### 3.3 M03 — Net Confirmed Merchandise Refunds

- **Definition** Merchandise-only confirmed refund amounts recognized on the date of confirmation, independent of the original sale month. **P:** M03 is a **signed net refund measure** if compensation events are approved; absent reversals it is nonnegative.
- **Scope** Link every refund to its original completed sale line for store/product/category attribution. Partial refunds and repeated partial refunds are possible, but aggregate confirmed refunds must not exceed the discounted merchandise line value.
- **Exclude** Requested, rejected, pending and unconfirmed refunds; tax/delivery returns; credit not tied to merchandise until a separate business policy is approved.
- **Open issue** Reversed refunds require a dated compensating event (preferred) **or** explicit refusal of analysis until resolved; do not silently drop or retroactively overwrite. The approved high-level refund-on-confirmation-date rule is preserved.
- **Acceptance** September sale and October confirmation contribute refund to October M03 only; partial refunds are counted once; original store/category attribution retained.

### 3.4 M04 — Net Merchandise Revenue

- **Definition** `M04(P, S) = M01(P, S) − M02(P, S) − M03(P, S)` for period `P` and authorized scope `S`. The only accepted unqualified user label **“net revenue”** in the retail MVP refers to **event-date net merchandise revenue**, not accounting profit and not an original-order-cohort metric. / “”，。
- **Important** A refund confirmed in October for a September order lowers October M04, not September M04. M04 can be negative when recognized refunds exceed new completed sales; never clamp to zero.
- **Acceptance** Exact reconciliation to M01–M03 at the same time boundaries and access scope. Show period, SGD, data-as-of and policy version.

### 3.5 M05 — Completed Order Count

- **Definition** Number of distinct orders whose final eligible completion event falls within the reporting period and whose originating store is authorized.
- **Exclude** Cancelled/not completed, repeated order lines, and refund count. Returns do not reduce the original order count.
- **Non-additivity** Order count by **product or category** may double-count a multi-category order if category counts are summed. A total must be recomputed using distinct `order_id`; prohibit `SUM(category_order_count)` as a company total.
- **Acceptance** An order with three lines counts once company-wide and once in its single originating store.

### 3.6 M06 — Sold Units

- **Definition** Total quantities on completed sale lines during the period.
- **Include** Positive sold quantities; do not subtract later refunded quantities.
- **Exclude** Cancelled/uncompleted lines, stock movements or returns counted as new sales.
- **Acceptance** Reconcile by store/category/product, while M06 remains distinct from future `net_units` or returned units (not approved here).

### 3.7 M07 — Average Order Value (AOV)

- **Definition** `(M01 − M02) / M05` on **the same set of completed orders**. Refunds recognized later are *not* deducted from this AOV. Display full label: **“AOV (after discounts, before refunds)”** / “（、）”。
- **Undefined cases** If `M05 = 0`, display **N/A — no completed orders**, not SGD 0.00 and not infinity.
- **Dimension restriction** Store/channel supported; per-category “AOV” requires an explicitly named alternative denominator and is **not** approved as M07, because a cross-category order can appear more than once.
- **Acceptance** Refund-only month has M04 negative but M07 N/A when M05=0.

### 3.8 M08 — Period-over-period Change

- **Definition** For an eligible additive or properly defined metric `X`: absolute change `Δ_X = X_current − X_prior`; percentage change `100 × Δ_X / X_prior` **only if `X_prior > 0`**. If prior = 0, negative or null, show percentage **N/A** and keep absolute Δ if both values exist.
- **Comparison contract** Same metric version, currency, authorized store set, dimensions and calendar convention. Default prior month comparison uses **two complete calendar months**, not an incomplete month against a full prior month.
- **Unsupported** Arbitrary percent growth when previous < 0, partial-month vs complete-month comparisons without explicit matched windows, or percent changes on undefined M07.
- **Acceptance** SGD 120,000 → 100,000: Δ = −20,000; growth = −16.666...%, display **−16.67%**.

### 3.9 M09 — Category Net Revenue Change Contribution

- **Definition** For each immutable/original category `c`, `Δ_c = M04(c, current) − M04(c, prior)`. Total `Δ_total = M04(all, current) − M04(all, prior)`; require `Σ_c Δ_c = Δ_total` before display rounding.
- **Output** Show signed **SGD Δ** first, descending by decline magnitude for a downward period; include offsetting growth as positive values. If total decline `Δ_total < 0`, an optional contribution share is `(-Δ_c)/(-Δ_total) × 100%` and **can exceed 100%** for a category when others offset a decline.
- **Coverage** Preserve category-at-sale for later refunds; explicit **Unassigned** category must be retained for unmapped records, never silently dropped.
- **Acceptance** Additive category reconciliation including zero-activity and new/discontinued categories (outer-join categories across periods); no causal claim such as “competitor caused the decrease” from this computation alone.

---

## 4. MR-01 to MR-10 — Cross-cutting business rules

| Rule ID | Proposed rule| Status and approval consequence|
|---|---|---|
| **MR-01 Scope & currency** | SGD merchandise-only. Apply caller's authorized store scope before aggregation; never expose unauthorized stores in totals, comparisons, drilldown or data provenance.| **A direction / P details** — approve currency exclusions and scope granularity. |
| **MR-02 Time & calendar** | Use Singapore local `[start,end)`, convert to UTC for storage/query. “Last month” means previous **fully completed** local calendar month; ambiguous dates request clarification.| **P** — approve boundary/relative-date interpretation. |
| **MR-03 Completion status** | One immutable sale recognition when order is completed. Pending/cancelled excluded. Returns must not change historical completed status; post-completion cancellation/void requires separately specified correction policy.| **B** — clarify completed-order corrections/voids. |
| **MR-04 Merchandise discount allocation** | Prefer posted line discounts. Allocate order-level merchandise discounts proportionally with deterministic integer-cent largest remainder and `line_id` tie-break. Never count header + lines twice.| **B** — approve allocation basis and discount eligibility. |
| **MR-05 Refunds, caps & reversals** | Only confirmed merchandise refunds; link to original line; cap cumulative refunded value and units; recognize at confirmation. Recommended reversal handling: separately timestamped signed compensating event, preserving audit history.| **B** — decide signed correction vs fail-closed/no reversal support. |
| **MR-06 Historical attribution** | Attribute sale and linked refunds to original store/product/category-at-sale snapshot. Keep Unknown/Unassigned explicitly; no retroactive category drift unless separately versioned.| **B** — approve category-at-sale definition and remap policy. |
| **MR-07 No-data vs zero; period completeness** | Actual zero only after source coverage validation. Missing records, partial load and stale feeds return INCOMPLETE/UNKNOWN, not 0. Current month flagged partial; omit default full-month comparison.| **B** — approve completeness watermark and permitted degraded answers. |
| **MR-08 Grain, de-dup and aggregation** | Unique sale/refund event IDs; aggregate sales and refunds independently before combining. M05 distinct by order and non-additive across categories.| **P** — approve keys, distinct/non-additive behavior. |
| **MR-09 Numerical representation** | Exact cents/DECIMAL; round once to 2 decimals for SGD, 2 decimal points for %, N/A for zero denominator; negatives preserved; reconciliations computed pre-rounding.| **P** — approve final display and rounding method (half-up proposed). |
| **MR-10 Lineage, freshness & restatement** | Include metric/version, timestamps, timezone, authorized scope, source snapshot/data-as-of, request ID, sanitized execution evidence and limitations. Late-arriving or corrected events trigger versioned as-of restatements, not silent unexplained changes.| **B** — approve restatement policy and freshness threshold. |

**Recommended approval decision / BA ：** Approve MR-01, MR-02, MR-08 and MR-09 in their proposed form if the reviewer accepts their specifics; resolve blocking MR-03–MR-07 and MR-10 before accepting M01–M09 as an implementable set. This recommendation is **not** a recorded approval.

---

## 5. Worked examples and reconciliation

All examples are **fictional specification fixtures**, not actual NovaMart business observations.

### Example A — Cross-month partial refund

A completed order on **5 September 2026** has one line: 2 units × SGD 50 = **SGD 100 gross**, a SGD 10 line discount, and one completed order. One unit receives a **confirmed SGD 45 merchandise refund on 3 October 2026**.

| Period | M01 gross | M02 discount | M03 confirmed refund | M04 net revenue | M05 orders | M06 units | M07 AOV |
|---|---:|---:|---:|---:|---:|---:|---:|
| September 2026 | 100.00 | 10.00 | 0.00 | **90.00** | 1 | 2 | **90.00** |
| October 2026 | 0.00 | 0.00 | 45.00 | **−45.00** | 0 | 0 | **N/A** |

**Interpretation** September remains a SGD 90 net merchandise sale; October shows a SGD 45 refund impact. AOV is not computable in October with zero completed orders.

### Example B — Refund reversal decision (conditional)

If Example A's SGD 45 confirmed refund is reversed on **2 November 2026**, the preferred signed-adjustment policy creates a **−SGD 45 M03** refund adjustment in November and **+SGD 45 M04** net-revenue impact, linked to the original refund. The September and October **as-of historical snapshots** remain reproducible. **Do not implement this fixture unless MR-05 and MR-10 are approved.**

### Example C — Order-level discount residual

Three eligible sale lines each have gross SGD 1.00. Order-level merchandise discount is **SGD 0.01**. Equal proportional allocation yields fractional cents. Allocate SGD 0.01 to the line with the lowest stable `line_id` under an approved tie-break; other lines receive zero. **M01=3.00, M02=0.01, completed merchandise value=2.99**, not 2.98 or 3.00.

### Example D — Category decline breakdown

| Category | September M04 (SGD) | October M04 (SGD) | Signed Δ (SGD) | Share of total decline* |
|---|---:|---:|---:|---:|
| Electronics| 50,000.00 | 35,000.00 | **−15,000.00** | 75% |
| Clothing| 40,000.00 | 32,000.00 | **−8,000.00** | 40% |
| Home| 30,000.00 | 33,000.00 | **+3,000.00** | −15% (offset) |
| **Total** | **120,000.00** | **100,000.00** | **−20,000.00** | **100%** |

`M08 = (100,000 − 120,000) / 120,000 = −16.67%` (display). `Σ Δ_category = −20,000`. **These are mathematical contributions, not evidence that a particular competitor, promotion or demand change caused the decline.**

### Example E — Multi-category order count

Order O-100 contains an Electronics line and a Home line, both completed in the same order. Company-wide **M05=1**; if order count is shown for each category each category may show **1**, but **1+1≠ company M05**. A category sum is not a valid overall order count.

---

## 6. Reference acceptance tests

Test statuses below are **DESIGNED — NOT EXECUTED**. The reference figures are expected outcomes for synthetic fixtures; no PostgreSQL or API run is claimed.

| ID | Fixture| Expected assertion| Covers |
|---|---|---|---|
| **T01** | Completed sale: 2×50, discount 10 | M01=100; M02=10; M04=90; M05=1; M06=2; M07=90 | M01,02,04–07 |
| **T02** | 45 refund in month after sale | Original-month M03=0; next-month M03=45; next-month M04=−45 | M03,04, MR-02/05 |
| **T03** | Only confirmed refund, no new orders | M05=0; M07=N/A; negative M04 retained | M04,05,07,09 |
| **T04** | 0.01 order discount across 3 equal lines | Allocations sum exactly 0.01, deterministic tie-break | M02, MR-04 |
| **T05** | Two partial refunds for one sale line | M01 counted once; refund amounts summed once; cap obeyed | M01,03, MR-08 |
| **T06** | Refund reversal 45 in later month | **Conditional:** later M03=−45; M04 contribution=+45; original history auditable | M03,04, MR-05/10 |
| **T07** | September 120k vs October 100k | Δ=−20k; M08=−16.67%; category Δ sum=−20k | M08,09 |
| **T08** | Two categories in one completed order | Company M05=1; category counts not summed into company total | M05, MR-08 |
| **T09** | Prior amount=0, <0 or missing | Percent change=N/A; Δ only if both periods known | M08, MR-07/09 |
| **T10** | Missing feed / partial current-month data | Mark incomplete/unknown; do not silently report 0 or compare partial vs full | MR-07/10 |
| **T11** | Request from Store A-only user includes Store B | No Store B data in totals, breakdown, evidence or logs disclosed to requester | MR-01 |

**Mandatory reconciliation gates** `M04 = M01 − M02 − M03`; `SUM(store M04) = scoped company M04`; `SUM(category M04, including Unassigned) = scoped company M04`; and `SUM(category Δ) = company Δ`. Use exact values prior to presentation rounding. Any failure must block the corresponding response, not be “explained” by the LLM.

### 6.1 Evidence packet required per answer

`metric_id` + `metric_version`; semantic label; time boundaries and timezone; authorized store scope; exact filters/dimensions; current vs previous period (if compared); result + unit; source snapshot/data-as-of and completeness state; sanitized compiled query/plan evidence (no secrets); request ID; limitation flags.

**Safe execution principle** An LLM's generated SQL string is never directly executed. A trusted FastAPI component authorizes a structured intent against approved metrics, dimensions and scopes and compiles bounded read-only queries; implementation choices remain subject to separate architecture/security sign-off.

---

## 7. Dependency and acceptance checklist

**BA sign-off prerequisites / BA ：**

- [ ] Metric owner confirms definitions M01–M09, source grains, date basis, included/excluded items and dimensional limits.
- [ ] Critical blocking rules MR-03, MR-04, MR-05, MR-06, MR-07 and MR-10 have written resolutions.
- [ ] Reference tests T01–T11 are accepted as the expected specification (tests can execute only after development approval).
- [ ] `M03` display label (“net confirmed refunds” under reversal policy) and M07 “before refunds” wording accepted.
- [ ] Financial scope explicitly excludes shipping, tax and costs; metric output is not presented as audited statutory revenue.
- [ ] Data model designer can represent historical classification, discount allocation, event IDs and as-of provenance **without approving DDL in this review**.
- [ ] Example A–E and reconciliations are independently recalculated by BA/product owner.
- [ ] Final approval recorded with name, date, version, conditions and rejected alternatives.

**Downstream artifacts affected** conceptual ERD → fact/semantic contract → data-generation test fixtures → approved query compiler → golden test harness → frontend metric labels/evidence panels. No dependency is declared implemented by this document.

---

## 8. Approval decisions

Each item can be marked **APPROVE AS PROPOSED / REVISE / REJECT / DEFER**. Leaving a blocking issue blank is **not approval**.

| Decision | BA recommended option / BA  | Why it matters| Reviewer decision |
|---|---|---|---|
| **D-01** Scope| SGD, merchandise only; no shipping or tax | Misleading gross/net values | __________ |
| **D-02** Calendar| SGT `[start,end)`; last fully completed month by default | Off-by-one date/period errors | __________ |
| **D-03** Corrections/voids| Preserve event history; separately auditable adjustment; define treatment before implementation | Orders and sales may be overstated | __________ |
| **D-04** Header discount| Proportional by gross eligible merchandise value, deterministic cent residual | Category/store reconciliation wrong | __________ |
| **D-05** Refund reversal| Dated signed refund compensation; M03 label becomes net confirmed refunds | Reversal-only period may report wrong net | __________ |
| **D-06** Category mapping| Category-at-sale snapshot, plus explicit Unassigned bucket | Category trend restates silently | __________ |
| **D-07** Completeness| Distinguish complete zero from missing data; partial period flagged | False “revenue fell to zero” claims | __________ |
| **D-08** Order counts| Distinct order; category order counts non-additive | Overcounting in rankings | __________ |
| **D-09** Display| Exact cents, half-up display 2 decimals, preserve negatives, N/A for zero denominator | Misleading growth/AOV | __________ |
| **D-10** Late-data restatement| Versioned as-of snapshots + disclosed corrections; agree freshness policy | Same question yields unexplained changes | __________ |

**Reviewer choices**

- [ ] **APPROVED WITHOUT CHANGES** — M01–M09 + MR-01–MR-10 + reference fixtures approved as specified; any conditional item must be resolved in the written record.
- [ ] **APPROVED WITH CONDITIONS** — list condition IDs, owner, due date and explicitly state which metric contracts remain blocked.
- [ ] **CHANGES REQUIRED — NOT APPROVED** — return to BA for revision.
- [ ] **REJECTED / DEFERRED** — record rationale.

**Product Owner** ________________________  
**Review date** ________________________  
**Decision reference** ________________________  
**Finance/Accounting reviewer (recommended)** ________________________  
**Conditions** __________________________________________________________

**Current recorded decision:** **PENDING — no signature received**. Approval of this dictionary **alone** does not authorize PostgreSQL implementation, FastAPI/Dify architecture finalization, access model deployment, or development GO.

---

## 9. Source trace and change control

**Source baseline** `03_METRICS_AND_DATA_DESIGN.md` (planning v0.1, dated 10 November 2026) and `02_PRD_V0_1.md`; project-owner decisions on five MVP directions recorded in the 23 November 2026 review conversation. The v0.1 proposal labeled accounting details as pending, which this v1.0 converts into explicit decision points.

**Version interpretation** `v1.0 — For Approval` means a complete **review candidate**, **not** a signed or production-ready definition. Following any reviewer change, publish `v1.0-rev1` or `v1.1` with a decision log and change impact on schema, fixtures, query planning and UX labels. Preserve approved previous definitions for reproducibility.

**Accountability** BA authors metric logic and test fixtures; Project Owner owns business-policy decisions; Data/Database Engineer validates feasibility and grain; Backend/AI Engineer must conform to approved contracts; Finance reviewer validates suitability before real-business use.

**Final recommendation / BA :** Set the metric approval gate to **PENDING**, not GO. Obtain written decisions for D-01–D-10, then reconcile the reference fixtures before conducting the separate conceptual ERD review.