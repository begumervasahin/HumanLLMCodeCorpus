import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.integrate import quad
def xE(z):
    return (omegaM * (1 + z) ** 3 + omegaK * (1 + z) ** 2 + omegaL) ** 0.5
def inverseE(z):
    return 1 / xE(z)
def dV(z):
    entries = np.rint(z * 100 + 1).astype(int)
    k = entries - 1
    E = (omegaM * (1 + z) ** 3 + omegaK * (1 + z) ** 2 + omegaL) ** 0.5
    answerAndError = [quad(inverseE, 0, c) for c in np.arange(0, z + 0.01, 0.01)]
    dC = [answerAndError[i][0] for i in range(0, entries)]
    dC[0] = 0
    if omegaK > 0:
        dM = math.sinh((omegaK ** 0.5) * dC[k]) / (omegaK ** 0.5)
    elif omegaK < 0:
        dM = math.sin((abs(omegaK) ** 0.5) * dC[k]) / (abs(omegaK) ** 0.5)
    else:
        dM = dC[k]
    dA = dM / (1 + z)
    dVc = (((1 + z) ** 2) * (dA ** 2)) / E
    return dVc
run = 0
x = np.arange(0, 5.02, 0.01)
x1, x2, x3 = [], [], []
while run < 3:
    if run == 0:
        omegaM, omegaK, omegaL = 1, 0, 0
    elif run == 1:
        omegaM, omegaK, omegaL = 0.05, 0.95, 0
    else:
        omegaM, omegaK, omegaL = 0.2, 0, 0.8
    for a in x:
        if run == 0:
            x1.append(dV(a))
        elif run == 1:
            x2.append(dV(a))
        else:
            x3.append(dV(a))
    run += 1
plt.plot(x, x1, label='Omega_M = 1, Omega_K = 0, Omega_Lambda = 0')
plt.plot(x, x2, label='Omega_M = 0.05, Omega_K = 0.95, Omega_Lambda = 0')
plt.plot(x, x3, label='Omega_M = 0.2, Omega_K = 0, Omega_Lambda = 0.8')
plt.xlabel('Redshift (z)')
plt.ylabel('Comoving Volume Element (dV)')
plt.legend()
plt.axis([0, 5, 0, 1.2])
plt.savefig('comovingvolume.png', dpi=80)
plt.show()