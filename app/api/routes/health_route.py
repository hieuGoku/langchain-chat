"""Health route for the API"""

from fastapi import APIRouter

from app.api.schemas.health import HealthResponse

router = APIRouter()


@router.get("/health", tags=["Health"])
def health() -> HealthResponse:
    """Return ok if the system is up."""
    return HealthResponse(status="ok")
