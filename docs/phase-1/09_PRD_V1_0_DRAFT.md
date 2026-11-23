# 09 — PRD v1.0 Draft / 产品需求文档 v1.0 草案

**Project / 项目:** QueryPilot AI — A Secure, Evidence-Based Retail Analytics Workbench  
**Version / 版本:** v1.0 **DRAFT — PRODUCT DECISIONS APPROVED, FULL PRD NOT APPROVED**  
**Date / 日期:** 2026-11-23  
**Source baseline / 来源:** `02_PRD_V0_1.md`, `08_PRD_REVIEW_NOTES.md`, and the project owner's explicit approval of five MVP recommendations on 2026-11-23.  
**Approval scope / 批准范围:** D1–D5 product recommendations only. **Architecture implementation, Dify selection, accounting validation, security, research, and Phase 1 development GO remain pending.**

## 1. Problem & vision / 问题与愿景

Retail managers need trustworthy answers about sales without writing SQL or relying only on predefined dashboards. QueryPilot AI translates a limited set of retail business questions into authorized analytical plans, independently computed PostgreSQL results, clear charts and auditable explanations.

零售经理需要在不懂 SQL 的情况下获得可信的销售分析。QueryPilot AI 首先在有限零售场景中将问题转换为受授权的分析计划，并提供可复核的查询结果、可视化与数据证据。

**Core showcase / 核心展示:** “Why did our revenue decrease last month?” / “为什么上个月收入下降？” System must explain **numerical contributors**, never assert unsupported causality. / 系统报告数值贡献，不擅自推断因果。

## 2. Approved product decisions / 已明确批准的产品决策

| ID | Decision / 决策 | Approval scope / 批准边界 |
|---|---|---|
| D1 | Fictional **NovaMart**, SGD only, `Asia/Singapore`; full calendar months / 虚构零售企业、新币、新加坡时区、完整日历月 | Product reporting baseline / 产品报表基线 |
| D2 | Net merchandise revenue = completed merchandise gross − posted merchandise discounts − confirmed merchandise refunds; sales dated by completion and refunds dated by confirmation / 商品净收入按完成销售、已入账折扣及确认退款事件计期 | **Demo reporting policy**, subject to detailed metric review; not GAAP/IFRS certification / 演示规则，细节仍须审核 |
| D3 | MVP includes sales KPI, ranking, period and store/product comparison, bounded revenue-decline diagnostics, charts, evidence and security; inventory/history are P1 / MVP 集中销售指标、排名、对比、有限下降诊断及安全可追溯 | Scope baseline / MVP 产品范围 |
| D4 | **English-language business questions P0**; bilingual explanations/docs as appropriate; Chinese-language NL question interpretation only after distinct evaluation (P1 candidate) / 英文问题先验证，中文自然语言输入另行评估 | Language scope / 语言范围 |
| D5 | LLM produces **typed intent/structured plan** only; trusted FastAPI layer validates scope and compiles SQL deterministically / LLM 不执行任意 SQL，后端受控编译 | **Safety principle approved**; Dify vs direct API and full architecture **not yet approved** |

## 3. Users and authorized scopes / 用户与权限

| Persona / 角色 | Goal / 目标 | MVP authorization |
|---|---|---|
| Retail owner / 零售企业老板 | Whole-business KPIs and category/store breakdown / 总览销售与门店表现 | All **demo** stores through trusted backend test principal / 在可信测试身份下访问所有虚构门店 |
| Store manager / 店长 | Own-store performance / 单门店表现 | Only assigned store IDs, enforced by backend **and** DB access controls / 后端及数据库均须限域 |
| Business analyst / 商业分析师 | Inspect evidence, executed SQL and definitions / 查看计算与查询依据 | Only stores explicitly assigned to their principal; analyst role does not bypass scope / 分析师不自动拥有全部门店权限 |
| Data steward / 指标管理员 | Review versioned metric definitions / 维护统一指标 | Developer-managed config in MVP, no user-facing metric administration UI / 首版不开发指标后台 |

