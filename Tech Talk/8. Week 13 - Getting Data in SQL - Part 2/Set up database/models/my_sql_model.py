"""
WARNING: DO NOT MAKE ANY CHANGES TO THE CODE, 
         PLEASE FOLLOW THE INSTRUCTIONS IN THE README FILE TO SET EVERYTHING UP
"""
from pydantic import BaseModel, Field

class MySQL(BaseModel):
    user: str = Field(default="")
    password: str = Field(default="")
    server: str = Field(default="locahost")
    port: int = Field(default=3306)
    database: str 

    def __str__(self) -> str:
        credentials = ":".join([self.user, self.password, '@']) if self.user and self.password else ""

        return f'mysql+pymysql://{credentials}{self.server}:{self.port}/{self.database}'