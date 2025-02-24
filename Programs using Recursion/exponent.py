
def exponent_using_recursion(base, exponent):
    if exponent == 0:
        return 1
    return base * exponent_using_recursion(base, exponent-1)

base = int(input("Enter a Base: "))
exponent = int(input("Enter the exponent: "))
print(f"The base is {base} and exponent is {exponent} is equal to {exponent_using_recursion(base, exponent)}")