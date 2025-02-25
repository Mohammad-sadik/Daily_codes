word = input("Enter name: ")
asci = ""
for i in word:
    asci+= str(ord(i))+ " "
print(f"The given word is {word}, Ascii value is {asci}")