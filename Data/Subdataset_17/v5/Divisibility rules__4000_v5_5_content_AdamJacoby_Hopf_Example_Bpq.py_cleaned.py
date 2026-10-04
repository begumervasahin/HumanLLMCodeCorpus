import numpy as np
import scipy.sparse as sps
from HopfClass import HopfAlgebra
from HopfConstructions import Tensor_Product, Drinfeld_Twist
from itertools import product
from Example_GeneralizedDihedralGroup import GeneralizedDihedralGroup
def compute_roots_of_unity(n):
    return [np.exp(2j * np.pi * i / n) for i in range(n)]
def compute_bpq_twist_matrices(p, q):
    dimension = (p * q) ** 2
    roots = compute_roots_of_unity(p)
    J = np.zeros(dimension, dtype=complex)
    JI = np.zeros(dimension, dtype=complex)
    for i, j in product(range(p), repeat=2):
        index = dimension * i + j
        J[index] = (1 / p) * roots[(-i * j) % p]
        JI[index] = (1 / p) * roots[(i * j) % p]
    return J, JI
def apply_bpq_twist(p, q, r):
    group1 = GeneralizedDihedralGroup(p, q, r, 'a', 'sigma')
    group2 = GeneralizedDihedralGroup(p, q, r, 'b', 'tau')
    tensor_product = Tensor_Product(group1, group2)
    J, JI = compute_bpq_twist_matrices(p, q)
    return Drinfeld_Twist(tensor_product, J, JI, 'J')
if __name__ == '__main__':
    p = 3
    q = 2
    r = 4
    twisted_group = apply_bpq_twist(p, q, r)
    print("Drinfeld Twist applied:", twisted_group)