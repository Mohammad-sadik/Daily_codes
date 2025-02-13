n=int(input("Enter number of natural numbrer : "))
sum=0
for _ in range(n):
    num = int(input())
    if num>0:
        sum += num
print("_"*20)
print(sum)