No actual personal customer data is required. / 不需要真实客户个人信息。

## 4. Core journeys / 核心流程

**J1 — KPI / 关键指标:** “What was October 2026 net merchandise revenue?” → parse metric and period → authorize → calculate → display SGD amount, metric version, scope, source `data_as_of`, query evidence. / 返回数额及可追溯依据。

**J2 — Ranking / 排名:** “Top 10 products by net revenue in October 2026.” → approved metric/product dimension → bounded rank/table; stable tie behavior; authorized stores only. / 限域排序。

**J3 — Comparison / 对比:** “Compare September and October 2026 net revenue by store.” → exact local month windows → current/prior, signed delta, percentage only if previous value > 0. / 比较两个月度及增长率。

**J4 — Bounded diagnosis / 有限诊断:** “Why did our revenue decrease last month?” → resolve last **complete real calendar month** from request time in Singapore (not latest dataset month), compare preceding month → compute total, category/store contributions and **gross–discount–refund accounting bridge**; show evidence and no unsupported causes. / 完整日历月诊断；缺数需提示。

**J5 — Clarify / 歧义澄清:** “How are sales?” → request metric or time period only when necessary; preserve existing known constraints; no guessing. / 缺参数先澄清。

**J6 — Refuse / 拒答:** requests for cross-store disclosure, customer emails, arbitrary SQL or `DELETE` → deny without executing prohibited query, reveal no restricted data. / 越权及写入拒绝。

**J7 — Insufficient data / 数据不足:** requested month has missing or nonfinal data → clearly report insufficient data; do not silently reinterpret period as latest complete dataset month. / 数据不全不可假装已完成。

## 5. MVP scope / 第一版边界

### P0 — Release requirements / 正式首版必须实现

- **Sales metrics:** M01 gross merchandise sales; M02 booked discount; M03 confirmed merchandise refund; M04 net merchandise revenue; M05 completed orders; M06 sold units; M07 AOV; M08 percent change; M09 category/store delta.
- **Analytical functions:** single KPI, top-N ranking, monthly comparison, category/product/store grouping, one bounded decline diagnostic.
- **Evidence & UI:** natural-language input (English), numerical summaries with only supported statements, KPI card, bar/line/table, metric details, source freshness, authorized SQL/query-plan evidence, safe errors.
- **Safety & quality:** typed plan validation, deterministic SQL templates, least privilege, read-only execution, store isolation, audit metadata, reproducible test fixtures and independent reference answers.

### P1 / 非首版阻塞项目

- Inventory low-stock analysis; persistent query history; saved analysis links; Chinese-language NL input **after** a separate evaluation.
- P1 is not silently promoted into P0. / P1 不能自动变成必须功能。

### Excluded / 排除

- Causal inference (“competitor X caused decline”), predictive forecasting, churn modeling, arbitrary SQL, writeback, unrestricted autonomous agents, customer PII access, enterprise multi-tenant SaaS, general dashboard-builder and production SLA.

## 6. Functional requirement matrix / 功能需求与验收

