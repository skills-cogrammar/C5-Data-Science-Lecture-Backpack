"""
WARNING: DO NOT MAKE ANY CHANGES TO THE CODE, 
         PLEASE FOLLOW THE INSTRUCTIONS IN THE README FILE TO SET EVERYTHING UP
"""

import json 
import os
from sqlalchemy import create_engine, text
from services.database_connection_factory import get_database_model


def get_database_engine(service: str, config: dict):
    model = get_database_model(service, config)

    if model is None:
        return None
    
    if not model:
        return None
    

    try:
        engine = create_engine(str(model))                        
        __test_engine_connection(engine)

        return engine
    except Exception as e:                
        return None
    
    
def __test_engine_connection(engine):
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))

    

def read_json(file_path: str):
    if not os.path.exists(file_path):
        return None
    
    with open(file_path, 'r') as file:
        return json.load(file)
    
def is_valid_config(config: dict):
    if config.get('service') == None:
        return False

    if config.get('connection_string') == None:
        return False
    
    return True