
from funcions import *
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
        n, e, b9, real_p, b7 = genera_claus(i)
        b8 = timeit.default_timer()
        p_found, q_found, b9 = fonk1(n, e)
        b10 = timeit.default_timer()
        b5.append(i)
        b6.append(b10 - b8)
        print("Factorization of N completed.")
        print("Real value of p:", real_p)
        print("Real value of b2:", b7)
        print("Found value of p:", p_found)
        print("Found value of b2:", q_found)
    plt.plot(b5, b6, '-gD')
    plt.xlabel("Number of bits")
    plt.ylabel("Seconds")
    plt.show()
fonk2()