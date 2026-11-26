# Role & Permission Matrix Approval Record

**Decision:** QP-APR-008 | **Date:** 2026-11-26 (Singapore) | **Approver:** Project Owner  
**Baseline:** [QP-SEC-RPM-001 v1.0](https://github.com/LCK0629/dify_quertPilot/blob/db1cbadcb8fcf899c2d613924b95a644bc18dd4e/docs/phase-1/22_ROLE_PERMISSION_MATRIX_V1_0.md), blob 980cde869cc6f3810cb48d7ac88307d0f938fd5f.

The Project Owner explicitly approved all six design recommendations, instructed GitHub updates and preparation of Security Registry Data Model v1.0, and explicitly retained Development NO-GO.

| ID | Approved design policy |
|---|---|
| RPM-D01 | Six user personas, capability and metric templates, optional grants through constrained approved templates |
| RPM-D02 | Explicit principal-wide store grants; no implicit owner all-store access |
| RPM-D03 | Deny overrides allow; controlled grant changes, separate reviewer and owner approval, no self-grant |
| RPM-D04 | Multi-role combination only within common principal-wide store scope; refuse unrepresentable role-specific requirements |
| RPM-D05 | Derived-output disclosure controls and conservative inference restrictions; residual inference risks require independent review before GO |
| RPM-D06 | Separate service identities, sanitized evidence and RPM-01–28 acceptance specifications |

**Disposition:** OWNER APPROVED — design baseline only. No actual grants, deployment or test execution authorized. Independent BA/DB/Security review remains outstanding, including sparse/differencing inference risk. Approval does not certify confidentiality or choose a database identity binding mechanism. PRE-03 owner decision portion is complete; verification and remaining PRE conditions are not closed.

Next: Security Registry Data Model v1.0, then identity/session and nonforgeable PostgreSQL authorization ADRs. Full PRD and separate Development GO remain pending. QP-APR-DEV-GO-001 remains unissued.
