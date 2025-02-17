def digit_summation(n):
    orginal = n
    summation = 0
    while n > 0:
        digit = n % 10
        summation += digit
        n = n//10
    return f"The given number is {orginal} and summation is {summation}."

num = int(input("Enter number : "))
print(digit_summation(num))