
from funcions import *
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
    sizes = []
    times = []
    for i in range(8, max_bits):
        n, e, d, real_p, real_q = genera_claus(i)
        start_time = timeit.default_timer()
        p_found, q_found, d_found = factoritza(n, e)
        end_time = timeit.default_timer()
        sizes.append(i)
        times.append(end_time - start_time)
        print("Factorization of N completed.")
        print("Real value of p:", real_p)
        print("Real value of q:", real_q)
        print("Found value of p:", p_found)
        print("Found value of q:", q_found)
    plt.plot(sizes, times, '-gD')
    plt.xlabel("Number of bits")
    plt.ylabel("Seconds")
    plt.show()
test()