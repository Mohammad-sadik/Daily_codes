#program for even num
a=int(input("Enter the n num : "))
if(a<0):
    print("================================================")
    print("   The given number is %d is invalid number" %a)
    print("================================================")
else:
    print("===================================================")
    print("\t HERE WE PRINT THE EVNE NUMBERS UP TO {}".format(a))
    print("===================================================")
    i=2
    while(i<=a):
       
        print("\t", i)
        i=i+2
    else:
        print("==================================================")
        print("\t T H I S   A   E L S E    B L O C K")
        print("==================================================")
