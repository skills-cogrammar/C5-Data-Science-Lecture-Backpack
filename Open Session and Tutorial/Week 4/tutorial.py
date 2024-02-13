# concept of increasing and decreasing patterns

# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

# loop for nine rows of our pattern 
# increase number of stars in pattern until the 5th row is reached
# Then decrease the pattern 
'''
pattern = "*"

for row in range(1, 10):

    if row <= 5:
        print(pattern * row)
    
    else:
        print(pattern * (10 - row))
'''

# Can you please explain string functions join and split and also dictionaries
# Could you go over string handling please

'''
test_string = "This is a test"
split_string = test_string.split(" ")
print(split_string)
joined_list = " ".join(split_string)
print(joined_list)

count = 0
for char in joined_list:
    if char.upper() == "T":
        count += 1

print(f"This is the number of this char {count}")
joined_list = joined_list.replace("i", "I", 5)
print(joined_list[5:])

numbers = [1, 2, 3, 4, 5]

for num in range(len(numbers)):
    numbers[num] = str(numbers[num])

print(numbers)

numbers = "-".join(numbers)
print(numbers)
'''
"""
test_dict = {"name": "Chris"}
test_dict["is_funny"] = False

print(test_dict["name"])
"""
"""
user_db = []

while True:
    user_input = input("Would you like to log in or register? (Enter: login/register)")

    if user_input.strip() == "register":
        username = input("Please enter your desired username: ").strip()
        password = input("Please enter your desired password: ")
        
        is_unique = True
        for account in user_db:
            if account["username"] == username:
                is_unique = False

        if is_unique:
            user_db.append({"username": username, "password": password})
            print("User registered")
        else:
            print("Cannot register user, username taken")

    elif user_input.strip() == "login":
        username = input("Please enter your username: ").strip()
        password = input("Please enter your password: ")
        
        for account in user_db:
            if account["username"] == username:
                if account["password"] == password:
                    print("Great you logged in")
                else:
                    print("Sorry wrong password")

    print(user_db)
"""
    
# could you go over list comprehension
# can you please show that how to check the type of data in list items. 
# i.e if list has integer item, string item and another list as list item.
"""
test_list = [1, 1.234, False, "Test"]

for item in test_list:
    print(type(item))
    item_type = f"{type(item)}"
    
    if item_type == "<class 'str'>":
        print("This is a string!")
    
    elif item_type == "<class 'bool'>":
        print("It's either true or false")
    
    elif item_type == "<class 'int'>":
        print(f"{item + 2}")
"""
'''
import pandas as pd
import math as m

number = m.sqrt(8)
print(number)

df = pd.read_excel("data_test.xlsx")
print(df)
print(df.iloc[66,0])
'''
# importing files - how do you import files
# Can you please explain how to import an excel file into python for interrogation

# Can you show a example of a logical error?
# Can you please go over try and except error handling
number = 100

for num in range(11):
    
    try:
        print(number / (10 - num))
        test = "test"
    
    except ZeroDivisionError:
        print("Haha you cannot divide by 0!")


