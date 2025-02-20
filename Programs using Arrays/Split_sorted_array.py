arr =  input("Enter the array: ").split()
arr = [int(i) for i in arr]
split = int(input("Enter the you want split: "))
high = split
final = []
low = 0

while len(arr) >= high:
    l = arr[low : low+split : 1]
    print(l)
    final.append(l)
    low = low+split
    high = low+split
final.append(arr[len(arr)-len(arr)%split::1])
print(final)