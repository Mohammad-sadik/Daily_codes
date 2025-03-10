#pay slip
empNo=int(input("Enter emp number: "))
empName=input("Enter emp name : ")
bSal=float(input("Enter Basic Salary : "))
if(bSal<=0):
    print("Sal is invalid")
else:
    if(bSal>=10000):
        da= bSal*(20/100)
        ta=bSal*(15/100)
        hra=bSal*(10/100)
        ma=bSal*(5/100)
        gpf=bSal*(2/100)
        lic=bSal*(3/100)
    else:
        da= bSal*(25/100)
        ta=bSal*(20/100)
        hra=bSal*(15/100)
        ma=bSal*(6/100)
        gpf=bSal*(2/100)
        lic=bSal*(3/100)
    tSal= bSal + da+ta+hra+ma
    netSal= bSal + da+ta+hra+ma-(gpf+lic)
    print("==========================================")
    print("\t E M P Y   I N F O R M A T I O N ")
    print("==========================================")
    print("\t Empy No is %s" %empNo)
    print("\t Empy Name is %s" %empName)
    print("\t Empy Baic slary is %s" %bSal)
    print("\t Empy DA is {}".format(da))
    print("\t Empy TA is {}".format(ta))
    print("\t Empy HRA is {}".format(hra))
    print("\t Empy MA is {}".format(ma))
    print("--------------------------------------------")
    print("Total Slary before dedations = {}".format(tSal))
    print("==========================================")
    print(" D E D A T I O N S ")
    print("==========================================")
    print("\t  Empy is GPF is {}".format(gpf))
    print("\t Empy LIC is {}".format(lic))
    print("--------------------------------------------")
    print("\t Empy Net salary is {}".format(netSal))
    print("==========================================")


    
    
        
