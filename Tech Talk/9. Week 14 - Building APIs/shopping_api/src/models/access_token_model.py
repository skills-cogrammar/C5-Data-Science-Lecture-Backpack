from pydantic import BaseModel

class AccessToken:
    access_token: str
    token_type: str