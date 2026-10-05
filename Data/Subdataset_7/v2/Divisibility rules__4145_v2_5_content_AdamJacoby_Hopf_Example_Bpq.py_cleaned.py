import numpy as np
from itertools import product
class class1:
    pass
def fonk1(b6, b7):
    pass
def fonk2(b8, b4, b5, name):
    pass
class class2:
    def fonk3(self, a1, a2, a3, a, sigma):
        pass
def fonk4(n):
    b1 = []
    for i in range(n):
        b1.append(np.exp(i * 2j * np.pi / n))
    return b1
def fonk5(a1, a2):
    b2 = (a1 * a2) ** 2
    b3 = fonk4(a1)
    b4 = np.zeros((b2 ** 2), dtype=complex)
    b5 = np.zeros((b2 ** 2), dtype=complex)
    for i, j in product(range(a1), range(a1)):
        b4[b2 * i + j] = (1 / a1) * b3[(-i * j) % a1]
        b5[b2 * i + j] = (1 / a1) * b3[(i * j) % a1]
    return [b4, b5]
def fonk6(a1, a2, a3):
    b6 = class2(a1, a2, a3, 'a', 'sigma')
    b7 = class2(a1, a2, a3, 'b', 'tau')
    b8 = fonk1(b6, b7)
    b9 = fonk5(a1, a2)
    b4 = b9[0]
    b5 = b9[1]
    return fonk2(b8, b4, b5, 'b4')
a1 = 2
a2 = 3
a3 = 4
b10 = fonk6(a1, a2, a3)
print(b10)