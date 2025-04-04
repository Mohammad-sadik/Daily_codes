num = int(input("Enter a number: "))
if num < 2:
    print("The given number is Not Prime number")
else:
    for n in range(2, num//2+1):
        if num % n == 0:
            print("The given number is Not Prime number")
            break
    else:
        print("The given number is Prime number")