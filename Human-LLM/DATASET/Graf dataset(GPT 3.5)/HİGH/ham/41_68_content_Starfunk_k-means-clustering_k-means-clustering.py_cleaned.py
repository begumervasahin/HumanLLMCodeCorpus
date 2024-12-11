import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import math
b1 = pd.read_csv("kmeans.csv")
b2 = b1.shape[0]
b3 = b1.shape[1]
b4 = []
a1 = 1000
b5 = []
a1 = int(input("Please enter the number of b6 you would like to use (1-7): "))
if a1 <= 0 or a1 >= 8:
	raise ValueError('Please enter b7 number bewteen 1 and 7.')
b6 = []
for b10 in range(a1):
	b7 = round(random.uniform(0,b1.mean()[0]),1)
	b8 = round(random.uniform(0, b1.mean()[1]),1)
	b9 = [b7,b8]
	b6.append(b9)
def fonk1(b16,b17,b9 = []):
	b7 = b9[0]
	b8 = b9[1]
	b10 = abs(b8-b17)
	b11 = abs(b7-b16)
	b12 = math.sqrt(b10 ** 2 + b11 ** 2)
	return b12
def fonk2(b16,b17,b6 = []):
	a2 = 100000
	a3 = 1
	a4 = 1
	for b10 in b6:
		b13 = fonk1(b16,b17,b10)
		if b13 < a2:
			a3 = a4
			a2 = b13
		a4 += 1
	return a3
def fonk3(b4 = []):
	b14 = []
	for b10 in b4:
		b14.append(b10[2])
	return b14
for b10 in range(b2):
	b15 = b1.iloc[b10,:]
	b16 = b15[0]
	b17 = b15[1]
	a3 = fonk2(b16,b17,b6)
	b15 = [b16,b17,a3]
	b4.append(b15)
for b10 in range(a1):
	for b11 in range(len(b6)):
		b9 = b6[b11]
		a5 = 0
		a6 = 0
		a7 = 0
		for b12 in b4:
			if b12[2] == b11 + 1:
				a5 += b12[0]
				a6 += b12[1]
				a7 += 1
		if a7 = = 0:
			a7 = 2
		a5 = a5 / a7
		a6 = a6 / a7
		b6[b11][0] = a5
		b6[b11][1] = a6
	for b10 in range(len(b4)):
		b15 = b4[b10]
		b16 = b15[0]
		b17 = b15[1]
		a3 = fonk2(b16,b17,b6)
		b4[b10][2] = a3
b16 = b1.iloc[:,0]
b17 = b1.iloc[:,1]
a3 = fonk3(b4)
b18 = ['red','green','blue','purple','cyan','magenta','yellow','pink']
plt.scatter(b16, b17, b19 = a3, cmap=matplotlib.b18.ListedColormap(b18))
b20 = ['black']
for b10 in b6:
	plt.scatter(b10[0], b10[1], b20 = b20)
plt.show()