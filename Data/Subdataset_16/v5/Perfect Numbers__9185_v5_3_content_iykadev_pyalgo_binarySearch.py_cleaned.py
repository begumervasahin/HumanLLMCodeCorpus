def fonk1(alist, item):
    a1 = 0
    b1 = len(alist) - 1
    while a1 <= b1:
        b2 = (a1 + b1)
        if alist[b2] == item:
            return True
        elif item < alist[b2]:
            b1 = b2 - 1
        else:
            a1 = b2 + 1
    return False
b3 = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(fonk1(b3, 3))
print(fonk1(b3, 13))
