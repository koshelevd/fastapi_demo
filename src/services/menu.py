from models.menu import Menu as MenuModel
from schemas.menu import MenuCreate, MenuUpdate
from .base import RepositoryDB


class RepositoryMenu(RepositoryDB[MenuModel, MenuCreate, MenuUpdate]):
    pass


menu_crud = RepositoryMenu(MenuModel)
