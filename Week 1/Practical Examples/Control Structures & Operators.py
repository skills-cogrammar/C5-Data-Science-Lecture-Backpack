'''
Booleans can only be one of two values
    True or False
'''

# Notice how the word lights up when we type it out.
var = True
var2 = False

'''
Values like 0, None and empty strings are by default False
'''

value = 0
value2 = None
value3 = ""

# Notice how all three will print : False
print(bool(value))
print(bool(value2))
print(bool(value3))

'''
Any other value aside from the above 3 will return true
'''

value4 = -28.398
value5 = "Hi I am a string!"

# Notice how both will print : True
print(bool(value4))
print(bool(value5))

'''
if, elif and else Statements
    IF condition is true : execute statments
'''

x = 10

if x > 6:
    
    '''
    The condition within the if statement is true, therefore the below print
        command will execute.
    '''

    print("x is greater than 6")

print("""
    This print is not within the scope of the if statement, therefore it will
        print, regardless if the condition above is true or false.
""")

is_raining = False

if is_raining == True:

    print("Bring a coat!")

else:

    print("Leave coat at home!")

user_num = int(input("Please enter a number : "))

if user_num == 0:
    print("Please enter a number that is not zero")

elif user_num < 10:
    print("Your number is less than 10")

elif user_num > 10:
    print("Your number is greater than 10")

else:
    print("Are you sure you entered a number?")


grade = int(input("Enter your grade : "))

if grade > 50:

    if grade > 75:
        print("You passed!")

    else:
        print("You passed, but you could improve!")

else:
    print("You will need to rewrite.")