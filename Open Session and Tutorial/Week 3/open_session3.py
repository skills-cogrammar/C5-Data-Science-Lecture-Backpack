
"""
value = 68.585732457698

output = "Your total on your order will be : ${:.2f}"
print(output.format(value))

print(round(value, 2))
"""
"""
# Question
test_string = "This is a test string"
#test_string.insert("Dave"[2]) #- doesn't work!


to_add = "Bla bla bla bla"[2]
print(test_string[:2] + to_add + test_string[2:])
"""

'''
name = "John"
surname = "Python"
curly_bracket = "{}"

print("My name is {} {}, and I am a thorough {} enjoyer \
      ".format(name, surname, surname))

print("My name is {0} {1}, and I am a thorough {1} enjoyer \
     ".format(name, surname))

x = "twenty four"
y = 39
z = 13
print("""Your order of : burger, which costs R{}
Your order of : pizza, which costs R{:.2f}
Your order of : pepsi, whcih costs R{:.2f}""".format(x, y, z))

print(f"""Your order of : burger, which costs R{name}
Your order of : pizza, which costs R{surname}
Your order of : pepsi, which costs R{z:.2f}""")
'''

"""
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

for number in range(len(sentence)):

    #print(f"iteration: {jam} character : {sentence[jam]}")
    if character == sentence[number]:
        count += 1 # count = count + 1

print(f"The character : {character} appeared {count} times")

"""
"""
count = 0
for character in "This is a test string":
    if character.lower() == "t":
        count += 1
"""
"""
count = 0
string = input("Please enter any string: ")
char = input("Please enter any char to count: ").lower()

for i in string:
    if i.lower() == char:
        count += 1
        print(count)
"""
        
"""
user_input = input("Please enter any string: ")
user_word = input("Please enter a word to count: ")

split_sent = user_input.split()
print(split_sent)
count = 0

for string in split_sent:
    print(string)
    print(f"Checking if {string == user_word}")
    if string == user_word:
        count += 1

print(f"Total Word Count: {count}")

"""

# insert
"""
test_string = "This is a string"
test_list = test_string.split()
test_list.insert(2, "NOT"[1])
print(test_list)
"""

# append
test_string = "This is a string"
test_list = test_string.split()

test_list.append(0)
test_list[2] = -1
print(test_list)

for i in range(len(test_list)):
    test_list[i] = str(test_list[i])

new_string = " ".join(test_list)

print(new_string)