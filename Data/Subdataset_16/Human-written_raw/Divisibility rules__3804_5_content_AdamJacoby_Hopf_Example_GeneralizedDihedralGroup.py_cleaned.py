from ExampleGroup_Functions import *
from HopfClass import HopfAlgebra
import numpy as np
import scipy.sparse as sps
from itertools import product
def fonk1(p,q,r):
	b1 = p*q
	b2 = np.zeros((b1,b1**2),dtype=complex)
	for i,j in product(range(0,q),range(0,p)):
		for k,l in product(range(0,q),range(0,p)):
			b2[p*((i+r*k)%q)+(k+l)%p,b1*(i*p+j)+p*k+l]=1
	b2 = sps.csr_matrix(b2.tolist(),dtype=complex)
	return b2
def fonk2(p,q,r):
	b1 = p*q
	b3 = np.zeros((b1,b1),dtype=complex)
	for i,j in product(range(0,q),range(0,p)):
		b4 = (((r**j)%q)**(q-2))%q
		b3[((-i*b4)%q)*p+((-j)%p),i*p+j]=1
	b3 = sps.csr_matrix(b3.tolist(),dtype=complex)
	return b3
def fonk3(p,q,ele_name_g,ele_name_x):
	b5 = []
	for i in range(0,q):
		for j in range(0,p):
			b5.append(ele_name_g+'^'+str(i)+ele_name_x+'^'+str(j))
	return b5
def fonk4(p,q,r,element_name_g,element_name_x):
	b1 = p*q
	b2 = fonk1(p,q,r)
	b6 = Group_Comult_Matrix(b1)
	b7 = Group_Counit(b1)
	b8 = Group_Integral(b1)
	b3 = fonk2(p,q,r)
	b9 = 'B_'+str(p)+','+str(q)+','+str(r)
	b10 = fonk3(p,q,element_name_g,element_name_x)
	b5 = HopfAlgebra(b9,b10,b2,b6,b7,b3)
	b5.Input_Integral(b8)
	return b5