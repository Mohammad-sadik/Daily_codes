def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if target >= arr[0] and target <= arr[len(arr) - 1]:
            if target == arr[mid]:
                return f"The target index in array is {mid}"
            elif target < arr[mid]:
                high = mid
            elif target > arr[mid]:
                low = mid
        else:
            return f"The given target is {target} not in array."


arr = input("Enter array: ").split()
arr = [int(i) for i in arr]
arr.sort()
target = int(input("Enter Target: "))
print(binary_search(arr, target))