
#In the dropbox we have for_example2.py which includes the below code:

#   stars = "*"
#        for i in range(0 ,10):
#                print(stars)
#                stars = stars + "*"

# This is for a pattern with incrementing stars. 
# For decrementing stars the example file has a different logic. 
# Why does [stars = stars - "*"] not work?"
"""
stars = "******"
stars = stars - "*"
print(stars)
"""

# Hi, I'm working on a uni buddy. 
# How can I introduce a while loop in the following code to 
# avoid duplicating the code below?

#try:
#    age = int(input(""How old are you?""))
#    if age < 18:
#        print(""You're starting university early, you must be a genius!"")
#    elif age <= 20 and age >= 18:
#        print(f""You'll meet lots of other students who are {age} too!"")
#    elif age >= 21:
#        print(""It's never too late to pursue your education!"")
#except ValueError:
#    age = int(input(""Looks like you made a mistake. Please try entering a number: ""))
#    if age < 18:
#        print(""You're starting university early, you must be a genius!"")
#    elif age <= 20 and age >= 18:
#        print(f""You'll meet lots of other students at The University of Everybody who are {age} too!"")
#    elif age >= 21:
#        print(""It's never too late to pursue your education!"")"

"""
while True:
    try:
        age = int(input("Please enter your age: "))
        
        if age < 18:
            print("You're starting university early, you must be a genius!")
        elif age <= 20 and age >= 18:
            print(f"You'll meet lots of other students who are {age} too!")
        elif age >= 21:
            print("It's never too late to pursue your education!")

        break
    except ValueError:
        print("Looks like you made a mistake. Please try entering a number.")
"""


#Create a function, insert, with the following features:
#Takes a list as its first argument.
#Takes any object as its second argument.
#The third argument is the non-negative index in 
# which the given object will be located in the result.
#Pushes the element that was previously located on the given index, 
#and the following elements, one position to the right.
#Returns a new list.
#print(insert(["A", "B", "C", "E"], "D", 3))

#expected output ['A', 'B', 'C', 'D', 'E']
"""
def insert_obj(list_to_edit, obj_to_add, index_of_item):

    current_list = list_to_edit
    current_index = index_of_item
    try:
        current_index = int(current_index)
    except:
        print("Please enter an int as an index value")

    current_list.insert(index_of_item, obj_to_add)
    return current_list

same_list = ['A', 'B', 'C', 'E']
same_list = insert_obj(same_list, "D", 3)
print(same_list)
"""

# Dropbox file: Task14. Holiday.py. 
# I cannot figure out how to make the dictionary output capitalised when 
# I first ask the user to choose a destination from a list. 
# capitalise doesn't seem to do anything. I guess I'm using it wrong!

"""
print("Please select a destination based on the list below: ")
dest_list = ["pretoria", "belgrade", "durban"]
for num in range(len(dest_list)):
    print(f"{num + 1} - {dest_list[num].capitalize()}")

user_input = int(input("Please enter the number of your destination: "))
user_input -= 1

print(f"You selected: {dest_list[user_input].capitalize()}")

"""


# I'm stuck with the logic behind/inside custom functions. 
# I am trying to return two different values out of the same function but this is creating a tuple which 
# I can't concatenate in a f-string. Is there a workaround?

# I'm working on a task about user defined functions. 
# I am embedding a user input into the function. 
# I then want to use this user input in another function. Is that possible?

# Task 11: Please could you explain capitalising alternative letters using a 
# for loop and capitalising alternative words ?