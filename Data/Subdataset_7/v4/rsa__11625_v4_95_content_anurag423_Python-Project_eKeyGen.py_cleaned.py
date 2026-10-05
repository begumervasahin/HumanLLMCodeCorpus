def fonk1(N, phiN):
    b1 = []
    b2 = []
    b3 = []
    for b4 in range(2, N):
        if N % b4 = = 0:
            b1.append(b4)
    for b4 in range(2, phiN):
        if phiN % b4 = = 0:
            b2.append(b4)
    for b4 in range(2, phiN):
        b3.append(b4)
    for b4 in range(len(b3)):
        for j in range(len(b1)):
            if b3[b4] % b1[j] == 0:
                b3[b4] = 0
    for b4 in range(len(b3)):
        for j in range(len(b2)):
            if b3[b4] % b2[j] == 0:
                b3[b4] = 0
    b5 = []
    for b4 in range(len(b3)):
        if b3[b4] != 0:
            b5.append(b3[b4])
    return b5