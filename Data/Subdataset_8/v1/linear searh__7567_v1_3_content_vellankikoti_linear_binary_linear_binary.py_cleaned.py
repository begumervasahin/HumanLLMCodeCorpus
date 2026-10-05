def linear_search(lst, key):
    for value in lst:
        if value == key:
            return True
    else:
        return False
        print("This will never get Executed")
lst_linear = [10, 20, 30, 40, 50]
key_linear = 30
print(linear_search(lst_linear, key_linear))
def binary_search(lst, key):
    if len(lst) == 0:
        return False
    else:
        mid = len(lst)
        if lst[mid] == key:
            return True
        elif key < lst[mid]:
            return binary_search(lst[:mid], key)
        else:
            return binary_search(lst[mid + 1:], key)
lst_binary = [10, 20, 30, 50, 60, 70, 80]
key_binary = 50
print(binary_search(lst_binary, key_binary))