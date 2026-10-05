def find_valid_e(N, phiN):
    factors_N = [i for i in range(2, N) if N % i == 0]
    factors_phiN = [i for i in range(2, phiN) if phiN % i == 0]
    possible_e = [i for i in range(2, phiN)]
    possible_e = [e for e in possible_e if not any(e % factor == 0 for factor in factors_N)]
    possible_e = [e for e in possible_e if not any(e % factor == 0 for factor in factors_phiN)]
    true_e = [e for e in possible_e if e != 0]
    return true_e