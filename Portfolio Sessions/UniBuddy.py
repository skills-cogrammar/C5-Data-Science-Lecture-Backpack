'''
[Case Study Story] --> Imagine the first day of university for a freshman named Alex. 
Alex is excited but also overwhelmed by the vast campus, numerous courses, and the sea of new faces. 
To aid new students like Alex, the university's IT department has developed a personalised chatbot. 
This chatbot, named "UniBuddy", is designed to make the transition smoother for freshmen.
Upon accessing the chatbot, Alex is prompted to enter their name, favourite colour, and age. 
Based on this input, UniBuddy offers a personalised greeting.
For instance, if Alex's favourite colour is blue,
    UniBuddy might suggest joining the university's "Blue Art Club".
If Alex is 18, the chatbot might provide information about freshman-specific events.
The chatbot also offers a feature where Alex can input specific queries, like "Where is the library?"
    or "How do I join the debate club?", 
        and UniBuddy responds with relevant information, all while adhering to a friendly tone,
        using string transformation methods to ensure the responses feel personalised and engaging.
'''

# Initialise message, for first time start
print('''
Welcome to UniBuddy! Your all-in-one app that makes your freshman journey a bit
easier to navigate!

    Please enter your credentials to get started! :
''')

user_name = input("Please enter your student name : ").capitalize()
user_age = int(input("Please enter your age : "))
fav_colour = input("Please enter your favourite colour : ").capitalize()

print(f"""
Welcome {user_name}! I see that your favourite colour is {fav_colour}.
I have a few suggestions based on your choice!
""")

if fav_colour == 'Red':

    print("If you like the colour RED, I have the following for you! Check out : ")

    print("""
1. Our red colour themed football club.
2. Our red themed art club.
3. Our vampire themed society.
4. Our twilight themed club
""")
    
elif fav_colour == 'Blue':

    print("If you like the colour BLUE, I have the following for you! Check out : ")

    print("""
1. Our fighting game club, where you can throw digital hands.
2. Our swimming club which include activites such as : aqua aerobics, rowing etc.
3. Our blue themed art club.
4. Our deep sea exploration club.
5. Our bird watching society.
""")

elif fav_colour == 'Yellow':

    print("If you like the colour YELLOW, I have the following for you! Check out : ")

    print("""
1. Our werewolf society
2. Our hiking club
3. Our mountain climbing club
4. Our dance club5
5. Our suntan society.
""")
    

else:
    print("I'm not sure if that was a colour you have entered, please try again.")


if user_age <= 22:

    print("Here are some freshman specific events!")
    print("The list of events Nizaam was totally writing down!")

else:

    print("Here are a few event suggestions that might be to your liking!")
    print("The list of events Nizaam was totally writing down!")

# FAQ ; frequently asked questions

question = input("Is there anything you would like to ask me? (type in q to quit) : ")

if question == 'How is your day':
    print("I exist, so my day is going rather well!")