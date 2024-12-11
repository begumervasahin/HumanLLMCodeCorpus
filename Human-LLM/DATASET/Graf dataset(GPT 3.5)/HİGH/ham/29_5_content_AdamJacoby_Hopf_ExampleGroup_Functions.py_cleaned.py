import numpy as np
from scipy.sparse import csr_matrix
from itertools import product
from HopfClass import HopfAlgebra
import sympy.combinatorics as comb
def fonk1(b4):
	b1 = np.zeros((b4),b3=complex)
	for i in range(0,b4):
		b1[i]=1
	return b1
def fonk2(b4):
	b1 = np.zeros((b4),b3=complex)
	for i in range(0,b4):
		b1[i]=1
	return b1
def fonk3(b4):
	b2 = np.zeros((b4**2,b4),b3=complex)
	for i in range(0,b4):
		b2[i+b4*i,i]=1
	return csr_matrix(b2.tolist(),b3 = complex)
def fonk4(name,b9,b10,b12):
    b4 = len(b9)
    b5 = HopfAlgebra(name,b9,b10,fonk3(b4),fonk2(b4),b12)
    b5.Input_Integral(fonk1(b4))
    return b5
def fonk5(P):
    b6 = list(P.elements)
    b4 = len(b6)
    b7 = max(list(b6[0]))
    b8 = comb.Permutation(b7)
    b6.remove(b8)
    b6.insert(0,b8)
    b9 = []
    for Element in b6:
        b9.append(str(list(Element)).replace(" ",""))
    b10 = np.zeros((b4,b4**2))
    for i, b14 in product(range(0,b4),range(0,b4)):
        b11 = b6.index(b6[i]*b6[b14])
        b10[b11,i*b4+b14]=1
    b10 = csr_matrix(b10.tolist(),b3=np.int8)
    b12 = np.zeros((b4,b4))
    for i in range(0,b4):
        b13 = b6[i]**-1
        b14 = b6.index(b13)
        b12[b14,i]=1
    b12 = csr_matrix(b12.tolist(),b3=np.int8)
    return {'element_names':b9,'b10':b10,'b12':b12}