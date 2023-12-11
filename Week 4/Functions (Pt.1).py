import random as rd

cpu_choice = rd.randint(1,3)
print(cpu_choice)

user_choice = int(input("Enter 1 for rock, 2 for paper, 3 for scissors : "))

# 1 = rock
# 2 = paper
# 3 = scissors
if cpu_choice == 1 and user_choice == 2:

    print("You win!")
    print("Paper beats rock!")

elif cpu_choice == user_choice:

    print("Its a tie!")

# The other checks Nizaam was too lazy to create

def addition(x, y):

    value = x + y
    return value

x = int(input("Please enter a number : "))
y = int(input("Please enter a number : "))

total = addition(x, y)
print(total * 4)