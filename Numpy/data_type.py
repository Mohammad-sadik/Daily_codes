import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr.dtype)

arr = np.array([1,2,3,4,5], dtype='S')
print(arr)
print(arr.dtype)

#Converting Data Type on Existing Arrays
arr = np.array([1, 2, 3, 4])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)