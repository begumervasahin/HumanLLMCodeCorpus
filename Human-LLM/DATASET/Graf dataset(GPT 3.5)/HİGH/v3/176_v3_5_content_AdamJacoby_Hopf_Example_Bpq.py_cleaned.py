import numpy as np
from itertools import product
class class1:
    pass
def fonk1(b5, b6):
    pass
def fonk2(b7, b3, b4, name):
    pass
class class2:
    def fonk3(self, a1, a2, a3, a, sigma):
        pass
def fonk4(n):
    return [np.exp(i * 2j * np.pi / n) for i in range(n)]
def fonk5(a1, a2):
    b1 = (a1 * a2) ** 2
    b2 = fonk4(a1)
    b3 = np.zeros((b1 ** 2), dtype=complex)
    b4 = np.zeros((b1 ** 2), dtype=complex)
    for i, j in product(range(a1), range(a1)):
        b3[b1 * i + j] = (1 / a1) * b2[(-i * j) % a1]
        b4[b1 * i + j] = (1 / a1) * b2[(i * j) % a1]
    return b3, b4
def fonk6(a1, a2, a3):
    b5 = class2(a1, a2, a3, 'a', 'sigma')
    b6 = class2(a1, a2, a3, 'b', 'tau')
    b7 = fonk1(b5, b6)
    b3, b4 = fonk5(a1, a2)
    return fonk2(b7, b3, b4, 'b3')
a1 = 2
a2 = 3
a3 = 4
b8 = fonk6(a1, a2, a3)
print(b8)