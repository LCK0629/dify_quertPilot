# QueryPilot AI API — S1 Engineering Foundation

**Status: S1 FOUNDATION ONLY / 完全禁用数据分析执行。**

This is a deliberately **fail-closed** FastAPI shell. It exists to establish packaging, deterministic offline tests and a local health endpoint. It is **not** a working analytics backend, identity service or database application.

## Local development / 本地开发

From the repository root (Python 3.11+):

```bash
cd apps/api
python -m venv .venv
# Activate .venv for your shell
python -m pip install -e ".[dev]"
python -m pytest -q
uvicorn querypilot_api.main:app --host 127.0.0.1 --port 8000
```

- `GET http://127.0.0.1:8000/healthz` → process health, `analytics=disabled`.
- `POST /v1/analytics/query` → **503** for every input. No SQL, DB login or model call is made.
- No `.env`, credentials, database migrations, Dify workflow or privileged APIs should be introduced in this branch.

**Security statement:** Passing these tests establishes only that this particular S1 stub denies all query requests. It is **not** a security evaluation of the future QueryPilot AI system.

Design authority: [Owner's limited foundation start record](../../docs/phase-1/36_OWNER_DESIGN_APPROVAL_LIMITED_START_2026_11_28.md). Full database/data-path authorization requires separate gate evidence and review.
