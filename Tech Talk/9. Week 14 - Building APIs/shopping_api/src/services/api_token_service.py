import datetime
from src.repository.database_repository import DatabaseRepository
from src.models.api_token_model import ApiToken
import uuid

class ApiTokenService():
    TABLE_NAME = 'api_token'
    COLUMNS = ['token', 'is_active', 'expires']

    def __init__(self, connection_string: str) -> None:
        self.__db_repo = DatabaseRepository(connection_string)

    def generate_token(self):
        token = str(uuid.uuid4())
        expires = datetime.datetime.now() + datetime.timedelta(days=30)        
        expires = expires.strftime('%Y-%m-%d')
        is_active = True

        api_token = ApiToken(token=token, expires=expires, is_active=is_active)

        self.__db_repo.create(self.TABLE_NAME, api_token.model_dump())

        return api_token.model_dump()
    
    def is_valid_token(self, token: str):
        table = self.__db_repo.get_table(self.TABLE_NAME)
        stmt = table.select().where(table.c.token == token)

        result = self.__db_repo.execute_statement(stmt)

        if not result:
            return False
        
        result = result[0]
        return result[1] and result[2] > datetime.datetime.now().date()
    


        