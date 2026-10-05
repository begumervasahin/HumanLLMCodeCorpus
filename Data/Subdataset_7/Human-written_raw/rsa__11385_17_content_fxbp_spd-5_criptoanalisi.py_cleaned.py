from funcions import *
import numpy as np
import matplotlib.pyplot as plt
import timeit
from genera_claus import genera_claus
def fonk1(N,e):
    b1 = factors_primers(N)
    if (len(b1)!=2):
        return 0, 0, 0
    b2 = b1[0]
    b3 = b1[1]
    b4 = (b2-1)*(b3-1)
    b5 = invers_modular(e,b4)
    return b2, b3, b5
def fonk2():
    a1 = 25
    b6 = list()
    b7 = list()
    for i in range(8, a1):
        n, e, b5, b2, b3 = genera_claus(i)
        b8 = timeit.default_timer()
        pDesc, qDesc, b9 = fonk1(n,e)
        b10 = timeit.default_timer()
        b6.append(i)
        b7.append(b10 - b8)
        print("S'ha factoritzat N")
        print("Nombre b2 real: " + str(b2))
        print("Nombre b3 real: "+ str(b3))
        print("Nombre b2 trobat: "+ str(pDesc))
        print("Nombre b3 trobat: "+ str(qDesc))
    plt.plot(b6,b7, '-gD')
    plt.xlabel("Nombre de bits")
    plt.ylabel("Segons")
    plt.show()
fonk2()