string = input("Enter String: ")
New =""
for char in string:
    if char.isalpha():
        New += char
print(f"After remove characters in string except alphabets: {New}")