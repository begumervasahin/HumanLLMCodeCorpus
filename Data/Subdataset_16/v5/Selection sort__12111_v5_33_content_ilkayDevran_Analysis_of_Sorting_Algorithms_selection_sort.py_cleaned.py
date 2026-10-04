def fonk1(alist):
    for j in range(len(alist) - 1):
        b1 = j
        for i in range(j + 1, len(alist)):
            if alist[i] < alist[b1]:
                b1 = i
        alist[j], alist[b1] = alist[b1], alist[j]
