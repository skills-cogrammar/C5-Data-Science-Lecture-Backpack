from datetime import datetime
from services.data_connection import DataConnection
from services.json import JsonService
from repositories.finance_repository import FinanceRepository
from repositories.transaction_repository import TransactionRepository
from models.transaction_model import Transaction

def add_transaction():    
    '''
        Performs the operations to create a new transaction
    '''

    while True:
        print("\033c", end="")
        show_add_transaction_menu()

        choice = input("-> ")

        if (choice == "1"):
            # Gets income transcation details and saves them
            transaction_details = get_transaction_details(is_income=True)
            transaction_repo.add_new_transaction(transaction_details)                   
        elif (choice == "2"):
            # Gets expense transcation details and saves them
            transaction_details = get_transaction_details(is_income=False)
            transaction_repo.add_new_transaction(transaction_details)            
        elif (choice == "3"):
            break
        else:
            print("Invalid choice. Please try again.")

        input("Enter to continue...")

def show_add_transaction_menu():
    '''
        Display the menu for the add transaction choice
    '''
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Back")

def get_transaction_details(is_income: bool) -> Transaction:
    '''
        Gets the details about a transaction

        Params
            is_income (bool) - Is the user entering income or an expense
        
        Return 
            A new transaction object

    '''

    print("\033c", end="")

    transaction_type = "Income" if is_income else "Expense"

    print(f"Fill out {transaction_type} details")
    print("="*40)

    title = input("Name: ")
    description = input("Description: ")
    amount = input("Amount: ")
    date = datetime.now().strftime("%Y-%m-%d")

    print("="*40)

    # convert the amount to negative if the transaction is an expense
    amount = -float(amount) if not is_income else float(amount)

    return Transaction(title, description, amount, date)


def view_transactions():
    '''
        Performs operations to view a transaction
    '''

    print("\033c", end="")
    print("View Transactions")
    print("="*40)

    while True:
        print("\033c", end="")
        show_view_transaction_menu()

        choice = input("-> ")

        if (choice == "1"):
            # Get the data from income trasaction
            income_transactions = transaction_repo.get_all_income_transactions()
            print_transcations(income_transactions)

        elif (choice == "2"):
            # Get the data from expense trasaction
            expense_transactions = transaction_repo.get_all_expense_transactions()
            print_transcations(expense_transactions)

        elif (choice == "3"):
            break
        else:
            print("Invalid choice. Please try again.")

        input("Enter to continue...")

def show_view_transaction_menu():
    '''
        Display the options for the view transaction menu
    '''
    print("1. View Income")
    print("2. View Expense")
    print("3. Back")

def print_transcations(transcations: list[Transaction]):
    '''
        Prints out the transactions from the transcation list 

        Params:
            transactions (list[Transaction]) - list of the transactions that have been performed
    '''
    for transaction in transcations:
        print(transaction)
        print("_"*40)

    print("="*40)


def view_balance():
    '''
        Performs the operations to show the balance
    '''
    while True:
        print("\033c", end="")
        print("Balance")
        print("="*40)

        show_balance_menu()

        choice = input("-> ")

        if choice == "1":            
            # Current balance
            balance = financal_repo.get_current_balance()
            print(f"Current Balance: ${balance:.2f}")
        elif choice == "2":  
            # Balance within date range
            start_date = get_date_input("Start Date (YYYY-MM-DD): ")
            end_date = get_date_input("End Date (YYYY-MM-DD): ")

            balance = financal_repo.get_balance_for_date_range(start_date, end_date)
            
            print(f"Balance in date range: ${balance:.2f}")

        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

        input("Enter to continue...")



def show_balance_menu():
    '''
        Show the options for displaying the balance
    '''
    print("1. Current Balance")
    print("2. Balance in date range")
    print("3. Back")

def get_date_input(message: str):
    '''
        Gets a valid date input from the user
    '''
    while True:
        try:
            date = input(message)

            return datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please try again.")

def show_welcome_screen():
    '''
        Displays the header for the application
    '''
    print("-"*40)
    print("Financial Tracker")    
    print("-"*40)

def show_menu():
    '''
        Shows the main screen options
    '''

    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. View Balance")
    print("4. Exit")

if __name__ == "__main__":    
    # Create global variables for the services that will be used
    global financal_repo, transaction_repo, data_connection
    
    # Setup the database connection,
    # If we ever wanted to change data sources, we would only ever 
    # need to change this single line of code 
    # If we wanted to work with a SQL database, we would have: 
    # data_connection = SqliteService("transactions.db")
    data_connection = JsonService("transactions.json")

    # Setup the repositories that will allow us to perform our queries 
    # We are passing the data source to each repository so that they 
    # Work with the correct data source.
    financal_repo = FinanceRepository(data_connection)
    transaction_repo = TransactionRepository(data_connection)

    while True:        
        print("\033c", end="")

        show_welcome_screen()
        show_menu()

        choice = input("-> ")

        if (choice == "1"):
            add_transaction()
        elif (choice == "2"):
            view_transactions()
        elif (choice == "3"):
            view_balance()
        elif (choice == "4"):
            break
        else:
            print("Invalid choice. Please try again.")
        