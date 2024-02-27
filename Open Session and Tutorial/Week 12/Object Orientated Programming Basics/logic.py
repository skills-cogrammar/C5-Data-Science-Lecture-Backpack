# Object Orientated Programming

# Generalise and create a blueprint of in our program for easier access.

# Functions inside of class are now referred to as methods
class Human:

    # Instance method
    def __init__(self, name, height, age, hobby): # Also known as properties
    # self is a representation of any object we create.
        
        self.name = name
        self.height = height
        self.age = age
        self.hobby = hobby

    def __str__(self):
        
        output = f"""
Human Name   : {self.name}
Human Height : {self.height}
Human Age    : {self.age}
Human Hobby  : {self.hobby}
"""
        return output

people = []

# An object
person1 = Human('Nizaam', 180, 25, 'Being a menace')
person2 = Human('Jimbo', 185, 28, 'Racing Cars')
person3 = Human('Jimmy', 177, 20, 'Contributing to society')

people.extend([person1, person2, person3])

for person in people:
    print(person)