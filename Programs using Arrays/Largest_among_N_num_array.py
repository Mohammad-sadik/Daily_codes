

array = input("Enter the areay : ").split()
array = list(map(lambda x: int(x), array))
c=1
max_value = array[0]
while len(array) != c:
    if max_value < array[c]:
        max_value = array[c]
    c+=1
print(f"The Largest among N numbers in an array is {max_value}.")