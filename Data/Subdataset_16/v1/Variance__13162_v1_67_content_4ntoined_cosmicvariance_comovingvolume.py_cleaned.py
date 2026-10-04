import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.integrate import quad
def fonk1(z, omegaM, omegaK, omegaL):
    return (omegaM * (1 + z)**3 + omegaK * (1 + z)**2 + omegaL)**0.5
def fonk2(z, omegaM, omegaK, omegaL):
    return 1 / fonk1(z, omegaM, omegaK, omegaL)
def fonk3(z, omegaM, omegaK, omegaL):
    b1 = int(z * 100 + 1)
    b2 = fonk1(z, omegaM, omegaK, omegaL)
    b3 = [quad(inverseE, 0, c, args=(omegaM, omegaK, omegaL)) for c in np.arange(0, z, 0.01)]
    b4 = [0] * b1
    for i in range(1, b1):
        b4[i] = b3[i-1][0]
    if omegaK > 0:
        b5 = math.sinh((omegaK**0.5) * b4[-1]) / (omegaK**0.5)
    elif omegaK < 0:
        b5 = math.sin((abs(omegaK)**0.5) * b4[-1]) / (abs(omegaK)**0.5)
    else:
        b5 = b4[-1]
    b6 = b5 / (1 + z)
    b7 = (((1 + z)**2) * (b6**2)) / b2
    return b7
b8 = [
    {'omegaM': 1, 'omegaK': 0, 'omegaL': 0},
    {'omegaM': 0.05, 'omegaK': 0.95, 'omegaL': 0},
    {'omegaM': 0.2, 'omegaK': 0, 'omegaL': 0.8}
]
b9 = np.arange(0, 5.02, 0.01)
b10 = []
for param in b8:
    b10.append([fonk3(z, **param) for z in b9])
plt.figure(b11 = (10, 6))
for i, plootArray in enumerate(b10):
    plt.plot(b9, plootArray, b12 = f'Case {i+1}')
plt.xlabel('z')
plt.ylabel('b7')
plt.title('Ploot Function for Different Cosmological Parameters')
plt.legend()
plt.axis([0, 5, 0, 1.2])
plt.show()