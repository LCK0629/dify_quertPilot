# QueryPilot AI

**A Secure, Evidence-Based Retail Analytics Workbench**  
**安全、可验证、面向零售业务的 AI 数据分析工作平台**

> **Status / 状态:** Phase 1 – Pre-Development Planning. MVP, metric, database design and development readiness plan baselines approved; architecture direction approved with conditions. **Development NO-GO.**
>
> MVP、指标、数据库设计及开发准备计划基线已批准，系统架构方向附条件批准；完整 PRD、剩余决策及开发准入仍待审核。

## Project vision / 项目目标

Enable retail business users to ask questions in everyday language, obtain safe and reproducible PostgreSQL query results, and inspect evidence-grounded analytics.

让零售业务用户通过自然语言查询 PostgreSQL 数据库，获得安全、可复核且有数据依据的分析结果。

**Core scenario / 核心场景:** “Why did our revenue decrease last month?”  
The MVP will investigate numerical contributions and show supporting calculations, **not claim unproven causal explanations**.

## Planned technology / 拟采用技术

- **Database:** PostgreSQL
- **Backend / Query Governance:** Python + FastAPI
- **AI interpretation:** LLM, with Dify vs direct API integration still under review
- **Frontend:** React
- **Version control:** GitHub

## Historical product decision update / 历史产品决策（2026-11-23）

The project owner **approved five MVP product recommendations** (NovaMart/SGD/Singapore time, demo revenue policy, sales-focused MVP, English-first questions, and structured-intent → governed SQL principle). This is **not** approval of PRD v1 in full, detailed metric contracts, the Dify implementation choice, security architecture, or the Phase 1 development gate.

项目负责人已批准五项 MVP 产品方向，但**尚未批准** PRD v1 全文、详细指标合同、Dify 最终选型、安全架构或开发准入。系统尚未开始开发。

- [PRD v1.0 Draft / 新版需求草案](docs/phase-1/09_PRD_V1_0_DRAFT.md)
- [Metric Definition Review / 指标审核](docs/phase-1/10_METRIC_DEFINITION_REVIEW.md)
- [Product Decision Record / 产品决策日志](docs/phase-1/11_PRODUCT_DECISION_RECORD.md)

## Current approval update / 当前审批状态（2026-11-26）

- [Architecture v1.1](docs/phase-1/12_SYSTEM_ARCHITECTURE_SECURITY_DESIGN_V1_1.md) — [conditional approval](docs/phase-1/13_ARCHITECTURE_APPROVAL_RECORD.md).
- [Conceptual ERD & Data Model v1.0](docs/phase-1/14_CONCEPTUAL_ERD_DATA_MODEL_V1_0.md) — approved baseline.
- [Physical Database Design v1.0](docs/phase-1/15_PHYSICAL_DATABASE_DESIGN_V1_0.md) — approved baseline.
- [Database Design Approval Record](docs/phase-1/16_DATABASE_DESIGN_APPROVAL_RECORD.md) — QP-APR-003/004; OD-01–07 remain open. GitHub design references summarize the Word candidates.

- [Development Readiness & Implementation Plan v1.0](docs/phase-1/17_DEVELOPMENT_READINESS_IMPLEMENTATION_PLAN_V1_0.md) — [plan approval QP-APR-006](docs/phase-1/18_DEVELOPMENT_READINESS_APPROVAL_RECORD.md). Planning baseline approved; implementation not authorized.

- [Business Metric Dictionary v1.0](docs/phase-1/19_BUSINESS_METRIC_DICTIONARY_V1_0_APPROVED.md) — DEC-BA-001 approved business baseline; tests specified, not executed.
- [OD Decision Resolution v1.0](docs/phase-1/20_OD_DECISION_RESOLUTION_V1_0.md) — seven proposed dispositions, reviewed for PRD consistency; all OPEN pending acceptance.
- [Database Design v1.1 Change Proposal](docs/phase-1/DB_DESIGN_V1_1_CHANGE_PROPOSAL.md) — proposed security-registry and database authorization amendments; not approved.

Next: obtain OD-01–07 dispositions, finalize the permission matrix, identity/security registry and nonforgeable database scope binding, reconcile and sign off the PRD, close PRE-01–PRE-10, and obtain a separate Development GO decision. See the current decision index in [00 Start Here](docs/phase-1/00_START_HERE.md).

## Phase 1 planning pack / 第一阶段文件

| Document | Description / 说明 |
|---|---|
| [00 Start Here](docs/phase-1/00_START_HERE.md) | Read this first; approval status and document map / 使用说明及审核状态 |
| [01 Research & User Validation](docs/phase-1/01_RESEARCH_AND_USER_VALIDATION.md) | Market, competitors, personas and validation plan / 市场、竞品、用户研究 |
| [02 PRD v0.1](docs/phase-1/02_PRD_V0_1.md) | Product scope, user stories and acceptance criteria / 产品需求及验收 |
| [03 Metrics & Data Design](docs/phase-1/03_METRICS_AND_DATA_DESIGN.md) | KPI definitions, conceptual data model / 指标定义、概念数据库设计 |
| [04 Architecture & Security](docs/phase-1/04_ARCHITECTURE_SECURITY_ADRS.md) | Proposed architecture and security boundaries / 架构与安全 |
| [05 Evaluation & Test Plan](docs/phase-1/05_EVALUATION_AND_TEST_PLAN.md) | Ground-truth testing and evaluation strategy / 测试评估方案 |
| [06 Roadmap & Backlog](docs/phase-1/06_ROADMAP_BACKLOG_GATE.md) | Dependencies, tasks and development approval gate / 路线图及开发准入 |
| [07 Scenario Catalog](docs/phase-1/07_TEST_SCENARIO_CATALOG.md) | 60 supported, 20 ambiguous/unsupported and 50 security test specifications / 测试场景目录 |

## What is done / 已有资料

Phase 1 **draft documents** and **test specifications** have been prepared. They are **not equivalent to executed tests, approved requirements, a deployed database or working software**.

## Next steps / 下一步

1. Complete user/competitor evidence or explicit risk acceptance and full PRD alignment.
2. Close or explicitly disposition OD-01–07 and independent BA/security reviews.
3. Execute the approved readiness plan's decision-closure workflow and approve the evaluation specifications; do not begin implementation.
4. Obtain separate development GO before implementation; no executed tests or working database claimed.

---

**Document version:** v0.1 · Initial planning baseline: 2026-11-10. Uploaded documents preserve their original content and draft status.