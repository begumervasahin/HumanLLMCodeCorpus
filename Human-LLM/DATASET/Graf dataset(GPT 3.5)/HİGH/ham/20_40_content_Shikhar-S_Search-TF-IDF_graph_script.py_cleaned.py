import matplotlib.pyplot as plt
import os,sys
from scipy.optimize import curve_fit
import math
def fonk1(b1,a,b,c,d):
	return  a*b1*b1*b1 + b*b1*b1 + c*b1 +d
def fonk2():
	b1 = list()
	b2 = list()
	b3 = os.getcwd()
	b4 = raw_input('Folder name:\n')
	b5 = os.path.join(b3,b4)
	a1 = 0
	for filename in os.listdir(b5):
		if(filename!='.DS_Store'):
			a1+=1
			print filename
			with open(os.path.join(b5,filename),'r') as F:
				for b6 in F:
					b6 = b6.split()
					b2.append(float(b6[0]))
					b1.append(float(b6[1]))
	b7 = list()
	b8 = list()
	b9 = curve_fit(func,b1,b2)
	[a,b,c,d]=b9[0]
	a2 = 0
	while a2<=1:
		b7.append(a2)
		b8.append(fonk1(a2,a,b,c,d))
		a2+=0.2
	return (b7,b8)
(p_v,q_v)=fonk2()
(p_f,q_f)=fonk2()
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision vs Recall')
plt.plot(p_v,q_v,b10 = 'Vector Space Model')
plt.plot(p_v,q_v,'bs')
plt.plot(p_f,q_f,b10 = 'Fuzzy Retrieval Model')
plt.plot(p_f,q_f,'r^')
plt.legend()
plt.axis([0.0,1.0,0.0,1.0])
plt.show()