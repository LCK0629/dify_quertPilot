# OD-01–OD-07 Decision Resolution v1.0

**ID:** QP-DE-OD-001 | **Date:** 2026-11-26 | **Status:** FOR APPROVAL | **Owners:** BA + Database Engineer | **Gate:** NO-GO

This is the first database decision-closure candidate under QP-APR-006. All seven decisions remain OPEN until their designated authority records acceptance. It supplements approved documents 14–16 and does not amend M01–M09. No implementation or tests have been performed.

| ID | Recommended decision | Alternative rejected or deferred | Authority |
|---|---|---|---|
| OD-01 | Exclude non-refund post-completion corrections from P0. Quarantine attempted voids or changes to recognized amounts, units, dates and attribution. Block affected analysis if source discrepancy is unresolved. | Silent rewrite; new sale-correction event without metric contract | BA + Owner |
| OD-02 | Allocate eligible header discount in integer cents by gross proportion, largest fractional remainder, stable line ID tie-break. Reject zero eligible gross with positive discount or any combined line cap violation. | Silent cap or redistribution | BA + Owner |
| OD-03 | Final only after expected date/store/channel/feed coverage, source watermark and independent control totals reconcile. Missing expected cells are UNKNOWN/MISSING; incomplete scope cannot produce a numeric KPI. | Inferring completeness from presence or absence of transactions | BA + Data Architect, Owner acceptance |
| OD-04 | Monetary refund reversal does not restore returned quantity in P0. Value-only refunds have zero returned quantity; amount and unit caps independently validated. | Implicit restocking or quantity reversal | BA + Owner |
| OD-05 | Stable IDs + immutable revisions, serialized atomic publication, unique committed publish sequence, snapshot cutoff and pinned metric/model version. Select latest eligible revision before status filters. | Mutable current-state tables or timestamp-only cutoff | Data Architect + Owner |
| OD-06 | Adopt candidate matrix below; deny unlisted combinations. Separate metric computation from component disclosure. | Arbitrary dimensions and category AOV | BA + Owner; Security review |
| OD-07 | Candidate daily publication by 06:00 SGT, covering prior local day; stale if latest required successful publication missed its deadline. Expose data-as-of and restatement state; no substitution of dataset month for requested real month. | Silent stale results or historical rewriting | PM + BA + Owner |

## Testable contracts

- OD-01: completed order gross 100, units 2, count 1; subsequent non-refund void request must not mutate the old snapshot. New affected reporting is withheld until resolved; no automatic negative sale, quantity or order event.
- OD-02: three equal gross lines 1.00 each and header discount 0.01 allocate 0.01/0/0 by stable tie-break; gross 3.00, discount 0.01, net 2.99. A line gross 1.00 already discounted 0.99 with allocated header 0.02 is rejected, not clipped. Independently supplied source totals required for finality.
- OD-03: complete expected feed with zero events yields COMPLETE_ZERO for additive metrics; absent expected coverage gives UNKNOWN; known partial gives INCOMPLETE. N/A requires independently approved applicability, not missing data. M07 without orders is N/A even on complete coverage. Provisional and stale are separate from coverage; P0 partial numeric output disabled. Proposed rule: withhold current/final claims on stale required feeds; pinned historical final snapshots may be queried only with explicit as-of context and current authorization, subject to BA acceptance.
- OD-04: original line net 100, quantity 2; confirmed refund 60 for one unit; reversal 20 leaves monetary net refund 40 and returned units 1. Remaining amount 60 and unit allowance 1, independently checked. Reversal cannot exceed its own original refund; no negative cumulative refund balance. Value-only refund cannot introduce a quantity return.
- OD-05: snapshot S1 cutoff 10 contains sale 100; late confirmed refund 20 for same reporting month in publication 11 gives S2 net 80; S1 stays 100. Publication failure exposes neither new partial rows nor new snapshot. Snapshot reproducibility does not preserve expired permissions.
- OD-06: one two-category order counts once in total; category order counts non-additive; M07 category/product denied. A user granted M04 but not M01/M02/M03 may see authorized M04 only, not the bridge or raw components. Security review must settle inference from combinations of permitted outputs.
- OD-07: at 06:01 SGT, missed required daily publication marks stale. Last month is prior real completed local month, not latest available dataset period; missing coverage produces insufficient_data. Historical fixture date anchor may be explicitly supplied by the test harness, never silently substituted in production. Restatement references superseded snapshot and affected periods, with current authorization.

## Candidate semantic matrix (not a permission grant)

| Metric | Total/date/store/channel | Category/product | Rank | Compare |
|---|---|---|---|---|
| M01–M04 | Allowed | Allowed | Store/category | Allowed |
| M05 | Allowed | Deny in P0 pending explicit cohort contract | Store only | Allowed |
| M06 | Allowed | Allowed | Store/category | Allowed |
| M07 | Allowed | Deny including category/product filters | Deny in P0 | Allowed |
| M08 | Derived from approved base metric, matched windows | Inherit base restrictions | Deny | Compare only |
| M09 | Total change plus category contributions | Category only; product denied | Within fixed diagnostic output | Fixed diagnostic only |

All slices require explicit capability, metric, scope, dependency/output permission and compatible snapshot. No user-supplied identifiers; stable ID ascending as rank tie-break; no unrestricted mixed-dimension queries. M09 diagnosis requires M04 and M09 plus permissions for any displayed bridge components. All candidate restrictions require BA/Security approval; they narrow query support, not metric definitions.

## Closure requirements

For each OD record decision, rationale, approver, date, affected files and accepted fixture. BA independently checks arithmetic and metric meaning; Security checks matrix; DB reviews cross-row and temporal integrity. Tests are specifications only until GO. Unresolved issues block affected implementation. Daily refresh and matrix restrictions are proposed, not approved. Full PRD and database authorization mechanism remain separate gates.
