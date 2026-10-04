def fonk1(lst):
    b1 = lst[:]
    b2 = False
    while not b2:
        b2 = True
        for idx in range(len(b1) - 1):
            if b1[idx] > b1[idx + 1]:
                b1[idx], b1[idx + 1] = b1[idx + 1], b1[idx]
                b2 = False
    return b1