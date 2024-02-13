names = [
    "Jimmy",
    "Billy",
    "John",
    "Sally",
    "Joe",
    "Johnny"
    ]

popped_name = names.pop(0)
#print(popped_name)

popped_name = "Jimbo"

names.insert(0, popped_name)
#print(names)


names.insert(0, "Sol")
#print(names)


numbers = [1, 2, 3, 4, 5]
ex_numbers = [6, 7, "Yes", False, "John"]

numbers.extend(ex_numbers)

#print(numbers)


'''if "Lucy" not in names:
    print("Not in list")



name = names[0]
print(name[1])

# Same result
for i in names:
    print(i)

for i in range(len(names)): # range(6)
    print(names[i])'''

my_dictionary = {
                "name":"Terry",
                "age":23,
                "is_funny":False
                } # key : value , key : value

popped = my_dictionary.pop("is_funny")
#print(popped)

#for i, j in my_dictionary.items(): # i = keys, j = values
    #print(f"{i} : {j}")

my_dictionary['is_funny'] = popped
#print(my_dictionary)

reference = my_dictionary["age"]
#print(reference)

value = my_dictionary.get("name")
#print(value)


my_dictionary["is_cool"] = True
#print(my_dictionary)

names = ["John Python", "Sol Badguy", "Kazuya Mishima", "Terry Bogard"]
# Change into dictionary : Key = name : value = surname
name_dictionary = {}

for i in names:
    names = i.split(" ")
    #print(names)

    name = names[0]
    surname = names[1]
    print(surname)
    name_dictionary[name] = surname
    
print(name_dictionary)
