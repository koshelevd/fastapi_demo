from models.dish import Dish as DishModel
from schemas.dish import DishCreate, DishUpdate
from .base import RepositoryDB


class RepositoryDish(RepositoryDB[DishModel, DishCreate, DishUpdate]):
    pass


dish_crud = RepositoryDish(DishModel)
