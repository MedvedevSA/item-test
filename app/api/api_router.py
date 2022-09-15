from fastapi import APIRouter

from app.api.endpoints import items
from app.api.endpoints import order

api_router = APIRouter()
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(order.router, prefix="/order", tags=["order"])