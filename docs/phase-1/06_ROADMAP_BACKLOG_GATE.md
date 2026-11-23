# 06 — Roadmap, Backlog, Risks & Phase Gate / 路线图、任务清单、风险与开发准入

**Version:** 0.1 DRAFT  
**Date:** 2026-11-10  
**Planning principle:** dependencies first, no implementation until Phase 1 review passed. / 按依赖排序，未批准不编码。

## 1. Proposed 3-week pre-development plan / 三周开发前计划

| Window / 时间 | Milestone / 里程碑 | Planned output / 预期成果 | Acceptance / 验收 |
|---|---|---|---|
| W1: Nov 10–16, 2026 | Research and user validation / 研究与用户验证 | Research report, interview notes, ranked top questions | 3–5 interviews or recorded evidence limitations; 2 competitor hands-on reviews targeted |
| W2: Nov 17–23, 2026 | Product rules and requirements / 产品范围与业务规则 | PRD v1, KPI dictionary, use cases, conceptual ERD | No ambiguous P0 requirements, revenue rules consistent, owner reviews scope |
| W3: Nov 24–30, 2026 | Architecture/security/evaluation review / 架构与评审 | ADRs, threat model, test matrix, nonfunctional targets, gate report | Owner approves boundary, test plan, architecture and risk disposition |

Dates are proposed, not appointments or work performed. Any user interviews or review sessions require actual coordination. / 时间只是计划，不代表已经安排了访谈。

## 2. Dependency-ordered backlog / 按依赖排序的任务池

| ID | Priority | Task / 任务 | Depends on / 依赖 | Deliverable / 输出 | Done when / 完成定义 | State |
|---|---|---|---|---|---|---|
| R-01 | P0 | Validate retail problems / 验证业务痛点 | None | Interview evidence | 3–5 documented qualified sessions, top 5 questions ranked | NOT STARTED |
| R-02 | P0 | Test competitor experience / 竞品实测 | Sample questions | Benchmark matrix | 2 products, 15 same questions, honest limitations | NOT STARTED |
| P-01 | P0 | Product scope definition / 功能范围冻结 | R-01 | PRD v1 approval | All P0 journeys, exclusions and acceptance approved | DRAFT |
| P-02 | P0 | Revenue and KPI contracts / 统一指标规则 | P-01 | Metric Dictionary v1 | Refund/date/AOV conventions signed off and goldens reconciled | DRAFT |
| D-01 | P0 | Conceptual entity/data plan / 概念数据规划 | P-02 | ERD + Data Dictionary | Fact grains, keys, scopes, quality rules reviewed | DRAFT |
| A-01 | P0 | Architecture review / 架构审核 | P-01, D-01 | Approved ADRs and diagram | Trust boundaries, adapter and execution model approved | DRAFT |
| S-01 | P0 | Threat model and roles / 安全威胁与权限 | P-01, A-01 | Security requirements | Cross-store attacks, DB role/RLS caveats reviewed | DRAFT |
| E-01 | P0 | Golden test blueprint / 标准答案测试规划 | P-02, D-01 | Test manifest blueprint | 60 supported + 20 refusal + 50 security scenarios specified | DRAFT |
| U-01 | P0 | User journey and low-fi UI / UI 流程草图 | P-01 | Four screen wireframes | Evidence, errors and scope controls covered | DRAFT |
| F-01 | P0 | Phase 1 gate review / 立项评审 | All P0 above | Signed gate decision | Owner accepts risk and approves requirements/architecture | BLOCKED |
| DEV-01 | Later | Physical PostgreSQL schema / 物理数据库 | F-01 approval | Versioned schema and fixtures | DDL, relationships and reconciliation tests pass | NOT AUTHORIZED |
| DEV-02 | Later | Secure FastAPI query service / 安全后端 | DEV-01 and approved design | Backend + tests | Compiler, read-only execution, roles pass tests | NOT AUTHORIZED |
| DEV-03 | Later | LLM intent integration / AI 接入 | DEV-02 and adapter selection | Adapter + evaluation | Meets supported-set accuracy/refusal | NOT AUTHORIZED |
| DEV-04 | Later | React analytics workbench / 前端工作台 | DEV-02 | UI + evidence panel | Core journeys complete and accessible | NOT AUTHORIZED |
| DEV-05 | Later | Integrated evaluation / 完整评估 | DEV-01–04 | Report | Meets approved release gates | NOT AUTHORIZED |

**No repo work:** This planning pack does not create issues, commits, branches or code in GitHub. / 尚未在 GitHub 修改仓库、创建 issue 或提交代码。

## 3. Risk register / 风险登记表

