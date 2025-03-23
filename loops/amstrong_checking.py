def Amstrong_checking(num):
    orginal = num
    l = len(str(num))
    total = 0
    for i in range(l):
        digit = num % 10
        total = total + digit ** l
        num = num // 10
        print(f"{i}: digit :{digit}, total:{total}")
    if orginal == total:
        return f"{orginal} is an Armstrong number."
    else:
        return f"{orginal} is an Not Armstrong number."

if __name__ == '__main__':
    num = int(input("Enter number : "))
    print(Amstrong_checking(num))