arr = input("Enter list of array :").split()
print(f"Finding the maximum number using max() function: {max(arr)}")
max_num = arr[0]
for i in arr[1::]:
    if max_num < i:
        max_num = i
print(f"Finding the maximum number using loop: {max_num}")