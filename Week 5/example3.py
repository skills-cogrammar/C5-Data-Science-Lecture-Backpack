#See this resource for more information about NumPy arrays: https://www.oreilly.com/library/view/python-for-data/9781491957653/ch04.html
import numpy as np
np.random.seed(0)  # seed for reproducibility

x1 = np.random.randint(10, size=6)  # Random One-dimensional array
x2 = np.random.randint(10, size=(3, 4))  # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5))  # Three-dimensional array

print('x1: ')
print(x1)
print('x1[0]: ')
print(x1[0])
print('x1[-1]: ')
print(x1[-1])

print('x2: ')
print(x2)
print('x2[2, -1]: ')
print(x2[2, -1])

print('x3: ')
print(x3)

print("x3 ndim: ", x3.ndim)
print("x3 shape:", x3.shape)
print("x3 size: ", x3.size)
print("dtype:", x3.dtype)

print("itemsize:", x3.itemsize, "bytes")
print("nbytes:", x3.nbytes, "bytes")
