"""
Practice Tasks for Day 1
✅ Task 1: Create a 3x3 identity matrix
✅ Task 2: Generate an array of 10 random numbers between 1-100
"""
import numpy as np

identity_matrix = np.eye(5,5)
print(f"identity matrix:\n {identity_matrix} \n")
#1d
random_value = np.random.randint(1,100,size=10)
print(f"random 1d value:\n {random_value}\n")
#2d
random_value2 = np.random.randint(1,100,size=(2,3))
print(f"Random 2d value:\n {random_value2}\n")
# Find the max & min values in your random array
print(f"Random array max value: {random_value.max()}")
print(f"Random array min value: {random_value.min()}")