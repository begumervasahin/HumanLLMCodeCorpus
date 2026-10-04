import matplotlib.pyplot as plt;
import numpy as np;
import math;
from scipy.integrate import quad;
j=1;
while j<4:
	if j==1:
		case1=True;
		case2=False;
		case3=False;
	if j==2:
		case1=False;
		case2=True;
		case3=False;
	if j==3:
		case1=False;
		case2=False;
		case3=True;
	if case1:
		omegaM=1;
		omegaK=0;
		omegaL=0;
	if case2:
		omegaM=.05;
		omegaK=.95;
		omegaL=0;
	if case3:
		omegaM=.2
		omegaK=0;
		omegaL=.8;
	def xE(z):
		return (omegaM*(1+z)**3+omegaK*(1+z)**2+omegaL)**.5;
	def inverseE(z):
		return 1/xE(z);
	def ploot(z):
		entries = np.rint(z*100+1).astype(int)
		k = entries - 1
		E=(omegaM*(1+z)**3+omegaK*(1+z)**2+omegaL)**.5;
		answerAndError=[quad(inverseE,0,c) for c in np.arange(0,z,.01)]
		dC=range(0,entries);
		i=1;
		while i<entries:
			dC[i]=answerAndError[i-1][0];
			i+=1;
		if omegaK>0:
			dM=math.sinh((omegaK**.5)*dC[k])/(omegaK**.5);
		if omegaK<0:
			dM=math.sin((abs(omegaK)**.5)*dC[k])/(abs(omegaK)**.5);
		if omegaK==0:
			dM=dC[k];
		dA=dM/(1+z);
		dVc=(((1+z)**2)*(dA**2))/E
		return dVc;
	x=np.arange(0,5.02,.01);
	x1=np.arange(0,5.02,.01);
	u=.01
	if j==1:
		plootArray1 = [ploot(z) for z in x]
	if j==2:
		plootArray2 = [ploot(z) for z in x]
	if j==3:
		plootArray3 = [ploot(z) for z in x]
	j+=1;
'''print("ploot(.13):");
print(ploot(.13));
print("ploot(.14):");
print(ploot(.14));
print("plootArray3[13]:");
print(plootArray3[13]);
print("plootArray3[14]:");
print(plootArray3[14]);'''
plt.plot(x1, plootArray1);
plt.plot(x, plootArray2);
plt.plot(x, plootArray3);
plt.axis([0,5,0,1.2])
plt.show();