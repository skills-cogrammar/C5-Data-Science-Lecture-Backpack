# Is there a difference in operation between the (while loop, break, continue) and (if, Elif, and else)?
# because I feel they both do similar operations or is there a difference?
"""
kittens = 0
question = input("Has a kitten attempted to take over the world?(y/n) ")

while question != "n":
    if question == "y":
        kittens += 1
        print(f"{kittens} have attempted world domination")
    
    elif question != "n":
        print("Invalid Input")
        print("Please enter either y or n")

    question = input("Has another kitten attempted to take over the world?(y/n) ")

if question == "n":
    print("The world is safe ... for now")
"""

# Can you show how to use the popup suggestions on VS code, the are very unintelligible to me at the moment
"""
test_str = "This is a test".split(maxsplit=1)

print(test_str)
"""

# Hi, I dont receive a prompt in the terminal when I put in code which requests for user input for example email address? 
"""
email = input("Please enter your email")
print()
print(f"Your email is: {email}")
"""

# "Hi there! I'm struggling with task 7. I was told by my mentor to do something different but it didn't work. 
#This is my code:
"""
from statistics import mean #built in function to calculate average 

answer = int(input("Enter a number:")) #keep writing a number
list_answers = [] #create a list for the numbers to be saved to
list_answers.append(answer) #saves answer to list

while True: #loop contiuosly 
    answer = int(input("Enter a number:")) #keep writing a number #problem that first number isn't being saved
    if answer == -1: #if -1, remove -1 from list (splice needed!)
        new_avg = mean(list_answers)
        print(new_avg)
        break
    print(list_answers) #will print list each time 
"""
# I'm struggling with saving the first input to the list. 
# Can someone help me figure out what I'm doing wrong and how I can improve this? 
# If you also have advice on how to split the list to exclude the last number (-1), I would appreciate it. 
# I tried splicing the list but I'm struggling with a list that changes. 


# Hi good evening. 
# Please check the following code. 
# I am trying to solve a logic problem 
# (which was asked under logic section in the selection test of this boot camp) through coding. 
# As far as I can remember the problem was something like “a group of kids have a certain number of marbles to play. 
# Each time they play a game they loose certain number of marbles and they hide the rest of the marbles under a tree. 
# A squirrel comes and steels some marbles till the number of marbles are higher than 12. 
# Also, the kids can only play the game if the total number of marbles are greater than or equal to 11. 
# How many games they can play. 
# I remember that the start number of marble in this game was such that before the last game the number 
# of marbles left was 11 so the squirrel cannot steel any, but they can still play 1 last game. 
"""
marbles = 100
game = 0
marbles_lost = 5
theft = 2

while marbles >= 11:
    game += 1
    marbles -= marbles_lost
    
    if marbles >= 12:
        marbles -= theft

print(f"Number of games: {game}")
"""
# Question 1) is the code correct?
# Question 2) Why does it only print to maximum of 5 times doesn’t matter if you increase the marbles to 70 or 80.
# Question 3) what is the best way to print the number of games they can play in this case rather than 
# printing the word “game” for the number of times they can play.


drinks = 0
while True:
    question = input("Have you had enough to drink?")
    print (question)

    if question != "yes":
        drinks = drinks +1
        print (f"You have had {drinks} drinks you, need another")

    else:
        print ("You have had enough")
        break