| ID | Priority | Requirement / 需求 | Measurable acceptance / 可验证验收 |
|---|---|---|---|
| FR-01 | P0 | English question input / 英文问句输入 | Each request yields one typed outcome with a request ID; no silent failure / 每次返回可识别状态 |
| FR-02 | P0 | Intent schema / 结构化分析意图 | Validated metric ID, time range, dimensions, filters, intent, sort/limit; invalid combinations cannot compile / 格式不符拒编译 |
| FR-03 | P0 | Metric catalog / 指标字典 | Each metric has definition, version, unit, allowed dimensions/filters and zero/negative rules / 每项指标有版本和规则 |
| FR-04 | P0 | Trusted query compilation / 受控 SQL 编译 | Only approved compiler templates and identifiers; values parameterized; raw LLM SQL never executed / 禁止直接执行生成 SQL |
| FR-05 | P0 | Secure execution / 安全执行 | Test roles use least-privilege read-only DB path, bounded rows/time, audited policy decisions / 只读与限额受测 |
| FR-06 | P0 | Exact KPI answers / KPI 精度 | M01–M07 reconcile to independent cent-precision reference fixtures / 核心数值按分对账 |
| FR-07 | P0 | Ranking & comparison / 排名与比较 | Correct month boundaries, store/category/product grouping and deterministic tie handling; previous <=0 displays N/A growth / 零与负基期不乱算百分比 |
| FR-08 | P0 | Revenue diagnosis / 收入下降诊断 | `Σ(category deltas)=total delta`, `Σ(store deltas)=total delta`, `Δgross−Δdiscount−Δrefund=Δnet`; each scoped identically, money exact to SGD cents / 三种对账 |
| FR-09 | P0 | Charts & table / 图表与数据表 | KPI for scalar, line for time series, bar for ranking, table for detailed comparison; chart numbers agree with table / 图表与表格一致 |
| FR-10 | P0 | Evidence output / 分析依据 | Successful response shows metric version, period, timezone, authorized scope, query provenance, `data_as_of`, results and caveats / 全部结果可追溯 |
| FR-11 | P0 | Clarify/unsupported/insufficient data / 歧义拒答数据不足 | Missing essentials or unavailable evidence yields non-execution or qualified response; cannot fabricate metric/period/causes / 不猜测 |
| FR-12 | P0 | Store authorization / 门店权限 | Denied cross-store requests disclose zero restricted data to client, logs and model; server never trusts client role / 门店隔离必须通过测试 |
| FR-13 | P0 | Audit & errors / 审计与错误 | Request ID, metric version, decision, safe query hash, latency, result count, status logged without secrets or customer PII / 不记录机密 |
| FR-14 | P1 | Inventory snapshots / 库存快照 | Threshold and snapshot freshness explicit; stale/no stock data not silently accepted / 数据过期提示 |
| FR-15 | P1 | Query history / 查询历史 | History is user-scoped, with reauthorization on viewing / 查看历史仍检查权限 |
| FR-16 | P1 | Chinese NL input / 中文自然语言提问 | Separate benchmark set and acceptance gate before enabling / 独立测试后才开放 |

## 7. Response contract & outcomes / 响应结构与状态

**Allowed outcome types / 可用状态:** `success`, `clarification`, `unsupported`, `denied`, `insufficient_data`, `execution_error`.

**Success payload / 成功结果字段:** `request_id`, `resolved_question`, `intent`, `metric_id`, `metric_version`, `time_start`, `time_end`, `timezone`, `currency`, `authorized_scope`, `data_as_of`, `table`, `chart_spec`, `backend_compiled_query_evidence`, `narrative`, `limitations`.

Other statuses always include `request_id`, safe message, category; details only where authorized. / 其他状态须安全说明，不显示内部错误堆栈。

**NL language:** English questions are tested for first release; Chinese instructions and bilingual display text may be added without claiming Chinese NL test coverage. / 英文自然语言问题先通过评测；双语解释不等于中文问句已合格。

## 8. Reporting assumptions & limits / 报表约定与边界

- Currency `SGD`; timezone `Asia/Singapore`; one fictional retailer NovaMart / 新币、新加坡时区、虚构企业。
- A calendar month covers local midnight inclusive through next local month midnight exclusive, `[start,end)`; “last month” means prior **complete** calendar month relative to question time / 上个完整日历月。
- `M04 = completed gross merchandise sales - line discounts - confirmed merchandise refunds` with sales recognized at completion, refunds at confirmation; excludes delivery/tax / 商品净收入按事件时间，排除税运费。
- AOV is **completed-order merchandise sales after discounts, before subsequent refunds**, divided by completed-order count; label it distinctly / AOV 不是事件净收入除订单数。
- Discounts/returns attributable to original store and historical sale-time category; original sales/refund facts never joined raw in a way that multiplies gross amounts / 退款保留原归属，先聚合再关联。
- Dataset may have incomplete months; return honest missing-data state, not confident numeric diagnosis / 数据不完整时不得伪造结论。
- Real finance/accounting deployment would need separate rules and owner approval; these are **fictional demo** reporting conventions / 并非真实会计准则认证。

