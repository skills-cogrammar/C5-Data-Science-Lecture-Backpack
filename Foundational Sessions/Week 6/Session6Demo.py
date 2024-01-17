# Purpose: Demonstrate the time complexity of different algorithms

import matplotlib.pyplot as plt
import time
import numpy as np

# Linear complexity algorithm: sum of first N natural numbers
def linear_algorithm(n):
    return sum(range(n))

# Quadratic complexity algorithm: generate multiplication table up to N
def quadratic_algorithm(n):
    return np.array([[i * j for j in range(n)] for i in range(n)])

# Logarithmic complexity algorithm: binary search
def logarithmic_algorithm(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1

# Measure execution time of an algorithm
def measure_time(func, *args):
    start = time.time()
    func(*args)
    return time.time() - start

# Test each algorithm with increasing input sizes and record the execution times
input_sizes = range(10, 1000, 10)
linear_times = [measure_time(linear_algorithm, size) for size in input_sizes]
quadratic_times = [measure_time(quadratic_algorithm, size) for size in input_sizes]
logarithmic_times = [measure_time(logarithmic_algorithm, list(range(size)), size - 1) for size in input_sizes]

# Plotting the execution times
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, linear_times, label='Linear O(n)')
plt.plot(input_sizes, quadratic_times, label='Quadratic O(n^2)')
plt.plot(input_sizes, logarithmic_times, label='Logarithmic O(log n)')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Algorithm Complexity Demonstration')
plt.legend()
plt.grid(True)
plt.show()
