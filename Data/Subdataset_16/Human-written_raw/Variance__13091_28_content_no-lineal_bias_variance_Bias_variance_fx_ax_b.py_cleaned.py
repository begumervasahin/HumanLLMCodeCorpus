from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
from numpy import arange, pi, sin
import random
import math
import os
a1 = 200
b1 = []
b2 = []
for i in range(a1):
	b3 = random.uniform(-1, 1)
	b4 = random.uniform(-1, 1)
	b5 = sin(b3*pi)
	b6 = sin(b4*pi)
	b7 = (b6-b5)/(b4-b3)
	b8 = b5 - (b7*b3)
	b1.append(b7)
	b2.append(b8)
b9 = arange(-1, 1.01, 0.01)
b10 = sin(b9*pi)
b11 = sum(b1)/len(b1)
b12 = sum(b2)/len(b2)
b13 = []
for elemento in b9:
	b14 = math.pow((b11 * elemento) + b12 - sin(elemento*pi), 2)
	b13.append(b14)
b15 = sum(b13)/len(b13)
print('b16 = %f' % b15)
b17 = []
b18 = []
for i in range(len(b9)):
	for j in range(a1):
		b19 = ((b1[j] - b11)*b9[i]) + (b2[j] - b12)
		b18.append(b19)
	b17.append(b18)
	b18 = []
b20 = []
b19 = []
for punto in b17:
	for recta in punto:
		b21 = math.pow(recta, 2)
		b19.append(b21)
	b20.append(b19)
	b19 = []
b22 = []
for punto in b20:
	b19 = sum(punto)/(len(punto)-1)
	b22.append(b19)
b23 = sum(b22)/len(b22)
print('Variance: %f' %b23)
plt.plot(b9, b10)
plt.grid(True)
plt.ylim(-2, 2)
plt.xlim(-1, 1)
for i in range(a1):
	plt.plot(b9, (b1[i]*b9)+b2[i], b24 = 0.5, color = 'g')
plt.plot(b9, (b11*b9)+b12, b24 = 0.5, color = 'r', linewidth = 2)
plt.text(-0.9, 1.75, 'b16: '+str(b15))
plt.text(-0.9, 1.64, 'Variance: '+str(b23))
plt.savefig(os.path.join('Sinusoidal_dos.png'), b25 = 300, format = 'png', bbox_inches = 'tight')