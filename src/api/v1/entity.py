from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from db.db import get_session
from schemas import entity as entity_schema
from services.entity import entity_crud

router = APIRouter()


@router.get("/", response_model=List[entity_schema.Entity])
async def read_entities(
    db: AsyncSession = Depends(get_session), skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve entities.
    """
    # get entities from db
    entities = await entity_crud.get_multi(db=db, skip=skip, limit=limit)
    return entities


@router.get("/{id}", response_model=entity_schema.Entity)
async def read_entity(
    *,
    db: AsyncSession = Depends(get_session),
    id: int,
) -> Any:
    """
    Get by ID.
    """
    # get entity from db
    entity = await entity_crud.get(db=db, id=id)
    if not entity:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    return entity


@router.post(
    "/", response_model=entity_schema.Entity, status_code=status.HTTP_201_CREATED
)
async def create_entity(
    *,
    db: AsyncSession = Depends(get_session),
    entity_in: entity_schema.EntityCreate,
) -> Any:
    """
    Create new entity.
    """
    # create item by params
    entity = await entity_crud.create(db=db, obj_in=entity_in)
    return entity


@router.put("/{id}", response_model=entity_schema.Entity)
async def update_entity(
    *,
    db: AsyncSession = Depends(get_session),
    id: int,
    entity_in: entity_schema.EntityUpdate,
) -> Any:
    """
    Update an entity.
    """
    # get entity from db
    entity = await entity_crud.get(db=db, id=id)
    if not entity:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    # update entity in db
    entity = await entity_crud.update(db=db, db_obj=entity, obj_in=entity_in)
    return entity


@router.delete("/{id}")
async def delete_entity(*, db: AsyncSession = Depends(get_session), id: int) -> Any:
    """
    Delete an entity.
    """
    entity = await entity_crud.get(db=db, id=id)
    if not entity:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return None
