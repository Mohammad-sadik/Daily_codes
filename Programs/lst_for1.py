n=int(input("enter num : "))
if (n<=0):
    print("The {} is given invalid".format(n))
else:
    l=list()
    for x in range(1, n+1):
        val=input("Enter {} value : ".format(x))
        l.append(val)
    else:
        print(l)
