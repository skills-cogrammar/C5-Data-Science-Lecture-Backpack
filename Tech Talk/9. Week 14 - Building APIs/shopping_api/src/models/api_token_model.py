from pydantic import BaseModel
from datetime import datetime

class ApiToken(BaseModel):
    token: str
    is_active: bool
    expires: datetime