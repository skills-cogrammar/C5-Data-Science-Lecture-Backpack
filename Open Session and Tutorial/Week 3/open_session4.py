#"Implement the check_unique_values() function so that it returns 
# True if the all values in column col_name are unique 
# and False otherwise. If the column does not exists, return None.

"""
def check_unique_values(csv_filename, col_name):
    # 1. find the column index
    col_index = find_col_index(csv_filename, col_name)
    if col_index == -1:
        return None
    # 2. read the CSV file and remove the header
    opened_file = open(csv_filename)
    read_file = reader(opened_file)
    rows = list(read_file)
    rows = rows[1:]
    # 3. create a frequency table with the column values
    freq = {}
    for row in rows:
 // I really don,t understand how this are working and the logic
        if row[col_index] in freq: 
            freq[row[col_index]] += 1
        else:
            freq[row[col_index]] = 1
    # 4. use the frequency table to check unicity
    for key in freq:
        if freq[key] > 1:
            return False
    return True  "
"rows = [
    [""Apple"", ""Red""],
    [""Banana"", ""Yellow""],
    [""Apple"", ""Green""],
    [""Cherry"", ""Red""],
    [""Apple"", ""Red""],
    [""Banana"", ""Yellow""]
]


freq = {}
for row in rows: 
    if row[col_index] in freq: #bnot sure how the values are accesed 
        freq[row[col_index]] += 1
        print(row)
    else:
        freq[row[col_index]] = 1

"""
"""
# Is it possible to create a star diamond pattern with one for loop only?
pattern = "*"
# Expected:
# @
# @@
# @@@
# @@@@
# @@@@@
# @@@@@@
# @@@@@@@
# @@@@@@
# @@@@@
# @@@@
# @@@
# @@
# @


for num in range(1, 8):
    # pattern
    to_print = pattern*num
    if num > 4:
        count_down = 8 - num
        to_print = pattern*count_down
        # reverse the pattern
    
    print(to_print)
"""

"""
#"I got feedback for this code: 
# Get the times for swimming, cycling, and running
swimming_time = int(input("Enter the swimming time (minutes): "))
cycling_time = int(input("Enter the cycling time (minutes): "))
running_time = int(input("Enter the running time (minutes): "))

# Calculate the total time
total_time = swimming_time + cycling_time + running_time

# Define the qualifying time and calculate the time difference
qualifying_time = 100

# Determine the award based on the time difference
if total_time < 106:
    award = "Provincial Colours"
elif total_time > 105 and 110 >= total_time:
    award = "Provincial Half Colours"
elif total_time >= 111 and 115 >= total_time:
    award = "Provincial Scroll"
else:
    award = "No award"

# Display the award
print(f"The participant will receive the award: {award}")

# Feedback: Unfortunately, your solution does not meet all the requirements for this 
# task as you are supposed 
# to incorporate some logic operators as well in your code. 
# The objective of this code was to work 
# with conditional statements and logic operators 
# for example if total_time > 101 and total_time < 105 using the "" and "" operator 
# will be an acceptable solution for this task. 
# Please read the instructions carefully to avoid such mistakes and 
# being asked to resubmit.

# I was not sure what to incorporate into this code to make it better. 
# I would really appreciate if you could help me out with this. Thanks."
"""

# How can I calculate the total inputs that an user enters in a while loop? 
# For example, if the user enters these numbers: 2, 4, 6 and 7, how can I calculate 
# that he has entered a total of 4 numbers?
"""
count = 0

while True:
    user_input = input("Please enter a number: ")

    if user_input == "-1":
        break

    count += 1

print(f"You entered {count} numbers")
"""

# Bit confused about [-5:]  [:5] [::5] [5::] specially when working with lists

rows = [
    "Apple", "Red",
    "Banana", "Yellow",
    "Apple", "Green",
    "Cherry", "Red",
    "Apple", "Red",
    "Banana", "Yellow"
    ]

print(rows[-1:5:-1])

