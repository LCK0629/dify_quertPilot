"""Fail-closed API foundation.

No database, LLM, identity-provider or business-data integration exists.
Analytics requests are denied until the separately approved gate is met.
"""

from typing import Literal

from fastapi import FastAPI, Response
from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: Literal["ok"] = "ok"
    stage: Literal["s1_foundation"] = "s1_foundation"
    analytics: Literal["disabled"] = "disabled"


app = FastAPI(
    title="QueryPilot AI — S1 Foundation",
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)


@app.get("/healthz", response_model=HealthResponse, include_in_schema=False)
def healthz() -> HealthResponse:
    """Provide a non-sensitive process health indicator, not an auth check."""
    return HealthResponse()


@app.post("/v1/analytics/query", include_in_schema=False)
def disabled_analytics(response: Response) -> dict[str, str]:
    """Deny all analytics without parsing or executing the request."""
    response.status_code = 503
    response.headers["Cache-Control"] = "no-store"
    return {
        "status": "disabled",
        "code": "DEVELOPMENT_GATE_NOT_CLEARED",
        "message": "Analytics is disabled until the authorization gate is approved.",
    }
