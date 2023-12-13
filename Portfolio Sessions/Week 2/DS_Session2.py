'''
# For those interested in using dictionaries
# Define the dictionary to store locations and their radiation levels
locations = {
    'Urban': [18, 20, 22],
    'Forest': [12, 14, 15]}
'''

''' 
# For those interested in using functions for this task
def calculate_average(levels):
    return sum(levels) / len(levels)
'''

# Define the lists to store locations and their radiation levels
locations = ["Urban", "Forest"]
levels = [[18, 20, 22], [12, 14, 15]]

# Process each location's data and calculate the average radiation level
# enumerate function is used to get a counter when iterating through a list
for i, location in enumerate(locations):
    # Debugging: Print the location and levels being processed
    print(f"Debug: Processing location {location} with levels {levels[i]}")
    average = sum(levels[i]) / len(levels[i])
    print(f"{location} Average Radiation Level: {average}")

# Now we'll write the part that allows continuous data input using a while loop
measurements = []
# Debugging: Inform the user that the data entry process is starting
print("Begin entering new radiation levels. Type 'done' to finish.")

# This loop will run indefinitely until 'done' is entered
while True:
    level = input("Enter radiation level or 'done' to finish: ")
    if level.lower() == 'done':
        # Debugging: Confirm that the loop exit condition has been met
        print("Debug: Exiting input loop.")
        break
    try:
        # Convert the input to an integer and add to the measurements list
        new_level = int(level)
        measurements.append(new_level)
        # Debugging: Confirm that a new level has been added
        print(f"Debug: Added level {new_level}")
    except ValueError:
        # Debugging: Inform the user of an invalid input
        print("Invalid input. Please enter a valid number or 'done'.")

# After exiting the loop, we'll calculate and display the average of the new measurements
if measurements:
    average = sum(measurements) / len(measurements)
    print(f"New Measurements Average Radiation Level: {average}")
else:
    # Debugging: Inform the user that no new measurements were entered
    print("Debug: No new measurements were entered.")
