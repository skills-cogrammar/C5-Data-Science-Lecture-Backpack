import math
'''
This is an example of block commenting / docstrings
'''

while True:
    print("""
investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan
""")
    selection = input("""Enter either 'investment' or 'bond' from the menu above to proceed : 
                      type in exit to terminate: """).lower()

    if selection == 'investment':

    # amount, years, intrest rate
    # P = The amount deposited
        P = float(input("Please enter the amount you would like to deposit : "))

    # r = Rate of interest (%) user shouldn't add the % symbol to input
        r = float(input("Please enter the rate of interest (exclude % symbol) : ")) / 100

    # t = amount of years of investment
        t = int(input("Please enter the years for investment : "))

        calculation_selection = input("Please select either simple or compound interest : ").lower()

        if calculation_selection == 'simple':

            print("Here is the math Nizaam was too lazy to do.")
            continue

        elif calculation_selection == 'compound':

            print("Here is the math Nizaam was too lazy to do.")
            continue

        else:

            print("Invalid selection")
            continue
    elif selection == 'bond':

        P = float(input("Enter the present value of your house : "))

        r = float(input("Please enter the rate of interest (exclude % symbol) : ")) / 100
        r = r / 12

        t = int(input("Please enter the amount of months planned for repayment : "))

        print("Here is the math Nizaam was too lazy to do.")
        continue

    elif selection == 'exit':

        print("Exiting. . . ")
        break

    else:

        print('Invalid input')
        continue