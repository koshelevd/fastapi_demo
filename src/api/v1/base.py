from fastapi import APIRouter

from api.v1.dish import router as dish_router
from api.v1.menu import router as menu_router
from api.v1.submenu import router as submenu_router

api_router = APIRouter()
api_router.include_router(menu_router, prefix="/menus", tags=["menus"])
api_router.include_router(submenu_router, tags=["submenus"])
api_router.include_router(dish_router, tags=["dishes"])
