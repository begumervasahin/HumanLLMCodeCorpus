import sys
import csv
import numpy as np
import numpy.ma as ma
import scipy
import matplotlib.pyplot as plt
def fonk1(b19, b20, b14, n, b16):
	b1 = (len(b19)/n)
	b2 = [[None for x in range(b14+1)] for b6 in range(n)]
	b3 = [[0.0 for x in range(b14+1)] for b6 in range(n)]
	for nf in range(0, n):
		Xtrain, b4 = b19[nf+b1:], b20[nf+b1:]
		Xtest, b5 = b19[nf:nf+b1], b20[nf:nf+b1]
		for deg in range(0, b14 + 1):
			b2[nf][deg] = np.poly1d(np.polyfit(Xtrain, b4, deg))
			a1 = 0.0
			for tr_ex in range (0, b1):
				b6 = b2[nf][deg](Xtest[tr_ex])
				a1 += (b5[tr_ex] - b6) ** 2
			b3[nf][deg] = a1 / float(b1)
	if(b16):
		b7 = np.average(b3, axis=0)
		plt.figure(1, b8 = (15, 5))
		plt.subplot(121)
		plt.plot(range(0, 10), b7, '.-')
		plt.ylim(0,0.5)
		plt.xlabel('k')
		plt.ylabel('Average MSE')
		plt.title('Mean Squared Error vs. k')
		b9 = np.where(b7 == np.amin(b7))
		b10 = np.polyfit(b19, b20, b9[0])
		b11 = np.poly1d(b10)
		b12 = np.linspace(-1, 1, 100)
		plt.subplot(122)
		plt.plot(b19, b20, '.', b12, b11(b12), '-')
		plt.ylim(-1,1)
		plt.xlabel('x')
		plt.ylabel('b6')
		plt.title('Best-Fitting Polynomial Regression')
		plt.show()
		return b10
def fonk2():
	b13 = sys.argv[1]
	b14 = int(sys.argv[2])
	b15 = int(sys.argv[3])
	b16 = bool(sys.argv[4])
	b17 = open(b13, 'rb')
	b18 = csv.reader(b17, delimiter=',')
	b19 = []
	b20 = []
	for i, row in enumerate(b18):
		if i > 0:
			b19.append(float(row[0]))
			b20.append(float(row[1]))
	b19 = np.array(b19)
	b20 = np.array(b20)
	fonk1(b19, b20, b14, b15, b16)
if b21 = = "__main__":
	fonk2()