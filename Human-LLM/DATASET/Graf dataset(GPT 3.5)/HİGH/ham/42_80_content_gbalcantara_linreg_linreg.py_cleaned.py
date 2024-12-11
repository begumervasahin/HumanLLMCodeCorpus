import numpy as np
import matplotlib.pyplot as plt
import random
import sys
def fonk1(b14, b15, b6, b7, m, a3):
	b1 = b14.transpose()
	a1 = 1
	while a1!=0 :
		for a2 in range(0, a3):
			b2 = np.dot(b14, b6)
			b3 = b2 - b15
			a1 = 0
			b4 = np.sum(b3 ** 2) / (2 * m)
			b5 = np.dot(b1, b3) / m
			b6 = b6 - b7 * b5
			a1 = round(b4,2)
		b7 = b7+0.00001
	return b6, b7
b8 = sys.argv[1] if len(sys.argv) > 1 else "0"
b9 = sys.argv[2] if len(sys.argv) > 2 else "0"
b10 = sys.argv[3] if len(sys.argv) > 3 else "0"
b11 = int(b8)
b12 = int(b9)
b13 = int(b10)
a2 = 0
b14 = np.zeros(shape=(20, 3))
b15 = np.zeros(shape=20)
for num in range(-10,10):
    b14[a2][0]=1
    b14[a2][1]=num
    b14[a2][2]=num**2
    b15[a2]=(((b11)*num**2)+((b12)*num)+b13)
    a2 = a2+1
m, b16 = np.shape(b14)
a3 = 5000
b7 = 0.000001
b6 = np.ones(b16)
b17 = np.random.uniform(-0.1,0.1,b15.shape)
b15 = b15 + b17
b6, b7 = fonk1(b14, b15, b6, b7, m, a3)
print 'learning b18 = ',b7
b19 = b6[0]
b20 = b6[1]
b21 = b6[2]
print 'b11 = ',b21
print 'b12 = ',b20
print 'b13 = ',b19
a4 = 0
b22 = np.zeros(shape=20)
b23 = np.zeros(shape=20)
for num in range(-10,10):
    b22[a4]=num
    b23[a4]=(((b21)*num**2)+((b20)*num)+b19)
    a4 = a4+1
plt.plot(b14,b15,'kx',b22,b23,)
plt.show()