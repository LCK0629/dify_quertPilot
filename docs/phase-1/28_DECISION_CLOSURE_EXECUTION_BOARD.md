# QueryPilot AI — Pre-Development Decision Closure Execution Board

**ID:** QP-PM-EXEC-2026-11-27  
**Baseline:** 27 November 2026, Asia/Singapore  
**Project state:** Pre-Development Decision Closure  
**Gate:** **DEVELOPMENT NO-GO** (approved plans and design baselines are not approval to implement)  
**Purpose:** Turn remaining P0 decisions into tracked, reviewable work with exact prerequisites, evidence and accountable *roles*. GitHub issues are opened, but none is assigned to a named engineer or scheduled for background execution.

## 1. Confirmed baseline — do not reopen without change request

- MVP product directions approved; M01–M09 and MR-01–MR-10 business baseline approved.
- Conceptual and physical retail DB v1.0 approved with implementation conditions.
- Architecture/security direction v1.1 approved with conditions; modular FastAPI controls policy/execution; Dify not trusted for SQL or authorization.
- Readiness plan v1.0 approved, **not** Development GO.
- OD-01–07: owner approval QP-APR-007, independent validation pending.
- Role & Permission Matrix: owner approval QP-APR-008, independent validation pending.
- Security Registry v1.0: proposed only, **not owner-approved**.
- Nonforgeable DB principal binding, identity/session ADR, Dify choice, full PRD v1.1, quality/research evidence and final GO: outstanding.
- No actual DDL, database fixtures, app code, model integration, or implementation tests represented as done.

## 2. GitHub execution board — nine issues

