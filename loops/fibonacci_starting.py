#Fibonacci starting from any two numbers

def result(n, first, second):
    list_a = [first, second]
    for i in range(n-2):
        list_a.append(int(list_a[-1]+int(list_a[-2])))
    return list_a

n= int(input("Enter the number of terms: "))
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
print(result(n,first, second))