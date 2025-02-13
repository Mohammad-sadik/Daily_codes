def lower_to_upper(word):
    new_word=""
    for i in word:
        if i>="a" and i<="z":
            new_word += chr(ord(i)-32)
        else:
            new_word+=i
    return new_word

word=input("Enter word in Lower case: ")
print(lower_to_upper(word))