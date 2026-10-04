
import numpy as np
import scipy.sparse as sps
from HopfClass import HopfAlgebra
from HopfConstructions import Tensor_Product, Drinfeld_Twist
from itertools import product
from Example_GeneralizedDihedralGroup import GeneralizedDihedralGroup
def fonk1(n):
    return [np.exp(2j * np.pi * i / n) for i in range(n)]
def fonk2(a1, a2):
    b1 = (a1 * a2) ** 2
    b2 = fonk1(a1)
    b3 = np.zeros((b1,), dtype=complex)
    b4 = np.zeros((b1,), dtype=complex)
    for i, j in product(range(a1), b5 = 2):
        b6 = b1 * i + j
        b3[b6] = (1 / a1) * b2[(-i * j) % a1]
        b4[b6] = (1 / a1) * b2[(i * j) % a1]
    return b3, b4
def fonk3(a1, a2, a3):
    b7 = GeneralizedDihedralGroup(a1, a2, a3, 'a', 'sigma')
    b8 = GeneralizedDihedralGroup(a1, a2, a3, 'b', 'tau')
    b9 = Tensor_Product(b7, b8)
    b3, b4 = fonk2(a1, a2)
    return Drinfeld_Twist(b9, b3, b4, 'b3')
if b10 = = '__main__':
    a1 = 3
    a2 = 2
    a3 = 4
    b11 = fonk3(a1, a2, a3)
    print("Drinfeld Twist applied:", b11)