from fastapi import APIRouter

from api.v1.entity import router as entity_router

api_router = APIRouter()
api_router.include_router(entity_router, prefix="/entities", tags=["entities"])
