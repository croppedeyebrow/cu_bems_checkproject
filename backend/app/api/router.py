from fastapi import APIRouter

from app.api.routes.anomalies import router as anomalies_router
from app.api.routes.dashboard import router as dashboard_router
from app.api.routes.health import router as health_router
from app.api.routes.imports import router as imports_router
from app.api.routes.metadata import router as metadata_router
from app.api.routes.predictions import router as predictions_router

api_router = APIRouter()
api_router.include_router(health_router, tags=["health"])
api_router.include_router(imports_router)
api_router.include_router(metadata_router)
api_router.include_router(dashboard_router)
api_router.include_router(predictions_router)
api_router.include_router(anomalies_router)