| ID | Risk / 风险 | Impact | Likelihood | Mitigation / 缓解 | Owner |
|---|---|---|---|---|---|
| K01 | Correct SQL, wrong KPI / SQL 对但业务错 | High | High | Metric contracts + independent golden tests | Data/BA lead |
| K02 | Cross-store data exposure / 数据越权 | Critical | Medium | Server-side scopes + DB least privilege/RLS + adversarial testing | Backend/security lead |
| K03 | Hallucinated cause / 虚构根因 | High | High | Rule-based diagnostics, constrained narrative, explicit uncertainty | AI/BA lead |
| K04 | Scope creep into complete BI product / 功能膨胀 | High | High | Freeze P0, P1 conditional, change review | PM/product owner |
| K05 | Dify deployment overhead / Dify 维护负担 | Medium | Medium | Compare direct API + adapter, local resources assessment | Architect |
| K06 | Synthetic dataset too easy / 模拟数据缺乏挑战 | High | Medium | Scenario-driven edge fixtures and holdout cases | Data lead |
| K07 | Model latency/API expense / AI 延迟费用 | Medium | Medium | Usage caps, benchmark provider, cache only safe metadata | AI/architect |
| K08 | Refund/date policy ambiguous / 退款时间规则模糊 | High | High | Metric dictionary sign-off before ERD implementation | Product owner |
| K09 | No available target users / 缺少访谈对象 | Medium | Medium | Recruit relevant reviewers, explicitly mark as unvalidated if unavailable | PM |
| K10 | Overstated portfolio claims / 作品集夸大完成度 | Medium | Medium | Evidence-based status tracker and final demo reproducibility | PM |

## 4. Decision log / 决策日志

| ID | Decision needed / 待决定 | PM recommendation / 建议 | Status |
|---|---|---|---|
| DEC-01 | Target audience / 用户 | Retail managers and analysts / 零售经理和分析师 | PROPOSED |
| DEC-02 | Product wedge / 核心切入点 | Sales diagnosis with evidence / 销售变化贡献分析 | PROPOSED |
| DEC-03 | Currency/timezone / 币种/时区 | SGD, Asia/Singapore for fictional NovaMart | PENDING APPROVAL |
| DEC-04 | Revenue policy / 收入计算 | Event-date net merchandise revenue, refunds recognized on confirmation date | PENDING APPROVAL |
| DEC-05 | AI/SQL boundary | Structured intent → deterministic trusted compiler | PENDING APPROVAL |
| DEC-06 | Dify or direct model adapter / Dify 选型 | Keep adapter, benchmark before lock-in | OPEN |
| DEC-07 | P1 inventory/history / 库存查询历史 | Defer until P0 meets gates | PROPOSED |
| DEC-08 | Chinese language MVP / 中文问题首发 | English verified initial set, Chinese exploratory until separate benchmark | OPEN |
| DEC-09 | Security data scope / 授权范围 | Two role patterns, store scoped access in backend and DB | PENDING APPROVAL |

## 5. Phase-gate checklist / 进入开发审核清单

- [ ] G01: Research assumptions explicitly validated/rejected or accepted with documented risk. / 用户假设可追溯。
- [ ] G02: Target users and top 5 scenarios approved. / 主要场景获批准。
- [ ] G03: PRD v1 P0/P1/out-of-scope frozen and accepted. / PRD 功能范围冻结。
- [ ] G04: Revenue, refund, AOV and calendar business metric contracts approved. / 核心指标获批准。
- [ ] G05: ERD/entity grains/data quality and synthetic dataset plan approved. / 数据设计获批准。
- [ ] G06: LLM boundary, SQL compilation and Dify/direct ADR approved. / 架构决策获批准。
- [ ] G07: Security threat model, role scope and data access policy approved. / 安全策略获批准。
- [ ] G08: Test matrix, thresholds and measurement protocol approved. / 评估方法获批准。
- [ ] G09: Wireframes and evidence explanation UX reviewed. / 主要界面获审核。
- [ ] G10: Owner records written GO / CONDITIONAL GO / NO-GO decision. / 负责人书面决定。

### Gate decision form / 开发准入记录

- Review date / 审核日期: __________
- Reviewer / 审核人: __________
- Approved PRD revision / PRD 版本: __________
- Approved metric dictionary revision / 指标版本: __________
- Approved architecture ADR revision / 架构版本: __________
- Open high risks / 未解决高风险: __________
- Decision / 结论: **NO-GO (default until signed)** / 默认不批准开发
- Conditions, if any / 附带条件: __________

## 6. Next action / 立即执行事项

**PM task / PM 任务:** Present PRD and metric definitions for owner review, prepare interview materials, recruit 3–5 relevant users, and perform two documented competitor hands-on evaluations. No implementation work is authorized at this point. / 下一步先确认范围与指标、进行访谈和竞品实测；任何代码必须等待审批。