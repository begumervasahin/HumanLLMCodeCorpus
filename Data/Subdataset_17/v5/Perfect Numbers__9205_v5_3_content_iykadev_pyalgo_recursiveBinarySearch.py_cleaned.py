def binary_search(alist, item):
    if not alist:
        return False
    midpoint = len(alist)
    if alist[midpoint] == item:
        return True
    elif item < alist[midpoint]:
        return binary_search(alist[:midpoint], item)
    else:
        return binary_search(alist[midpoint + 1:], item)
test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search(test_list, 3))
print(binary_search(test_list, 13))
