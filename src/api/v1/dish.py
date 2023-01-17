from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from db.db import get_session
from schemas import dish as dish_schema
from services.dish import dish_crud
from services.submenu import submenu_crud

router = APIRouter()


@router.get("/menus/{menu_id}/submenus/{submenu_id}/dishes/", response_model=list[dish_schema.Dish])
async def read_dishes(
    menu_id: str, submenu_id: str, db: AsyncSession = Depends(get_session), skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve dishes.
    """
    return await dish_crud.get_multi(db=db, skip=skip, limit=limit, menu_id=menu_id, submenu_id=submenu_id)


@router.get("/menus/{menu_id}/submenus/{submenu_id}/dishes/{id}", response_model=dish_schema.Dish)
async def read_dish(
    *,
    menu_id: str,
    submenu_id: str,
    db: AsyncSession = Depends(get_session),
    id: str,
) -> Any:
    """
    Get by ID.
    """
    dish = await dish_crud.get(db=db, id=id, menu_id=menu_id, submenu_id=submenu_id)
    if not dish:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    return dish


@router.post(
    "/menus/{menu_id}/submenus/{submenu_id}/dishes", response_model=dish_schema.Dish, status_code=status.HTTP_201_CREATED
)
async def create_dish(
    *,
    menu_id: str,
    submenu_id: str,
    db: AsyncSession = Depends(get_session),
    dish_in: dish_schema.DishCreate,
) -> Any:
    """
    Create new dish.
    """
    submenu = await submenu_crud.get(db=db, id=submenu_id, menu_id=menu_id)
    if not submenu:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Submenu not found"
        )
    return await dish_crud.create(db=db, obj_in=dish_in, submenu_id=submenu_id)


@router.patch("/menus/{menu_id}/submenus/{submenu_id}/dishes/{id}", response_model=dish_schema.Dish)
async def update_dish(
    *,
    menu_id: str,
    submenu_id: str,
    db: AsyncSession = Depends(get_session),
    id: str,
    dish_in: dish_schema.DishUpdate,
) -> Any:
    """
    Update a dish.
    """

    dish = await dish_crud.get(db=db, id=id, menu_id=menu_id, submenu_id=submenu_id)
    if not dish:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return await dish_crud.update(db=db, db_obj=dish, obj_in=dish_in)

@router.delete("/menus/{menu_id}/submenus/{submenu_id}/dishes/{id}")
async def delete_dish(*, menu_id: str, submenu_id: str, db: AsyncSession = Depends(get_session), id: str) -> Any:
    """
    Delete a dish.
    """
    dish = await dish_crud.get(db=db, id=id, menu_id=menu_id, submenu_id=submenu_id)
    if not dish:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return await dish_crud.delete(db=db, id=id)
