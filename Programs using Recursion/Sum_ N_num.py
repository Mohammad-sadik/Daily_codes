def sum(num):
    if num==0:
        return 0
    return  num + sum(num-1)

num = int(input("Enter the number: "))
print(f"The given N number is {num} & sum of N number is {sum(num)}")