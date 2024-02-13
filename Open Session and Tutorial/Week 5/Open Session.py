#can you merge 2 lists to create/ and create a dictionary with it? 
#For example if you had a game inventory and wanted to count the number of each item 
#in there (e.g. number of rupees, goblin horns etc)
'''
item_type = [
    "number of rupees", 
    "goblin horns", 
    "potions", 
    "unicorn horns", 
    "dragon tongues"]

item_counts = [100000, 25, 10, 1, 0]

item_dict = {}

# Using Enumerate to create a dict out of two lists
"""
for index, value in enumerate(item_type):
    
    # dict_name[dict_key] = dict_value
    item_dict[value] = item_counts[index]
"""
for index in range(len(item_type)):
    print(f"Index Number {index} is accessing {item_type[index]} in item_type list.")
    print(f"Index Number {index} is accessing {item_counts[index]} in item_counts list.")
    
    # dict_name[dict_key] = dict_value
    item_dict[item_type[index]] = item_counts[index]

#would you use dict(zip(list1, list2))?
"""
item_dict = dict(zip(item_type, item_counts))
"""

print(item_dict)

'''

'''
#I got feedback for this code:
# Get the user's age
age = int(input("Enter your age: "))

# Check the age and print the appropriate message

if age > 100:
    print("Sorry, you're dead.")
elif age >= 65:
    print("Enjoy your retirement!")
elif age >= 40:
    print("You're over the hill.")
elif age == 21:
    print("Congrats on your 21st!")
elif age < 13:
    print("You qualify for the kiddie discount.")
else:
    print("Age is but a number.")


#Feedback: As per the specified task requirements, if the age is 101 or older, 
#the program is expected to print out the message 'Sorry, you're dead.'. 
#Regrettably, the current implementation displays the message 
#'You're over the hill.' To address this, I recommend reorganizing your 
#conditional statements in descending order, starting from the highest age 
#and progressing downwards. This adjustment will help rectify the current logical error 
#and ensure the correct execution of the program.

#Please could you help me with this as I am not sure how to incorporate this feedback 
#into my code. Thanks."

'''

"""
#How can we add color format to our programmes in Python?
# Example from: https://www.geeksforgeeks.org/print-colors-python-terminal/
from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

def blue_highlight(string_value):
    print(Back.BLUE + string_value)
    print(Style.RESET_ALL)

blue_highlight("This is a test")
"""


"""
I am confused about when to use return or not in a function and 
the different ways of calling a function with or without a return statement
"""

def add_one(num):
    num += 1
    return num

counter = 0
counter = add_one(counter)

print(counter)


