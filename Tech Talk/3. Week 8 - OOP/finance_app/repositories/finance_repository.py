from services.data_connection import DataConnection
from datetime import datetime

class FinanceRepository():
    '''
        Used to perform operations that will get financial information based 
        no the data stored in the database
    '''

    def __init__(self, data_connection: DataConnection) -> None:
        # Create an instance of the DataConnection class,
        # Used reading and writing to the data source
        self.data_connection = data_connection

    def get_current_balance(self):
        '''
            Get the current balance of the account
        '''
        
        # Get all transactions
        all_transactions = self.data_connection.get_all()

        balance = 0

        # Calculate the balance based on all of the transactions
        for transaction in all_transactions:
            balance += transaction.amount

        return balance
    
    def get_balance_for_date_range(self, start_date: datetime, end_date: datetime):
        all_transactions = self.data_connection.get_all()

        dates_in_range = []

        # Get the balance for all transactions in the date range
        for transaction in all_transactions:
            if start_date <= self.__convert_to_date(transaction.date) <= end_date:
                dates_in_range.append(transaction)

        return sum(transaction.amount for transaction in dates_in_range)


    def __convert_to_date(self, date_string: str) -> datetime:
        '''
            Converts a string to a date object

            Params:
                date_string (str) - The date string to be converted.

            Return:
                datetime - The date object.
        '''
        return datetime.strptime(date_string, '%Y-%m-%d')
        