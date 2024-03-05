from pydantic import BaseModel, Field
from src.enum.roles import Role

class User(BaseModel):
    id: str
    role: int
    first_name: str = Field(default=None)
    last_name: str = Field(default=None)
    email: str
    cart: list[str] = Field(default=[]) # Contains a list of product Ids
    wishlist: list[str] = Field(default=[]) # Contains a list of product Ids
    
