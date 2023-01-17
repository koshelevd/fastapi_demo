import datetime
from sqlalchemy import Column, DateTime, func, String
from sqlalchemy.dialects.postgresql import UUID
import uuid

from db.db import Base


class BaseModel(Base):
    __abstract__ = True

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, comment="Идентификатор")

    created_at = Column(
        DateTime,
        nullable=False,
        comment="Дата и время создания",
        default=datetime.datetime.now,
        server_default=func.now(),
    )
    updated_at = Column(
        DateTime,
        nullable=False,
        comment="Дата и время последнего обновления",
        default=datetime.datetime.now,
        server_default=func.now(),
        onupdate=func.now(),
    )
    title = Column(String(20), nullable=False, comment="Название")
    description = Column(String(50), nullable=True, comment="Описание")
