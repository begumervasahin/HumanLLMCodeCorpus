def fonk1(alist, item):
    if len(alist) == 0:
        return False
    b1 = len(alist)
    if alist[b1] == item:
        return True
    elif item < alist[b1]:
        return fonk1(alist[:b1], item)
    else:
        return fonk1(alist[b1+1:], item)
b2 = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(fonk1(b2, 3))
print(fonk1(b2, 13))
