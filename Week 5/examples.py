import copy

import pandas as pd

# tuples
# sets
# lists
numbers = [1,3,4,6,4,2,53]
check = isinstance(numbers[1], int)

nums = numbers.copy()
nums.append(87)

num_copy = copy.deepcopy(numbers)

print(numbers)
print(nums)
print(num_copy)

names = {'John', 'Joe', 'Terry'}
print(type(names))



value = sum([1,2,3,4,5,6])
print(value) # 21

def sumofnumbers(*numbers):
    
    total = 0
    for num in numbers:
        
        total += num
    return total
    
print(sumofnumbers(1,2,3,4,6)) # 16


sentence = f"{23.123125423454:.2f}"
print(sentence)


string = input(": ")
x = {}

for i in string:

    if i in x:
        x[i] += 1
    
    else:
        x[i] = 1

print(x)

