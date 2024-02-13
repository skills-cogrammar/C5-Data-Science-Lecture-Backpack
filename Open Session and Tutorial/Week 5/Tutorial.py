
#task 11:
#i am trying to make each alternative word of the entered string upper/lower 
#case in 2nd section of code but it does not seem to be working, please could you help?
"""
string = input("Please enter a string: ")           
#user input for string

new_string = ""
string_list = []         
#empty string to add to

#first section of code is to make each alternating character of the inputted 
#string uppercase and lower case (e.g. hElLo)

for alternate in range(len(string)):                
  
    if alternate % 2 == 0:
        new_string += string[alternate].upper()              
        #if even then makes character uppercase 
    
    else:
        new_string += string[alternate].lower()
        #if odd then makes character lowercase 

print(f"The new string with alternating letter is: {new_string}")


#the 2nd section of code makes each word of the entered string uppercase or lowercase 
split_word = string.split()

for alternate in range(len(split_word)):

    if alternate % 2 == 0:
        string_list.append(split_word[alternate].upper())
    else:
        string_list.append(split_word[alternate].lower())
print(split_word)
print(string_list)
new_alt_string = " ".join(string_list)

print(f"The new string with alternating letters is {new_alt_string}")
"""


#Hi.
#I have a question related to the functions task ..

#If we are trying to write a function to calculate the total cost of a 
#hotel visit based on number of nights.
#The function could look like this:
"""
def hotel_cost(num_nights, hotel):
    #hotel_list = [100, 1000, 10]
    hotel_cost_dict = {"Brazil": 100, "Japan": 1000, "South Africa": 10}

    #print(hotel_list[2])
    #print(hotel_cost_dict["South Africa"])

    hotel_cost = hotel_cost_dict[hotel] * num_nights
    return hotel_cost

print(hotel_cost(7,"Brazil"))
"""

#Regarding the cost_per_night. What is best practise?
#1) define cost_per_night = 100 elsewhere in the algortithm
#2) ""hardcode"" a value straight into the function eg 100
#3) set cost_per_night as a local variable
# ie. def hotel_cost(num_nights, cost_per_night ):
#      hotel_cost = cost_per_night * num_nights
#      return hotel_cost

#thanks



#Is there any difference between:
'''
def add_one(num):
    """
    Adds 1 to the passed int value
    """
    return num + 1

num = add_one(1)

#and 

def add_one(num):
    y = num + 1
    return y
'''

"""
postal_code = {1002: "You know where", 1003: "Nowhere", 1004: "India", }

print(f"I live in: {postal_code[1002]}")
"""



#can you go over string manipulation again please?
#for string manipulation I'm trying to use list comprehension to check conditions, 
#and creating a list using .split()
"""
test_string = "This*is*a*test"

string_list = test_string.split("*")
print(string_list)

if "test" in string_list:
    print("This is a test string, because it contains test")

else:
    print("This is not a test!")

new_string = " ".join(string_list)
print(new_string)

new_list = [value.upper() if index % 2 == 0 else value.lower() for index, value in enumerate(string_list)]
print(new_list)
"""
#How can we check and alternatively change the case of words in the list?

"""
Looping through lists and dictionary
"""

"""
can you explain error handling little bit
"""

"""
Could you please show how to import a module in which we define a function 
and call it in another program?
"""

import test.import_me_please as test

num = test.add_int(100)

print(num)