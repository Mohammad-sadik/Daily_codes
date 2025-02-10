char=input("Enter char : ")
vowels = ["a", "e", "i", "o", "u"]
if char.isalpha():
    char = char.lower()
    if char in vowels:
        print(f"The given char is {char}, & it is a vowel")
    else:
        print(f"The given char is {char}, & it is a consonant")
else:
    print(f"The given char is {char} is not a char")