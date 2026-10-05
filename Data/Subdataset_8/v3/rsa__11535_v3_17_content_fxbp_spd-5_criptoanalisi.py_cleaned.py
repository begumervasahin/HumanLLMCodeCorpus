
from funcions import factors_primers, invers_modular
import numpy as np
import matplotlib.pyplot as plt
import timeit
from genera_claus import genera_claus
def factoritza(N, e):
    prime_factors = factors_primers(N)
    if len(prime_factors) != 2:
        return 0, 0, 0
    p, q = prime_factors
    phi_n = (p - 1) * (q - 1)
    d = invers_modular(e, phi_n)
    return p, q, d
def test():
    max_bits = 25
    key_sizes = []
    processing_times = []
    for i in range(8, max_bits):
        n, e, d, p, q = genera_claus(i)
        start_time = timeit.default_timer()
        p_desc, q_desc, d_desc = factoritza(n, e)
        end_time = timeit.default_timer()
        key_sizes.append(i)
        processing_times.append(end_time - start_time)
        print("Factorization completed for N")
        print("Real prime factor p: " + str(p))
        print("Real prime factor q: " + str(q))
        print("Computed prime factor p: " + str(p_desc))
        print("Computed prime factor q: " + str(q_desc))
    plt.plot(key_sizes, processing_times, '-gD')
    plt.xlabel("Number of bits")
    plt.ylabel("Seconds")
    plt.show()
if __name__ == "__main__":
    test()