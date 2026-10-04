def fonk1(alist):
    for index in range(1, len(alist)):
        b1 = alist[index]
        b2 = index
        while b2 > 0 and alist[b2 - 1] > b1:
            alist[b2] = alist[b2 - 1]
            b2 -= 1
        alist[b2] = b1