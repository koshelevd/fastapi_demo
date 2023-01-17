import uuid

from pydantic import BaseModel


class SubmenuBase(BaseModel):
    title: str
    description: str | None


class SubmenuCreate(SubmenuBase):
    pass


# Properties to receive on entity update
class SubmenuUpdate(SubmenuBase):
    title: str | None


class SubmenuInDBBase(SubmenuBase):
    id: uuid.UUID

    class Config:
        orm_mode = True


# Properties to return to client
class Submenu(SubmenuInDBBase):
    dishes_count: int | None


# Properties stored in DB
class SubmenuInDB(SubmenuInDBBase):
    pass
