from src.models.product import Product
from src.services.product_service import ProductService
from src.services.user_service import UserService

class ProductController():
    TABLE_NAME = "products"
    COLUMNS = ["id", "name", "price"]
    
    def __init__(self, connection_string: str):
        self.__service = ProductService(connection_string)
        self.__user_service = UserService(connection_string)
        

    def create(self, product: Product):
        return self.__service.create(product)
    
    def get_all(self):
        return self.__service.get_all()
    
    def get(self, id: str):
        return self.__service.get(id)
    
    def update(self, product: Product):
        return self.__service.update(product)
    
    def delete(self, id: str):
        return self.__service.delete(id)
    
    def is_admin(self, user_id):
        return self.__user_service.is_admin(user_id)


    

        