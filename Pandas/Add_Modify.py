import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
df["Salary"] =[50000, 60000, 70000]
print(df) # Add a Salary column

df.loc[1, "Age"] = 31
print(df)