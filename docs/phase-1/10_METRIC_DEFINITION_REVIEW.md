# 10 — Business Metric Definition Review / 核心业务指标审核记录

**Project:** QueryPilot AI / NovaMart fictional retail dataset  
**Version:** 0.2 REVIEW DRAFT / 指标审核草案  
**Date:** 2026-11-23  
**Source:** `03_METRICS_AND_DATA_DESIGN.md` (v0.1), PRD v1.0 draft, project-owner approval of D1–D5 product recommendations.  
**Status:** **HIGH-LEVEL D2 POLICY APPROVED / D2 高层口径已批准**. Detailed recognition, data quality, edge-case and reconciliation rules are **still pending metric signoff** / 详细规则仍需审核，未正式冻结。
**Implementation:** None / 尚未建数据库或运行计算。

## 1. Approved top-level demo reporting decisions / 已批准的演示口径

- Fictional retailer **NovaMart**; **SGD** only; business timezone `Asia/Singapore`. / 虚构零售企业、仅新币、业务时区为新加坡。
- **Calendar months** use `[month start, next month start)` in local timezone. / 日历月使用左闭右开的完整区间。
- **Sales recognition event** occurs when an order is completed. / 订单完成时确认销售事件。
- **Discount** is the posted merchandise discount on that completed-sale line. / 折扣属于完成订单商品行。
- **Refund recognition event** occurs when a merchandise refund is confirmed; it may fall in a later month than the original order. / 确认退款在确认月份冲减，不回写原销售月份。
- **Net merchandise revenue = completed merchandise gross sales − posted merchandise discounts − confirmed merchandise refunds**, excluding tax and delivery. / 商品净收入公式已作为项目演示政策批准。
- The above is **not** accounting certification for a real company; finance/compliance treatment would require separate approval. / 不等同于真实会计报表规则认证。

## 2. Formal metric contract proposals / 指标契约建议

| ID | UI Label / 显示名 | Grain / 粒度 | Rule / 计算 | Edge handling / 边界 |
|---|---|---|---|---|
| M01 | Gross merchandise sales / 商品销售总额 | Completed sale lines | `Σ(quantity × list_unit_price)` of completed sale events | Exclude canceled/uncompleted orders, tax/delivery |
| M02 | Booked merchandise discounts / 商品销售折扣 | Completed sale lines | `Σ(posted_discount_amount)` | Use positive discount amounts; never sum line price again after refund join |
| M03 | Confirmed merchandise refunds / 确认商品退款 | Confirmed refund lines | `Σ(merchandise_refund_amount)` by `confirmed_refund_at` | Positive amount, applies to original store and sale-time category |
| M04 | Net merchandise revenue / 商品净收入 | Unified sale/refund events | `M01 − M02 − M03` | Can be negative; do not clamp; exclude taxes and delivery |
| M05 | Completed orders / 完成订单数 | Order headers | `COUNT(DISTINCT order_id)` completed in reporting period | Zero if none; scope by authorized original store |
| M06 | Sold units / 完成销售件数 | Completed sale lines | `Σ(quantity)` | Refunds do not subtract from this specifically labeled metric |
| M07 | AOV (before later refunds) / 平均已完成订单商品金额 | Same completed-order cohort | `(M01 − M02) / M05` for completed sales in period | If M05=0 → N/A, not zero; excludes later confirmed refunds |
| M08 | Revenue change (%) / 净收入增长率 | Identical authorized scope, two periods | `(current M04 − prior M04) / prior M04 ×100` only if prior>0 | prior≤0 → N/A and show signed monetary delta |
| M09 | Category/store contribution / 分类及门店贡献 | Aggregated M04 by dimension | `Δdimension = M04_current − M04_prior` | Full dimension set must reconcile to total; negative and positive offsets allowed |

**Status of M01–M09:** Method proposed consistent with D2; **pending detailed review/signoff**. / 方法与已批准 D2 一致，但尚待完整指标审核。

## 3. Event fact contract / 统一收入事件模型

Proposed approved analytical view: `fact_merchandise_events` / 建议事件事实层。

