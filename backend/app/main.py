from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.API_VERSION,
    )

    @app.get("/")
    def root() -> dict[str, str]:
        return {
            "message": "CU-BEMS Backend is running",
            "health": f"{settings.API_PREFIX}/health",
            "docs": "/docs",
        }

    app.include_router(api_router, prefix=settings.API_PREFIX)
    return app


app = create_app()
