'''name = "John"
surname = "Python"
curly_bracket = "{}"

print("My name is {} {}, and I am a thorough {} enjoyer \
      ".format(name, surname, surname))

print("My name is {0} {1}, and I am a thorough {1} enjoyer \
     {{}}  ".format(name, surname))

x = "twenty four"
y = 39
z = 13
print("""Your order of : burger, which costs R{}
Your order of : pizza, which costs R{:.2f}
Your order of : pepsi, whcih costs R{:.2f}""".format(x, y, z))

print(f"""Your order of : burger, which costs R{name}
Your order of : pizza, which costs R{surname}
Your order of : pepsi, which costs R{z:.2f}""")'''

# program that counts how many instances of a character there are in a string

count = 0
sentence = input("Please enter your string : ").lower()

while True:
    
    character = input("Please enter the character you would like to count : ").lower()

    if len(character) > 1:
        print("You have entered more than one character, please try again ")

    
    elif not character.isalpha():
        print("You have entered a number or symbol. please try again")


    else:
        break

for jam in range(len(sentence)):

    #print(f"iteration: {jam} character : {sentence[jam]}")
    if character == sentence[jam]:
        count += 1 # count = count + 1

print(f"The character : {character} appeared {count} times")