| Column | Rule / 规则 |
|---|---|
| `event_id` | Unique prefixed sale-line/refund-line identity; guarantees deduplication / 唯一事件键 |
| `event_type` | `sale` or `refund` / 销售或退款 |
| `event_at` | Sale: order `completed_at`; refund: `confirmed_refund_at` / 按不同事件时间 |
| `store_id` | Original selling store / 原销售门店 |
| `product_id`, `category_id_at_sale` | Original product and historic category / 原产品及销售时类别 |
| `gross_sales_amount` | Sale full item price, refund = 0 / 商品标价总额 |
| `discount_amount` | Sale discount, refund = 0 / 商品折扣 |
| `refund_amount` | Refund amount, sale = 0 / 退款金额 |
| `net_revenue_effect` | gross − discount − refund / 净收入事件贡献 |

**Join rule / 关联原则:** never raw-join one sale line to multiple refund lines and sum original sale amount. Pre-aggregate sale and refund facts or use a `UNION ALL` event view with unique IDs. / 禁止一对多退款关联重复统计销售额。

**Scope rule / 权限原则:** filter authorized stores *before* KPI aggregation; apply exactly the same scope across total/category/store and accounting bridge. / 所有分解必须使用相同已授权范围。

## 4. Worked reference fixtures / 独立测试规格（尚未实际执行）

### Fixture F-01 — Cross-month refund / 跨月退款

Original completed line: 2 × SGD 50 list price = SGD 100, SGD 10 posted discount, completed **2026-09-05**; one SGD 45 confirmed refund dated **2026-10-03**. / 9月完成销售、10月确认部分退款。

| Metric | September 2026 | October 2026 |
|---|---:|---:|
| M01 Gross | 100.00 | 0.00 |
| M02 Discounts | 10.00 | 0.00 |
| M03 Confirmed refunds | 0.00 | 45.00 |
| M04 Net merchandise revenue | **90.00** | **−45.00** |
| M05 Completed order count | 1 | 0 |
| M07 AOV | **90.00** | **N/A** |

**Expected invariant:** A September order refunded in October does not retrospectively change September M04 or September AOV under the approved event-date convention. / 跨月退款不回溯修改之前月份。

### Fixture F-02 — Revenue decline and category bridge / 收入下降分类对账

| Category | Sep SGD | Oct SGD | Δ SGD |
|---|---:|---:|---:|
| Electronics | 50,000 | 35,000 | −15,000 |
| Clothing | 40,000 | 32,000 | −8,000 |
| Home | 30,000 | 33,000 | +3,000 |
| **Total** | **120,000** | **100,000** | **−20,000** |

Expected `Δtotal = −20,000.00`, MoM `−16.7%` (display one decimal), and `Σ Δcategory = −20,000.00`. This is illustrative fixture data, **not an observed result**. / 这只是标准测试输入示例。

### Fixture F-03 — Accounting bridge identity / 商品净收入桥接恒等式

For any fixed scope and period pair:
`ΔM04 = ΔM01 − ΔM02 − ΔM03`.

Test implementation must construct a deterministic fixture that includes increases and decreases in each component and reconcile to **SGD 0.01 precision** using decimal arithmetic. / 折扣和退款增长应使净收入下降；以 Decimal 分精度对账。

### Fixture F-04 — Permission scope / 门店权限

Owner principal sees all demo store events; manager authorized for `store_id=A` cannot retrieve events from `store_id=B` through any grouping, rank, error or response to LLM. / 门店经理无法通过任何查询或模型上下文获取其他门店资料。

### Fixture F-05 — Zero/negative baseline / 零或负基期

If `prior_M04 <= 0`, show signed SGD delta and `growth_percent: null` with N/A reason; do not use division by zero or ambiguous negative-baseline “growth”. / 负数或零基期不计算常规增长率。

### Fixture F-06 — Incomplete period / 不完整月份

If request asks “last month” at **2026-11-23** in `Asia/Singapore`, target October vs September, **even if demo dataset ends in August**. Return insufficient-data state or explicitly qualified partial analysis, not a silently substituted July/August comparison. / 不可将“上个月”替换为数据集最近月份。

## 5. Remaining design issues / 详细审核中发现的待解决问题

