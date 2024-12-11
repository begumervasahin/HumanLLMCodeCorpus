def fonk1(n):
    a1 = 2
    b1 = []
    while a1 <= n:
        a2 = 2
        while not(a2 = = a1) and not(a1%a2 == 0):
            a2 = a2 + 1
        if a2 = = a1:
            b1.append(a1)
        a1 = a1 + 1
    return b1
fonk1(10)