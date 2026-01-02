from fastapi import APIRouter
from api.v1 import auth, products, categoty

api_router = APIRouter()

api_router.include_router(auth.api_router, prefix="/auth", tags=["auth"])
api_router.include_router(products.api_router, prefix="/productos", tags=["productos"])
api_router.include_router(categoty.api_router, prefix="/categorias", tags=["categorias"])