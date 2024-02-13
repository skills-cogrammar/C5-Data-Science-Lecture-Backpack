# This is 4 to the power of 3
x = pow(4, 3) #( 4 * 4 * 4 )
# Demo
# 4 X 4 = 16
# 16 X 4 = 64
#print(x)

# Using double asterisk operator as an alternative
y = 4**3
#print(y)

num = 1


# ask the user to select 1 of two options - music or movies
# make sure the user's input is not case sensative 
# display recommendation based on selection

while True:
    user_selection = "Music - Select for a list of recommended music tracks\n"
    user_selection += "Movies - Select for a list of recommended movies\n"
    user_selection += "Please select either Music or Movies in order to proceed: "

    selection = input(user_selection)

    

    selection = selection.lower()
    selection = selection.strip()

    if (selection == "movies"):
        print("Thank you, Movies selected")
        break

    elif (selection == "music"):
        print("Thank you, Music selected")
        break

    else:
        movies_matched_chars = 0
        music_matched_chars = 0
        # Check for a minimum of 3 or more matching character to make a suggestion

        movies = "movies"
        music = "music"
        error_message = ""

        if len(selection) == 5:
            for index in range(len(selection)):
                if selection[index] == music[index]:
                    music_matched_chars += 1

            if music_matched_chars >= 3:
                error_message += "\nDid you perhaps mean Music?"

        elif len(selection) == 6:
            for index in range(len(selection)):
                if selection[index] == movies[index]:
                    movies_matched_chars += 1

            if movies_matched_chars >= 3:
                error_message += "\nDid you perhaps mean Movies?"

        error_message += "\nSorry invalid input - please try again\n"

        print(error_message)

