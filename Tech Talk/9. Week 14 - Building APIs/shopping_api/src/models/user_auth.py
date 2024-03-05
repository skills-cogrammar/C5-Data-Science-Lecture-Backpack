from pydantic import BaseModel

class UserAuth(BaseModel):
    user_id: str
    email: str
    password_hash: str