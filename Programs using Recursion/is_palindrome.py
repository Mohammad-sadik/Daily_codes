def is_palindrome(s):
    if len(s) <= 0: # base case
        return True
    elif s[0] != s[-1]:
        return False

    return is_palindrome(s[1:-1]) # recursive case
print(f'Is hello is palindrome {is_palindrome("Hello")}')
print(f'Is madam is palindrome {is_palindrome("madam")}')