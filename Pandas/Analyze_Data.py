import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
print(f"# Shows mean, min, max... : \n{df.describe()}\n") # Shows mean, min, max, etc.
print(f"Average age : {df["Age"].mean()}\n")
print(f"Count unique cities: {df['City'].value_counts()}\n")
