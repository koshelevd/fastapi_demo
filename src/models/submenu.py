import uuid

from sqlalchemy import Column, ForeignKey, func, select
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import column_property, relationship, object_session

from models import BaseModel, Dish


class SubMenu(BaseModel):
    """Модель меню."""
    __tablename__ = "submenu"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, comment="Идентификатор")

    dishes = relationship("Dish", back_populates="submenu")

    menu_id = Column(ForeignKey("menu.id", ondelete="CASCADE"), nullable=True, comment="Меню")
    menu = relationship("Menu", back_populates="submenus")

    dishes_count = column_property(
        select(func.count(Dish.id))
        .where(Dish.submenu_id == id)
        .correlate_except(Dish)
        .scalar_subquery()
    )
