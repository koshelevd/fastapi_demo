from typing import Optional

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from models.submenu import SubMenu as SubmenuModel
from schemas.submenu import SubmenuCreate, SubmenuUpdate
from .base import RepositoryDB


class RepositorySubmenu(RepositoryDB[SubmenuModel, SubmenuCreate, SubmenuUpdate]):
    async def get(self, db: AsyncSession, id: str, menu_id: str) -> Optional[SubmenuModel]:
        statement = select(self._model).where(self._model.id == id, self._model.menu_id == menu_id)
        results = await db.execute(statement=statement)
        return results.scalar_one_or_none()

    async def update(
        self,
        db: AsyncSession,
        *,
        db_obj,
        obj_in,
        menu_id: str,
    ) -> SubmenuModel:
        """Update an object."""
        query = update(self._model).values(**obj_in.dict()).filter(self._model.id == db_obj.id,
                                                                   self._model.menu_id == menu_id)
        await db.execute(query)
        await db.commit()
        return db_obj


submenu_crud = RepositorySubmenu(SubmenuModel)
