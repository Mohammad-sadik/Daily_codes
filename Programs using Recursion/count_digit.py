def count_digit(n, digit):
    last_digit = n%10

    if n == 0: # base case
        return 0

    elif last_digit == digit:   # recursive case
        return 1 + count_digit(n//10, digit)
    else:
        return count_digit(n//10, digit)

print(count_digit(1124223455, 4))