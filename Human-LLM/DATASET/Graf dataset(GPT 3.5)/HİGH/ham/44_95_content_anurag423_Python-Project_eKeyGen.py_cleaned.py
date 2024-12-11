def fonk1(N,phiN):
    import numpy as np
    b1 = []
    b1 = np.array(b1,dtype=int)
    for b2 in range(2,N):
        if N % b2 = = 0:
            b1 = np.append(b1, b2)
    b3 = []
    b3 = np.array(b3,dtype=int)
    for b2 in range(2,phiN):
        if phiN % b2 = = 0:
            b3 = np.append(b3, b2)
    b4 = []
    b4 = np.array(b4,dtype=int)
    for b2 in range(2,phiN):
        b4 = np.append(b4, b2)
    for b2 in range(0,len(b4)):
        for j in range(0,len(b1)):
            if b4[b2] % b1[j] == 0:
                b4[b2] = 0
    for b2 in range(0,len(b4)):
        for j in range(0,len(b3)):
            if b4[b2] % b3[j] == 0:
                b4[b2] = 0
    b5 = []
    b5 = np.array(b5,dtype=int)
    for b2 in range(0,len(b4)):
        if b4[b2] != 0:
            b5 = np.append(b5, b4[b2])
    return b5