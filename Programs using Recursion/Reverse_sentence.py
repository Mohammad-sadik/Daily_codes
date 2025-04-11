# word = input("Enter word : ")
# new = ""
# for i in word:
#     new = i + new
# print(f"The given word is {word}, the reverse of the word {new}")
####################################################3

def reverse_the_sentence(word):
    k = len( word)
    if k == 0:
        return ""

    return word[k-1] + reverse_the_sentence(word[:k-1:1])

print(f"The given word is {word}, the reverse of the word {reverse_the_sentence(word)}")
