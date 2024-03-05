from src.models.user import User
from src.repository.database_repository import DatabaseRepository
from sqlalchemy import select
import uuid

class UserService():
    TABLE_NAME = "user"
    COLUMNS = ['id', 'role', 'first_name', 
               'last_name', 'email', 'cart', 'wishlist']

    def __init__(self, connection_string: str) -> None:
        self.__db_repo = DatabaseRepository(connection_string)
        
    def is_admin(self, user_id: str):
        user = self.get_user(user_id)

        if not user:
            return False

        return user.role == 0
    
    def create(self, user: User):
        return self.__db_repo.create(self.TABLE_NAME, user.model_dump())
    
    def update(self, user: User):
        return self.__db_repo.update(self.TABLE_NAME, user.model_dump())
    
    def get_user(self, user_id: str):
        user_details = self.__db_repo.get(self.TABLE_NAME, user_id)
        cart = [value[1] for value in self.__get_shopping_cart(user_id)]
        wishlist = [value[1] for value in self.__get_wishlist(user_id)]

        if user_details is None:
            return None

        user_details = dict(zip(self.COLUMNS, user_details))
        user_details["cart"] = cart
        user_details["wishlist"] = wishlist

        return User(**user_details)
    
    def __get_shopping_cart(self, user_id: str):
        table = self.__db_repo.get_table("cart")

        statment = select(table).where(table.c.user_id == user_id)

        shopping_cart = self.__db_repo.execute_statement(statment)

        return shopping_cart
    
    def __get_wishlist(self, user_id: str):
        table = self.__db_repo.get_table("wishlist")

        statment = select(table).where(table.c.user_id == user_id)
        wishlist = self.__db_repo.execute_statement(statment)

        return wishlist
    
    def add_to_cart(self, user_id: str, product_id: str):
        id = str(uuid.uuid4())

        details = {
            "id": id,
            "user_id": user_id,
            "product_id": product_id
        }

        self.__db_repo.insert("cart", details)

    def add_to_wishlist(self, user_id: str, product_id: str):
        id = str(uuid.uuid4())

        details = {
            "id": id,
            "user_id": user_id,
            "product_id": product_id
        }

        self.__db_repo.insert("wishlist", details)