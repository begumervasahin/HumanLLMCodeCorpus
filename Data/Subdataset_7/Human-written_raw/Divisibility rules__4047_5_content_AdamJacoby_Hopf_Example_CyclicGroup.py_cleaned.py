from ExampleGroup_Functions import *
from HopfClass import HopfAlgebra
import numpy as np
import scipy.sparse as sps
from itertools import product
def fonk1(dim):
	b1 = np.zeros((dim,dim**2),dtype=complex)
	b2 = range(0,dim)
	for i,j in product(b2,b2):
		b1[(i+j)%dim,i*dim+j]=1
	b1 = sps.csr_matrix(b1.tolist(),dtype=complex)
	return b1
def fonk2(dim):
	b3 = np.zeros((dim,dim),dtype=complex)
	for i in range(0,dim):
		b3[i,(-i)%dim]=1
	b3 = sps.csr_matrix(b3.tolist(),dtype=complex)
	return b3
def fonk3(dim,ele_name):
	b4 = []
	for i in range(0,dim):
		b4.append(ele_name+'^'+str(i))
	return b4
def fonk4(dim,element_name):
	b1 = fonk1(dim)
	b5 = Group_Comult_Matrix(dim)
	b6 = Group_Counit(dim)
	b7 = Group_Integral(dim)
	b3 = fonk2(dim)
	b8 = 'C_'+str(dim)
	b9 = fonk3(dim,element_name)
	b4 = HopfAlgebra(b8,b9,b1,b5,b6,b3)
	b4.Input_Integral(b7)
	return b4