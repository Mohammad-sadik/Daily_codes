words = "The quick brown fox jumped over the lazy dog".split()
max_val = max([len(i) for i in words])
max_word = [word for word in words if max_val == len(word)]

print(f"The longest word is: '{"".join(max_word)}' with length {max_val}")