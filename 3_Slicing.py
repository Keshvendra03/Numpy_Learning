import numpy as np

# A 4x4 matrix containing numbers 1 to 16
array = np.array([
    [1,  2,  3,  4],   # Row 0
    [5,  6,  7,  8],   # Row 1
    [9,  10, 11, 12],  # Row 2
    [13, 14, 15, 16]])  # Row 3

# Select a single row by index
print(array[1])
# Output: [5 6 7 8]

# Negative Indexing (Count from the bottom)
print(array[-2])
# Output: [9 10 11 12]

# Slicing a range of rows
print(array[0:3])
# Output:
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

# Slicing with a "Step" (Jump)
print(array[0:4:2])
# Output:
# [[ 1  2  3  4]
#  [ 9 10 11 12]]

# Reversing the order of rows
print(array[::-1])
# Output:
# [[13 14 15 16] ... (and so on backwards) ... [1 2 3 4]]

# Select a single column
print(array[:, 0])
# Output: [1 5 9 13]
# Explanation: The ':' means "All Rows". The '0' means "Column 0".
# Note: This returns a flat list (1D array).

# Select multiple columns
print(array[:, 0:3])
# Output:
# [[ 1  2  3]
#  [ 5  6  7]
#  [ 9 10 11]
#  [13 14 15]]
# Explanation: "All Rows", but only Columns 0 up to (not including) 3.

# Extract the Top-Left corner (2x2)
print(array[0:2, 0:2])
# Output:
# [[1 2]
#  [5 6]]

# Extract the Bottom-Right corner (2x2)
print(array[2:, 2:])
# Output:
# [[11 12]
#  [15 16]]