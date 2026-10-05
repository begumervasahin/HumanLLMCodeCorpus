
from funcions import factors_primers, invers_modular
import numpy as np
import matplotlib.pyplot as plt
import timeit
from genera_claus import genera_claus
def factoritza(N, e):
    llista_factors = factors_primers(N)
    if len(llista_factors) != 2:
        return 0, 0, 0
    p = llista_factors[0]
    q = llista_factors[1]
    phi_n = (p - 1) * (q - 1)
    d = invers_modular(e, phi_n)
    return p, q, d
def test():
    max_bits = 25
    mides = []
    temps = []
    for i in range(8, max_bits):
        n, e, d, p, q = genera_claus(i)
        temps_inicial = timeit.default_timer()
        pDesc, qDesc, dDesc = factoritza(n, e)
        temps_final = timeit.default_timer()
        mides.append(i)
        temps.append(temps_final - temps_inicial)
        print("Factorization completed for N")
        print("Real prime factor p: " + str(p))
        print("Real prime factor q: " + str(q))
        print("Computed prime factor p: " + str(pDesc))
        print("Computed prime factor q: " + str(qDesc))
    plt.plot(mides, temps, '-gD')
    plt.xlabel("Number of bits")
    plt.ylabel("Seconds")
    plt.show()
if __name__ == "__main__":
    test()