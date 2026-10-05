import numpy as np
from itertools import product
from HopfClass import HopfAlgebra
from HopfConstructions import Tensor_Product, Drinfeld_Twist
from Example_GeneralizedDihedralGroup import GeneralizedDihedralGroup
def calculate_roots_of_unity(n):
    roots = []
    for i in range(n):
        roots.append(np.exp(i * 2j * np.pi / n))
    return roots
def compute_Bpq_twist(p, q):
    dim = (p * q) ** 2
    omega = calculate_roots_of_unity(p)
    J = np.zeros((dim ** 2), dtype=complex)
    JI = np.zeros((dim ** 2), dtype=complex)
    for i, j in product(range(p), range(p)):
        J[dim * i + j] = (1 / p) * omega[(-i * j) % p]
        JI[dim * i + j] = (1 / p) * omega[(i * j) % p]
    return J, JI
def compute_Bpq(p, q, r):
    G1 = GeneralizedDihedralGroup(p, q, r, 'a', 'sigma')
    G2 = GeneralizedDihedralGroup(p, q, r, 'b', 'tau')
    G = Tensor_Product(G1, G2)
    J, JI = compute_Bpq_twist(p, q)
    return Drinfeld_Twist(G, J, JI, 'J')