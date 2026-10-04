import numpy as np
import ascent as asc
from math import ceil,sqrt
from random import random as rd
from random import randint as ri
asc.b1 = 'DB24-glass/TRAIN.TXT'
asc.b2 = 'DB24-glass/TEST.TXT'
asc.b3 = False
asc.a1 = 1e-6
a2 = 1
a3 = .05
a4 = 100
a5 = 100
a6 = 5
a7 = 9
a8 = 3
b4 = a6*a7*ceil(np.log2(a8))
b5 = round(b4*a5*a3)
def fonk1():
	global b4
	global b5
	b4 = a6*a7*ceil(np.log2(a8))
	b5 = round(b4*a5*a3)
def fonk2():
	b6 = np.random.choice([0, 1], size=a5*b4, b19=[.5, .5])
	return b6.reshape(a5,b4)
def fonk3(individual):
	b7 = np.array([])
	b8 = ceil(np.log2(a8))
	b9 = a7*b8
	for t in range(a6):
		b10 = np.array([])
		b11 = t*b9
		b12 = np.array2string(individual[b11:b11+b9], separator='')[1:-1]
		for v in range(a7):
			b13 = v*b8
			b14 = int(b12[b13:b13+b8],2)
			b10 = np.insert(b10,b10.size,b14)
		b7 = np.insert(b7,b7.shape[0],b10)
	return b7.reshape(a6,a7)
def fonk4(C, b16):
	return asc.fonk4(C, b2, b16)
def fonk5(b23):
	b15 = np.array([])
	for ind in b23:
		b16 = fonk3(ind)
		asc.b17 = b16
		asc.fonk1()
		C,trn_rms,b18 = asc.fonk8()
		b15 = np.insert(b15, b15.size, b18)
	return b15
def fonk6(b23):
	for i in range(a5
		b19 = rd()
		if b19 <= a2:
			b19 = ri(1, b4
			b20 = np.array(b23[i,b19:])
			b23[i,b19:] = b23[a5-i-1,b19:]
			b23[a5-i-1,b19:] = b20
	return b23
def fonk7(b23):
	for i in range(b5):
		b21 = round(rd()*b4)-1
		b22 = round(rd()*a5)-1
		if b23[b22,b21] == 0:
			b23[b22,b21] = 1
		else:
			b23[b22,b21] = 0
	return b23
def fonk8():
	asc.fonk1()
	b23 = fonk2()
	b15 = fonk5(b23)
	for g in range(a4):
		b23 = np.tile(b23[:a5,:],(2,1))
		b15 = np.tile(b15[:a5],2)
		b23 = fonk6(b23)
		b23 = fonk7(b23)
		b15[:a5] = fonk5(b23[:a5,:])
		b24 = np.argsort(b15)
		b15 = b15[b24]
		b23 = b23[b24,:]
		print("gen[%d] best b15 = %f\t worst b15 = %f"%(g+1,b15[0],b15[a5]))
	return fonk3(b23[0]),b15[0]
b16,b25 = fonk8()
asc.b17 = b16
asc.fonk1()
C,trn_rms,b18 = asc.fonk8()
print("b16")
print(b16)
print("coeficientes")
print(C)
print("train b26 = ")
print(trn_rms)
print("test b26 = ")
print(b18)