# OD-01–OD-07 Business & Data Decision Approval Record

**Decision ID:** QP-APR-007  
**Date:** 2026-11-26 (Singapore)  
**Approver:** Project Owner  
**Approved baseline:** [QP-DE-OD-001 v1.0 at reviewed revision](https://github.com/LCK0629/dify_quertPilot/blob/b8c12f8caeff5b17158a925b0b7f1d3467c94080/docs/phase-1/20_OD_DECISION_RESOLUTION_V1_0.md) (blob 227dd4f5e30160bdbf561146e064cf349b2137a4; substantive revision 8237515db1885f6884b8c852f3b2dfabdb0be71d).
**Evidence:** Project Owner explicitly approved the latest GitHub OD-01–OD-07 Decision Resolution and instructed recording approval, updating repository documentation and preparing the Role & Permission Matrix.

## Disposition

All seven **business/data policy decisions are approved by the Project Owner**. This record controls over historical proposed/open labels in document 20. Independent BA, DB and Security verification, executable acceptance evidence and implementation authorization remain separate; no such sign-off or test pass is asserted.

| ID | Approved policy disposition | Required verification / downstream owner |
|---|---|---|
| OD-01 | Exclude non-refund post-completion corrections from P0; quarantine and withhold affected analyses; preserve history. | BA/DB: mutation and quarantine fixtures |
| OD-02 | Gross-proportional exact-cent allocation with stable tie-break, no summary duplication, distinct additional promotions only with known provenance; reject combined cap violations and ambiguous provenance. | BA/DB: allocation, source reconciliation and rejection fixtures |
| OD-03 | Final only after expected coverage, watermarks and independent controls reconcile; no partial numeric KPI, no fabricated zero; historical pinned final snapshots require explicit as-of and current authorization. | BA/DB: missing, zero, provisional and stale fixtures |
| OD-04 | Monetary reversal does not restore returned quantity; value and unit caps independently enforced, including event-time prefix checks. | BA/DB: reversal and concurrency fixtures |
| OD-05 | Stable identity, immutable revisions, serialized atomic publication, cutoff and pinned metric/model versions; current authorization on historical access. | DB: snapshot reproducibility and atomicity fixtures |
| OD-06 | Approved semantic boundaries including product ranking for M01–M04/M06, M05/M07 category/product restrictions, store/category M09 reconciliations; no implicit grants or component disclosure. | BA/Security: matrix, inference and entitlement verification |
| OD-07 | Daily publication by 06:00 SGT for prior local day; missed required deadline is stale, disclose as-of/restatement; no substitution of requested real calendar month. | BA/PM/DB: deadline, stale and restatement fixtures |

The deadline policy supersedes the earlier 36-hour review suggestion. Approval includes the testable contracts in document 20 as specifications, not results. No change to approved M01–M09 arithmetic or data grain. Preserve original review artifacts for traceability.

## Consequences and remaining gates

- Owner decision disposition: 7/7 approved. PRE-02 owner decision portion complete; independent role reviews and fixture acceptance evidence remain outstanding.
- OD-06 semantic authorization is not a user-role grant. PRE-03, PRE-04, PRE-05, PRE-06 and database v1.1 security design remain open.
- Prepare Role & Permission Matrix v1.0 for separate approval; reconcile PRD v1.1 and readiness evidence later.
- Development remains NO-GO. No DDL, synthetic data generation, code, deployment or implementation test execution authorized. QP-APR-DEV-GO-001 remains unissued.
