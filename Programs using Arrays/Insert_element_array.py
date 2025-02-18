def check_valid(n):
    index = int(input("Enter the index value : "))
    if index < n:
        return index
    print("Enter the correct index Value.")
    check_valid(n)

list_i = input("Enter Array : ").split()
index = check_valid(len(list_i))
value = input("Enter the value : ")
list_i[index] = value
print(list_i)