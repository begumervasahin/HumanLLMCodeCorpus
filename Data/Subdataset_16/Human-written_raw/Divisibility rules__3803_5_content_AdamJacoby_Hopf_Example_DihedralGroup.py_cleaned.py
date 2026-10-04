from ExampleGroup_Functions import *
from HopfClass import HopfAlgebra
import numpy as np
import scipy.sparse as sps
from itertools import product
def fonk1(n):
	b1 = 2*n
	b2 = np.zeros((b1,b1**2),dtype=complex)
	b3 = range(0,n)
	for i,j in product(b3,[0,1]):
		for k,l in product(b3,[0,1]):
			b2[2*((i+((-1)**j)*k)%n)+(j+l)%2,b1*(i*2+j)+2*k+l]=1
	b2 = sps.csr_matrix(b2.tolist(),dtype=complex)
	return b2
def fonk2(n):
	b1 = 2*n
	b4 = np.zeros((b1,b1),dtype=complex)
	for i,j in product(range(0,n),[0,1]):
		b4[2*(((-1)**(j+1)*i)%n)+j,i*2+j]=1
	b4 = sps.csr_matrix(b4.tolist(),dtype=complex)
	return b4
def fonk3(n,ele_name_g,ele_name_x):
	b5 = []
	for i in range(0,n):
		for j in [0,1]:
			b5.append(ele_name_g+'^'+str(i)+ele_name_x+'^'+str(j))
	return b5
def fonk4(n,element_name_g,element_name_x):
	b1 = 2*n
	b2 = fonk1(n)
	b6 = Group_Comult_Matrix(b1)
	b7 = Group_Counit(b1)
	b8 = Group_Integral(b1)
	b4 = fonk2(n)
	b9 = 'D_'+str(n)
	b10 = fonk3(n,element_name_g,element_name_x)
	b5 = HopfAlgebra(b9,b10,b2,b6,b7,b4)
	b5.Input_Integral(b8)
	return b5