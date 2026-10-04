import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.integrate import quad
def xE(z, omegaM, omegaK, omegaL):
    return (omegaM * (1 + z)**3 + omegaK * (1 + z)**2 + omegaL)**0.5
def inverseE(z, omegaM, omegaK, omegaL):
    return 1 / xE(z, omegaM, omegaK, omegaL)
def ploot(z, omegaM, omegaK, omegaL):
    entries = int(z * 100 + 1)
    E = xE(z, omegaM, omegaK, omegaL)
    answerAndError = [quad(inverseE, 0, c, args=(omegaM, omegaK, omegaL)) for c in np.arange(0, z, 0.01)]
    dC = [0] * entries
    for i in range(1, entries):
        dC[i] = answerAndError[i-1][0]
    if omegaK > 0:
        dM = math.sinh((omegaK**0.5) * dC[-1]) / (omegaK**0.5)
    elif omegaK < 0:
        dM = math.sin((abs(omegaK)**0.5) * dC[-1]) / (abs(omegaK)**0.5)
    else:
        dM = dC[-1]
    dA = dM / (1 + z)
    dVc = (((1 + z)**2) * (dA**2)) / E
    return dVc
params = [
    {'omegaM': 1, 'omegaK': 0, 'omegaL': 0},
    {'omegaM': 0.05, 'omegaK': 0.95, 'omegaL': 0},
    {'omegaM': 0.2, 'omegaK': 0, 'omegaL': 0.8}
]
x = np.arange(0, 5.02, 0.01)
plootArrays = []
for param in params:
    plootArrays.append([ploot(z, **param) for z in x])
plt.figure(figsize=(10, 6))
for i, plootArray in enumerate(plootArrays):
    plt.plot(x, plootArray, label=f'Case {i+1}')
plt.xlabel('z')
plt.ylabel('dVc')
plt.title('Ploot Function for Different Cosmological Parameters')
plt.legend()
plt.axis([0, 5, 0, 1.2])
plt.show()