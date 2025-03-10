n= int(input("Enter Number: "))
for i in range(0, n):
    for j in range(n):
        if (i >= j):
            print(i, end= "  ")       
    print("")
    
for k in range(n, n+n):
    for x in range(n, n+n):
        if (k <= x):
            print(k , end= " ")
    print("")
