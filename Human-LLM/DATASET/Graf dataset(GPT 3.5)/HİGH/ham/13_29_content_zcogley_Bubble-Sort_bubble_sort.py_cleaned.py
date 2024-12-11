def fonk1(lst):
    b1 = lst[:]
    b2 = False
    while b2 = = False:
        a1 = 0
        a2 = 0
        a3 = 0
        if len(b1) % b3 = = 0:
            a3 = len(b1)
        else:
            a3 = len(b1) - 1
        while a1 < a3:
            b4 = b1[a1]
            b5 = b1[a1+1]
            if b4 > b5:
                b1[a1] = b5
                b1[a1+1] = b4
                a2 += 1
            a1 = a1 + 1
        if a2 = = 0:
            b2 = True
    return b1