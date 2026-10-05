import numpy as np
from scipy.sparse import csr_matrix
from itertools import product
from HopfClass import Algebra
def fonk1(n):
    b1 = []
    for i in range(0,n):
        for j in range(0,n):
            b1.append('T_'+str(i)+','+str(j))
    return b1
def fonk2(n):
    b2 = n**2
    b3 = np.zeros((b2,b2**2))
    for i,j,k in product(range(0,n),range(0,n),range(0,n)):
        b3[i*n+k,b2*(i*n+j)+n*j+k]=1
    return csr_matrix(b3.tolist())
def fonk3(n):
    b2 = n**2
    b4 = np.zeros((b2**2))
    for i,j in product(range(0,n),range(0,n)):
        b4[b2*(n*i+j)+n*j+i]=n
    return b4
def fonk4(n):
    b5 = Algebra('M_'+str(n),fonk1(n),fonk2(n))
    b5.Input_Casimir(fonk3(n))
    return b5