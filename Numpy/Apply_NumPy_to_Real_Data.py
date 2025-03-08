
import numpy as np
file_path = r"C:\Users\bike_sales.txt"
data = np.loadtxt(file_path, delimiter=',', skiprows=1)
print(data[:5])  # First five rows
print(np.mean(data, axis=0))  # Column-wise mean
