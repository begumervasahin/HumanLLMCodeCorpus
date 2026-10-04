from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
from numpy import arange, pi, sin
import numpy as np
import random
import math
import os
a1 = 200
b1 = []
for i in range(a1):
    b2 = random.uniform(0, 1.0)
    b3 = random.uniform(0, 1.0)
    b4 = sin(2*b2*pi)
    b5 = sin(2*b3*pi)
    b6 = math.sqrt(math.pow((b3-b2), 2) + math.pow((b5-b4), 2))
    b7 = max(b4, b5) - b6/2
    b1.append(b7)
b8 = arange(0, 1, 0.01)
b9 = sin(2*b8*pi)
b10 = []
b11 = []
for number in b1:
	b11.append(number)
	b10.append(b11)
	b11 = []
b12 = []
for element in b10:
	b12.append(element*len(b8))
b13 = sum(b1)/len(b1)
b14 = b13
b15 = [b14]*len(b8)
b16 = []
for element in b8:
	b17 = math.pow(b13 - sin(2*element*pi), 2)
	b16.append(b17)
b18 = sum(b16)/len(b16)
print('b19 = %f' % b18)
b20 = sum(b1)/len(b1)
b21 = [x-b20 for x in b1]
b22 = [math.pow(x, 2) for x in b21]
b23 = sum(b22)
b24 = b23/(len(b1)-1)
print('b25 = %f' % b24)
plt.plot(b8, b9)
plt.grid(True)
plt.ylim(-2, 2)
plt.xlim(0, 1)
for element in b12:
	plt.plot(b8, element, b26 = 0.5, color = 'g')
plt.plot(b8, b15, b26 = 0.5, color = 'r', linewidth = 2)
plt.text(0.5, 1.75, 'b19 = '+str(b18))
plt.text(0.5, 1.64, 'b25 = '+str(b24))
plt.show()