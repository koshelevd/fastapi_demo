from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from db.db import get_session
from schemas import submenu as submenu_schema
from services.submenu import submenu_crud

router = APIRouter()


@router.get("/menus/{menu_id}/submenus/", response_model=list[submenu_schema.Submenu])
async def read_submenus(
    menu_id: str, db: AsyncSession = Depends(get_session), skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve submenus.
    """
    return await submenu_crud.get_multi(db=db, skip=skip, limit=limit, menu_id=menu_id)


@router.get("/menus/{menu_id}/submenus/{id}", response_model=submenu_schema.Submenu)
async def read_submenu(
    *,
    menu_id: str,
    db: AsyncSession = Depends(get_session),
    id: str,
) -> Any:
    """
    Get by ID.
    """
    submenu = await submenu_crud.get(db=db, id=id, menu_id=menu_id)
    if not submenu:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    return submenu


@router.post(
    "/menus/{menu_id}/submenus/", response_model=submenu_schema.Submenu, status_code=status.HTTP_201_CREATED
)
async def create_submenu(
    *,
    menu_id: str,
    db: AsyncSession = Depends(get_session),
    submenu_in: submenu_schema.SubmenuCreate,
) -> Any:
    """
    Create new submenu.
    """
    return await submenu_crud.create(db=db, obj_in=submenu_in, menu_id=menu_id)


@router.patch("/menus/{menu_id}/submenus/{id}", response_model=submenu_schema.Submenu)
async def update_submenu(
    *,
    menu_id: str,
    db: AsyncSession = Depends(get_session),
    id: str,
    submenu_in: submenu_schema.SubmenuUpdate,
) -> Any:
    """
    Update a submenu.
    """
    submenu = await submenu_crud.get(db=db, id=id, menu_id=menu_id)
    if not submenu:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return await submenu_crud.update(db=db, db_obj=submenu, obj_in=submenu_in, menu_id=menu_id)


@router.delete("/menus/{menu_id}/submenus/{id}")
async def delete_submenu(*, menu_id: str, db: AsyncSession = Depends(get_session), id: str) -> Any:
    """
    Delete a submenu.
    """
    submenu = await submenu_crud.get(db=db, id=id, menu_id=menu_id)
    if not submenu:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return await submenu_crud.delete(db=db, id=id)
