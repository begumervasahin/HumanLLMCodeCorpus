import numpy as np
import scipy.sparse as sps
from HopfClass import HopfAlgebra
from HopfConstructions import Tensor_Product, Drinfeld_Twist
from itertools import product
from Example_GeneralizedDihedralGroup import GeneralizedDihedralGroup
def roots_of_unity(n):
    return [np.exp(2j * np.pi * i / n) for i in range(n)]
def bpq_twist(p, q):
    dim = (p * q) ** 2
    omega = roots_of_unity(p)
    J = np.zeros((dim, ), dtype=complex)
    JI = np.zeros((dim, ), dtype=complex)
    for i, j in product(range(p), repeat=2):
        J[dim * i + j] = (1 / p) * omega[(-i * j) % p]
        JI[dim * i + j] = (1 / p) * omega[(i * j) % p]
    return [J, JI]
def bpq(p, q, r):
    G1 = GeneralizedDihedralGroup(p, q, r, 'a', 'sigma')
    G2 = GeneralizedDihedralGroup(p, q, r, 'b', 'tau')
    G = Tensor_Product(G1, G2)
    J, JI = bpq_twist(p, q)
    return Drinfeld_Twist(G, J, JI, 'J')
if __name__ == '__main__':
    p = 3
    q = 2
    r = 4
    twisted_group = bpq(p, q, r)
    print("Drinfeld Twist applied:", twisted_group)