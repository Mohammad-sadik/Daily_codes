n=int(input("Enter num : "))
if(n<=0):
    print("Invalid")
else:
    i,s=1,0
    while(i<=n):
        print("\t \t", i)
        s=s+i
        i=i+1
        
    else:
        print("==============================")
        print("\tSUM\t", s)
        print("==============================")
