from HopfClass import *
import numpy as np
from itertools import product
import scipy.sparse as sps
def fonk1(n,g,x):
	b1 = []
	for i in range(0,n):
		for j in range(0,n):
			b1.append(g+'^'+str(j)+x+'^'+str(i))
	return b1
def fonk2(n):
	b2 = [0]*(n+1)
	b2[0]=1
	b2[n]=-1
	b3 = np.roots(b2)
	b1 = np.zeros((n**2,n**4),dtype=complex)
	b4 = range(0,n)
	for i, j, k in product(b4,b4,b4):
		for l in range(0,n-j):
			b1[((i+k)%n)+n*(j+l),i+n*j+(k+n*l)*n**2]=b3[(n-1)-(-j*k)%n]
	b1 = sps.csr_matrix(b1.tolist(),dtype=complex)
	return b1
def fonk3(n,mult):
	b5 = n**2
	b1 = np.zeros((b5**2,b5),dtype=complex)
	b6 = np.zeros(b5)
	b6[1]=1
	b6[n]=1
	b7 = np.zeros(b5)
	b7[0]=1
	b8 = [b7]
	b4 = range(1,n)
	for i in b4:
		b9 = np.kron(b7,b6)
		b7 = mult.dot(b9)
		b8.append(b7)
	b4 = range(0,n)
	for i, j in product(b4,b4):
		for l in range(0,j+1):
			b1[((i+l)%n)+(j-l)*n+(i+n*l)*b5,i+j*n]=b8[j][l+(j-l)*n]
	return b1
def fonk4(n):
	b1 = np.zeros((n),dtype=complex)
	for i in range(0,n):
		b1[i]=1
	return b1
def fonk5(n):
	b5 = n**2
	b2 = [0]*(n+1)
	b4 = range(0,n)
	b2[0]=1
	b1 = np.zeros((b5,b5),dtype=complex)
	b2[n]=-1
	b3 = np.roots(b2)
	for i, j in product(b4,b4):
		b1[((-i)%n)+j*n]=(-1)**j*b3[(i*j)%n]
	b1 = sps.csr_matrix(b1.tolist(),dtype=complex)
	return b1