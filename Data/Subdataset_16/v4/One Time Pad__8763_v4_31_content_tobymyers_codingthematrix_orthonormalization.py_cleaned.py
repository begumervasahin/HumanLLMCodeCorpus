from orthogonalization import orthogonalize, aug_orthogonalize
from matutil import listlist2mat, coldict2mat
from vecutil import list2vec
from math import sqrt
from vec import Vec
def fonk1(vec):
    return sqrt(vec * vec)
def fonk2(L):
    b1 = orthogonalize(L)
    b2 = [fonk1(b8) for b8 in b1]
    return [(1 / norm) * b8 for b8, norm in zip(b1, b2)]
def fonk3(v, multipliers):
    return Vec(v.D, {i: v[i] * multipliers[i] for i in v.D})
def fonk4(L):
    b1, b3 = aug_orthogonalize(L)
    b2 = [fonk1(b8) for b8 in b1]
    b4 = [fonk3(sigma, b2) for sigma in b3]
    b5 = [(1 / norm) * b8 for b8, norm in zip(b1, b2)]
    return b5, b4
if b6 = = "__main__":
    b7 = listlist2mat([[6, 6], [2, 0]])
    b8 = [list2vec(b8) for b8 in [[6, 6], [2, 0]]]
    b5, b4 = fonk4(b8)
    print("b5:", b5)
    print("b4:", b4)
    b9 = coldict2mat(b5)
    b10 = coldict2mat(b4)
    print("b9:", b9)
    print("b10:", b10)
    b8 = [list2vec(b8) for b8 in [[2, 3], [2, 1], [1, 1]]]
    print("Original matrix:", coldict2mat(b8))
    b5, b4 = fonk4(b8)
    print("b5:", b5)
    print("b4:", b4)
    b9 = coldict2mat(b5)
    b10 = coldict2mat(b4)
    print("b9:", b9)
    print("b10:", b10)
    print("Reconstructed matrix:", b9 * b10)