# Linear Algebra

import numpy as np

# 1
# B1 = np.array([0, -50])
# B2 = np.array([70, 0])

# B = B1 + B2
# print(B)

# --------------------------------------------

# 2
# A = np.array([0,5])
# rotation_transformation = np.array([[0, -1], [1, 0]])

# rotated_A = np.matmul(rotation_transformation, A)
# print(rotated_A)



# 3
# V = np.array([3, 4])
# print(V * 2)

# --------------------------------------------

# 4
# U = np.array([80, 80])
# V = np.array([0, 80])

# dot_product = np.dot(U, V)
# print(f"dot product: {dot_product}")
# # print(1 * 3 + 2 * 4)

# u_norm = np.sqrt(np.dot(U, U))
# v_norm = np.sqrt(np.dot(V, V))
# print(f"u_norm: {u_norm}")
# print(f"v_norm: {v_norm}")

# cos_theta = dot_product / (u_norm * v_norm)
# print(f"cos_theta: {cos_theta}")

# # theta in degrees
# theta = np.arccos(cos_theta) * 180 / np.pi
# print(f"theta: {theta}")

# # if not multiplying by 180 / np.pi, theta is in radians
# theta = np.arccos(cos_theta)
# print(f"theta: {theta}")

# --------------------------------------------

# 5

# mat_A = np.array([[1, 2], [3, 4]])

# print(f"multiply by scalar: \n{mat_A * 2}")
# print(f"addition: \n{mat_A + mat_A}")
# print(f"multiplication: \n{np.matmul(mat_A, mat_A)}")

# The process of matrix multiplication is as follows:
# 1. Multiply the first row of the first matrix with the first column of the second matrix.
# 2. Multiply the second row of the first matrix with the first column of the second matrix.
# 3. Multiply the first row of the first matrix with the second column of the second matrix.
# 4. Multiply the second row of the first matrix with the second column of the second matrix.
# 5. Add the products.

# --------------------------------------------

# 6



