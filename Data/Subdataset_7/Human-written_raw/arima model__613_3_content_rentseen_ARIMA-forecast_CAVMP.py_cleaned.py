from __future__ import print_function
import pandas as pd
import numpy as np
from scipy import  stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot
from matplotlib.pylab import rcParams
from statsmodels.tsa.arima_model import ARIMA
import random
import math
from operator import attrgetter
import time
b1 = time.time()
a1 = 15
a2 = 20
a3 = 150
a4 = 0.06111
a5 = 20
a6 = 0.6
a7 = 16
a8 = 3
a9 = 1
b2 = open("CAVMP_result_4_4_8.txt","w")
def fonk1(b37):
	b3 = a8
	b4 = a9
	b5 = np.log(b37)
	b6 = [-1]
	b7 = False
	for b29 in range(b3,-1,-1):
		if(b7):
			break
		for j in range(b4,-1,-1):
			try:
				b8 = ARIMA(b5, b19=(b29, 0, j))
				b9 = b8.fit(disp=-1)
				b6 = b9.fonk10(len(b37), len(b37), dynamic=True)
				b6 = np.exp(b6)
				if(math.isnan(b6[0])):
					continue
				b7 = True
				break
			except:
				continue
	if(b6[0]==-1):
		print('bingo')
	return b6[0]+0.008
def fonk2():
	b10 = []
	b11 = random.randrange(0,6)
	for t in range(a5):
		b12 = (math.sin(b11+t)+1+a6*random.random())*a4
		b10.append(b12)
	return b10
class class1:
	def fonk3(self):
		self.b13 = fonk2()
		self.b14 = len(self.b13)
	def fonk4(self):
		return fonk1(self.b13)
	def fonk5(self,b10):
		self.b13.append(b10)
		self.b14 = self.b14+1
	def fonk6(self):
		print(self.b13)
class class2:
	def fonk7(self,b10):
		self.b14 = random.randrange(a1-5,a1)
		self.b15 = []
		self.b16 = b10
		self.a10 = -1
		self.a11 = -1
		for b29 in range(self.b14):
			b17 = class1()
			self.b15.append(b17)
	def fonk8(self, other):
		return self.a10 < other.a10
	def fonk9(self):
		self.a10 = self.fonk10()
	def fonk10(self):
		a12 = 0
		for b29 in range(self.b14):
			a12 = a12+self.b15[b29].fonk10()
		if(a12>1):
			a12 = 1
		return a12
	def fonk11(self):
		for b29 in range(self.b14):
			self.b15[b29].fonk13()
class class3:
	def fonk12(self,b10):
		self.b14 = a2
		self.b18 = []
		self.b19 = b10
		for b29 in range(self.b14):
			b3 = class2(self.b19)
			self.b18.append(b3)
	def fonk13(self):
		for b29 in range(self.b14):
			self.b18[b29].fonk13()
			print()
class class4:
	def fonk14(self):
		self.b13 = 0.07+0.06*random.random()
		self.b20 = []
		self.b3 = -1
		self.b14 = 0
	def fonk15(self, other):
         return self.b13 < other.b13
	def fonk16(self,b10):
		self.b20.append(b10)
		self.b14 = self.b14+1
	def fonk17(self):
		print(self.b20)
'''
b20 = fonk2()
b10 = fonk1(b20)
b20.append(b10)
print(b10)
plt.plot(b20,b21 = 'red')
plt.show()
'''
'''
b3 = class2()
print(b3.fonk10())
'''
for b29 in range(b31):
	b22 = []
	for b29 in range(a7):
		b12 = class3(b29)
		b22.append(b12)
	b23 = []
	for b29 in range(a7):
		b24 = []
		for j in range(a7):
			b24.append(0)
		b23.append(b24)
	b7 = []
	for b29 in range(a7):
		b7.append(False)
	for b29 in range(a7):
		if(b7[b29]==False):
			b7[b29]=True
			while(True):
				b12 = random.randrange(0,a7)
				if(b7[b12]==False):
					b7[b12]=True
					b23[b29][b12]=1
					b23[b12][b29]=1
					break
	a13 = 8
	b25 = []
	for b29 in range(a3):
		b12 = class4()
		b25.append(b12)
	b25.sort(b26 = True)
	'''
	for b29 in range(a3):
		print(b25[b29].b13)
	'''
	b7 = []
	for b29 in range(a3):
		b7.append(False)
	a14 = 0
	while(a14<a3):
		b27 = random.randrange(min(3,a3-a14),min(14,a3-a14)+1)
		b28 = []
		for b29 in range(b27):
			b10 = random.randrange(0,a3-a14)
			b10 = b10+1
			a15 = 0
			a16 = 0
			while(a15<b10):
				while(b7[a16]):
					a16 = a16+1
				a15 = a15+1
				a16 = a16+1
			b28.append(a16-1)
			b7[a16-1]=True
			a14 = a14+1
		for b29 in range(b27):
			for j in range(b27):
				if(b29 = =j):
					continue
				b25[b28[b29]].fonk16(b28[j])
	b30 = []
	for b29 in range(a7):
		if(b29%b31 = =0):
			print('b29 = ',b29)
		for j in range(b22[b29].b14):
			b30.append(b22[b29].b18[j])
			b22[b29].b18[j].fonk9()
	b30.sort()
	b32 = len(b30)
	for b29 in range(b32):
		b30[b29].a11 = b29
	'''
	for b29 in range(len(b30)):
		print(b30[b29].a10)
	'''
	def fonk18(b29,j):
		b10 = b30[b29].b16
		b33 = b30[j].b16
		if(b10 = =b33):
			return True
		if(b23[b10][b33]==1):
			return True
		return False
	def fonk19(n,b3):
		b7 = False
		a16 = -1
		for b29 in range(b25[n].b14):
			if(b25[b25[n].b20[b29]].b3!=-1):
				for k in range(b32):
					if(b30[k].a11 = =b25[b25[n].b20[b29]].b3):
						a16 = k
						break
				if(not fonk18(a16,b3)):
					b7 = True
					break
		return b7
	a17 = 0
	b24 = 0
	for b29 in range(a3):
		b24 = 0
		for j in range(b32):
			b24 = b24+1
			if(b30[j].a10+b25[b29].b13<1):
				if(not fonk19(b29,j)):
					b25[b29].b3 = b30[j].a11
					b30[j].a10 = b30[j].a10+b25[b29].b13
					b30.sort()
					b24 = b24-1
					break
		if(b24 = =b32):
			a17 = a17+2
			print("connect state changed")
			for j in range(b32):
				if(b30[j].a10+b25[b29].b13<1):
					b30[j].a10 = b30[j].a10+b25[b29].b13
					break
	b30.sort()
	b34 = b30[0].a10
	b35 = b30[b32-1].a10
	a18 = 0
	for b29 in range(b32):
		a18 = a18+b30[b29].a10
	b36 = float(a18)/b32
	b2.write(str(a17))
	b2.write('\t')
	b2.write(str(b34))
	b2.write('\t')
	b2.write(str(b36))
	b2.write("\t")
	b2.write(str(b35))
	b2.write("\n")
	print(str(a17))
	print(str(b34))
	print(str(b36))
	print(str(b35))
	print('a17 is ', a17)
'''
for b29 in range(a3):
	b25[b29].fonk17()
'''
'''
b10 = fonk2()
print(b10)
b37 = pd.Series(b10)
b37.b38 = pd.Index(sm.tsa.datetools.dates_from_range('2001','2020'))
plt.plot(b37)
plt.show()
'''
b2.close()
b39 = time.time()
print("run time",b39-b1)