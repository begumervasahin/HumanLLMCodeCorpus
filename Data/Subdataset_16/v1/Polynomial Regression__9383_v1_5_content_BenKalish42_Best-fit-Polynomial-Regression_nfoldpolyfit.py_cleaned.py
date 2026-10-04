import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
def fonk1(b21, b19, b16, n, b18):
    b1 = len(b21)
    b2 = [[None for _ in range(b16 + 1)] for _ in range(n)]
    b3 = [[0.0 for _ in range(b16 + 1)] for _ in range(n)]
    for nf in range(n):
        start, b4 = nf * b1, (nf + 1) * b1
        b5 = np.concatenate((b21[:start], b21[b4:]))
        b6 = np.concatenate((b19[:start], b19[b4:]))
        Xtest, b7 = b21[start:b4], b19[start:b4]
        for deg in range(b16 + 1):
            b2[nf][deg] = np.poly1d(np.polyfit(b5, b6, deg))
            b8 = sum((b7[tr_ex] - b2[nf][deg](Xtest[tr_ex])) ** 2 for tr_ex in range(b1))
            b3[nf][deg] = b8 / float(b1)
    if b18:
        b9 = np.mean(b3, axis=0)
        plt.figure(b10 = (15, 5))
        plt.subplot(121)
        plt.plot(range(b16 + 1), b9, '.-')
        plt.ylim(0, 0.5)
        plt.xlabel('k')
        plt.ylabel('Average MSE')
        plt.title('Mean Squared Error vs. k')
        b11 = np.argmin(b9)
        b12 = np.polyfit(b21, b19, b11)
        b13 = np.poly1d(b12)
        b14 = np.linspace(np.min(b21), np.max(b21), 100)
        plt.subplot(122)
        plt.plot(b21, b19, '.', b14, b13(b14), '-')
        plt.ylim(np.min(b19), np.max(b19))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Best-Fitting Polynomial Regression')
        plt.show()
        return b12
def fonk2():
    b15 = sys.argv[1]
    b16 = int(sys.argv[2])
    b17 = int(sys.argv[3])
    b18 = bool(int(sys.argv[4]))
    b21, b19 = [], []
    with open(b15, 'r') as csvfile:
        b20 = csv.reader(csvfile, delimiter=',')
        next(b20)
        for row in b20:
            b21.append(float(row[0]))
            b19.append(float(row[1]))
    b21 = np.array(b21)
    b19 = np.array(b19)
    fonk1(b21, b19, b16, b17, b18)
if b22 = = "__main__":
    fonk2()