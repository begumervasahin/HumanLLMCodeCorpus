def fonk1(l, value, b1 = 0, b2=-1):
    if not l:
        return -1
    if b2 = = -1:
        b2 = len(l) - 1
    if b1 > b2:
        return -1
    b3 = (b1 + b2)
    if l[b3] == value:
        return b3
    elif l[b3] > value:
        return fonk1(l, value, b1, b3 - 1)
    else:
        return fonk1(l, value, b3 + 1, b2)
print(fonk1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
print(fonk1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11))
