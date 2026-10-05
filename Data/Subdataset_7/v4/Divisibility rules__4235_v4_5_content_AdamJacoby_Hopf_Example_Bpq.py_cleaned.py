import numpy as np
import scipy.sparse as sps
from itertools import product
from HopfClass import HopfAlgebra
from HopfConstructions import Tensor_Product, Drinfeld_Twist
from Example_GeneralizedDihedralGroup import GeneralizedDihedralGroup
def fonk1(n):
    b1 = []
    for i in range(n):
        b1.append(np.exp(i * 2j * np.pi / n))
    return b1
def fonk2(p, q):
    b2 = (p * q) ** 2
    b3 = fonk1(p)
    b4 = np.zeros((b2 ** 2), dtype=complex)
    b5 = np.zeros((b2 ** 2), dtype=complex)
    for i, j in product(range(p), range(p)):
        b4[b2 * i + j] = (1 / p) * b3[(-i * j) % p]
        b5[b2 * i + j] = (1 / p) * b3[(i * j) % p]
    return b4, b5
def fonk3(p, q, r):
    b6 = GeneralizedDihedralGroup(p, q, r, 'a', 'sigma')
    b7 = GeneralizedDihedralGroup(p, q, r, 'b', 'tau')
    b8 = Tensor_Product(b6, b7)
    b4, b5 = fonk2(p, q)
    return Drinfeld_Twist(b8, b4, b5, 'b4')