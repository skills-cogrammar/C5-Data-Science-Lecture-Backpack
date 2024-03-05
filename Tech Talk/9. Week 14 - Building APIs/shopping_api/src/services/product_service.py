from src.repository.database_repository import DatabaseRepository
from src.models.product import Product

class ProductService():
    TABLE_NAME = "product"
    COLUMNS = ["id", "name", "price"]


    def __init__(self, connection_string: str) -> None:
        self.__db_repo = DatabaseRepository(connection_string)

    def create(self, product: Product):
        return self.__db_repo.create(self.TABLE_NAME, product.model_dump())
    
    def get_all(self):
        result = self.__db_repo.get_all(self.TABLE_NAME)
        result = [dict(zip(self.COLUMNS, value)) for value in result]
        return result
    
    def get(self, id: str):
        result = self.__db_repo.get(self.TABLE_NAME, id)

        return dict(zip(self.COLUMNS, result))
    
    def update(self, product: Product):
        product = product.model_dump()
        id = product.pop("id")
        
        return self.__db_repo.update(self.TABLE_NAME, id, product.model_dump())
    
    def delete(self, id: str):
        return self.__db_repo.delete(self.TABLE_NAME, id)