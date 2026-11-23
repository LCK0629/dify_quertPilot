# 08 — PRD v0.1 Review Notes / PRD 正式审核记录

**Project / 项目:** QueryPilot AI  
**Review date / 审核日期:** 2026-11-23  
**Based on / 审核基线:** `02_PRD_V0_1.md`, `03_METRICS_AND_DATA_DESIGN.md`, `04_ARCHITECTURE_SECURITY_ADRS.md`, `06_ROADMAP_BACKLOG_GATE.md` on `main`  
**Reviewer role / 审核角色:** Technical PM / BA / Architect (AI-assisted review)  
**Disposition / 结论:** **REVISE AND RESUBMIT / 修改后复审** — not approved; no implementation authorized / 未批准开发

## 1. Strengths / 已经合理的设计

- **Clear wedge / 核心场景清楚:** Retail sales analytics and limited revenue-decline contribution analysis, not an all-purpose SQL chatbot / 零售销售分析和有限收入下降贡献诊断，而非通用 SQL Chatbot。
- **Trust boundary / 安全边界合理:** LLM provides typed intent; FastAPI validates scope and compiles approved query shapes / LLM 提供结构化意图，FastAPI 执行受控编译和权限验证。
- **Data-model discipline / 数据设计意识正确:** Event-dated sales and refunds with separate grains, reconciled aggregation / 销售与退款分离，支持收入对账。
- **Explicit non-goals / 反范围明确:** No causal inference, customer PII retrieval, unrestricted generated SQL, forecasting or autonomous writeback in MVP / MVP 不做因果推断、客户隐私查询、任意 SQL、预测或自动写回。
- **Acceptance ambition / 可量化验收:** Query correctness, numerical reconciliation, security rejection and evidence traceability are explicitly planned / 已提出正确性、安全和可追溯的衡量标准。

## 2. Required changes before PRD v1 / PRD v1 前必须处理

| Finding | Severity | Recommendation / 建议 | Owner | Status |
|---|---|---|---|---|
| R01: MVP too broad without delivery slices / 首版缺少增量交付切片 | High | Keep security across every slice; define S1 KPI, S2 compare/rank, S3 bounded revenue diagnosis, S4 evidence + role regression. All P0 remain release requirements, but delivery order becomes explicit / 以逐段可验收方式交付，不放弃权限保护。 | PM | Proposed |
| R02: `why` diagnostic may imply causality / “为什么”易被误解为因果解释 | High | Define supported diagnostic as category/store deltas + gross/discount/refund bridges; quantity change may be reported, but **price–volume–mix causal attribution is outside MVP unless a mathematically validated decomposition is specified** / 限定为数值变化贡献，不声称推断购买原因。 | BA | Proposed |
| R03: Business clock and freshness / 月份日期与数据完整性 | High | Define last complete calendar month in `Asia/Singapore` using request time; do not silently replace with last available dataset month; disclose missing/incomplete data and decline to assert a complete-month comparison / 不可悄悄用数据库最新月份取代上月。 | BA/Data | Pending approval |
| R04: Revenue vs AOV metric naming / Revenue 与 AOV 口径 | High | Accept distinct event-date M04 net merchandise revenue and pre-refund M07 AOV only after the reporting policy is approved; names/tooltips must distinguish them / 区分收入与未扣退货的订单均值。 | Product owner | Pending approval |
| R05: Refund/category attribution / 退款分类归属 | High | Fix original-store and historical-at-sale category attribution; separately aggregate sales/refund facts before joining; set reconciliation at SGD cent precision after aggregation / 原销售门店及历史类别归属，避免一对多重复计数。 | Data lead | Proposed |
| R06: Language support ambiguity / 中英文用户问题 | Medium | English natural-language benchmark in P0; Chinese explanations/documentation can be bilingual; Chinese NL querying to require a separate tested scope or P1 release / 英文问题先作为 P0，中文自然语言查询另行实测。 | Product owner | Pending approval |
| R07: Authorization persona specifics / 权限范围不够具体 | High | Use at least two distinct principals: all-stores owner/test analyst, one-store manager; formalize denied cross-store interactions and do not trust LLM/user-supplied role claims / 明确多门店和单门店测试身份。 | Security | Pending approval |
| R08: Dataset and golden questions / 数据集测试依据 | High | Document scenario fixture seeds, dates, expected reference calculations and who independently verifies them; scenario list alone is not a passed test / 测试目录不等于已验证答案。 | QA/Data | Planned |
| R09: Dify selection not evidence-backed / Dify 仍未定 | Medium | Maintain an LLM intent adapter with a side-by-side decision on cost, complexity, testability and latency before architecture approval / 建立对比决策再选型。 | Architect | Open |
| R10: Query refusal/evidence semantics / 拒答及证据 | Medium | Define UI/API status types `success`, `clarification`, `unsupported`, `denied`, `execution_error`, `insufficient_data`; every status has request ID and safe explanation / 前后端统一处理结果类型。 | PM/Backend | Proposed |

