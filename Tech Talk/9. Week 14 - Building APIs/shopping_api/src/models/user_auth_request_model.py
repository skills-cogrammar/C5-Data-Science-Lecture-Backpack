from pydantic import BaseModel

class UserAuthRequest(BaseModel):
    email: str
    password: str