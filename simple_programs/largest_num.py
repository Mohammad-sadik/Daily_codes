"""	Find largest among three numbers"""
a=int(input("Enter the 1st Number : "))
b=int(input("Enter the 2nd Number : "))
c=int(input("Enter the 3rd Number : "))
#max_val= max(a,b,c) # 1st process
list_a=[a,b,c]
max_val=a
for i in list_a[1:]:
    if max_val< i:
        max_val=i

print(f"The given values {a}, {b}, {c}. The largest among three numbers is {max_val}.")