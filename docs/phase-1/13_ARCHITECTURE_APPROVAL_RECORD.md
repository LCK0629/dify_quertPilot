# Architecture Approval Record

**Decision ID:** QP-APR-005 (assigned for this record)

**Date:** 26 November 2026

**Approver:** Project Owner

**Evidence:** Owner replied “approve” following publication of [System Architecture & Security Design v1.1](12_SYSTEM_ARCHITECTURE_SECURITY_DESIGN_V1_1.md), commit `78833dde69e1282a762b039e9748d28eaa3d937c`.

**Disposition:** Approved with conditions, interpreting the owner's approval in accordance with the architect's preceding conditional-approval recommendation. No separate approval of unresolved implementation details is inferred.

## Accepted direction

- Modular FastAPI monolith with a replaceable IntentAdapter; Dify is a proposed adapter, not a trust authority.
- Shared conversational interface for multiple authorized roles.
- Two-stage authorization: chat access before AI interpretation; function, metric, dependency and data scope authorization before controlled execution.
- Deterministic SQL compilation, least privilege, read-only analytics, snapshot-bound evidence and defense in depth.
- Local-first deployment direction and security testing requirements.

## Conditions and remaining gates

- OD-01 through OD-07 remain open; no change to approved business metrics or retail data model.
- Final permission matrix, security registry persistence and nonforgeable database scope binding require review.
- Dify/model selection, identity provider, egress, license and implementation limits remain subject to validation and approval as applicable.
- No actual security tests or implementation acceptance are claimed.
- PRD alignment, dependency dispositions and separate development readiness approval remain necessary.

**Architecture direction: APPROVED WITH CONDITIONS. Development: NO-GO.**

The linked v1.1 review candidate and historical product decision record are retained unchanged for auditability. This record supplies the later approval disposition, not a retrospective rewrite of prior status. Next recommended deliverable: Development Readiness & Implementation Plan — For Approval.
