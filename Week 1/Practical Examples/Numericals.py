'''
There are three types of numbers in Python : 
    --> Integers : whole numbers that are either positive or negative values.
        e.g. -32, 0, 600, 138227

    --> Floats : decimal numbers that are also either positive or negative values.
        e.g. 6.2, -27.157, 33.33333

    --> Complex : numbers that have both a real and imaginary part, which are
        both floats

When we declare numbers in Python, it is able to determine the data type of the 
    value based on the data's characteristics.
'''

num_one = 7 # >> no decimal point, no quotation marks (so it cannot be a string)
            #   meaning it has to be an integer

avg_grade = 8.3 # >> has a decimal point, no quotation marks, meaning it has to be
                # a float.

'''
Arithmetic Operations
    If we have numbers in Python, we can of course do math to them.
        Some basic operations include : 

            Addition       (+)
            Subtraction    (-)
            Multiplication (*)
            Division       (/)
            Modulus        (%)
            Exponents      (**)
'''

x = 24
y = 12

adding = x + y
print(adding) # Result >> 36

subtracting = x - y
print(subtracting) # Result >> 12

division = x / y
print(division) # Result >> 2

mod = x % y
print(mod) # Result >> 0

exponents = x ** y
print(exponents) # Result >>  95,367,431,640,625

'''
Casting data types
'''

x = 4.2

# To string
x_str = str(x)

# To integer
x_int = int(x)

# To float
x_float = float(x)