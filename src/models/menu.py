import uuid

from sqlalchemy import Column, func, select, cast
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import column_property, relationship

from models import BaseModel, Dish
from models.submenu import SubMenu


class Menu(BaseModel):
    """Модель меню."""
    __tablename__ = "menu"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, comment="Идентификатор")

    submenus = relationship("SubMenu", back_populates="menu")

    submenus_count = column_property(
        select(func.count(SubMenu.id))
        .where(cast(SubMenu.menu_id, UUID()) == cast(id, UUID()))
        .correlate_except(SubMenu)
        .scalar_subquery()
    )

    dishes_count = column_property(
        select(func.count(Dish.id))
        .join(SubMenu)
        .where(cast(Dish.submenu_id, UUID) == cast(SubMenu.id, UUID), cast(SubMenu.menu_id, UUID) == cast(id, UUID))
        .correlate_except(Dish)
        .scalar_subquery()
    )
