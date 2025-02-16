a = int(input("Enter start number: "))
b = int(input("Enter end number: "))
empty = []

for i in range(a, b + 1):
    if i < 2:
        continue
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        empty.append(i)

print(f"Prime numbers between range of {a} & {b}:", empty)
