import numpy as np
arr_0 = np.array(2)
arr_1 = np.array([1,2,3]) #1D array (Vector)
arr_2 = np.array([[1,2,3],[4,5,6]]) #a 2D Array (Matrix)
arr_3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]) #a 3D Array (Tensor)

print(f"This is 0'D array: {arr_0} & dimensions is {arr_0.ndim}")
print(f"This is 1'D array: {arr_1} & dimensions is {arr_1.ndim}")
print(f"This is 2'D array:  {arr_2} & dimensions is {arr_2.ndim}")
print(f"This is 3'D array:  {arr_3} & dimensions is {arr_3.ndim}") #3d is useful in image processing, deep learning, and 3D modeling.

""" In this array the innermost dimension (5th dim) has 4 elements, the 4th dim has 1 element that is the vector, the 3rd dim has 1 element that is the matrix with the vector, the 2nd dim has 1 element that is 3D array and 1st dim has 1 element that is a 4D array."""
arr_5 = np.array([1,2,3,4,5], ndmin=5)
print(f"This is 3'D array: {arr_5}")
print('number of dimensions+ :', arr_5.ndim)