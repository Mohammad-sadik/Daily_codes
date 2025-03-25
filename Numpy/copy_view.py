import numpy as np

arr = np.array([1,2,3,4,5])
x = arr.copy() # create a new base
y = arr.view() # base is arr
print(f"copy : {x}")
print(f"View : {y}")

print("-"*40)
x[0] = 10
print("* "*7 + "copy" + " *"*7)
print(f"Orginal : {arr}")
print(f"copy : {x}")

print("-"*40)
print("* "*7 + "View" + " *"*7)
y[0] = 10
print(f"Orginal : {arr}")
print(f"copy : {y}")

print("Checking base")
print(f"base for copy: {x.base}")
print(f"base for view: {y.base}")