# 01 — Research & User Validation / 商业研究与用户验证

**State / 状态:** Desk research drafted; user validation and hands-on trials outstanding.  
**Research date / 研究日期:** 2026-11-10.

## 1. Research question / 研究核心问题

Is there a defensible need for a small retail business analytics product that provides controlled natural-language analysis, traceable business metrics, and reproducible calculations? / 零售企业是否需要一个规模较小、聚焦自然语言分析、统一指标及可复核计算的平台？

### Problem hypotheses / 待验证问题假设

| ID | Hypothesis / 假设 | Evidence required / 所需证据 | Status |
|---|---|---|---|
| H01 | Managers regularly require unplanned comparisons not covered by dashboards / 管理者常需仪表板之外的临时比较 | 3+ interview examples, frequency and time-cost | Unvalidated |
| H02 | KPI ambiguity produces conflicting decisions / 指标定义不一致影响决策 | Concrete examples of disagreement about refunds, date or AOV | Unvalidated |
| H03 | Users need to inspect evidence before trusting AI answers / 用户希望核实 AI 答案 | Usability tests of evidence panel vs plain response | Unvalidated |
| H04 | Guarded multi-step diagnosis provides more value than a single query / 多维收入诊断更实用 | Task completion and value rating | Unvalidated |
| H05 | A constrained retail schema is sufficient for a strong portfolio MVP / 受控零售数据模型足以展示工程能力 | 60-question coverage and score from test design | Unvalidated |

## 2. Primary users / 主要用户

- **P1 Retail owner / 店主:** monitors net revenue, store/category performance; wants concise verified outcomes; limited SQL expertise (hypothesis).
- **P2 Store manager / 店长:** focuses on store-level comparisons, top/bottom products, margins where cost data exists (do not promise margin absent cost).
- **P3 Business analyst / 分析师:** needs exact metric definitions, filters, query SQL, repeatable numerical comparisons.
- **P4 Data steward/admin / 数据管理人员:** approves metric catalog, authorized views, roles; secondary MVP stakeholder.

**Primary MVP audience / MVP 主要对象:** P1–P3. No enterprise deployment or real data access is assumed.

## 3. Competitor landscape / 竞品研究

This is a product-capability scan of official sources, **not** a head-to-head quality benchmark. / 以下为官方资料研究，不是实测准确率比较。

| Solution / 产品 | Documented capabilities / 官方能力 | Implication for QueryPilot / 设计启示 |
|---|---|---|
| Metabase Metabot | Natural language questions, SQL generation, chart creation and chart analysis; available across plans | A basic NL→SQL→chart app is undifferentiated. Require explicit retail metric contract and tests. |
| ThoughtSpot Spotter | Converts questions to search tokens grounded in governed semantic layer; traceable, auditable queries | Governed, inspectable analytics are established best practice, not unique invention. |
| Power BI Copilot | Semantic-model-connected conversational analysis; organizational capacity licensing requirements | Data model preparation is essential, and advanced features may have cost/access constraints. |
| Tableau Agent in Pulse | Conversational questions across Pulse metrics, supported periods and dimensions; explicit limitations | Target clearly defined metrics, disclose unsupported questions and avoid causal overclaim. |

**Evidence links / 参考依据:**

- Metabase Metabot, official current documentation: https://www.metabase.com/docs/latest/ai/metabot
- Metabase v60 release announcement, 2026-04-16: https://www.metabase.com/releases-ai/metabase-60
- ThoughtSpot Spotter: https://www.thoughtspot.com/product/agents/spotter
- Power BI Copilot requirements: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-enable-power-bi
- Tableau Agent in Pulse Q&A/limitations: https://help.tableau.com/current/online/en-us/pulse_ask_discover_qa.htm
- Tableau release notes dated 2026-10-23: https://help.tableau.com/current/online/en-us/pulse_intro.htm

### Competitive advantage proposed / 差异化主张

**Not novel individually:** conversational queries, charts, semantic layers, query evidence.  
**Portfolio differentiation:** an end-to-end **testable** pipeline: recognized retail intents → versioned metric definitions → authorized structured query → compiled SQL → reconciliation → evidence-bound result and honest uncertainty. / 强调可验证、可审计的工程实现，非宣称首创自然语言 BI。

### Hands-on baseline still required / 待进行竞品实测

Benchmark at least two accessible products with 15 identical fictional retail questions. Record availability, success/failure, metric interpretation, SQL transparency, time to answer and trial/hosting constraints. Do not compare only marketing claims. / 至少以 15 个统一测试问题进行竞品实际体验，记录正确性、透明度、体验和成本条件。

## 4. Research literature / 学术依据

Spider 2.0 (ICLR 2025) uses 632 enterprise text-to-SQL workflows. The authors report 21.3% task success for their o1-preview-based agent baseline, illustrating the difficulty of complex real-world workflows. **This is not an expected QueryPilot accuracy rate** because the domain, schema and benchmark differ. / Spider 2.0 强调企业 SQL 复杂性，该数字不可直接作为本项目预期准确率。

Reference: https://proceedings.iclr.cc/paper_files/paper/2025/hash/46c10f6c8ea5aa6f267bcdabcb123f97-Abstract-Conference.html

## 5. Interview protocol / 用户访谈方案

**Target sample / 目标样本:** 3–5 qualified retail managers/analysts; opportunistic or convenience sample, **not representative market proof**.  
**Session / 单次访谈:** 20–30 min, consent before notes, avoid collecting actual private sales data.

1. When did you last need an answer outside your existing dashboard? / 上次遇到现成仪表板回答不了的问题是什么？
2. How did you get the answer, and how long did it take? / 如何取得答案、耗时多久？
3. When your team says 'revenue', what exactly is included? / 你们的收入指标包含哪些项目？
4. What do you investigate when revenue falls? / 销售下降时首先分析什么？
5. Which business questions need an analyst? / 哪些问题需要分析师协助？
6. Would you trust an AI answer with only a chart? What evidence do you need? / 只有图表是否足够信任？
7. What data would you never want an AI assistant to access? / 什么数据不能让 AI 接触？
8. Rank: speed, accuracy, transparency, flexibility, low cost. / 请对速度、准确、透明、自由度、成本排序。
9. Observe participant attempting three questions on a low-fidelity prototype. / 用低保真原型完成三个任务。
10. Ask for concrete examples and willingness to adopt; avoid leading questions. / 收集真实例子，避免诱导回答。

### User validation acceptance / 用户研究验收

- 3–5 interview records (anonymous role/date/notes); no fabricated participants. / 3–5 份匿名访谈记录。
- At least five confirmed or rejected needs, each linked to evidence. / 至少五项需求有接受或拒绝证据。
- Top 5 questions ranked by frequency, business impact and feasibility. / 高价值问题排序。
- An explicit list of assumptions still unproven. / 记录残余假设。

## 6. Competitor and research decisions / 市场决策

- **Recommend:** retail sales performance + diagnostic breakdowns / 零售销售和诊断式拆分。
- **Avoid:** claiming causality from sales data alone / 不把销售数据等同于因果证据。
- **Avoid:** rebuilding an entire BI authoring system / 不复制完整 BI 平台。
- **Pending:** hands-on study, interview outcomes, pricing/hosting viability for chosen competitors / 待竞品实测与用户验证。