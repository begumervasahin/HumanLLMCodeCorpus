import numpy as np
def eKey(N, phiN):
    factors_N = [i for i in range(2, N) if N % i == 0]
    factors_phiN = [i for i in range(2, phiN) if phiN % i == 0]
    possible_e = [i for i in range(2, phiN)]
    for e in possible_e[:]:
        for factor in factors_N:
            if e % factor == 0:
                possible_e.remove(e)
                break
    for e in possible_e[:]:
        for factor in factors_phiN:
            if e % factor == 0:
                possible_e.remove(e)
                break
    return possible_e
N = 35
phiN = 24
print("Possible values for e:", eKey(N, phiN))