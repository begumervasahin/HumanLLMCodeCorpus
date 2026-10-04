def fonk1(alist, item):
    a1 = 0
    while a1 < len(alist):
        if alist[a1] == item:
            return True
        elif alist[a1] > item:
            return False
        a1 += 1
    return False
b1 = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(fonk1(b1, 3))
print(fonk1(b1, 13))
