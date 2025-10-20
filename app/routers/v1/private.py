from fastapi import APIRouter

from app.routers.v1.favorites.crud import favorites_router

private_router = APIRouter(prefix='/private/v1')

private_router.include_router(favorites_router)