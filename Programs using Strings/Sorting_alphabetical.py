def sort_order(word):
    for i in range(len(word)):
        min_index = i
        for j in range(i+1,len(word)):
            if word[j] < word[min_index]:
                min_index = j
            word[i], word[min_index] = word[min_index], word[i]

    return f"The sorted order is {word}"
words = (input("Enter word: ").lower()).split()
print(f"The given word is {words}. {sort_order(words)}")

# words = input("Enter word: ").lower()
# words = sorted(words)
# print(words)