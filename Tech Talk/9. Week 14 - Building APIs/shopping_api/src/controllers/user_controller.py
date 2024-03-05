from src.models.user import User
from src.services.user_service import UserService

class UserController():
    TABLE_NAME = "user"
    COLUMNS = ['user_id', 'role', 'first_name', 
               'last_name', 'email', 'cart', 'wishlist']
    
    def __init__(self, connection_string):
        self.__service = UserService(connection_string)

    def update(self, user: User):
        return self.__service.update(user)


    def get_user(self, user_id: str):
        return self.__service.get_user(user_id)    
    
    def add_to_cart(self, user_id: str, product_id: str):
        return self.__service.add_to_cart(user_id, product_id)


    def add_to_wishlist(self, user_id: str, product_id: str):
        return self.__service.add_to_wishlist(user_id, product_id)
    
    def is_admin(self, user_id):
        return self.__service.is_admin(user_id)
    