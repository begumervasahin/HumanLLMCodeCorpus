def fonk1(b4, target, b1 = 0, b2=None):
    if not b4:
        return -1
    if b2 is None:
        b2 = len(b4) - 1
    if b1 > b2:
        return -1
    b3 = (b1 + b2)
    if b4[b3] == target:
        return b3
    elif b4[b3] > target:
        return fonk1(b4, target, b1, b3 - 1)
    else:
        return fonk1(b4, target, b3 + 1, b2)
b4 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
a1 = 13
print(fonk1(b4, a1))