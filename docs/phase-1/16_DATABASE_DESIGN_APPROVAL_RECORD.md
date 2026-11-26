# Database design approval record / 数据库设计审批记录

Recorded 2026-11-26 (Singapore). Project Owner explicitly approved the conceptual and physical design in chat, and on 26 November requested approval and GitHub publication. This record supplements, not replaces, the historical product and architecture decisions.

| Decision | Document | Disposition |
|---|---|---|
| QP-APR-003 | QP-DE-DM-001 Conceptual ERD & Data Model v1.0 | Approved design baseline, subject to outstanding implementation conditions |
| QP-APR-004 | QP-DE-PD-001 Physical Database Design & Data Specification v1.0 | Approved design baseline, subject to outstanding implementation conditions |

The earlier Business Metric Dictionary v1.0 approval is inherited as the business baseline; BA independent validation remains required. Approval does not certify tests, implementation, or unresolved policies.

- [Conceptual and logical design — GitHub reference](14_CONCEPTUAL_ERD_DATA_MODEL_V1_0.md)
- [Physical design — GitHub reference](15_PHYSICAL_DATABASE_DESIGN_V1_0.md)
- [Architecture approval](13_ARCHITECTURE_APPROVAL_RECORD.md) remains unchanged.

## Conditions / 条件
OD-01 non-refund completed-order corrections; OD-02 discount cap exceptions; OD-03 finality; OD-04 quantity restoration on refund reversal; OD-05 detailed version storage validation; OD-06 permitted metric dimensions; OD-07 freshness and restatement policy require closure or explicit disposition before affected implementation. The physical design proposes quarantine/rejection, immutable revisions, restricted AOV and daily SGT 06:00 publication, not independently validated production policies. BA and security review remain outstanding. Full PRD sign-off and development readiness review remain separate.

**Development gate: NO-GO.** No DDL, data generation, migrations, application code or security tests authorized by these approvals. Next: Development Readiness & Implementation Plan — For Approval, coordinated with PM and architecture owner.

The GitHub references are Markdown technical summaries of the approved Word review candidates, not byte-identical copies. Original Word documents retain their original review status for auditability.
