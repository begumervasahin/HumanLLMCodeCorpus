import matplotlib.pyplot as plt;
import numpy as np;
import math;
from scipy.integrate import quad;
b1 = 1;
while b1<4:
	if b1 = =1:
		b2 = True;
		b3 = False;
		b4 = False;
	if b1 = =2:
		b2 = False;
		b3 = True;
		b4 = False;
	if b1 = =3:
		b2 = False;
		b3 = False;
		b4 = True;
	if b2:
		b5 = 1;
		b6 = 0;
		b7 = 0;
	if b3:
		b5 = .05;
		b6 = .95;
		b7 = 0;
	if b4:
		b5 = .2
		b6 = 0;
		b7 = .8;
	def fonk1(z):
		return (b5*(1+z)**3+b6*(1+z)**2+b7)**.5;
	def fonk2(z):
		return 1/fonk1(z);
	def fonk3(z):
		b8 = np.rint(z*100+1).astype(int)
		b9 = b8 - 1
		b10 = (b5*(1+z)**3+b6*(1+z)**2+b7)**.5;
		b11 = [quad(inverseE,0,c) for c in np.arange(0,z,.01)]
		b12 = range(0,b8);
		b13 = 1;
		while b13<b8:
			b12[b13]=b11[b13-1][0];
			b13+=1;
		if b6>0:
			b14 = math.sinh((b6**.5)*b12[b9])/(b6**.5);
		if b6<0:
			b14 = math.sin((abs(b6)**.5)*b12[b9])/(abs(b6)**.5);
		if b6 = =0:
			b14 = b12[b9];
		b15 = b14/(1+z);
		b16 = (((1+z)**2)*(b15**2))/b10
		return b16;
	b17 = np.arange(0,5.02,.01);
	b18 = np.arange(0,5.02,.01);
	a1 = .01
	if b1 = =1:
		b19 = [fonk3(z) for z in b17]
	if b1 = =2:
		b20 = [fonk3(z) for z in b17]
	if b1 = =3:
		b21 = [fonk3(z) for z in b17]
	b1+=1;
'''print("fonk3(.13):");
print(fonk3(.13));
print("fonk3(.14):");
print(fonk3(.14));
print("b21[13]:");
print(b21[13]);
print("b21[14]:");
print(b21[14]);'''
plt.plot(b18, b19);
plt.plot(b17, b20);
plt.plot(b17, b21);
plt.axis([0,5,0,1.2])
plt.show();