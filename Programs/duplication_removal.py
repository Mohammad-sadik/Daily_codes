def duplicates(arr):
    if not arr:
        return 0

    seen = set()
    i = 0
    for j in range(1 , len(arr)):
        if arr[j] not in seen:
            seen.add(arr[j])
            arr[i] = arr[j]
            i += 1
    return arr[:i]

arr = [1,1,2,3,4,2,4,5,6]
print(f"Original Array: {arr}")
new_arr = duplicates(arr)
print(f"Array after Removing Duplicates: {new_arr}")