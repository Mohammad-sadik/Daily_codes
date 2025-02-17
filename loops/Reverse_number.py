def is_palindrome_number(num):
    original=num
    reversed_num=0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10
    return f"The given number {original} The reverse of the given num is {reversed_num}"

num=int(input("Enter your number : "))
num_f=0
print(is_palindrome_number(num))