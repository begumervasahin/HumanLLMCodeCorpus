import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
COSMO_PARAMETERS = [
    {"omega_M": 1, "omega_K": 0, "omega_L": 0, "label": "Omega_M = 1, Omega_K = 0, Omega_Lambda = 0"},
    {"omega_M": 0.05, "omega_K": 0.95, "omega_L": 0, "label": "Omega_M = 0.05, Omega_K = 0.95, Omega_Lambda = 0"},
    {"omega_M": 0.2, "omega_K": 0, "omega_L": 0.8, "label": "Omega_M = 0.2, Omega_K = 0, Omega_Lambda = 0.8"}
]
def xE(z, omega_M, omega_K, omega_L):
    return (omega_M * (1 + z) ** 3 + omega_K * (1 + z) ** 2 + omega_L) ** 0.5
def inverseE(z, omega_M, omega_K, omega_L):
    return 1 / xE(z, omega_M, omega_K, omega_L)
def dV(z, omega_M, omega_K, omega_L):
    entries = np.rint(z * 100 + 1).astype(int)
    k = entries - 1
    E = xE(z, omega_M, omega_K, omega_L)
    answerAndError = [quad(inverseE, 0, c, args=(omega_M, omega_K, omega_L)) for c in np.arange(0, z + 0.01, 0.01)]
    dC = [answerAndError[i][0] for i in range(entries)]
    dC[0] = 0
    if omega_K > 0:
        dM = np.sinh((omega_K ** 0.5) * dC[k]) / (omega_K ** 0.5)
    elif omega_K < 0:
        dM = np.sin((abs(omega_K) ** 0.5) * dC[k]) / (abs(omega_K) ** 0.5)
    else:
        dM = dC[k]
    dA = dM / (1 + z)
    dVc = (((1 + z) ** 2) * (dA ** 2)) / E
    return dVc
x = np.arange(0, 5.02, 0.01)
plots = [[] for _ in range(len(COSMO_PARAMETERS))]
for i, params in enumerate(COSMO_PARAMETERS):
    for z in x:
        plots[i].append(dV(z, params["omega_M"], params["omega_K"], params["omega_L"]))
plt.figure(figsize=(10, 6))
for i, params in enumerate(COSMO_PARAMETERS):
    plt.plot(x, plots[i], label=params["label"])
plt.xlabel('Redshift (z)')
plt.ylabel('Comoving Volume Element (dV)')
plt.legend()
plt.axis([0, 5, 0, 1.2])
plt.savefig('comovingvolume.png', dpi=80)
plt.show()