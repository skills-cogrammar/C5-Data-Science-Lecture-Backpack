from services.data_connection import DataConnection
from models.transaction_model import Transaction

import json
import os


class JsonService(DataConnection):
    '''
        Used to read from and write to a JSON file
    '''

    def __init__(self, connection) -> None:
        # Performs the operations set out by the DataConnection constructor (see DataConnection to see what happens in __init__)
        super().__init__(connection)

    def get(self, id: str) -> Transaction:
        '''
            Gets a single transcation from the database

            Params:
                id (str) - The id of the transaction we want to get 
            
            Return:
                Transaction - matching the ID in the database
        '''
        all_transactions = self.__get_transactions_from_file()

        for transaction in all_transactions:
            if transaction.id == id:
                return transaction
        
        return None

    def get_all(self) -> list[Transaction]:
        '''
            Gets all of the transactions in the JSON file

            Return:
                List[Transaction] - All transactions in the JSON file
        '''
        return self.__get_transactions_from_file()

    def insert(self, transaction: Transaction) -> None:
        '''
            Adds a new transaction to the json file 

            Params:
                transaction (Transactio) : Transaction to be saved
        '''

        all_transactions = self.__get_transactions_from_file()
        all_transactions.append(transaction)
        self.__write_to_json(all_transactions)        

    def __write_to_json(self, transactions: list[Transaction]) -> None:
        '''
            Writes the transactions to the json file

            Params:
                transactions (List[Transaction]) : List of transactions to be saved to the json file.                                                     
        '''        

        with open(self.connection, 'w') as f:
            json.dump(self.__convert_object_list_to_dict(transactions), f, indent=4)
        

    def __convert_object_list_to_dict(self, transactions: list[Transaction]) -> dict:
        '''
            Converts a list of transactions into a list of dictionaries 

            Params:
                transactions (List[Transaction]) : List of transactions to be converted to dictionaries.                                                     
            
            Return:
                List[dict] - List of dictionaries representing the transactions.
        '''
        output = []

        for transaction in transactions:
            output.append(transaction.get_dict())
            
        return output
    
    def __get_transactions_from_file(self) -> list[Transaction]:
        '''
            Gets all of the transactions from the JSON file

            Return 
                List[Transaction] - The transactions saved in the file.
        '''

        # Check if the file exists, if not, create a new file and exit function
        if os.path.exists(self.connection) == False:
            with open(self.connection, 'w') as f:
                json.dump([], f)

            return []

        # Get the data from the file
        with open(self.connection) as f:
            data = json.load(f)

        transactions = []

        # Convert the dictionaries into objects and add them to the output list.
        for transaction in data:
            try:
                transactions.append(Transaction(**transaction))
            except:
                # Log error over here
                pass

        return transactions