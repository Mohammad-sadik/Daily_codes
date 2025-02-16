def prime_factor(num):
    i = 2
    List_a = []
    list_b = []
    while num != 1:
        if num % i == 0:
            List_a.append(i)
        for j in List_a[::]:
            if num % j == 0:
                list_b.append(j)
                num = num / j
        i += 1
    return list_b
num=int(input("Enter a number : "))
print(prime_factor(num))