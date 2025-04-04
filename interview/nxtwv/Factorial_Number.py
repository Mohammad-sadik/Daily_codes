num = int(input("Enter Number: "))
f_num =1
for i in range(2,num+1):
    f_num *= i
print(f"The factorial of {num} is {f_num}")