
def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    max_val = find_max(lst[1:])
    print(max_val)
    return lst[0] if lst[0] > max_val else max_val
print(find_max([1,2,3,9,8,7]))