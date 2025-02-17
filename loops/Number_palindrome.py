def is_palindrome_number(num):
    original=num
    reversed_num=0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10
    if original == reversed_num:
        return f"The given number {original} is Palindrome Number"
    else:
        return f"The given number {original} is Not Palindrome Number"

num=int(input("Enter your number : "))
num_f=0
print(is_palindrome_number(num))