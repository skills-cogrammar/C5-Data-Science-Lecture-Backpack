# Import necessary libraries
import time
from StringBuilder import StringBuilder

# ASCII Representation
# Converting characters to their ASCII values
ascii_chars = ['A', 'B', 'C']
ascii_values = [ord(char) for char in ascii_chars]
print("ASCII Values:", ascii_values)  # Shows ASCII values of 'A', 'B', 'C'

# Unicode Representation
# Converting characters, including non-Latin and emoji, to Unicode code points
unicode_chars = ['A', 'λ', '🙂']
unicode_values = [ord(char) for char in unicode_chars]
print("Unicode Values:", unicode_values)
# Unicode Values: [65, 955, 128578]

# UTF-8 Encoding
# Converting strings to their UTF-8 encoded byte representation
utf8_strings = ['A', 'λ', '🙂']
utf8_encoded = [s.encode('utf-8') for s in utf8_strings]
print("UTF-8 Encoded Values:", utf8_encoded)
# UTF-8 Encoded Values: [b'A', b'\xce\xbb', b'\xf0\x9f\x99\x82']

# String Concatenation using '+'
word1 = "Hello"
word2 = "World"
sentence = word1 + " " + word2
print(sentence)  # Output: "Hello World"

# Demonstration of string concatenation using join()
word1 = "Hello"
word2 = "World"
sentence = " ".join([word1, word2])
print(sentence)  # Output: "Hello World"

# String Concatenation using '+'
start_time = time.time()
concat_str = ""
for _ in range(10000):
    concat_str += "hello "
end_time = time.time()
print("Time with '+':", end_time - start_time)
# Time with '+': 0.019999027252197266

# String Concatenation using 'join()'
start_time = time.time()
join_str = ''.join(["hello " for _ in range(10000)])
end_time = time.time()
print("Time with 'join()':", end_time - start_time)
# Time with 'join()': 0.00049591064453125

# Creating an instance of StringBuilder
string_builder = StringBuilder()

# Adding strings
string_builder.add("Hello ")
string_builder.add("world! ")
string_builder.add("This is a StringBuilder example.")

# Building the final string
final_string = string_builder.build()
print("Final String:", final_string)

# Clearing the StringBuilder
string_builder.clear()
print("After Clearing:", str(string_builder))

# Rebuilding with different strings
string_builder.add("Another ")
string_builder.add("example string.")
print("Rebuilt String:", string_builder)


# References for further exploration:
# - ASCII and Unicode: https://www.ascii-code.com/, https://www.unicode.org/
# - Python String Operations: https://docs.python.org/3/library/stdtypes.html#string-methods
# - Performance Comparison: https://ddosify.com/blog/python-string-operations-performance/
