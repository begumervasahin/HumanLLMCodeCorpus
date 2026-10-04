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
    R = [adjust(sigma, {i: norms[i] for i in range(len(norms))}) for sigma in sigmadict]
    Q = [(1 / norm) * l for l, norm in zip(Lstar, norms)]
    return Q, R
if __name__ == "__main__":
    l = [list2vec(vec) for vec in [[6, 6], [2, 0]]]
    Q, R = aug_orthonormalize(l)
    print("Q:", Q)
    print("R:", R)
    Q_mat = coldict2mat(Q)
    R_mat = coldict2mat(R)
    print("Q_mat:\n", Q_mat)
    print("R_mat:\n", R_mat)
    l = [list2vec(vec) for vec in [[2, 3], [2, 1], [1, 1]]]
    print("Original matrix:\n", coldict2mat(l))
    Q, R = aug_orthonormalize(l)
    print("Q:", Q)
    print("R:", R)
    Q_mat = coldict2mat(Q)
    R_mat = coldict2mat(R)
    print("Q_mat:\n", Q_mat)
    print("R_mat:\n", R_mat)
    print("Reconstructed matrix:\n", Q_mat * R_mat)