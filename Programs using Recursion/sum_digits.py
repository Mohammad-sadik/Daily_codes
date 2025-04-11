n = 12345
# k = 0
# while True:
#     if n == 0:
#         break
#     k += n%10
#     print(k)
#     n = n//10
#
# print("***********")
# print(k)


def sum_of_digits(n):
    if n == 0:
        return 0
    return n%10 + sum_of_digits(n//10)

print(sum_of_digits(n))
