from fastapi import APIRouter

from app.routers.v1.favorites.crud import favorites_router

public_router = APIRouter(prefix='/public/v1')

public_router.include_router(favorites_router)