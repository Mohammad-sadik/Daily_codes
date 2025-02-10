year= int(input("Enter Year : "))
if (year%4==0 and year%100!=0) or (year%400 ==0):
    print(f"The given year is {year}, and it is a leap year")
else:
    print(f"The given year is {year}, and it is not a leap year")
