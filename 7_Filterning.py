# Filtering refers to the process of selecting elements from an array that match a given condition

import numpy as np

ages = np.array([[21,65,24,46,94,74,25,34,17],
                 [9,84,16,92,31,12,31,24,4]])

# Adults are typically 18 and older (including seniors)
teenagers = ages[ages <= 18]
adults = ages[(ages > 18) & (ages <= 65)]

print("Teenagers:", teenagers)
print("Adults:", adults)

adults = np.where(ages>=18, ages, 0)
#where preserve the original shape of our data
print(adults)