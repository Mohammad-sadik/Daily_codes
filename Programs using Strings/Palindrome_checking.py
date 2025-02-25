word = input("Enter a word: ")
new=0
for i in range(len(word)//2):
    if word[i] == word [-i-1]:
        new+=1
if new == len(word)//2:
    print(f"{word} is a Palindrome.")
else:
    print(f"{word} is a Not Palindrome.")