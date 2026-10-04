import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.integrate import quad
cases = [
    {"omegaM": 1, "omegaK": 0, "omegaL": 0},
    {"omegaM": 0.05, "omegaK": 0.95, "omegaL": 0},
    {"omegaM": 0.2, "omegaK": 0, "omegaL": 0.8}
]
def xE(z, omegaM, omegaK, omegaL):
    return np.sqrt(omegaM * (1 + z)**3 + omegaK * (1 + z)**2 + omegaL)
def inverseE(z, omegaM, omegaK, omegaL):
    return 1 / xE(z, omegaM, omegaK, omegaL)
def ploot(z, omegaM, omegaK, omegaL):
    entries = int(np.rint(z * 100 + 1))
    k = entries - 1
    E = xE(z, omegaM, omegaK, omegaL)
    answer_and_error = [quad(inverseE, 0, c, args=(omegaM, omegaK, omegaL)) for c in np.arange(0, z, 0.01)]
    dC = np.zeros(entries)
    for i in range(1, entries):
        dC[i] = answer_and_error[i - 1][0]
    if omegaK > 0:
        dM = np.sinh(np.sqrt(omegaK) * dC[k]) / np.sqrt(omegaK)
    elif omegaK < 0:
        dM = np.sin(np.sqrt(abs(omegaK)) * dC[k]) / np.sqrt(abs(omegaK))
    else:
        dM = dC[k]
    dA = dM / (1 + z)
    dVc = ((1 + z)**2 * dA**2) / E
    return dVc
x = np.arange(0, 5.02, 0.01)
ploot_arrays = []
for case in cases:
    omegaM = case["omegaM"]
    omegaK = case["omegaK"]
    omegaL = case["omegaL"]
    ploot_array = [ploot(z, omegaM, omegaK, omegaL) for z in x]
    ploot_arrays.append(ploot_array)
for idx, ploot_array in enumerate(ploot_arrays):
    plt.plot(x, ploot_array, label=f"Case {idx + 1}")
plt.xlabel('Redshift (z)')
plt.ylabel('dVc')
plt.axis([0, 5, 0, 1.2])
plt.legend()
plt.show()