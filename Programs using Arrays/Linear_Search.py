arr = input("Enter the array: ").split()
arr = [int(i) for i in arr]
num = int(input("Enter the target number : "))
for i in range(len(arr)):
    if num == arr[i]:
        print(f"The target number: {num}. The index of Target number is {i}")
        break
else:
    print(f"The target number: {num} is not in {arr}")