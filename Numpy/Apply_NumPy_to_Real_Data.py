
import numpy as np
file_path = r"C:\users\sadik\Downloads\Data Science\Excel\bike_sales.txt"
data = np.loadtxt(file_path, delimiter=',', skiprows=1, dtype=str)
print(data[:5])  # First five rows