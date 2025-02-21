def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    print(f"left :{left}")
    middle = [x for x in arr if x == pivot]
    print(f"middle :{middle}")
    right = [x for x in arr if x > pivot]
    print(f"right:{right}")
    return quick_sort(left) + middle + quick_sort(right)

arr = input("Enter array: ").split()
arr = [int(i) for i in arr]
# arr.sort()
# print(arr)
"""_________"""
# arr=sorted(arr)
# print(arr)
"""_________"""
print(quick_sort(arr))