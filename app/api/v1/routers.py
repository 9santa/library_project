from fastapi import APIRouter

from app.api.v1.endpoints import endpoints_router

main_router = APIRouter(prefix='/api/v1')
main_router.include_router(endpoints_router)
