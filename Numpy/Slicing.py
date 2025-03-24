import numpy as np
from streamlit import columns

# 1 D
arr = np.array([1, 2, 3, 4, 5])
print(arr[1:5:1]) # [start:end:step]. OR [start:end]
# Negative Slicing
print(arr[-4:])

#2D
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0, 1:5]) # row Slicing
print(arr[0:2, 2]) # columns Slicing
print(arr[:, 3])