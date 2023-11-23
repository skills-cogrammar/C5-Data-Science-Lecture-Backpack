
'''
The print function is used when the final output of the data is needed.
    We achieve this by entering the print command with an argument.
        command + argument = statement OR
            print(argument) = output
'''

# You will notice that the output will simply give 'Hello World',
#   since that was the statement we created.
print("Hello World!")

'''
The input function is a means to receive user input, should we require it.
    To achieve this we enter the input command along with the instructions for the user.
        variable = input(instructions (argument))
'''

name = input("Please enter your name : ")

'''
Note that in order to store whatever value the user provides us with we
    should use a variable to do so

Therefore, if the user typed in "John" then the variable 'name' would then store
    the value and we may invoke it as we please.

Also note that, until a value is provided, our program will be halted.
'''

'''
Speaking of variables, they are a named storage location in memory for values to
    be stored, e.g. name = "Jimmy"

Keep in mind that :
    - All variables need a descriptive name, it would be difficult to ascertain
        what the variable 'x' is storing. Instead, we can name it according to
            the value we are storing, for instance, if we were storing how much
                health our player has in a game, we could name that variable
                    'health_points' instead of 'hp' or 'points'.
'''

# To create a variable it's as simple as variable = value
greeting = "Hello There"

response = "General Kenobi"

# note that 'greeting' stores 'Hello There' and 'response' stores 'General Kenobi'

'''
We can assign variables to other variables interestingly. In Python, the variable
    value can be updated as the program runs.

Additionally, we can assign multiple variables at once, in one line.
'''

python_is_cool = 100

# Note that here 'another_variable' value is 100, which was 'python_is_cool'
#   original value.
another_variable = python_is_cool

# At this point 'python_is_cool' value was updated to 1000. However, another_variable
# value will remain at 100, since it took place BEFORE the reassignment occured.
python_is_cool = 1000

multiple, variables, assigned = 5, 10, 15