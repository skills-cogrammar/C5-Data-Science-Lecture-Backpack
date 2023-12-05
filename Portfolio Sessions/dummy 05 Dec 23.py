# NizBot

print("Hello There, can you hear me? Is my audio good?")

print("Please make enter your details below : ")

while True:
    try:

        user_name = input("Please enter your name : ").capitalize()
        user_age = int(input("Please enter your age : "))
        user_fav = input("Please enter your favourite colour : ").capitalize()

        if not user_name.isalpha():
            print("Silly Billy")

        elif not user_fav.isalpha():
            print("Silliest Billy")

        else:

            print(f"Welcome {user_name}, I hope you like sarcasm.")
            break

    except ValueError:
        print("You have not entered a number for your age. Please try again")


if user_age <= 22:

    print("""
          I noticed you're a freshman, here are a few suggestions
          based on your freshman status, or don't take these, up to you.
          """)
    
    print("""
    1.  There is the freshman initiation ceremony, that is happening in
        the main hall @ 13h00 (if you're looking at this @ 13h00 what
            are you doing reading this?)

    2.  There are several parties happening on campus grounds, go check them out!
          
    3.  The cinema club is doing a presentation on the campus and it's various
          facilities, check it out if you'd like a better lay of the land.
 """)
    
if user_fav == "Red":

    print("""
        I see your favourite colour is red! Try checking out the
            following clubs that might interest you : 
""")
    
    print("""
        1. Join our red themed boxing club!

        2. Join our Clifford the Big Red Dog appreciation society!

        3. Join our Red Knights chess club and learn tactics!
""")
    
if user_fav == "Blue":

    print("""
        I see your favourite colour is blue! Try checking out the
            following clubs that might interest you : 
""")
    
    print("""
        1. Join our aquatic activities club where we partake in :
            - water polo
            - swimming
            - diving
        
        2. Join our Blues Clues apprieciation society!

        3. Join our Blues genre orentaited Band Club!


""")
    
if user_fav == "Yellow":

    print("""
        I see your favourite colour is yellow! Try checking out the
            following clubs that might interest you : 
""")
    
    print("""
        1. Join our SpongeBob apprieciation society!

        2. Join our Forest Explorers club!

        3. Join our Sunshine Breakfast club!
""")
    
print("""
        Welcome to our FAQ (frequently asked questions) section!
        Please ask away! 
""")

faq_file = open("input.txt", "r")
faq_list = [] # This is a list

for lines in faq_file:
    
    temp = lines.strip('\n')
    temp = temp.split()

    joined = " ".join(temp)
    faq_list.append(joined)

#print(faq_list)

print("This a list of our most frequently asked questions : ")
for count, quest in enumerate(faq_list, start=1):
    print(f"{count}. {quest}")

choice = int(input("Please enter the number question you'd like to ask : "))
index = choice - 1

if index == 0:
    print(f"You have chosen : {faq_list[index]}")

    print("It's to your right, straight down the hall. Silly.")
