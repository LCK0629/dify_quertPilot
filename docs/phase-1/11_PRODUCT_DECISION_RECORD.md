# 11 — Product Decision Record / 产品决策记录

**Project:** QueryPilot AI  
**Recorded on / 记录日期:** 2026-11-23  
**Evidence / 决策依据:** Project owner in this conversation explicitly approved the **five MVP recommendations in `08_PRD_REVIEW_NOTES.md`** and asked to prepare PRD v1 draft and review core metrics while retaining separate architecture and development-gate review. / 项目负责人在聊天中明确批准 08 审核报告中的五项 MVP 建议，要求推进 PRD v1 和指标审核，架构及开发批准另行处理。

## A. Explicitly approved / 已批准的五项产品决策

| Decision ID | Approved recommendation / 已批准建议 | Status | Scope caveat / 边界说明 |
|---|---|---|---|
| PD-01 / D1 | Fictional NovaMart; SGD; `Asia/Singapore`; full local calendar months / 虚构零售、SGD、新加坡时区 | **APPROVED** | Demo reporting assumptions, not real enterprise configuration / 演示业务假设 |
| PD-02 / D2 | Completed-sale gross less booked merchandise discounts and confirmed merchandise refunds; refund recognized at confirmation date / 完成销售减折扣与确认退款 | **APPROVED — HIGH-LEVEL** | Detailed KPIs, refund reversals, precision and data completeness still require separate metric review / 具体规则未全部冻结 |
| PD-03 / D3 | MVP sales KPI, comparison, rank, bounded revenue decline diagnosis, chart and evidence with security; inventory/history P1 / 首版销售分析为主 | **APPROVED** | See PRD v1 for testable scope / 详见新版 PRD |
| PD-04 / D4 | English NL questions P0; bilingual docs/explanations; Chinese NL questions later after a separate benchmark / 首版英文问句优先 | **APPROVED** | Chinese-language questions not claimed as P0 tested / 不声称已验证中文提问 |
| PD-05 / D5 | LLM returns structured intent; trusted FastAPI service authorizes and deterministically compiles SQL; no unrestricted SQL execution / LLM 仅规划、后端受控编译 | **APPROVED — PRINCIPLE** | Dify vs direct API, deployment details and comprehensive security architecture remain pending / 具体技术方案待评审 |

## B. Distinct approvals explicitly NOT granted / 明确尚未批准的事项

| Area | Status / 状态 | Gate owner / 审核负责人 |
|---|---|---|
| Whole PRD v1 implementation contract / PRD v1 全文正式签核 | **DRAFT / 待审核** | Project owner |
| Detailed M01–M09 metric definitions / 详细指标合同 | **REVIEW PENDING** | Product owner / BA, finance subject expert if real deployment |
| MR-01–MR-10 edge rules and data model completeness / 边界规则与数据质量 | **PENDING** | Product owner / data lead |
| User research and competitor hands-on evidence / 用户与竞品实证 | **NOT DONE** | PM |
| PostgreSQL conceptual/physical schema review / 数据库正式设计 | **NOT APPROVED** | Data architect |
| Dify vs direct LLM integration choice / AI 框架选型 | **OPEN** | Solution architect |
| LLM API contract, auth and threat model / 安全架构和威胁模型 | **NOT APPROVED** | Security architect |
| Golden results and tests executed / 标准答案与测试运行 | **NOT DONE** | QA / data team |
| Phase 1 GO and coding authorization / 开发准入 | **NO-GO** | Project owner |

## C. Documents produced after approval / 本轮新增文件

- `09_PRD_V1_0_DRAFT.md` — PRD v1.0 reflecting PD-01–PD-05. / 新版 PRD 草案。
- `10_METRIC_DEFINITION_REVIEW.md` — Metric contracts, reference fixture expectations and ten open edge decisions. / 核心指标审核。
- `11_PRODUCT_DECISION_RECORD.md` — This owner-approval and residual-risk record. / 当前决策日志。

**Previous versions remain intact / 旧文件保留:** `02_PRD_V0_1.md`, `03_METRICS_AND_DATA_DESIGN.md`, `08_PRD_REVIEW_NOTES.md`.

## D. Next meeting / 下次审核议程

1. Resolve metric edge-case proposals MR-01–MR-10, especially refund reversal, order-level discount allocation and completeness watermark / 确认退款撤回、整单折扣分摊及数据完整性。
2. Perform PRD v1 requirement-to-metric traceability check and explicit signoff / 审查新版 PRD 与指标是否一致。
3. Review conceptual ERD and auth/store scope separately / 单独审查数据库与权限。
4. Decide Dify vs direct API only after documented comparison / 经过比较再决定技术选型。
5. Complete user/competitor evidence or owner-authorized risk acceptance before formal Phase 1 GO / 研究证据或风险接受后才能签发 GO。

**No code, database or full architecture is approved by this decision record. / 本记录不构成编码、数据库开发或架构批准。**
