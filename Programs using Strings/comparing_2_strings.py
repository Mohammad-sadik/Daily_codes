def compare(str1, str2):
    if len(str1) != len(str2):
        return "Strings are not equal"

    for i in range(len(str2)):
        if str1[i] != str2[i]:
            return "Strings are not equal"
    return "Strings are equal"

str_1 = input("Enter first string: ")
str_2 = input("Enter second string: ")
print(f"{compare(str_1, str_2)}")
