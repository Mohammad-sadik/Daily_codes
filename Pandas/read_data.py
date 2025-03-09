#Read Data from a CSV File
import pandas as pd
path = r"C:\Users\Bike_Sales_CSV_Lab.csv"
df = pd.read_csv(path) # loading the data from CSv
print(df.head())