import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.integrate import quad
def fonk1(z):
    return (omegaM * (1 + z) ** 3 + omegaK * (1 + z) ** 2 + b11) ** 0.5
def fonk2(z):
    return 1 / fonk1(z)
def fonk3(z):
    b1 = np.rint(z * 100 + 1).astype(int)
    b2 = b1 - 1
    b3 = (omegaM * (1 + z) ** 3 + omegaK * (1 + z) ** 2 + b11) ** 0.5
    b4 = [quad(inverseE, 0, c) for c in np.arange(0, z + 0.01, 0.01)]
    b5 = [b4[i][0] for i in range(0, b1)]
    b5[0] = 0
    if omegaK > 0:
        b6 = math.sinh((omegaK ** 0.5) * b5[b2]) / (omegaK ** 0.5)
    elif omegaK < 0:
        b6 = math.sin((abs(omegaK) ** 0.5) * b5[b2]) / (abs(omegaK) ** 0.5)
    else:
        b6 = b5[b2]
    b7 = b6 / (1 + z)
    b8 = (((1 + z) ** 2) * (b7 ** 2)) / b3
    return b8
a1 = 0
b9 = np.arange(0, 5.02, 0.01)
x1, x2, b10 = [], [], []
while a1 < 3:
    if a1 = = 0:
        omegaM, omegaK, b11 = 1, 0, 0
    elif a1 = = 1:
        omegaM, omegaK, b11 = 0.05, 0.95, 0
    else:
        omegaM, omegaK, b11 = 0.2, 0, 0.8
    for a in b9:
        if a1 = = 0:
            x1.append(fonk3(a))
        elif a1 = = 1:
            x2.append(fonk3(a))
        else:
            b10.append(fonk3(a))
    a1 += 1
plt.plot(b9, x1, b12 = 'Omega_M = 1, Omega_K = 0, Omega_Lambda = 0')
plt.plot(b9, x2, b12 = 'Omega_M = 0.05, Omega_K = 0.95, Omega_Lambda = 0')
plt.plot(b9, b10, b12 = 'Omega_M = 0.2, Omega_K = 0, Omega_Lambda = 0.8')
plt.xlabel('Redshift (z)')
plt.ylabel('Comoving Volume Element (dV)')
plt.legend()
plt.axis([0, 5, 0, 1.2])
plt.savefig('comovingvolume.png', b13 = 80)
plt.show()