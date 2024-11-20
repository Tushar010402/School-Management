from fastapi import APIRouter
from app.core.config import get_settings
from app.api.api_v1.endpoints import auth, schools, tenants, fees, academic, portal

settings = get_settings()
api_router = APIRouter(prefix=settings.API_V1_STR)

# Include route modules
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(tenants.router, prefix="/tenants", tags=["Tenants"])
api_router.include_router(schools.router, prefix="/schools", tags=["Schools"])
api_router.include_router(fees.router, prefix="/fees", tags=["Fees"])
api_router.include_router(academic.router, prefix="/academic", tags=["Academic"])
api_router.include_router(portal.router, prefix="/student", tags=["Student Portal"])