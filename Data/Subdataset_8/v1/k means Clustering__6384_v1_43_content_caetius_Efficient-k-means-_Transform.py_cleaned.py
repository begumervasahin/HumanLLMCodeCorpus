import numpy as np
from itertools import combinations
from math import acos, sqrt, pow, pi, cos, sin
'''Projections along dimensions: (d+1)->(d+1)^2 and back'''
def pComp(A):
    interim = np.matmul(A.transpose(), A)
    return np.reshape(interim, -1)
def qDecomp(q, d):
    xxT = np.outer(q, q)
    xxT = getClosestSymMatrix(xxT)
    x = -xxT[:, d - 1]
    return x
def qComp(x):
    interim = np.outer(x, x)
    return np.reshape(interim, -1)
'''Cartesian -> Spherical'''
def cartesianToSpherical(x):
    d = len(x)
    phi = np.zeros((d-1))
    d_ = len(phi)
    sum_squares = pow(x[d_], 2) + pow(x[d_-1], 2)
    last_angle = acos(x[d_-1] / sqrt(sum_squares))
    if x[d_] >= 0:
        phi[d_-1] = last_angle
    else:
        phi[d_-1] = 2 * pi - last_angle
    for k in range(d_-2, -1, -1):
        sum_squares = sum_squares + pow(x[k], 2)
        phi[k] = acos(x[k] / sqrt(sum_squares))
    return phi
'''Spherical -> Cartesian'''
def sphericalToCartesian(phi):
    dim = len(phi)
    x = np.zeros(dim + 1)
    sins = 1
    for i in range(0, dim):
        x[i] = sins * cos(phi[i])
        sins *= sin(phi[i])
    x[dim] = sins
    return x
'''Alternative Code: Appendix method'''
'''P-Q: Appendix Version'''
def pCompAlt(A, j):
    d = len(A[0, :])
    p = np.array([])
    p_1 = np.reshape(np.multiply(A, A), (1, A.shape[0] * A.shape[1]))
    p = np.append(p, p_1)
    index = range(d + 1)
    comb = list(combinations(index, 2))
    for i in range(d - j):
        p_2 = 2 * np.multiply(A[i, [x[0] for x in comb]], A[i, [x[1] for x in comb]])
        p = np.append(p, p_2)
    return p
def qDecompAlt(q, d, j):
    x_ = np.sqrt(np.abs(q[0:d]))
    signs = q[d * (d - j):d * (d - j) + d - 1]
    x = np.zeros(d)
    x[0] = np.absolute(x_[0])
    for i in range(1, len(x_)):
        if signs[i - 1] < 0:
            x[i] = -np.absolute(x_[i])
        else:
            x[i] = np.absolute(x_[i])
    return x
def getClosestSymMatrix(A):
    return (A + A.T) / 2
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
p_comp_result = pComp(A)
print("pComp result:")
print(p_comp_result)
q = np.array([1, 2, 3])
dimension = 3
q_decomp_result = qDecomp(q, dimension)
print("\nqDecomp result:")
print(q_decomp_result)
q_comp_result = qComp(q_decomp_result)
print("\nqComp result:")
print(q_comp_result)
x = np.array([1, 2, 3])
spherical_result = cartesianToSpherical(x)
print("\nSpherical coordinates:")
print(spherical_result)
cartesian_result = sphericalToCartesian(spherical_result)
print("\nCartesian coordinates:")
print(cartesian_result)
p_comp_alt_result = pCompAlt(A, 1)
print("\npCompAlt result:")
print(p_comp_alt_result)
q_decomp_alt_result = qDecompAlt(q_comp_result, dimension, 1)
print("\nqDecompAlt result:")
print(q_decomp_alt_result)