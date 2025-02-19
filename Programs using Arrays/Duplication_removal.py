arr = input("Enter array : ").split()
#print(list(set(arr)))
final = []
for i in arr:
    if i not in final:
        final.append(i)
print(f"After Removing Duplicates: {final}")
