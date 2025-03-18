import numpy as np

arr = np.array([10, 20, 50, 60])
# Statistical functions
print(f"This is mean: {np.mean(arr)}")
print(f"This is median: {np.median(arr)}")
print(f"This is standard deviation: {np.std(arr)}")
print(f"Sum along columns: {np.sum(arr,axis=0)}") # Sum along columns