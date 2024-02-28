"""
WARNING: DO NOT MAKE ANY CHANGES TO THE CODE, 
         PLEASE FOLLOW THE INSTRUCTIONS IN THE README FILE TO SET EVERYTHING UP
"""
from pydantic import BaseModel, Field

class Postgres(BaseModel):
    user: str = Field(default="postgres")
    password: str = Field(default="postgres")
    server: str = Field(default="localhost")
    port: int = Field(default=5432)        
    database: str

    def __str__(self) -> str:
        credentials = ":".join([self.user, self.password]) if self.user and self.password else ""

        return f"postgresql://{credentials}@{self.server}:{self.port}/{self.database}"