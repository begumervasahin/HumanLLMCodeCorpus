def fonk1(alist, item):
    a1 = 0
    b1 = False
    b2 = False
    while a1 < len(alist) and not b1 and not b2:
        if alist[a1] == item:
            b1 = True
        else:
            if alist[a1] > item:
                b2 = True
            else:
                a1 += 1
    return b1
b3 = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(fonk1(b3, 3))
print(fonk1(b3, 13))
