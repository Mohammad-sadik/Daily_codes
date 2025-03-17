import copy

list1 = [[1, 2, 3], [4, 5, 6]]
shallow_copy = copy.copy(list1)
shallow_copy[0][0] = 99

print("Original List:", list1)
print("Shallow Copy:", shallow_copy, "\n")
# ********************************************
list1 = [[1, 2, 3], [4, 5, 6]]
deep_copy = copy.deepcopy(list1)
deep_copy[0][0] = 99
print("Original List:", list1)
print("Deep Copy:", deep_copy)