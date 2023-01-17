import uuid

from pydantic import BaseModel


class MenuBase(BaseModel):
    title: str
    description: str | None


class MenuCreate(MenuBase):
    pass


# Properties to receive on entity update
class MenuUpdate(MenuBase):
    title: str | None


class MenuInDBBase(MenuBase):
    id: uuid.UUID

    class Config:
        orm_mode = True


# Properties to return to client
class Menu(MenuInDBBase):
    dishes_count: int | None
    submenus_count: int | None


# Properties stored in DB
class MenuInDB(MenuInDBBase):
    pass
