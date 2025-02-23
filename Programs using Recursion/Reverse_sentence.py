def reverse_the_sentence(word):
    if len(word) == 0:
        return ""
    return word[len(word)-1] + reverse_the_sentence(word[0:len(word)-1:1] )

word = input("Enter word : ")
print(f"The given word is {word}, the reverse of the word {reverse_the_sentence(word)}")
