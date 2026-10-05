def binary_search(l, value, low=0, high=-1):
    if not l:
        return -1
    if high == -1:
        high = len(l) - 1
    if low == high:
        if l[low] == value:
            return low
        else:
            return -1
    mid = (low + high)
    if l[mid] > value:
        return binary_search(l, value, low, mid - 1)
    elif l[mid] < value:
        return binary_search(l, value, mid + 1, high)
    else:
        return mid
test_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(binary_search(test_list, 13))
print(binary_search(test_list, 8))
