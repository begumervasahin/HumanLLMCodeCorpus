def ordered_sequential_search(alist, item):
    pos = 0
    while pos < len(alist):
        if alist[pos] == item:
            return True
        elif alist[pos] > item:
            return False
        pos += 1
    return False
test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(ordered_sequential_search(test_list, 3))
print(ordered_sequential_search(test_list, 13))
