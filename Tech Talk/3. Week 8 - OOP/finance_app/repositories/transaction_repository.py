from services.data_connection import DataConnection
from models.transaction_model import Transaction

class TransactionRepository():
    '''
        Connects to the data source and filters the results to 
        match the results that the user wants
    '''
    
    def __init__(self, data_connection: DataConnection) -> None:
        # Create an instance of the DataConnection class,
        # Used reading and writing to the data source
        self.data_connection = data_connection

    def get_transactions(self):
        '''
            Get all transactions from the database
        '''

        return self.data_connection.get_all()
    
    
    def get_transaction(self, id: str) -> Transaction:
        '''
            Gets a single transaction from the database
            by the id passed in.

            Params:
                id (str) - The id of the transaction to get

            Return:
                Transaction - The transaction that was found.
                None - If no transaction was found.
        '''
        return self.data_connection.get(id)
    
    def get_all_income_transactions(self) -> list[Transaction]:
        '''
            Get all of the income transactions from the database

            Return:
                List[Transaction] - A list of all income.
        '''

        all_transactions = self.data_connection.get_all()

        output = []

        for transaction in all_transactions:
            if transaction.amount > 0:
                output.append(transaction)

        return output
    
    def get_all_expense_transactions(self) -> list[Transaction]:
        '''
            Gets all expenses from the database 

            Return:
                List[Transaction] - A list of all expenses.                    
        '''
        all_transactions = self.data_connection.get_all()

        output = []

        for transaction in all_transactions:
            if transaction.amount < 0:
                output.append(transaction)

        return output
    
    def add_new_transaction(self, transaction: Transaction):
        '''
            Adds a transaction to the database 

            Params:
                transaction (Transaction) - The transaction to be added.
        '''        

        self.data_connection.insert(transaction)
    


