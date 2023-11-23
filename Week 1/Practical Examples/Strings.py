'''
What are Strings?
    - Any data made up of a sequence of letters or other characters
    - Simply put, strings are just characters that have been "strung" together.

Strings are detected by either quotations ("") or inverted commas ('')
'''

quotation_str = "The quick brown fox jumps over the lazy dog"

inverted_comma_str = 'Strings are rather useful, what do you think?'

'''
Strings can be added to one another. This is referred to as concatenation.
    We achieve this by merging strings with the '+' symbol
'''

name = "Pieter"
surname = "Parker"

full_name = name + surname

# If we print above, the two strings will be merged with no space inbetween

# We can alliviate that with :
full_name = name + " " + surname

# We can take this one step further with f-strings
# Great for particularly long strings that we'd like to output.
full_name = f"{name} {surname}"

'''
String methods : means to manipulate strings to what we may need.

    A few we'll go over are :

        len()
        upper()
        lower()
        capitalize()
        strip()
        split()
        join()
        replace()
'''

# The len method will output the length value of a string
# Keep in mind that len will count spaces in the string as well.
word = "batman"

len_word = len(word)
print(len_word) # Result >> 6

# The upper method will take a string and convert all characters to uppercase.
message = "PyThOn Is FuN"

new_message = message.upper()
print(new_message) # Result >> PYTHON IS FUN

# The lower method will take a string and convert all characters to lowercase.
message = "PyThOn Is FuN"

new_message = message.lower()
print(new_message) # Result >> python is fun

# The capitalize method will take a string and convert the first letter in a
#   string to uppercase and the rest of the characters to lowercase,
#       should there be any other uppercase characters.

message = "PyThOn Is FuN"

new_message = message.capitalize()
print(new_message) # Result >> Python is fun

# The strip method will remove a symbol that we specify from a string.
#   Keep in mind that strip will only remove from the ends of a string.

message = "****They've*taken*the*hobbits*to*Eisenguard!****"

message_strip = message.strip("*")
print(message_strip) # Result >> They've*taken*the*hobbits*to*Eisenguard!

# The split method will split a string by a specified symbol. However, once the
#   split has occured the string will then be placed in what's called a list,
#       which we shall cover in another lecture.

message = "The-king-of-iron-fist"

message_split = message.split("-")
print(message_split) # Result >> ["The", "king", "of", "iron", "fist"]

# The join method will take a list of strings and concatenate them to form a string

list_example = ["The", "king", "of", "iron", "fist"]

list_join = " ".join(list_example)
print(list_join) # Result >> "The king of iron fist"

# The replace method will replace any specified character in a string with a new
#   character / symbol. Keep in mind that replace requires two arguments to function
#       First one to identify what to replace, and the second to identify what to
#           replace with.

message = "Hey!you!over!there!"

message_replace = message.replace("!", " ")
print(message_replace) # Result >> Hey you over there

'''
Indexing : 
    Strings are basically a list of characters. An example would be "Hello", which
        consists of the characters H+e+l+l+o

And Python assigns each character with an index value so : 
    "H" would be index 0 (if we counted backwards this would be -1)
    "e" would be index 1 (if we counted backwards this would be -2)
    "l" would be index 2 (if we counted backwards this would be -3)
    "l" would be index 3 (if we counted backwards this would be -4)
    "o" would be index 4 (if we counted backwards this would be -5)
'''

'''
String slicing is a way of extracting one or multiple characters from a string, based
    on their index position.

Remember that slicing is done character by character, not word by word.
'''
string = "Hello"

idx = string[4]
print(idx) # Result >> "o"

slice_str = string[0:2] # remember the following when selecting what to slice : 
                        # [start : end : step]
print(slice_str) # Result >> "He"
