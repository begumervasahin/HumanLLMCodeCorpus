def find_valid_e(N, phiN):
    factors_N = []
    factors_phiN = []
    possible_e = []
    for i in range(2, N):
        if N % i == 0:
            factors_N.append(i)
    for i in range(2, phiN):
        if phiN % i == 0:
            factors_phiN.append(i)
    for i in range(2, phiN):
        possible_e.append(i)
    for i in range(len(possible_e)):
        for j in range(len(factors_N)):
            if possible_e[i] % factors_N[j] == 0:
                possible_e[i] = 0
    for i in range(len(possible_e)):
        for j in range(len(factors_phiN)):
            if possible_e[i] % factors_phiN[j] == 0:
                possible_e[i] = 0
    true_e = []
    for i in range(len(possible_e)):
        if possible_e[i] != 0:
            true_e.append(possible_e[i])
    return true_e