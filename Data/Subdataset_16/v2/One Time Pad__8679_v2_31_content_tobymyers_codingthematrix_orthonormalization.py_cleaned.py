from orthogonalization import orthogonalize, aug_orthogonalize
from matutil import *
from vecutil import *
from math import sqrt
def fonk1(vec):
    return sqrt(vec * vec)
def fonk2(vectors):
    b1 = orthogonalize(vectors)
    b2 = [fonk1(vec) for vec in b1]
    return [(1 / norm) * vec for vec, norm in zip(b1, b2)]
def fonk3(vector, multipliers):
    return Vec(vector.D, {i: vector[i] * multipliers[i] for i in vector.D})
def fonk4(vectors):
    b1, b3 = aug_orthogonalize(vectors)
    b2 = [fonk1(vec) for vec in b1]
    b4 = [fonk3(sigma, b2) for sigma in b3]
    b5 = [(1 / norm) * vec for vec, norm in zip(b1, b2)]
    return b5, b4
if b6 = = "__main__":
    b7 = [list2vec(l) for l in [[6, 6], [2, 0]]]
    Q1, b8 = fonk4(b7)
    b9 = coldict2mat(Q1)
    b10 = coldict2mat(b8)
    print("Orthonormalized Vectors (b5):")
    print(b9)
    print("Adjustment Matrix (b4):")
    print(b10)
    print("Product of b5 and b4:")
    print(b9 * b10)
    b11 = [list2vec(l) for l in [[2, 3], [2, 1], [1, 1]]]
    Q2, b12 = fonk4(b11)
    b13 = coldict2mat(Q2)
    b14 = coldict2mat(b12)
    print("Original Vectors:")
    print(coldict2mat(b11))
    print("Orthonormalized Vectors (b5):")
    print(b13)
    print("Adjustment Matrix (b4):")
    print(b14)
    print("Product of b5 and b4:")
    print(b13 * b14)