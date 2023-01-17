import uuid

from pydantic import BaseModel, condecimal


class DishBase(BaseModel):
    title: str
    description: str | None
    price: float


class DishCreate(DishBase):
    pass


# Properties to receive on entity update
class DishUpdate(DishBase):
    title: str | None


class DishInDBBase(DishBase):
    id: uuid.UUID

    class Config:
        orm_mode = True


# Properties to return to client
class Dish(DishInDBBase):
    pass


# Properties stored in DB
class DishInDB(DishInDBBase):
    pass
