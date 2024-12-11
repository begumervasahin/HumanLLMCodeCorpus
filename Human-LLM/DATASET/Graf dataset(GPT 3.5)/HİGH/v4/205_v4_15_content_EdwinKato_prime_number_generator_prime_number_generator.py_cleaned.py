def fonk1(n):
    b1 = []
    for j in range(2, n + 1):
        b2 = True
        for b3 in range(2, j):
            if j % b3 = = 0:
                b2 = False
                break
        if b2:
            b1.append(j)
    return b1
fonk1(10)