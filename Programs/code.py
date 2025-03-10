n=4

for j in range(1,2*n):
    i=1
    d=n-j+1
    for k in range(1,2*n):
        if (j==i or k==i or j==2*n-i or k==2*n-i) and (k<j):
            print((d), end="")
        i=i+1

    print()