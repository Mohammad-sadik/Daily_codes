def fibonacci(n):
    if n <= 1:
        return n # base case
    else:
        return fibonacci(n-1)+fibonacci(n-2) # recursive case

num = int(input("Enter the num: "))
for i in range(num):
    print(fibonacci(i), end=" ")