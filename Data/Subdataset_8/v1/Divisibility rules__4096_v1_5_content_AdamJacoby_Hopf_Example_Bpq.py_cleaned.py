import numpy as np
import scipy.sparse as sps
from itertools import product
class HopfAlgebra:
    pass
def Tensor_Product(G1, G2):
    pass
def Drinfeld_Twist(G, J, JI, name):
    pass
class GeneralizedDihedralGroup:
    def __init__(self, p, q, r, a, sigma):
        pass
def Roots_Of_Unity(n):
    out = []
    for i in range(n):
        out.append(np.exp(i * 2j * np.pi / n))
    return out
def Bpq_Twist(p, q):
    dim = (p * q) ** 2
    omega = Roots_Of_Unity(p)
    J = np.zeros((dim ** 2), dtype=complex)
    JI = np.zeros((dim ** 2), dtype=complex)
    for i, j in product(range(p), range(p)):
        J[dim * i + j] = (1 / p) * omega[(-i * j) % p]
        JI[dim * i + j] = (1 / p) * omega[(i * j) % p]
    return [J, JI]
def Bpq(p, q, r):
    G1 = GeneralizedDihedralGroup(p, q, r, 'a', 'sigma')
    G2 = GeneralizedDihedralGroup(p, q, r, 'b', 'tau')
    G = Tensor_Product(G1, G2)
    temp = Bpq_Twist(p, q)
    J = temp[0]
    JI = temp[1]
    return Drinfeld_Twist(G, J, JI, 'J')
p = 2
q = 3
r = 4
result = Bpq(p, q, r)
print(result)