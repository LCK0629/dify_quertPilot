# QueryPilot AI — Phase 1 Planning Pack / 第一阶段规划文件包

**Version / 版本:** v0.1 (Draft, not approved)  
**Planning baseline / 规划基线:** 2026-11-10  
**Current phase / 当前阶段:** Pre-development research and requirements / 开发前研究与需求规划  
**Implementation / 实施状态:** NOT STARTED / 尚未开始

## Purpose / 目标

QueryPilot AI is a secure, retail-focused natural-language analytics workbench. It should translate business questions into **authorized, reproducible analyses**, not simply generate arbitrary SQL.

QueryPilot AI 是面向零售行业的安全自然语言分析工作平台；目标是输出可授权、可复核的数据分析，而不是直接执行不受控制的 AI SQL。

## File map / 文档目录

1. [Research & User Validation](01_RESEARCH_AND_USER_VALIDATION.md) — Competitors, personas, research hypotheses and interview plan / 竞品、用户研究与验证方案
2. [PRD v0.1](02_PRD_V0_1.md) — Requirements, MVP scope, use cases and acceptance criteria / 产品需求与 MVP 范围
3. [Metrics & Data Design](03_METRICS_AND_DATA_DESIGN.md) — KPI rules, conceptual ERD and dataset plan / 指标字典、ERD 与数据集规划
4. [Architecture & Security](04_ARCHITECTURE_SECURITY_ADRS.md) — System architecture, Dify alternatives, security and architecture decisions / 架构、安全与技术决策
5. [Evaluation & Test Plan](05_EVALUATION_AND_TEST_PLAN.md) — Ground-truth results and security/quality test design / 标准答案与测试评估方案
6. [Roadmap & Backlog](06_ROADMAP_BACKLOG_GATE.md) — Tasks, dependencies, risks and phase gate / 开发路线图与审核门槛
7. [Test Scenario Catalog](07_TEST_SCENARIO_CATALOG.md) — 60 supported, 20 ambiguous/unsupported, 50 security test cases / 130 个测试场景规格

## Research status / 研究状态

| Item / 项目 | State / 状态 |
|---|---|
| Preliminary market research / 初步市场研究 | Draft delivered / 初稿已交付 |
| User interviews / 用户访谈 | Not conducted / 未进行 |
| Hands-on competitor benchmarks / 竞品实测 | Not conducted / 未进行 |
| PRD / 产品需求 | Draft, not approved / 草案，未批准 |
| KPI contracts / 业务指标规则 | Proposed, not approved / 待审核 |
| Database ERD / 数据库 ERD | Conceptual design only / 仅概念设计 |
| Architecture & security / 架构安全 | Proposed, not approved / 待审核 |
| Golden answers / 标准测试答案 | Not yet calculated / 未计算 |
| Tests / 测试 | Specifications only, not executed / 仅有设计，未执行 |
| Implementation / 系统开发 | Not started / 尚未开发 |

## Non-negotiable guardrails / 核心原则

- **No unrestricted LLM-generated SQL execution.** / 不允许直接执行未经控制的 LLM SQL。
- **Use read-only access, authorization and bounded query execution.** / 只读、权限检查、查询资源限制。
- **Business metrics must be approved and reproducible.** / 业务指标需统一且可复核。
- **Numerical contribution does not establish causation.** / 数值贡献不等于因果证明。
- **Phase 1 requires formal GO decision before development.** / 未正式审核通过，不进入开发阶段。

## Recommended review order / 审核顺序

1. PRD and MVP scope / 先审核产品需求与范围。
2. Metric dictionary and data model / 再审核指标与数据库设计。
3. Architecture and security / 然后审核架构及安全边界。
4. Evaluation plan and backlog / 最后审核测试方案与开发任务。

## Phase Gate / 开发准入

- Product owner approval / 项目负责人批准：**PENDING**
- PRD approved / PRD 已批准：**NO**
- Metric contract approved / 指标已批准：**NO**
- Architecture approved / 架构已批准：**NO**
- Security model approved / 安全方案已批准：**NO**
- Development authorized / 开发已授权：**NO**

_This repository contains planning materials, not evidence of a working product. / 仓库目前仅存放规划资料，不代表系统已开发。_
