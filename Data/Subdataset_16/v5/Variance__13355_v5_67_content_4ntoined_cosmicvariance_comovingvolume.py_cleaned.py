import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.integrate import quad
b1 = [
    {"b12": 1, "b13": 0, "b14": 0},
    {"b12": 0.05, "b13": 0.95, "b14": 0},
    {"b12": 0.2, "b13": 0, "b14": 0.8}
]
def fonk1(z, b12, b13, b14):
    return np.sqrt(b12 * (1 + z)**3 + b13 * (1 + z)**2 + b14)
def fonk2(z, b12, b13, b14):
    return 1 / fonk1(z, b12, b13, b14)
def fonk3(z, b12, b13, b14):
    b2 = int(np.rint(z * 100 + 1))
    b3 = b2 - 1
    b4 = fonk1(z, b12, b13, b14)
    b5 = [quad(inverseE, 0, c, args=(b12, b13, b14)) for c in np.arange(0, z, 0.01)]
    b6 = np.zeros(b2)
    for i in range(1, b2):
        b6[i] = b5[i - 1][0]
    if b13 > 0:
        b7 = np.sinh(np.sqrt(b13) * b6[b3]) / np.sqrt(b13)
    elif b13 < 0:
        b7 = np.sin(np.sqrt(abs(b13)) * b6[b3]) / np.sqrt(abs(b13))
    else:
        b7 = b6[b3]
    b8 = b7 / (1 + z)
    b9 = ((1 + z)**2 * b8**2) / b4
    return b9
b10 = np.arange(0, 5.02, 0.01)
b11 = []
for case in b1:
    b12 = case["b12"]
    b13 = case["b13"]
    b14 = case["b14"]
    b15 = [fonk3(z, b12, b13, b14) for z in b10]
    b11.append(b15)
for idx, b15 in enumerate(b11):
    plt.plot(b10, b15, b16 = f"Case {idx + 1}")
plt.xlabel('Redshift (z)')
plt.ylabel('b9')
plt.axis([0, 5, 0, 1.2])
plt.legend()
plt.show()