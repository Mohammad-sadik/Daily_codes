num=input("Enter your number : ")
fn=""
for i in num[-1::-1]:
    fn+=i
print(f" The given number is {num} & Reverse the digits of is {fn}")