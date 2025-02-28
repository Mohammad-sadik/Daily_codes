string = input("Enter String: ").lower()
sub_str = input("Enter Sub-String: ").lower()
if sub_str in string:
    print(f"Substring found at index {string.index(sub_str)}.")
else:
    print("Substring not found ")