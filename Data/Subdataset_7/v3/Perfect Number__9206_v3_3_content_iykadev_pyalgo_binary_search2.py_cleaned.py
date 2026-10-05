def fonk1(arr, target, b1 = 0, b2=None):
    if not arr:
        return -1
    if b2 is None:
        b2 = len(arr) - 1
    while b1 <= b2:
        b3 = (b1 + b2)
        if arr[b3] == target:
            return b3
        elif arr[b3] < target:
            b1 = b3 + 1
        else:
            b2 = b3 - 1
    return -1
b4 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(fonk1(b4, 13))
print(fonk1(b4, 8))
