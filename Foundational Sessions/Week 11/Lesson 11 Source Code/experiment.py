import random
import time
import matplotlib.pyplot as plt
from RecursiveHeap import RecursiveHeap
from IterativeHeap import IterativeHeap

sizes = [10, 100, 1000, 10000, 50000, 100000, 500000, 1000000]
recursive_times = []
iterative_times = []

for size in sizes:
    elements = [random.randint(1, 1000) for _ in range(size)]

    # Test RecursiveHeap
    rh = RecursiveHeap()
    start_time = time.time()
    for el in elements:
        rh.insert(el)
    while rh.retrieve() is not None:
        pass
    recursive_times.append(time.time() - start_time)

    # Test IterativeHeap
    ih = IterativeHeap()
    start_time = time.time()
    for el in elements:
        ih.insert(el)
    while ih.retrieve() is not None:
        pass
    iterative_times.append(time.time() - start_time)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(sizes, recursive_times, label='Recursive Heap', marker='o')
plt.plot(sizes, iterative_times, label='Iterative Heap', marker='x')
plt.xlabel('Number of Elements')
plt.ylabel('Time (seconds)')
plt.title('Recursive vs Iterative Heap Performance')
plt.legend()
# plt.xscale('log')
# plt.yscale('log')
plt.grid(True)
plt.show()
