# print n num of odd & positive intigers
n= int(input("Enter the val : "))
if (n<=0):
    print("=============================================")
    print(" The given num is {} is not valid number".format(n))
    print("=============================================")
else:
    print("The given num is %0.1f" %(n))
    print("Here is the odd numbers up to {}".format(n))
    print("=============================================")
    print("=============================================")
    i=1  #initixations
    while(i<=n): # condition
        print("\t", i)
        i=i+2  #updating part
    else:
        print("=============================================")
        print("=============================================")
        print("\t here is the else bock")
        print("=============================================")
   
