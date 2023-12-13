'''Banking app with a solid UI (user interface)
- Checking Balances
- Transferring Funds
- Depositing Money
- Withdrawing Money
- Checking Account limits
- Confirmation Prompts
'''
import random as rd

def check_bal():

    current_balance = rd.randint(100, 999999)
    return f"Your current balance is R{current_balance}"





print("Welcome to SafeBank Banking App!\nPlease enter your details below : ")

while True:
    user_email = input("Enter your email address : ")

    if '@' in user_email and '.' in user_email:
        print("Email Exists")
    else:
        print("Invalid Email, try again!")
        continue

    user_pin = input("Please enter your PIN : ")

    if len(user_pin) == 4 and user_pin.isdigit():
        print("User PIN accepted.")
        break

    else:
        print("Invalid PIN, try again")

print("Welcome! Please make a selection below : ")

print("""
1. to check your current balance
2. to transfer funds
3. to deposit an amount of money
""")

choice = input("Please make your selection (enter the number) : ")

if choice == '1':

    confirm_pin = input("Please enter your PIN to confirm action : ")

    if user_pin == confirm_pin:
        balance = check_bal()
        print(balance)
    else:
        print("Incorrect PIN")