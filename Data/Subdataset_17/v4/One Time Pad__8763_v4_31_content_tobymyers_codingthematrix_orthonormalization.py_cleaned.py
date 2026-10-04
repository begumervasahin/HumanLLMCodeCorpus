from orthogonalization import orthogonalize, aug_orthogonalize
from matutil import listlist2mat, coldict2mat
from vecutil import list2vec
from math import sqrt
from vec import Vec
def find_norm(vec):
    return sqrt(vec * vec)
def orthonormalize(L):
    Lstar = orthogonalize(L)
    norms = [find_norm(l) for l in Lstar]
    return [(1 / norm) * l for l, norm in zip(Lstar, norms)]
def adjust(v, multipliers):
    return Vec(v.D, {i: v[i] * multipliers[i] for i in v.D})
def aug_orthonormalize(L):
    Lstar, sigmadict = aug_orthogonalize(L)
    norms = [find_norm(l) for l in Lstar]
    R = [adjust(sigma, norms) for sigma in sigmadict]
    Q = [(1 / norm) * l for l, norm in zip(Lstar, norms)]
    return Q, R
if __name__ == "__main__":
    m = listlist2mat([[6, 6], [2, 0]])
    l = [list2vec(l) for l in [[6, 6], [2, 0]]]
    Q, R = aug_orthonormalize(l)
    print("Q:", Q)
    print("R:", R)
    Q_mat = coldict2mat(Q)
    R_mat = coldict2mat(R)
    print("Q_mat:", Q_mat)
    print("R_mat:", R_mat)
    l = [list2vec(l) for l in [[2, 3], [2, 1], [1, 1]]]
    print("Original matrix:", coldict2mat(l))
    Q, R = aug_orthonormalize(l)
    print("Q:", Q)
    print("R:", R)
    Q_mat = coldict2mat(Q)
    R_mat = coldict2mat(R)
    print("Q_mat:", Q_mat)
    print("R_mat:", R_mat)
    print("Reconstructed matrix:", Q_mat * R_mat)