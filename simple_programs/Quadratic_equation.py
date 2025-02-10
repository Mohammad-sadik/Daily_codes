def quadratic_eqaution(a,b,c):
    equ_1=(-b + (b**2 - 4*a*c)**0.5)/2*a
    equ_2= (-b - (b**2 - 4*a*c)**0.5)/2*a
    return f"The roots for the given Quadratic equation is {equ_1} and {equ_2}"

a= float(input("Enter coefficient a: " ))
b= float(input("Enter coefficient a: " ))
c= float(input("Enter coefficient a: " ))
if a==0:
    print("The given equation is Not Quadratic equation")
else:
    print(quadratic_eqaution(a, b,c))
