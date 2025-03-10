#print 1 to n num
n=int(input("enter n value: "))
if(n<=0):
    print("===================================")
    print("\t {} is invalid number".format(n))
    print("====================================")
else:
    i=1 #initilization
    while(i<=n):
        print("\t %d" %i, end=" ")
        i=i+1 #updating part
    else:
        print("\n ==========================")
        print(" This is else block")
        print("=============================")
