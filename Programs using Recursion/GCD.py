# def gcd(a, b, max_v):
#     if (a % max_v == 0) and (b % max_v == 0):
#         return max_v
#     return gcd(a, b, max_v-1)
# fst_value = int(input("Enter first value : "))
# sec_value = int(input("Enter second value : "))
# max_v = (max(fst_value, sec_value)) // 2
# print(gcd(fst_value,sec_value, max_v))
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

fst_value = int(input("Enter first value: "))
sec_value = int(input("Enter second value: "))

print("GCD:", gcd(fst_value, sec_value))
