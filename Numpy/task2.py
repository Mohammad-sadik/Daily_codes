""" Exercise 1: Create an Array
Create a NumPy array with these numbers: [5, 10, 15, 20, 25]
👉 Task: Print the array.

💡 Hint: Use np.array()."""
import numpy as np
arr = np.array([5, 10, 15, 20, 25])
print(arr)
"""Exercise 2: Create a 3x3 Array of Zeros
Make a 3x3 array filled with zeros.
👉 Task: Print the array.

💡 Hint: Use np.zeros()
"""
zeros = np.zeros([3,3],dtype=int)
print(f"3x3 array filled with zeros: \n {zeros}")

"""🔹 Exercise 3: Pick a Number from an Array
Given this array:

arr = np.array([10, 20, 30, 40, 50])
👉 Task: Print the third number in the array.

💡 Hint: Remember, indexing starts from 0!
"""
