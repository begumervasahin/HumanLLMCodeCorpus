
from funcions import *
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
        n, e, b5, real_p, b8 = genera_claus(i)
        b9 = timeit.default_timer()
        p_found, q_found, b10 = fonk1(n, e)
        b11 = timeit.default_timer()
        b6.append(i)
        b7.append(b11 - b9)
        print("Factorization of N completed.")
        print("Real value of b2:", real_p)
        print("Real value of b3:", b8)
        print("Found value of b2:", p_found)
        print("Found value of b3:", q_found)
    plt.plot(b6, b7, '-gD')
    plt.xlabel("Number of bits")
    plt.ylabel("Seconds")
    plt.show()
fonk2()