| Order | Issue | Responsible roles | Dependency / required evidence | Status |
|---|---|---|---|---|
| 1 | [#1 PRE-04 Security Registry](https://github.com/LCK0629/dify_quertPilot/issues/1) | Security + DB, Product Owner approval | [Formal Security Review 29](29_SECURITY_REGISTRY_SECURITY_REVIEW_FOR_APPROVAL.md) recommends REVISE & RESUBMIT; revise SR-D01–06, trust model, tests and exact candidate | OPEN; revision authorized; revised candidate pending; NOT APPROVED |
| 2 | [#2 PRE-05 PostgreSQL authorization](https://github.com/LCK0629/dify_quertPilot/issues/2) | Security + DB + Backend | Coordinate #1 and #3; sign nonforgeable DB identity/privilege ADR, no caller-asserted scope | BLOCKER |
| 3 | [#3 PRE-06 Identity/session](https://github.com/LCK0629/dify_quertPilot/issues/3) | Security + Solution Architect | Coordinate #1, #2; verified session, CSRF, bootstrap, revocation, audit, credential lifecycle | OPEN |
| 4 | [#4 PRE-01 PRD v1.1](https://github.com/LCK0629/dify_quertPilot/issues/4) | PM + BA, Security/DB reviewers | Draft in parallel; full signoff requires #1–3, reconcile ALIGN-01–12 | OPEN |
| 5 | [#5 DB v1.1 design reconciliation](https://github.com/LCK0629/dify_quertPilot/issues/5) | DB + Security + BA | Depends on #1–3, preserve approved retail grain/metrics | OPEN |
| 6 | [#6 PRE-07 Dify/direct ADR](https://github.com/LCK0629/dify_quertPilot/issues/6) | Solution Architect + AI | Coordinate #3/4; provider, egress, licensing, cost and typed adapter selection | OPEN |
| 7 | [#7 PRE-08 Evaluation protocol](https://github.com/LCK0629/dify_quertPilot/issues/7) | QA + BA + Security | Independent goldens, acceptance and adversarial test specs; #2, #4 | OPEN |
| 8 | [#8 PRE-09 User/competitor evidence](https://github.com/LCK0629/dify_quertPilot/issues/8) | PM + BA + Product Owner | Conduct and record actual work or explicit risk acceptance; may run in parallel | OPEN |
| 9 | [#9 PRE-10 Final Development Gate](https://github.com/LCK0629/dify_quertPilot/issues/9) | PM + Product Owner + Security | All #1–8, no critical open blocker; written QP-APR-DEV-GO-001 | NO-GO |

**Owners are role responsibilities, not GitHub account assignments.** No team member's consent, schedule or availability is assumed.

## 3. Proposed review cadence — estimates, not booked meetings

| Window (SGT) | Working focus | Decision checkpoint |
|---|---|---|
| **Nov 27 (Fri)** | Verify baselines, publish SR review and DB auth candidate, open GitHub issue board | Initial backlog and risk order recorded |
| **Nov 30–Dec 1 (Mon–Tue)** | Security Registry SR-D01–06 review; begin DB identity/options and session design; start research outreach | Explicit SR design disposition or revision request; no implied approval |
| **Dec 2–3 (Wed–Thu)** | Nonforgeable DB authorization ADR and identity/session decision; parallel PRD v1.1 and Dify comparison | Security/DB cross-review of trust boundary, before DB v1.1 freeze |
| **Dec 4–7 (Fri–Mon)** | DB v1.1/PRD alignment, Dify decision, reference-test specification and user/competitor evidence | Drafts submitted for owner/independent review |
| **Dec 8–9 (Tue–Wed)** | Integrate all signed decisions, security risk reviews and remaining evidence | Determine whether all G-01–17 requirements have evidence |
| **Dec 10–11 (Thu–Fri)** | **Earliest tentative final gate window only if dependencies complete** | Separate Development GO or documented NO-GO; no automatic development start |

**Timing risk:** If credible identity isolation cannot be demonstrated within accepted architectural assumptions, the schedule slips; this is a safety gate, not a feature to waive. If interviews/access are unavailable, document limitation and obtain explicit risk acceptance rather than claiming completion. No background work or automatic future delivery is claimed by these planned windows.

## 4. Sequence, parallel work, hard gates

- **Primary critical path:** #1 registry → #2 + #3 identity/DB authorization → #5 integrated DB design → #4 PRD owner signoff → #9 gate.
- **Parallel allowed:** #4 PRD drafting, #6 Dify comparison, #7 test planning, #8 real user/competitor research.
- **Cannot start:** SQL migrations, security registry DDL, app/backend/AI/frontend implementation, synthetic dataset generation or execution of system tests until written Development GO.
- **No partial authorization:** A staff chatbot user may have `chat.use` without financial metrics. Any permitted request still requires independent metric, action, store, disclosure and DB boundary checks.

## 5. Required signoffs and definition of done

| Deliverable | Acceptance evidence |
|---|---|
| Security registry | Reviewed exact schema/versions, SR-D01–D06 owner disposition, independent Security/DB review, negative test design |
| DB authorization + identity | Signed ADR for verified principal mapping and protected grants, RLS/definer privilege test plan, session/revocation, residual risk |
| Database v1.1 | Separate approved design amendment consistent with M01–M09, OD-01–07, QP-APR-008 and DB privilege model |
| PRD v1.1 | Owner signoff with requirement/metric/permission traceability, English-first scope and sanitized evidence contract |
| Dify choice | Signed vendor/adapter ADR with license, cost, egress, retention and fallback analysis |
| Evaluation/research | Independent oracle methods and signed test specs; actual interviews/competitor findings or explicit limitations |
| Final gate | Every critical design issue has signed resolution; Security and Product Owner issue distinct GO/NO-GO record |

## 6. PM controls

1. GitHub Issues #1–9 are the active task tracker, `docs/phase-1/` stores versioned decisions.
2. Do not close issues on document creation alone; closure requires accepted evidence and decision record linked in issue.
3. Historical review drafts do not override later approval records.
4. Any change to approved business metrics, OD policies, permission grants or database grain requires formal change request and upstream re-review.
5. The PM will report **approved decisions, drafts, blockers and actual implementation** separately; no invented progress percentages.

**Latest Security Architect disposition (2026-11-27):** [Formal Security Registry Security Review 29](29_SECURITY_REGISTRY_SECURITY_REVIEW_FOR_APPROVAL.md) submitted under [Issue #1](https://github.com/LCK0629/dify_quertPilot/issues/1), recommending **REVISE & RESUBMIT**. Project Owner accepted the review recommendation; Database Engineer design revisions and subsequent registry approval remain pending. The document is not QP-APR-009, PRE-04 remains open and Development is NO-GO.

## Project Owner review disposition — 2026-11-27

[Project Owner disposition — Document 30](30_SECURITY_REGISTRY_REVIEW_DISPOSITION_RECORD.md) records QP-DEC-SR-REVIEW-001: **REVISE & RESUBMIT accepted; design-only DB-R01–DB-R06 authorized.** SR-D01–SR-D06 remain unapproved. Issue #1 remains open pending revised registry v1.1 and independent review. QP-APR-009 and QP-APR-DEV-GO-001 remain unissued. **Development NO-GO.**
