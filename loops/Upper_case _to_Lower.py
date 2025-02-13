def lower_to_upper(word):
    new_word=""
    for i in word:
        if i>="A" and i<="Z":
            lower_num= ord(i)+32
            new_word+=chr(lower_num)
        else:
            new_word += i
    return new_word

word= input("Enter your upper case word: ")
print(lower_to_upper(word))
"""________________________________________________________________________________________"""
# new=""
# for i in word:
#     new+= i.upper()
# print(f"The lowerd case word is {word}, after converting the upper case {new}")
"""_______________________________________________________________________________________"""
# #print(f"The lowerd case word is {word}, after converting the upper case {word.upper()}")
