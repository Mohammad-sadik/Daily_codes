num= int(input("Enter a number : "))
num_final=1
for i in range(num , 0, -1):
    num_final *= i
print(f"The factorial of {num} is {num_final}")