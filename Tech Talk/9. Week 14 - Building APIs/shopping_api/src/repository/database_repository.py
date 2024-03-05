from sqlalchemy import create_engine, text, Table, MetaData
from sqlalchemy import select, insert, update, delete

class DatabaseRepository:
    def __init__(self, connection_string: str) -> None:
        self.__connection_string = connection_string

        if not self.__check_connection():
            raise Exception("Database connection failed")
        
        self.engine = create_engine(self.__connection_string)

    def get_connection(self):
        return create_engine(self.__connection_string)
    
    def create(self, table_name: str, values: dict):
        table_name = Table(table_name, MetaData(), autoload_with=self.engine)

        with self.engine.connect() as conn:
            stmt = insert(table_name).values(values)      
            conn.execute(stmt)
            conn.commit() 

    def get_all(self, table_name: str,):
        table_name = Table(table_name, MetaData(), autoload_with=self.engine)

        with self.engine.connect() as conn:
            stmt = select(table_name)
            result = conn.execute(stmt)
            return result.fetchall()
        
    def get(self, table_name: str, id: str):
        table_name = Table(table_name, MetaData(), autoload_with=self.engine)

        with self.engine.connect() as conn:
            stmt = select(table_name).where(table_name.columns.id == id)
            result = conn.execute(stmt)
            return result.fetchone()
        
    def update(self, table_name: str, id: str, values: dict):
        table_name = Table(table_name, MetaData(), autoload_with=self.engine)

        with self.engine.connect() as conn:
            stmt = update(table_name).where(table_name.columns.id == id).values(values)
            conn.execute(stmt)
            conn.commit()

    def delete(self, table_name: str, id: str):
        table_name = Table(table_name, MetaData(), autoload_with=self.engine)

        with self.engine.connect() as conn:
            stmt = delete(table_name).where(table_name.columns.id == id)
            conn.execute(stmt)
            conn.commit()
        
    def execute_statement(self, statement):
        with self.engine.connect() as conn:
            result = conn.execute(statement)
            return result.fetchall()
        
    def get_table(self, table_name: str):
        table_name = Table(table_name, MetaData(), autoload_with=self.engine)
        return table_name
            

    def __check_connection(self):
        try:            
            self.__test_engine_connection()
            return True
        except Exception as e:
            print(e)
            return False
        
    def __test_engine_connection(self):
        engine = create_engine(self.__connection_string)

        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))            


        