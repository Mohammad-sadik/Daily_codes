import numpy as np
arr = np.array([[10, 20, 30], [40, 50, 60]])
# Reshaping an array
print(arr.reshape(3,2))
# Stacking arrays
arr1 = np.array([1, 3, 4, 5])
arr2 = np.array([2,4,5,6])

print(np.hstack([arr1, arr2])) # Horizontal stacking
print(np.vstack([arr1, arr2])) # Vertical stacking