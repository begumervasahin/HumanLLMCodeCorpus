import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.integrate import quad
def fonk1(z, omegaM, omegaK, omegaL):
    return (omegaM * (1 + z) ** 3 + omegaK * (1 + z) ** 2 + omegaL) ** 0.5
def fonk2(z, omegaM, omegaK, omegaL):
    return 1 / fonk1(z, omegaM, omegaK, omegaL)
def fonk3(z, omegaM, omegaK, omegaL):
    b1 = np.rint(z * 100 + 1).astype(int)
    b2 = b1 - 1
    b3 = fonk1(z, omegaM, omegaK, omegaL)
    b4 = [quad(inverseE, 0, c, args=(omegaM, omegaK, omegaL)) for c in np.arange(0, z + 0.01, 0.01)]
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
b9 = np.arange(0, 5.02, 0.01)
b10 = [
    (1, 0, 0),
    (0.05, 0.95, 0),
    (0.2, 0, 0.8)
]
plt.figure()
for i, (omegaM, omegaK, omegaL) in enumerate(b10):
    b11 = [fonk3(a, omegaM, omegaK, omegaL) for a in b9]
    plt.plot(b9, b11, b12 = f'Omega values {i+1}')
plt.axis([0, 5, 0, 1.2])
plt.legend()
plt.savefig('comovingvolume.png', b13 = 80)
plt.show()