import matplotlib.pyplot as plt;
import numpy as np;
import math;
from scipy.integrate import quad;
def fonk1(z):
	return (omegaM*(1+z)**3+b7*(1+z)**2+b11)**.5;
def fonk2(z):
	return 1/fonk1(z);
def fonk3(z):
	b1 = np.rint(z*100+1).astype(int)
	b2 = b1-1
	b3 = (omegaM*(1+z)**3+b7*(1+z)**2+b11)**.5;
	b4 = [quad(inverseE,0,c) for c in np.arange(0,z+.01,.01)]
	b5 = [b4[i][0] for i in range(0,b1)]
	b5[0]=0
	if b7>0:
		b6 = math.sinh((b7**.5)*b5[b2])/(b7**.5);
	if b7<0:
		b6 = math.sin((abs(b7)**.5)*b5[b2])/(abs(b7)**.5);
	if b7 = =0:
		b6 = b5[b2];
	b8 = b6/(1+z);
	b9 = (((1+z)**2)*(b8**2))/b3
	return b9
a1 = 0
b10 = np.arange(0,5.02,.01)
while a1<3:
	if a1 = =0:
		omegaM,b7,b11 = 1,0,0
	if a1 = =1:
		omegaM,b7,b11 = .05,.95,0
	if a1 = =2:
		omegaM,b7,b11 = .2,0,.8
	if a1 = =0:
		b12 = [fonk3(a) for a in b10]
	if a1 = =1:
		b13 = [fonk3(a) for a in b10]
	if a1 = =2:
		b14 = [fonk3(a) for a in b10]
	a1+=1
plt.plot(b10,b12)
plt.plot(b10,b13)
plt.plot(b10,b14)
plt.axis([0,5,0,1.2])
plt.savefig('comovingvolume.png',b15 = 80)