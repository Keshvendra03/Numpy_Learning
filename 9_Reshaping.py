import numpy as np

# 1. Create a base array with 12 items (0 to 11)
arr = np.arange(12)
print(f"Original array (12 items): {arr}")

# 2. Reshape into (3, 4) -> 3 rows, 4 columns
shape_3x4 = arr.reshape(3, 4)
print(f"Reshaped to (3, 4):\n{shape_3x4}\n")

# 3. Reshape into (4, 3) -> 4 rows, 3 columns
shape_4x3 = arr.reshape(4, 3)
print(f"Reshaped to (4, 3):\n{shape_4x3}\n")

# 4. Reshape into (2, 2, 3) -> 3D array: 2 blocks, 2 rows each, 3 columns each
shape_3d = arr.reshape(2, 2, 3)
print(f"Reshaped to (2, 2, 3):\n{shape_3d}")