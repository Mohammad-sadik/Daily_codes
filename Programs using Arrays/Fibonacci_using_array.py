def result(n):
    if n <= 0:
        return  []
    elif n == 1:
        return [0]
    list_a = [0, 1]
    for i in range(n-2):
        list_a.append(int(list_a[-1]+int(list_a[-2])))
    return list_a

n= int(input("Enter the number of terms: "))
print(result(n))