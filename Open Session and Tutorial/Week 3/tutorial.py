# Create a function, skip_one, that takes a list as input and returns the same 
# list skipping every other element and including the first.
"""
def skip_one(skip_list):
    new_list = skip_list[::2]
    return new_list

sample_list_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
sample_list_2 = [
    "Apple", "Red",
    "Banana", "Yellow",
    "Apple", "Green",
    "Cherry", "Red",
    "Apple", "Red",
    "Banana", "Yellow"
    ]

output_1 = skip_one(sample_list_1)
output_2 = skip_one(sample_list_2)

print(output_1)
print(output_2)
"""

# Could you show us logical errors examples?
"""
num = 50
add_2 = num + 2

print(add_2)
"""

# What will be the value of x after executing the following code:
"""
x = []

def f():
    x = []
    x.append(1)
    x.append(2)
    x.append(3)
    return x

x = f()

print(x)
"""

# Can you please explain compilation and runtime errors

# Compilation Error
"""
n = int( input("Enter a number: "))
if(n<5):
    print(n)
"""
"""
sample_list_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

for i in range(50):
    print(sample_list_1[i])
"""

"""
# Global Var
g_example = ":)"

def example_func():
    local_var = 0
    print(local_var)
    print(g_example)

example_func()
"""

#print(g_example )


"""
def add_2(var_num):
    var_num += 2

    return var_num

test_1 = add_2(1)
test_2 = add_2(13)
test_3 = add_2(55)
test_4 = add_2(76)

print(test_1)
print(test_2)
print(test_3)
print(test_4)
"""

# How do we add the numbers that we take from the users input during a while loop?
# How to calculate the average of the numbers that were entered by the user?
# How we take more input from single input?
"""
count = 0 
total = 0 

while True:
    user_num = input("Please enter a number: ")
    if not user_num.isnumeric() and user_num != "-1":
        print("Please enter only a number")
    elif user_num == "-1":
        average = total / count
        break
    else:
        count = count + 1
        total += int(user_num)



print(f"Total values added: {count}")
print(f"Average values added: {average}")

"""
count = 0 
total = 0 
output_string = ""

while True:
    user_num = input("Please enter a number: ")

    if user_num.lower() == "bye":
        break

    try:
        user_num = float(user_num )

        count = count + 1
        total += user_num
        output_string += f"{user_num} "

    except:
        print("Please enter only a number or a float")

average = total / count

print(f"Total values added: {count}")
print(f"Average values added: {average}")
print(f"All values added: {output_string}")