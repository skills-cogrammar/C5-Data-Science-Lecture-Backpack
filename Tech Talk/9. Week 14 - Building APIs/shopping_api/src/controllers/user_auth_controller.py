from src.models.user_auth_request_model import UserAuthRequest
from src.services.api_token_service import ApiTokenService

from src.services.auth_service import AuthService



class UserAuthController():
    TABLE_NAME = "user_auth"
    ALGORITHM = "HS256"

    def __init__(self, connection_string: str):        
        self.__api_token_service = ApiTokenService(connection_string)
        self.__auth_service = AuthService(connection_string)

    def create_user(self, user: UserAuthRequest):
        return self.__auth_service.create_user(user)

    def generate_api_token(self):
        return self.__api_token_service.generate_token()
    
    def is_valid_token(self, token: str):
        return self.__api_token_service.is_valid_token(token)
    
    def authenticate_user(self, email: str, password: str):
        return self.__auth_service.authenticate_user(email, password)
    
    def create_access_token(self, user_id: str):
        return self.__auth_service.create_access_token(user_id)