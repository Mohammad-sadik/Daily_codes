def power_using_recursion(num, power):
    if power == 0:
        return 1
    return num * power_using_recursion(num, power - 1)
num = int(input("Enter number: "))
power = int(input("Enter power: "))
print(f"The given number& power are {num} & {power}, and the of the number {power_using_recursion(num, power)}.")