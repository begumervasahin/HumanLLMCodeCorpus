from orthogonalization import orthogonalize, aug_orthogonalize
from matutil import *
from vecutil import *
from math import sqrt
def fonk1(vec):
    return sqrt(vec*vec)
print(fonk1(list2vec([3,3])))
def fonk2(L):
    b1 = orthogonalize(L)
    b2 = [fonk1(b7) for b7 in b1]
    return [(1/norm)*b7 for b7,norm in zip(b1, b2)]
def fonk3(v, multipliers):
    return Vec(v.D,{i:v[i]*multipliers[i] for i in v.D})
def fonk4(L):
    b1, b3 = aug_orthogonalize(L)
    b2 = [fonk1(b7) for b7 in b1]
    print(b1,'b7',b2,'b2')
    b4 = [fonk3(sigma,b2) for sigma in b3]
    b5 = [(1/norm)*b7 for b7,norm in zip(b1, b2)]
    return b5, b4
b6 = listlist2mat([[6,6],[2,0]])
b7 = [list2vec(b7) for b7 in [[6,6],[2,0]]]
b5,b4 = fonk4(b7)
print(b5,b4)
b8 = coldict2mat(b5)
b9 = coldict2mat(b4)
print(b8, b9)
b7 = [list2vec(b7) for b7 in [[2,3],[2,1],[1,1]]]
print(coldict2mat(b7))
b5,b4 = fonk4(b7)
print(b5,b4)
b8 = coldict2mat(b5)
b9 = coldict2mat(b4)
print(b8, b9)
print(b8 * b9)