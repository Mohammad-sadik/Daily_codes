arr = input("Enter a Array: ").split()
#arr = list(map(lambda x:int(x), arr))
arr = [int(n) for n in arr]
avg = sum(arr)/ len(arr)

print(f"The Average Value of Numbers in an Array: {avg}")