"""
WARNING: DO NOT MAKE ANY CHANGES TO THE CODE, 
         PLEASE FOLLOW THE INSTRUCTIONS IN THE README FILE TO SET EVERYTHING UP
"""

from models.ms_sql_model import SQLServer
from models.postgres_model import Postgres
from models.my_sql_model import MySQL

def get_database_model(service: str, config_data: dict[str]):
    try:
        return __get_connection_from_service(service, config_data)
    except Exception as e:
        print(f'Error: {e}')
        return None


def __get_connection_from_service(service: str, config_data: dict[str]):
    if service == 'ms_sql_server':               
        return SQLServer(**config_data)
    elif service == 'postgres':
        return Postgres(**config_data)    
    elif service == 'mysql':
        return MySQL(**config_data)
    else:
        None