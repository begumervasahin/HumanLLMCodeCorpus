from ExampleGroup_Functions import *
from HopfClass import HopfAlgebra
import numpy as np
import scipy.sparse as sps
from itertools import product
def GeneralizedDihedralGroup_Mult_Matrix(p,q,r):
	dim = p*q
	mult = np.zeros((dim,dim**2),dtype=complex)
	for i,j in product(range(0,q),range(0,p)):
		for k,l in product(range(0,q),range(0,p)):
			mult[p*((i+r*k)%q)+(k+l)%p,dim*(i*p+j)+p*k+l]=1
	mult = sps.csr_matrix(mult.tolist(),dtype=complex)
	return mult
def GeneralizedDihedralGroup_Antipode(p,q,r):
	dim = p*q
	antipode = np.zeros((dim,dim),dtype=complex)
	for i,j in product(range(0,q),range(0,p)):
		inv=(((r**j)%q)**(q-2))%q
		antipode[((-i*inv)%q)*p+((-j)%p),i*p+j]=1
	antipode = sps.csr_matrix(antipode.tolist(),dtype=complex)
	return antipode
def GeneralizedDihedralGroup_Element_Names(p,q,ele_name_g,ele_name_x):
	out = []
	for i in range(0,q):
		for j in range(0,p):
			out.append(ele_name_g+'^'+str(i)+ele_name_x+'^'+str(j))
	return out
def GeneralizedDihedralGroup(p,q,r,element_name_g,element_name_x):
	dim=p*q
	mult = GeneralizedDihedralGroup_Mult_Matrix(p,q,r)
	comult = Group_Comult_Matrix(dim)
	counit = Group_Counit(dim)
	int = Group_Integral(dim)
	antipode = GeneralizedDihedralGroup_Antipode(p,q,r)
	name = 'B_'+str(p)+','+str(q)+','+str(r)
	element_names = GeneralizedDihedralGroup_Element_Names(p,q,element_name_g,element_name_x)
	out = HopfAlgebra(name,element_names,mult,comult,counit,antipode)
	out.Input_Integral(int)
	return out