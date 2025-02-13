# Calculate x to the power y
x = int(input("Enter x value : "))
y= int(input("Enter y value : "))
print(f"The {x} to the power of {y} is equal to {x**y}")
#-----------------------------------------------------------
sqr=1
for i in range(y):
    sqr=x* sqr
print(f"The {x} to the power of {y} is equal to {sqr}")