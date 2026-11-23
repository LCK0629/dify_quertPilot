# QueryPilot AI

**A Secure, Evidence-Based Retail Analytics Workbench**  
**安全、可验证、面向零售业务的 AI 数据分析工作平台**

> **Status / 状态:** Phase 1 – Pre-Development Planning (Draft / Not Approved). **No implementation is claimed.**
>
> 当前处于开发前规划阶段；**PRD、核心指标与架构尚未正式批准**，本仓库不代表已完成产品开发。

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

1. Validate the primary retail problems and user workflows / 验证用户需求。
2. Review and approve MVP scope and metric definitions / 审批范围与 KPI 规则。
3. Approve the data model and secure SQL architecture / 审批数据库与安全架构。
4. Establish ground-truth answers and evaluation baselines / 建立标准答案测试集。
5. Pass the Phase 1 **GO / NO-GO** gate before implementation / 通过正式开发审核后才编码。

---

**Document version:** v0.1 · Initial planning baseline: 2026-11-10. Uploaded documents preserve their original content and draft status.