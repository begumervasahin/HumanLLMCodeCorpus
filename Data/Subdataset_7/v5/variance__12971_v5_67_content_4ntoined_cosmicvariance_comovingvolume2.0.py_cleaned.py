import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
b1 = [
    {"omega_M": 1, "omega_K": 0, "omega_L": 0, "b14": "b2 = 1, Omega_K = 0, Omega_Lambda = 0"},
    {"omega_M": 0.05, "omega_K": 0.95, "omega_L": 0, "b14": "b2 = 0.05, Omega_K = 0.95, Omega_Lambda = 0"},
    {"omega_M": 0.2, "omega_K": 0, "omega_L": 0.8, "b14": "b2 = 0.2, Omega_K = 0, Omega_Lambda = 0.8"}
]
def fonk1(z, omega_M, omega_K, omega_L):
    return (omega_M * (1 + z) ** 3 + omega_K * (1 + z) ** 2 + omega_L) ** 0.5
def fonk2(z, omega_M, omega_K, omega_L):
    return 1 / fonk1(z, omega_M, omega_K, omega_L)
def fonk3(z, omega_M, omega_K, omega_L):
    b3 = np.rint(z * 100 + 1).astype(int)
    b4 = b3 - 1
    b5 = fonk1(z, omega_M, omega_K, omega_L)
    b6 = [quad(inverseE, 0, c, args=(omega_M, omega_K, omega_L)) for c in np.arange(0, z + 0.01, 0.01)]
    b7 = [b6[i][0] for i in range(b3)]
    b7[0] = 0
    if omega_K > 0:
        b8 = np.sinh((omega_K ** 0.5) * b7[b4]) / (omega_K ** 0.5)
    elif omega_K < 0:
        b8 = np.sin((abs(omega_K) ** 0.5) * b7[b4]) / (abs(omega_K) ** 0.5)
    else:
        b8 = b7[b4]
    b9 = b8 / (1 + z)
    b10 = (((1 + z) ** 2) * (b9 ** 2)) / b5
    return b10
b11 = np.arange(0, 5.02, 0.01)
b12 = [[] for _ in range(len(b1))]
for i, params in enumerate(b1):
    for z in b11:
        b12[i].append(fonk3(z, params["omega_M"], params["omega_K"], params["omega_L"]))
plt.figure(b13 = (10, 6))
for i, params in enumerate(b1):
    plt.plot(b11, b12[i], b14 = params["b14"])
plt.xlabel('Redshift (z)')
plt.ylabel('Comoving Volume Element (dV)')
plt.legend()
plt.axis([0, 5, 0, 1.2])
plt.savefig('comovingvolume.png', b15 = 80)
plt.show()