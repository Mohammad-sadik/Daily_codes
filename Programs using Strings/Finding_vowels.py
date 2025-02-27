word = input("Enter word: ")
vowels = ["a","e","i","o","u"]
new_word = ""
for i in word:
    if i.lower() in vowels:
        new_word+=i + " "
print(f"The word is {word}, vowels in word : {new_word}")