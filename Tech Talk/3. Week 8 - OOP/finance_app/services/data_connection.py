from abc import ABC, abstractmethod
from models.transaction_model import Transaction

import os

class DataConnection(ABC):
    '''
        Abstract class that is used to represet the methods and attributes that should be 
        included in a data connection class
    '''
    
    def __init__(self, connection) -> None:

        # Create a path to the data folder 
        full_path = f"data/{connection}"
        self.connection = full_path

        # Make sure the file exists
        self.__create_folder()

    def __create_folder(self):
        '''
            Creates a new data folder if one does not exist 
        '''

        # Create a data folder if one does not exist
        if not os.path.exists("data"):
            os.makedirs("data")            

    @abstractmethod
    def get(self, id: str) -> Transaction:
        '''
            Get a single item from the database

            Params:
                id (str) - The ID of the transaction to be retrieved

            Returns:
                Transaction - The transaction object
        '''
        pass

    @abstractmethod 
    def get_all(self) -> list[Transaction]:
        '''
            Get all of the transactions from the database

            Return:
                List[Transaction]
        '''
        pass

    @abstractmethod        
    def insert(self, data: Transaction) -> None:
        '''
            Adds a transaction to the database.

            Params:
                data (Transaction) - The transaction to be added
        '''
        pass