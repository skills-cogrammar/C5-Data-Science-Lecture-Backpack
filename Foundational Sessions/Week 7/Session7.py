import numpy as np

# Define a Node class to represent each element in the list
class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Initialize the next reference to None

# Define a SinglyLinkedList class to represent the entire list
class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list to None

    # Method to add a new element at the end of the list
    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if self.head is None:
            self.head = new_node  # If the list is empty, make the new node the head
            return
        # If the list is not empty, traverse to the end of the list
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node  # Link the last node to the new node

    # Method to add a new element at the beginning of the list
    def prepend(self, data):
        new_node = Node(data)  # Create a new node with the given data
        new_node.next = self.head  # Link the new node to the current head
        self.head = new_node  # Make the new node the new head of the list

    # Method to print all elements in the list
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" -> ")  # Print the data of each node
            cur_node = cur_node.next
        print("None")  # Indicate the end of the list

    def delete(self, key):
        cur_node = self.head

        # Case 1: Deleting the head node
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        # Case 2: Deleting a non-head node
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        # If the key is not found in the list
        if cur_node is None:
            return

        # Unlink the node from the list
        prev.next = cur_node.next
        cur_node = None

# Creating an instance of SinglyLinkedList
sll = SinglyLinkedList()
sll.append(3)  # Appending 3 to the list
sll.append(5)  # Appending 5 to the list
sll.prepend(1) # Prepending 1 to the list
sll.print_list()  # Output: 1 -> 3 -> 5 -> None

sll.delete(5)  # Deleting 5 from the list
sll.print_list()  # Output: 1 -> 3 -> None

# ------------------------------------------------------------

# Example of array operations in Python
from array import array
arr = array('i', [1, 2, 3, 4])
# Access
print(arr[0])  # Output: 1
# Insertion
arr.append(5)
print(arr)  # Output: array('i', [1, 2, 3, 4, 5])
# Deletion
arr.pop()
print(arr)  # Output: array('i', [1, 2, 3, 4])
# Update
arr[0] = 0
arr[1] = 1
arr[2] = 2
print(arr) # Output: array('i', [0, 1, 2, 4])
# Iterate
for i in arr:
    print(i, end=" ")  # Output: 0 1 2 4

# ------------------------------------------------------------

import numpy as np

# Creating a Numpy array
np_arr = np.array([1, 2, 3, 4])

# Mathematical Computations
# Vectorized addition
addition = np_arr + np_arr
print(addition)  # Output: [2, 4, 6, 8]

# Reshaping
reshaped = np_arr.reshape((2, 2))
print(reshaped)  # Output: [[1, 2], [3, 4]]

# Slicing
sliced = np_arr[1:3]
print(sliced)  # Output: [2, 3]

# Advanced: Broadcasting and Matrix operations
multiplied = np_arr * np_arr
print(multiplied)  # Output: [1, 4, 9, 16]

# ------------------------------------------------------------

arr = [1, 2, 3, 4]
# Access
print(arr[0])  # Output: 1
# Insertion
arr.append(5)
print(arr)  # Output: [1, 2, 3, 4, 5]
# Deletion
arr.pop()
print(arr)  # Output: [1, 2, 3, 4]
# Update
arr[0] = 0
arr[1] = 1
arr[2] = 2
print(arr) # Output: [0, 1, 2, 4]
# Iterate
for i in arr:
    print(i, end=" ")  # Output: 0 1 2 4



