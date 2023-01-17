from sqlalchemy import Column, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import DECIMAL

from models.base import BaseModel


class Dish(BaseModel):
    """Модель блюда."""
    __tablename__ = "dish"

    price = Column(DECIMAL(5, 2), nullable=False, comment="Цена")

    submenu_id = Column(ForeignKey("submenu.id", ondelete="CASCADE"), nullable=True, comment="Подменю")
    submenu = relationship("SubMenu", back_populates="dishes")
