import numpy as np

# 0-D Array
array = np.array('A')
print(array.ndim)
# Output: 0

# 1-D Array
array = np.array(['A', 'B', 'C'])
print(array.ndim)
# Output: 1

# 2-D Array
array = np.array([['A', 'B', 'C'],
                  ['D', 'E', 'F'],
                  ['G', 'H', 'I']])
print(array.ndim)
# Output: 2

# 3-D Array
array = np.array([
    [['A', 'B', 'C'], ['D','E', 'F'], ['G','H', 'I']],  # Block 0 (Page 1)
    [['j', 'k', 'l'], ['M','n', 'o'], ['p','q', 'R']],  # Block 1 (Page 2)
    [['s', 't', 'u'], ['v','w', 'x'], ['y','z', '']]   # Block 2 (Page 3)
])
print(array.ndim)
# Output: 3

# Method 1: Chain Indexing (Standard Python)
print(array[0][0][0])
# Output: 'A'

# Method 2: Multidimensional Indexing (The NumPy Way)
print(array[0, 1, 2])
# Output: 'F' (Block 0, Row 1, Column 2)

# Let's break down the coordinates:
# array[1,2,2] -> Block 1, Row 2, Col 2 -> 'R'
# array[0,0,0] -> Block 0, Row 0, Col 0 -> 'A'
# array[1,1,0] -> Block 1, Row 1, Col 0 -> 'M'

word = array[1,2,2] + array[0,0,0] + array[1,1,0]
print(word)
# Output: RAM