| ID | Problem / 问题 | Proposed resolution / 初步处理 | Sign-off |
|---|---|---|---|
| MR-01 | Completion status changes / 订单从完成状态发生变化 | Capture immutable completion event; define reversal policy separately if business needs it / 保留完成事件，不直接用可变最新状态推翻历史 | PENDING |
| MR-02 | Refund confirmed then reversed / 退款撤回或失败 | Model reversal as separate signed adjustment event or explicitly exclude such scenarios from MVP test data; do not silently erase confirmed refunds / 用调整事件建模，或明确首版不涵盖 | PENDING |
| MR-03 | Multi-line / order-level discounts / 整单折扣 | MVP assumes line-attributable posted discounts; define deterministic proportional allocation with cents balancing **if** order-level discounts are present / 首版尽量行级折扣，整单折扣须分摊规则 | PENDING |
| MR-04 | Historical category reassignment / 历史类别变化 | Preserve `category_id_at_sale` on sale and refund; define if later reporting category hierarchy reorg should restate history / 快照销售时分类 | PENDING |
| MR-05 | Missing/late data and `data_as_of` / 数据缺失与迟到 | Define a documented completeness/finality watermark per period; never infer “complete” merely because any rows exist / 建立月份数据完整标记 | PENDING |
| MR-06 | Multiple partial refunds / 多次部分退款 | Ensure cumulative refunded qty ≤ sold qty and cumulative refund amounts ≤ post-discount eligible sale value; prevent sale duplication / 多次退货上限和去重 | PENDING |
| MR-07 | Orders crossing stores / 多门店订单 | Assume one store/channel per order in MVP; reject inconsistent imported records / MVP 一张订单只归一个渠道门店 | PENDING |
| MR-08 | Currency/rounding / 币种与四舍五入 | Store SGD as `numeric`/Decimal, reconcile using unrounded underlying values, display two decimals; no FX / 使用精确小数，在总和后展示舍入 | PENDING |
| MR-09 | Refunds by original product/store but in new period / 不同期间的分类对账 | Every category/store bridge must sum all eligible recognized sale/refund events, including refund-only groups / 不可漏掉仅存在退款的类别 | PENDING |
| MR-10 | Quantity vs causal attribution / 数量变化与根因 | Report sold-units changes as observed measurements; **do not claim price/volume/mix causal decomposition** until a mathematically audited method is approved / 只报告销量变化，尚不做严格因果分解 | PENDING |

## 6. Required data validation tests / 数据质量验收建议

- PK/FK and uniqueness; non-null completed timestamps; `status` consistency / 主外键、时间、状态。
- Nonnegative list price, discounts, refund amount; positive completed line quantity / 非负金额与正数量。
- `discount_amount <= quantity*unit_list_price` / 折扣上限。
- Partial refund quantity/amount cannot exceed original purchased eligible amount, across all confirmed refunds / 累计退款上限。
- All monetary calculations use exact decimal arithmetic; compare stored cents after agreed rounding policy / 金额精度。
- Store/category/product rollups reconcile with authorized total; ensure groups with refunds but no current sales appear / 聚合对账。
- Timezone conversion uses `Asia/Singapore` calendar dates and stored UTC timestamps / 时区。
- Incomplete data flagged through explicit data completeness contract / 数据完整性标记。

## 7. Review decisions and exit gate / 本轮决定与结束条件

**Accepted as product direction / 已批准方向:** NovaMart, SGD, Singapore timezone; D2 event-date gross-minus-discount-minus-confirmed-refund policy; P0 sales analytics and bounded diagnostics. / 已获同意的产品方向。

**Not yet signed off / 尚待批准:** M01–M09 detailed definitions, MR-01–MR-10 edge cases, factual event-grain fields, date completeness contract, independent computed fixtures and test measurements. / 详细指标及所有边界项未批准。

**Recommended next approval / 下一个建议审核对象:** approve or amend MR-01–MR-10 with a signed metric contract revision; then freeze physical PostgreSQL ERD for a separate database review. / 先冻结指标规则，再审核实体关系和物理数据库设计。

**Not an implementation artifact / 非实现成果:** No DDL, PostgreSQL instance, SQL run or successful evaluation is represented by this review. / 尚未建数据库或实际执行测试。
