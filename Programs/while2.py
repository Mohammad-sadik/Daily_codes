#print n to 1 num
n=int(input("enter n value: "))
if(n<=0):
    print("===================================")
    print("\t {} is invalid number".format(n))
    print("====================================")
else:
    i=1 #initilization
    while(n>=i):
        print("\t %d" %n, end=" ")
        n=n-1 #updating part
    else:
        print("\n ==========================")
        print(" This is else block")
        print("=============================")
