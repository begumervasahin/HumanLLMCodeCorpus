
from funcions import factors_primers, invers_modular
import numpy as np
import matplotlib.pyplot as plt
import timeit
from genera_claus import genera_claus
def fonk1(N, e):
    b1 = factors_primers(N)
    if len(b1) != 2:
        return 0, 0, 0
    b2 = b1[0]
    b3 = b1[1]
    b4 = (b2 - 1) * (b3 - 1)
    b5 = invers_modular(e, b4)
    return b2, b3, b5
def fonk2():
    a1 = 25
    b6 = []
    b7 = []
    for i in range(8, a1):
        n, e, b5, b2, b3 = genera_claus(i)
        b8 = timeit.default_timer()
        pDesc, qDesc, b9 = fonk1(n, e)
        b10 = timeit.default_timer()
        b6.append(i)
        b7.append(b10 - b8)
        print("Factorization completed for N")
        print("Real prime factor b2: " + str(b2))
        print("Real prime factor b3: " + str(b3))
        print("Computed prime factor b2: " + str(pDesc))
        print("Computed prime factor b3: " + str(qDesc))
    plt.plot(b6, b7, '-gD')
    plt.xlabel("Number of bits")
    plt.ylabel("Seconds")
    plt.show()
if b11 = = "__main__":
    fonk2()