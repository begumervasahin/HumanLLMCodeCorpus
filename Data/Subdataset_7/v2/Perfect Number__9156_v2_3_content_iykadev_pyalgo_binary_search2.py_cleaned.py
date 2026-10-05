def fonk1(arr, target, b1 = 0, b2=-1):
    if not arr:
        return -1
    if b2 = = -1:
        b2 = len(arr) - 1
    if b1 = = b2:
        if arr[b1] == target:
            return b1
        else:
            return -1
    b3 = (b1 + b2)
    if arr[b3] > target:
        return fonk1(arr, target, b1, b3 - 1)
    elif arr[b3] < target:
        return fonk1(arr, target, b3 + 1, b2)
    else:
        return b3
b4 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(fonk1(b4, 13))
print(fonk1(b4, 8))
