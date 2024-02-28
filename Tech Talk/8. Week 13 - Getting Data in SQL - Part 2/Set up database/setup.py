"""
WARNING: 
         DO NOT MAKE ANY CHANGES TO THE CODE, 
         PLEASE FOLLOW THE INSTRUCTIONS IN THE README FILE TO SET EVERYTHING UP
"""

import os
import pandas as pd
import threading
import time
from sqlalchemy import text, insert, Table, MetaData

from services.database_connection import get_database_engine
from services.input_handler import get_args, is_args_valid, get_database_details

def insert_to_database(file_name, table_name, engine):
    df = pd.read_csv(file_name)   

    table_name = Table(table_name, MetaData(), autoload_with=engine)

    print(table_name)
    
    with engine.connect() as conn:
        for i, row in df.iterrows():                                
            values = row.to_dict()

            stmt = insert(table_name).values(**values)
            conn.execute(stmt)
            conn.commit()

def insert_all_data(engine):
    tables = ['actor', 'address', 'customer', 'film_actor', 'film', 'inventory', 'language', 'payment', 'rental']

    with engine.connect() as conn:
        for name in tables:            
            try:
                insert_to_database(f"final/{name}.csv", name, engine)                
            except Exception as e:                
                conn.rollback()

def reset_database_tables(engine):
    if not os.path.exists('scripts/create.sql'):
        print("\033[91m")
        print("Important database file missing, please pull the repository again to reset the dependencies")
        print("\033[0m")

        exit()

    with open('scripts/create.sql', 'r') as f:
        scripts = f.readlines()
    
    with engine.connect() as conn:
        for script in scripts:

            script = text(script)
            try:
                conn.execute(script)
                conn.commit()
            except Exception as e:                
                conn.rollback()

    
def loading_animation():
    emojis = ['⚫','🔵','🟢','🟡','🟠','🔴']
    idx = 0
    while not done:
        print(f'{emojis[idx % len(emojis)]}', end='\r')
        idx += 1
        time.sleep(0.5)    

if __name__ in "__main__":
    global done
    done = False

    args = get_args()

    if not is_args_valid(args):
        print("\033[91m")
        print("Please add all the connection details")        
        print("Example: python script.py -s postgres -sr localhost -p 5432 -db postgres -u postgres -pw postgres")
        print("\033[0m")
        print("For help: python script.py -h")
        exit()

    args = {k: v for k, v in args.__dict__.items() if v is not None}
    db_details = get_database_details(args)

    if not db_details:
        print("\033[91m")
        print("Please provide a config file or connection details")
        print("\033[0m")        
        exit()

    engine = get_database_engine(db_details[0], db_details[1])    

    if (engine == None):
        print("error loading the database engine")
        exit()
    
    confirm_next_step = ''


    print("\033[92m")

    print("All of the data in the database will be deleted past this step")
    while confirm_next_step not in ['y', 'n']:
        confirm_next_step = input("Are you sure you want to continue? (y/n): ").lower()
    
    print("\033[0m")

    if confirm_next_step == 'n':
        print("Exiting...")        
        exit()

    animation_thread = threading.Thread(target=loading_animation)
    animation_thread.start()

    print('Resetting Database')    
    reset_database_tables(engine)
    

    print('Inserting data')
    insert_all_data(engine)   

    done = True    
    animation_thread.join()    

    print('DONE')