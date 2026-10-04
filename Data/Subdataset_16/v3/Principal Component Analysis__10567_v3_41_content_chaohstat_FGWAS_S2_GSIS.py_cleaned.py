import numpy as np
from numpy.linalg import eig
from scipy.stats import chi2
def fonk1(b17, b18, b19):
    b1 = np.dot(b19, b17).T
    b2 = np.sum(b1 * b1, axis=1)
    b2[b2 = = 0] += 1e-6
    b3 = 1.0 / b2
    b5, b4 = eig(b18)
    b5 = np.real(b5)
    b5[b5 < 0] = 0
    b6 = np.sqrt(b5)
    b7 = np.dot(np.dot(b4, np.diag(b6)), b4.T)
    b7 = np.real(b7)
    b8 = np.sum(np.dot(b1, b7) ** 2, axis=1) * b3
    b9 = np.mean(b8)
    b10 = np.var(b8)
    b11 = np.mean((b8 - b9) ** 3)
    b12 = b11 / (4 * b10)
    b13 = b9 - (2 * b10 ** 2 / b11)
    b14 = (8 * b10 ** 3) / (b11 ** 2)
    b15 = 1 - chi2.cdf((b8 - b13) / b12, b14)
    b16 = -np.log10(b15)
    return b16, b8
def fonk2():
    a1 = 100
    a2 = 10
    b17 = np.random.rand(a1, a2)
    b18 = np.random.rand(a1, a1)
    b19 = np.random.rand(a1, a1)
    b16, b8 = fonk1(b17, b18, b19)
    print("b16:", b16)
    print("b8:", b8)
if b20 = = "__main__":
    fonk2()