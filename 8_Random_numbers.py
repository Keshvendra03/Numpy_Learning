import numpy as np

rng = np.random.default_rng()

print(rng.integers(1,101, size=5))# 1-D array
print(rng.integers(1,101, size=(2,4))) #2-D array

#rng = np.random.default_rng(seed=1)
#seed is used to reproduce the same result
print(rng.integers(1,100,size=(2,3)))

print(np.random.uniform(-1,1))  #Random number from -1 to 1

array = np.array([1,2,3,4,5])
rng.shuffle(array)
print(array)

fruits = np.array(["Apple","Orange","cherry"])
print(fruits)
fruits = rng.choice(fruits)
print(fruits)
