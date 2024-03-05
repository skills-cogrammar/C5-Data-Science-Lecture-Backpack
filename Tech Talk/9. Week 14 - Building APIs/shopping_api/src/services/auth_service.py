import os 
from dotenv import load_dotenv

from datetime import timedelta, datetime
from passlib.context import CryptContext
from jose import jwt
from sqlalchemy import select

from src.models.user_auth_request_model import UserAuthRequest
from src.models.user_auth import UserAuth
from src.models.user import User

from src.repository.database_repository import DatabaseRepository
import uuid

load_dotenv()

class AuthService():    
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = "HS256"

    def __init__(self, connection_string: str) -> None:
        bcrypt = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.bcrypt = bcrypt

        self.__db_repo = DatabaseRepository(connection_string)        

    def create_user(self, user: UserAuthRequest):
        user_id = str(uuid.uuid4())
        user_model = UserAuth(user_id=user_id, email=user.email, password_hash=self.bcrypt.hash(user.password))
        self.__db_repo.create("user_auth",  user_model.model_dump())

        self.__add_to_user_table(user_model)

    def __add_to_user_table(self, user: UserAuth):
        new_user = User(id=user.user_id, email=user.email, role=1)

        new_user = new_user.model_dump()
        new_user.pop('cart')
        new_user.pop('wishlist')

        self.__db_repo.create("user", new_user)


    def authenticate_user(self, email: str, password: str):
        table = self.__db_repo.get_table("user_auth")

        statement = select(table).where(table.c.email == email)

        result = self.__db_repo.execute_statement(statement)        

        if not result:
            return None
        
        columns = ['user_id', 'email', 'password_hash']
        
        user = result[0]

        user = dict(zip(columns, user))

        if not self.bcrypt.verify(password, user['password_hash']):
            return None
        
        user.pop('password_hash')

        return user
    
    def create_access_token(self, user_id: str):
        expires_delta = timedelta(minutes=30)
        expires = datetime.utcnow() + expires_delta

        encode = {"id": user_id, "exp": expires}

        return jwt.encode(encode, self.SECRET_KEY, algorithm=self.ALGORITHM)


        
