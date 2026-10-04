def binary_search(l, value, low=0, high=-1):
    if not l:
        return -1
    if high == -1:
        high = len(l) - 1
    if low > high:
        return -1
    mid = (low + high)
    if l[mid] == value:
        return mid
    elif l[mid] > value:
        return binary_search(l, value, low, mid - 1)
    else:
        return binary_search(l, value, mid + 1, high)
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11))
