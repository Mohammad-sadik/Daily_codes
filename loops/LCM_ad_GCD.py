def gcd_lcm(list_a):
    # Find GCD
    max_num = []
    for j in range(2, min(list_a) + 1):
        for i in list_a:
            if i % j != 0:
                break
        else:
            max_num.append(j)

    gcd_value = max(max_num, default=1)
    # Find LCM
    final_lcm = 1
    for i in list_a:
        final_lcm *= i

    lcm_value = final_lcm // gcd_value

    return f"The GCD is {gcd_value} & LCM is {lcm_value}"

if __name__ == "__main__":
    list_a = [int(input(f"Enter number: ")) for i in range(2)]
    print(gcd_lcm(list_a))
