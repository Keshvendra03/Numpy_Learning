import numpy as np

# --- PART 1: DOT PRODUCT ---
print("--- DOT PRODUCT ---")

# 1. Multiply (2,3) by (3,2)
# inner dimensions must match: (2, 3) @ (3, 2) -> Result is (2, 2)
mat_a = np.array([[1, 2, 3],
                  [4, 5, 6]]) # Shape (2, 3)

mat_b = np.array([[7, 8],
                  [9, 1],
                  [2, 3]])    # Shape (3, 2)

# Method A: Using np.dot()
dot_result = np.dot(mat_a, mat_b)
print(f"Result using np.dot():\n{dot_result}\n")

# Method B: Using @ operator (standard for matrix multiplication in Python 3.5+)
at_result = mat_a @ mat_b
print(f"Result using @ operator:\n{at_result}")