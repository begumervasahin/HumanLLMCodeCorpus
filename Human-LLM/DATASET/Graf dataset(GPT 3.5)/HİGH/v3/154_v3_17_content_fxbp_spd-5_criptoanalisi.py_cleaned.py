
from funcions import factors_primers, invers_modular
import numpy as np
import matplotlib.pyplot as plt
import timeit
from genera_claus import genera_claus
def fonk1(N, e):
    b1 = factors_primers(N)
    if len(b1) != 2:
        return 0, 0, 0
    p, b2 = b1
    b3 = (p - 1) * (b2 - 1)
    b4 = invers_modular(e, b3)
    return p, b2, b4
def fonk2():
    a1 = 25
    b5 = []
    b6 = []
    for i in range(8, a1):
        n, e, b4, p, b2 = genera_claus(i)
        b7 = timeit.default_timer()
        p_desc, q_desc, b8 = fonk1(n, e)
        b9 = timeit.default_timer()
        b5.append(i)
        b6.append(b9 - b7)
        print("Factorization completed for N")
        print("Real prime factor p: " + str(p))
        print("Real prime factor b2: " + str(b2))
        print("Computed prime factor p: " + str(p_desc))
        print("Computed prime factor b2: " + str(q_desc))
    plt.plot(b5, b6, '-gD')
    plt.xlabel("Number of bits")
    plt.ylabel("Seconds")
    plt.show()
if b10 = = "__main__":
    fonk2()