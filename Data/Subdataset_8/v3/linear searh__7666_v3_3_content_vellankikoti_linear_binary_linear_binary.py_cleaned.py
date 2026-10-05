def linear_search(lst, key):
    return key in lst
lst_linear = [10, 20, 30, 40, 50]
key_linear = 30
print(f"Linear Search: {linear_search(lst_linear, key_linear)}")
def binary_search(lst, key):
    if not lst:
        return False
    mid = len(lst)
    if lst[mid] == key:
        return True
    elif key < lst[mid]:
        return binary_search(lst[:mid], key)
    else:
        return binary_search(lst[mid + 1:], key)
lst_binary = [10, 20, 30, 50, 60, 70, 80]
key_binary = 50
print(f"Binary Search: {binary_search(lst_binary, key_binary)}")