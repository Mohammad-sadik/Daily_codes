#print weather it is +ve or -ve or zer0
a=int(input("Enter number : "))
if(a>0):
    print("{} is +ve".format(a))
else:
    if(a<0):
        print("{} is -ve".format(a))
    else:
        print("{} is zero".format(a))
        
