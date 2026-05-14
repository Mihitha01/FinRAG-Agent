from fastapi import FastAPI

from api.routes import health
from config.settings import get_settings


def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        description="Standalone reusable Agentic RAG prototype service.",
    )

    app.include_router(health.router)

    return app


app = create_app()

# Creates the FastAPI app
# Registers the health route
# Exposes app for uvicorn