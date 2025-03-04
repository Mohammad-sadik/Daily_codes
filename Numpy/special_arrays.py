import numpy as np

zero_array = np.zeros((2,3)) # 2 rows, 3 columns
# Array of Zeros : This is useful when initializing empty arrays.

ones_array = np.ones((3,3)) # 3x3 matrix of ones
#Array of Ones: This is useful for multiplication-based operations.

identity_matrix = np.eye(3)  # 3x3 Identity matrix
#Identity Matrix: Used in linear algebra, machine learning, and matrix operations.
#An identity matrix has 1's on the diagonal and 0's elsewhere.

random_value = np.random.rand(3,3)# 3x3 matrix of random numbers
#Output: (Values will change each time)
# Used in probability, simulations, and AI models.

random_int_value = np.random.randint(5,10,size =(3,3))
#Useful in games, data shuffling, and sampling.

print(f"Zero array: \n {zero_array} \n")
print(f"Ones array: \n {ones_array} \n")
print(f"Identity matrix: \n {identity_matrix}\n")
print(f"Random matrix: \n {random_value}\n")
print(f"Random int value: \n {random_int_value}")