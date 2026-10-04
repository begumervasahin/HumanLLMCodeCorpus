def fonk1(alist):
    b1 = len(alist)
    for fillslot in range(b1 - 1, 0, -1):
        a1 = 0
        for location in range(1, fillslot + 1):
            if alist[location] > alist[a1]:
                a1 = location
        alist[fillslot], alist[a1] = alist[a1], alist[fillslot]
b2 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
fonk1(b2)
print(b2)
