'''def even(n):
    return 1 & n == 0
num= int(input("Enter a number: "))
print(f'the given is even: {even(num)}')'''

even_list = input("Enter numbers : ").split()
is_even = list(filter(lambda x: (int(x) & 1) == 0, even_list))
print(f'The even in the list are : {is_even}')