**Detailed metric review and remaining open rules / 详细指标待核问题:** see `10_METRIC_DEFINITION_REVIEW.md`.

## 9. Quality and release measures / 质量指标

All are targets, **not achieved results** / 均为目标而非测试成绩：

| Measure / 指标 | Initial acceptance proposal / 初始要求 |
|---|---|
| End-to-end supported-answer correctness / 支持问题正确率 | ≥90% over at least 60 independent golden questions / 至少60题，正确率≥90% |
| Core KPI reconciliation / 核心业务指标对账 | 100% on predefined reference assertions / 100% |
| Security isolation & unsafe-query rejection / 安全拦截 | 100% of defined 50-case adversarial suite / 50个定义攻击测试全通过 |
| Traceability / 数据可追溯性 | 100% successful answers show required evidence / 成功答案全部展示 |
| Grounded narratives / 有依据的解释 | No unsupported numerical/causal claims in ≥30 reviewed responses / 至少30条抽检无虚构 |
| Usability / 可用性 | ≥80% task completion among ≥5 testers / 至少5位用户 |
| Latency / 延迟 | Provisional p95 ≤15s on ≥30 representative runs, conditions and costs recorded / 待实际验证 |

## 10. Development slices / 逐段交付计划（仅计划）

- **S0 — Pre-development gate / 开发前门槛:** Approve research risk disposition, metric dictionary, ERD, security threat model, Dify/direct ADR, evaluation plan and product PRD. / 先审核才能编码。
- **S1 — Governed KPI foundation / 受控 KPI 基础:** Physical PostgreSQL data model + reference fixtures, trusted metric calculation, store-scoped API, evidence; security present from first executable query. / 第一条查询也必须有权限控制。
- **S2 — Ranking & period compare / 排名与环比:** Add controlled dimensions, date rules, charts and golden tests. / 排名时间比较。
- **S3 — Diagnostic bridge / 下降诊断:** Add fixed category/store/gross–discount–refund decomposition, reconciliation, grounded narratives. / 可对账的收入诊断。
- **S4 — UI, hardening & evaluation / 前端和最终测试:** User journey review, complete security and golden suites, audit and reproducibility. / 演示前验收。

These are **delivery slices**, not claims of code completion. / 不是已完成功能。

## 11. Open approvals / 仍待审核

| Area | State | Needed evidence / 所需证据 |
|---|---|---|
| D1–D5 high-level product choices / 五项产品决策 | **APPROVED by project owner / 已获明确同意** | Recorded in `11_PRODUCT_DECISION_RECORD.md` |
| Detailed metric contract & refund edge cases / 具体指标与退款边界 | **REVIEW PENDING / 待审核** | Approve exact examples and no-double-count rules |
| User interview evidence / 用户访谈 | **NOT COMPLETED** | 3–5 qualified interviews or explicitly accepted evidence limitation |
| Competitor hands-on benchmarking / 竞品实测 | **NOT COMPLETED** | Standard question comparison and limitations |
| Physical/authorization architecture & Dify selection / 架构与 Dify 选型 | **NOT APPROVED** | ADR and security review |
| Golden answers & tests / 标准答案及测试 | **NOT EXECUTED** | Independent fixtures, expected outputs, recorded run results |
| Development authorization / 开发许可 | **NO-GO** | Explicit later signoff on all Phase 1 gate items |

## 12. PRD v1 review outcome / v1 文档结论

**Product direction and five MVP recommendations approved; this consolidated PRD v1.0 remains a review draft, not an accepted implementation contract.** / 五项产品决策已获批准，但 v1.0 综合需求文档仍为待复审草案，不代表实现或开发许可。

**Next review / 下一审核:** Validate metric edge cases and finalize acceptance criteria, then separately review architecture and Phase 1 gates. / 下一步审核指标边界、验收标准，再分别审核架构与开发门槛。
