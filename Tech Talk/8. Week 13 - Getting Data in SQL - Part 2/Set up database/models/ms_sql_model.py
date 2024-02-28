"""
WARNING: DO NOT MAKE ANY CHANGES TO THE CODE, 
         PLEASE FOLLOW THE INSTRUCTIONS IN THE README FILE TO SET EVERYTHING UP
"""
from pydantic import BaseModel, Field

class SQLServer(BaseModel):
    user: str = Field(default="")
    password: str = Field(default="")    
    server: str = Field(default="localhost")        
    driver: str = Field(default="SQL Server Native Client 11.0")
    database: str

    def __str__(self) -> str:
        credentials = ":".join([self.user, self.password, "@"]) if self.user and self.password else ""
        return f'mssql+pyodbc://{credentials}{self.server}/{self.database}?driver={self.driver}'