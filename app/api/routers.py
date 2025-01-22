from fastapi import APIRouter

from app.api.endpoints.user import router as user_router
from app.api.endpoints.category import router as category_router
from app.api.endpoints.product import router as product_router

main_router = APIRouter()

main_router.include_router(category_router)
main_router.include_router(product_router)
main_router.include_router(user_router)
