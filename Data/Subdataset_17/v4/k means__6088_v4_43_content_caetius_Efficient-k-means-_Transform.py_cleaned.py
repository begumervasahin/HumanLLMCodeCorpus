import numpy as np
from itertools import combinations
from math import acos, sqrt, pow, pi, cos, sin
import Matrix
def pComp(A):
    interim = np.matmul(A.transpose(), A)
    return np.reshape(interim, -1)
def qDecomp(q, d):
    xxT = Matrix.getClosestSymMatrix(np.reshape(q, (d, d)))
    x = -xxT[d - 1]
    return x
def qComp(x):
    interim = np.outer(x, x)
    return np.reshape(interim, -1)
def cartesianToSpherical(x):
    d = len(x)
    phi = np.zeros(d - 1)
    sum_squares = pow(x[d - 1], 2) + pow(x[d - 2], 2)
    last_angle = acos(x[d - 2] / sqrt(sum_squares))
    if x[d - 1] >= 0:
        phi[d - 2] = last_angle
    else:
        phi[d - 2] = 2 * pi - last_angle
    for k in range(d - 3, -1, -1):
        sum_squares += pow(x[k], 2)
        phi[k] = acos(x[k] / sqrt(sum_squares))
    return phi
def sphericalToCartesian(phi):
    dim = len(phi)
    x = np.zeros(dim + 1)
    sins = 1
    for i in range(dim):
        x[i] = sins * cos(phi[i])
        sins *= sin(phi[i])
    x[dim] = sins
    return x
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
    x_ = np.sqrt(np.abs(q[:d]))
    signs = q[d * (d - j):d * (d - j) + d - 1]
    x = np.zeros(d)
    x[0] = np.abs(x_[0])
    for i in range(1, len(x_)):
        x[i] = -np.abs(x_[i]) if signs[i - 1] < 0 else np.abs(x_[i])
    return x