from fastapi import APIRouter
from config.settings import get_settings

router = APIRouter(prefix="/api/v1/health", tags=["health"])


@router.get("")
def health_check() -> dict:
    settings = get_settings()

    return {
        "status": "ok",
        "service": settings.app_name,
        "version": settings.app_version,
        "environment": settings.environment,
    }

# Creates GET /api/v1/health
# Returns service status