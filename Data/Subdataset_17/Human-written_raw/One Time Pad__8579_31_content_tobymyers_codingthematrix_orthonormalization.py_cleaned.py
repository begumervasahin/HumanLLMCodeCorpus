from orthogonalization import orthogonalize, aug_orthogonalize
from matutil import *
from vecutil import *
from math import sqrt
def find_norm(vec):
    return sqrt(vec*vec)
print(find_norm(list2vec([3,3])))
def orthonormalize(L):
    Lstar = orthogonalize(L)
    norms = [find_norm(l) for l in Lstar]
    return [(1/norm)*l for l,norm in zip(Lstar, norms)]
def adjust(v, multipliers):
    return Vec(v.D,{i:v[i]*multipliers[i] for i in v.D})
def aug_orthonormalize(L):
    Lstar, sigmadict = aug_orthogonalize(L)
    norms = [find_norm(l) for l in Lstar]
    print(Lstar,'l',norms,'norms')
    R = [adjust(sigma,norms) for sigma in sigmadict]
    Q = [(1/norm)*l for l,norm in zip(Lstar, norms)]
    return Q, R
m = listlist2mat([[6,6],[2,0]])
l = [list2vec(l) for l in [[6,6],[2,0]]]
Q,R = aug_orthonormalize(l)
print(Q,R)
Q_mat = coldict2mat(Q)
R_mat = coldict2mat(R)
print(Q_mat, R_mat)
l = [list2vec(l) for l in [[2,3],[2,1],[1,1]]]
print(coldict2mat(l))
Q,R = aug_orthonormalize(l)
print(Q,R)
Q_mat = coldict2mat(Q)
R_mat = coldict2mat(R)
print(Q_mat, R_mat)
print(Q_mat * R_mat)