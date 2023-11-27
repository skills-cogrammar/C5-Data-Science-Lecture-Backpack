'''
Here in this example, we do not know how many times our user will add kittens
    therefore, the use of a while loop works here, since if the condition remains
        true, we can keep adding kittens.
'''

# These lines here are to initialise our while loop
# if the user were to say no, then the loop will not commence.

kittens = 0
question = input("Has a kitten attempted world domination (y/n) : ")

# doesn't this syntax look familiar?
while question == 'y':

    kittens = kittens + 1 # there is a short-hand method for this :
                            # kittens += 1
    
    print(f"{kittens} kittens has attempted world domination")

    # This input is here either to restart the loop, or end it, by making
    #   the condition false.
    question = input("Add another kitten? (y/n) : ")

'''
Please take caution when creating infinite loops. As it may impact your device
    since it will become computationally expensive due to so many iterations being
        run in rapid sucession.
'''

'''while True:

    print("I am an infinite loop!")
    print("And no one can stop me!")'''

while True:

    question = input("Do you wish to stop me? (y/n) : ")

    if question == 'y':

        print("As you wish")
        break

while True:

    print("I am a loop!")
    question = input("Would you like me to continue? (y/n) : ")

    if question == "y":

        print("Back to the beginning!")
        continue

    else:

        print("I shall cease")
        break

'''
Difference with for loops is that we techically know how many times our loop will
    loop.

'''

# So instead of doing something like this :
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")

# We could simply do :

for output in range(11):
    print("Why hello there.")


string = "coffee"

for letter in string:
    print(letter)

# Remember that range follows the same procedure as string slicing.
#   range(start, end, step)