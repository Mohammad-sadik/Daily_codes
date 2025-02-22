def factorial(num):
    if num > 1:
        fact = num * factorial(num-1)
        return fact
    elif num == 0 or num == 1:
        return 1

num = int(input("Enter a number: "))
print(f"Factorial of {num}: {factorial(num)}")
