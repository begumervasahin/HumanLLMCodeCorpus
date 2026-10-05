def fonk1(N, phiN):
    b1 = [i for i in range(2, N) if N % i == 0]
    b2 = [i for i in range(2, phiN) if phiN % i == 0]
    b3 = [i for i in range(2, phiN)]
    b3 = [e for e in b3 if not any(e % factor == 0 for factor in b1)]
    b3 = [e for e in b3 if not any(e % factor == 0 for factor in b2)]
    b4 = [e for e in b3 if e != 0]
    return b4