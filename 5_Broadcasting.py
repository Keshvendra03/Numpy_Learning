#Broadcasting is a set of rules that allows NumPy to perform arithmetic operations on arrays that have different shapes.

import numpy as np

# --- Part 1: The Concept ---

# Create a "Row" Vector (Shape: 1 row, 4 columns)
array1 = np.array([[1, 2, 3, 4]])

# Create a "Column" Vector (Shape: 4 rows, 1 column)
# Note the extra brackets around each number!
array2 = np.array([[1], [2], [3], [4]])

print(array1.shape)
# Output: (1, 4)

print(array2.shape)
# Output: (4, 1)

# --- The Magic of Broadcasting ---
print(array1 * array2)

# --- Part 2: Exercise ---

# Row vector: 1 to 10
array1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])

# Column vector: 1 to 10 vertical
array2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])

print(array1.shape)
# Output: (1, 10)

print(array2.shape)
# Output: (10, 1)

print(array1 * array2)

# 1. Add scalar (5) to a matrix
# When you add a scalar, NumPy adds it to EVERY element in the matrix.
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
scalar_result = matrix + 5
print(f"Matrix + 5:\n{scalar_result}\n")

# 2. Add vector (3,) to matrix (5,3)
# The matrix has 3 columns. The vector has 3 items.
# NumPy 'broadcasts' the vector across every row of the matrix.
matrix_5x3 = np.ones((5, 3))  # Matrix of ones
vector_3 = np.array([10, 20, 30]) # Vector

broadcast_result = matrix_5x3 + vector_3
print(f"Matrix (5,3) + Vector (3,):\n{broadcast_result}\n")
