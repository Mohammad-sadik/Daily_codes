import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
print(df["Name"], "\n") # Get only the "Name" column

print(df[["Name", "Age"]], "\n")

print(df[["Name", "Age", "City"]], "\n")
# Filter Data (e.g., People older than 30)
print(df[df['Age'] > 30])
