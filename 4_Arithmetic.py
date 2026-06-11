import numpy as np

array = np.array([1,2,3])

#scaler Arithmatic
print(array+1)
print(array-2)
print(array*3)
print(array/4)
print(array**5)

#vectorized math func
array = np.array([1.5,2.22,3.68])
print(np.sqrt(array))
print(np.round(array))

#Exercise
Radii = np.array([2,4,3])
print(np.pi*Radii**2)

#Element-wise arithmatic
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
print(array1 + array2)
print(array1 * array2)

#comparison operator
scores = np.array([99,87,65,56,79])
print(scores == 100)
print(scores >= 60)

scores[scores < 60] = 0
print(scores)