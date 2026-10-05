import numpy as np
from itertools import combinations
from math import acos, sqrt, pi, cos, sin
def compute_projection(A):
    interim = np.matmul(A.transpose(), A)
    return interim.flatten()
def decompose_vector(q, d):
    xxT = np.outer(q, q)
    xxT = _get_closest_symmetric_matrix(xxT)
    x = -xxT[:, d - 1]
    return x
def compose_vector(x):
    interim = np.outer(x, x)
    return interim.flatten()
def cartesian_to_spherical(x):
    d = len(x)
    phi = np.zeros((d - 1))
    sum_squares = pow(x[-1], 2) + pow(x[-2], 2)
    last_angle = acos(x[-2] / sqrt(sum_squares))
    phi[-1] = last_angle if x[-1] >= 0 else 2 * pi - last_angle
    for k in range(d - 3, -1, -1):
        sum_squares += pow(x[k], 2)
        phi[k] = acos(x[k] / sqrt(sum_squares))
    return phi
def spherical_to_cartesian(phi):
    dim = len(phi)
    x = np.zeros(dim + 1)
    sins = 1
    for i in range(dim):
        x[i] = sins * cos(phi[i])
        sins *= sin(phi[i])
    x[-1] = sins
    return x
def compute_alt_projection(A, j):
    d = len(A[0])
    p = np.array([])
    p_1 = np.multiply(A, A).reshape(1, -1)
    p = np.append(p, p_1)
    index = range(d + 1)
    comb = list(combinations(index, 2))
    for i in range(d - j):
        p_2 = 2 * np.multiply(A[i, [x[0] for x in comb]], A[i, [x[1] for x in comb]])
        p = np.append(p, p_2)
    return p
def decompose_alt_vector(q, d, j):
    x_ = np.sqrt(np.abs(q[:d]))
    signs = q[d * (d - j):d * (d - j) + d - 1]
    x = np.zeros(d)
    x[0] = np.absolute(x_[0])
    for i in range(1, len(x_)):
        x[i] = -np.absolute(x_[i]) if signs[i - 1] < 0 else np.absolute(x_[i])
    return x
def _get_closest_symmetric_matrix(A):
    return (A + A.T) / 2
if __name__ == "__main__":
    A = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
    p_comp_result = compute_projection(A)
    print("Projection result:")
    print(p_comp_result)
    q = np.array([1, 2, 3])
    dimension = 3
    q_decomp_result = decompose_vector(q, dimension)
    print("\nDecomposition result:")
    print(q_decomp_result)
    q_comp_result = compose_vector(q_decomp_result)
    print("\nComposition result:")
    print(q_comp_result)
    x = np.array([1, 2, 3])
    spherical_result = cartesian_to_spherical(x)
    print("\nSpherical coordinates:")
    print(spherical_result)
    cartesian_result = spherical_to_cartesian(spherical_result)
    print("\nCartesian coordinates:")
    print(cartesian_result)
    p_comp_alt_result = compute_alt_projection(A, 1)
    print("\nAlternative projection result:")
    print(p_comp_alt_result)
    q_decomp_alt_result = decompose_alt_vector(q_comp_result, dimension, 1)
    print("\nAlternative decomposition result:")
    print(q_decomp_alt_result)