## 3. Recommended MVP boundary / 建议首版范围

### P0 Release must-have / 正式发布前必须具备
1. **Safe KPI query / 安全 KPI 查询:** gross merchandise sales, booked discounts, confirmed refunds, net merchandise revenue, completed orders, units, AOV.
2. **Comparison & ranking / 对比和排名:** month-over-month, store/category/product, with authorization.
3. **Limited revenue decline investigation / 有限收入下降诊断:** compare prior two complete months; show exact revenue delta, category and store contributors, plus gross/discount/refund component deltas; refrain from unsupported causes.
4. **Evidence & UX / 证据与用户体验:** KPI definitions, reporting dates, timezone, data-as-of, executed safe SQL/plan, charts/tables, ambiguity and refusal handling.
5. **Security & evaluation / 安全与测试:** backend-approved plans, read-only least privilege, store isolation, reference answer testing and telemetry.

### P1 / 非首版阻塞
- Inventory low-stock, query history, saved links / 低库存、查询历史、分享链接。
- Chinese natural-language querying, if first-release English results are reliable and a distinct Chinese evaluation set is prepared / 中文自然语言问题输入需独立验证。

### Excluded / 排除
- Causal explanations, forecasting, customer churn, arbitrary SQL, unrestricted autonomous agents, production multi-tenancy / 真正因果解释、预测、客户流失、自由 SQL、自主代理、多租户商用系统。

## 4. Specific benchmark for flagship journey / 收入下降演示验收

**Question / 问题:** `Why did our revenue decrease last month?`

When using `2026-11-23` local request date, resolved periods must be **2026-10-01 to 2026-11-01 (exclusive)** vs **2026-09-01 to 2026-10-01 (exclusive)**. / 若在 2026-11-23 提问，比较的是 10 月与 9 月完整日历月。

Reference fixture already specified in metrics doc: Sep SGD 120,000 vs Oct SGD 100,000, delta SGD −20,000; category contributions −15,000 / −8,000 / +3,000, summing to −20,000; growth −16.7% to 1 decimal. This is **fictional specification data, not a query result**. / 这是虚构测试例，不是真实运行结果。

**Acceptance / 验收:** Aggregate and category reconciliation exact to cents after aggregation; correct store authorization; category/store and gross–discount–refund components demonstrably reconcile; no unsupported causal assertion; evidence fields and data-as-of are displayed. If data is incomplete, return `insufficient_data` or explicitly qualified analysis, not a confident complete-month answer.

## 5. Owner decisions requested / 需要项目负责人批准的 5 项

| Decision | PM default recommendation / 项目经理默认建议 | Status |
|---|---|---|
| D1 — Retail reporting setup / 零售报表基础 | Fictional NovaMart, SGD, Asia/Singapore, complete calendar months / 虚构零售、SGD、新加坡时区 | PENDING |
| D2 — Metric policy / 业务指标口径 | Completed merchandise gross − discounts − confirmed refunds, using sale/refund event dates; AOV excludes later refunds / 事件时间口径，AOV 单独定义 | PENDING |
| D3 — MVP feature boundary / MVP 功能 | Sales KPI + compare/rank + bounded decline diagnostics + evidence/security; inventory/history deferred / 先销售分析，库存/历史延后 | PENDING |
| D4 — User language / 问题输入语言 | English NL P0, bilingual docs/UI guidance; Chinese NL P1 until benchmarked / 英文优先、中文另测 | PENDING |
| D5 — AI boundary / AI 安全边界 | Structured intent + deterministic compiler, Dify-vs-direct adapter decision pending comparison / 意图模型与确定性编译，Dify 选型未定 | PENDING |

## 6. Immediate tasks / 下一步任务

1. **Owner scope review / 项目负责人审核:** Confirm D1–D5; record exceptions explicitly. / 对上述决策确认或说明例外。
2. **PRD v1 drafting / 编写 PRD v1:** Apply approved decisions and revised acceptance criteria; maintain link to v0.1. / 批准后更新，不覆盖原稿。
3. **Metric Dictionary sign-off / 指标审核:** Review refund event timing, completion/cancellation, AOV, timezone and category history. / 审核退款、取消、时间、类别归属。
4. **Architecture review / 架构审核:** Validate role isolation and query-plan contract; compare Dify and direct API. / 确认权限隔离与查询契约。
5. **Research evidence / 研究证据:** Recruit and document 3–5 user interviews; benchmark two competitor products on same question set, or explicitly accept unvalidated assumptions as risks. / 进行用户访谈、竞品实测或记录风险。
6. **Written Phase 1 gate / 正式准入:** Only proceed to PostgreSQL implementation after signed GO decision. / 签署 GO 后才开发。

## 7. Review outcome / 审核结论

**REVISE AND RESUBMIT — NO-GO for implementation.** / 需要修改与复审，目前不准进入编码阶段。

This document records proposals and review findings, **not owner approval, test execution, or implemented features**. / 本记录仅为建议和审查结果，不代表用户已批准、测试已执行或功能已开发。
