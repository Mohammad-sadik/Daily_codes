import numpy as np
#1D
print("* "*5 + "1D Array" + " *"*5)
arr = np.array([1,2,4])
for i in arr:
    print(i)
#2D
print("* "*5 + "2D Array" + " *"*5)
arr = np.array([[1,2,3],[4,5,6]])
for i in arr:
    print(i)
#If we iterate on a n-D array it will go through n-1th dimension one by one.
arr = np.array([[1,2,3],[4,5,6]])
for i in arr:
    for j in i:
        print(j)

print("\nIterating Arrays Using nditer()")
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
    print(x)
