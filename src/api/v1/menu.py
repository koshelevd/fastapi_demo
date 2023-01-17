from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from db.db import get_session
from schemas import menu as menu_schema
from services.menu import menu_crud

router = APIRouter()


@router.get("/", response_model=list[menu_schema.Menu])
async def read_menus(
    db: AsyncSession = Depends(get_session), skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve menus.
    """
    return await menu_crud.get_multi(db=db, skip=skip, limit=limit)


@router.get("/{id}", response_model=menu_schema.Menu)
async def read_menu(
    *,
    db: AsyncSession = Depends(get_session),
    id: str,
) -> Any:
    """
    Get by ID.
    """
    menu = await menu_crud.get(db=db, id=id)
    if not menu:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    return menu


@router.post(
    "/", response_model=menu_schema.Menu, status_code=status.HTTP_201_CREATED
)
async def create_menu(
    *,
    db: AsyncSession = Depends(get_session),
    menu_in: menu_schema.MenuCreate,
) -> Any:
    """
    Create new menu.
    """
    return await menu_crud.create(db=db, obj_in=menu_in)


@router.patch("/{id}", response_model=menu_schema.Menu)
async def update_menu(
    *,
    db: AsyncSession = Depends(get_session),
    id: str,
    menu_in: menu_schema.MenuUpdate,
) -> Any:
    """
    Update a menu.
    """
    menu = await menu_crud.get(db=db, id=id)
    if not menu:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return await menu_crud.update(db=db, db_obj=menu, obj_in=menu_in)


@router.delete("/{id}")
async def delete_menu(*, db: AsyncSession = Depends(get_session), id: str) -> Any:
    """
    Delete a menu.
    """
    menu = await menu_crud.get(db=db, id=id)
    if not menu:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return await menu_crud.delete(db=db, id=id)
