def ordered_sequential_search(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos += 1
    return found
test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(ordered_sequential_search(test_list, 3))
print(ordered_sequential_search(test_list, 13))
