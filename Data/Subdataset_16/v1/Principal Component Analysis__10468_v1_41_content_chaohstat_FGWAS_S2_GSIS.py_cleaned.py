import numpy as np
from numpy.linalg import eig
from scipy.stats import chi2
def fonk1(b19, b20, b21):
    a1, b1 = b19.shape
    b2 = np.dot(b21, b19).T
    b3 = np.sum(b2 * b2, axis=1)
    b3[b3 = = 0] += 1e-6
    b4 = b3 ** (-1)
    b6, b5 = eig(b20)
    b6 = np.real(b6)
    b6[b6 < 0] = 0
    b7 = np.diag(b6 ** 0.5)
    b8 = np.dot(np.dot(b5, b7), b5.T)
    b8 = np.real(b8)
    b9 = np.sum(np.dot(b2, b8) ** 2, axis=1) * b4
    b10 = np.mean(b9)
    b11 = np.var(b9)
    b12 = np.mean((b9 - b10) ** 3)
    b13 = b12 / (4 * b11)
    b14 = b10 - 2 * b11 ** 2 / b12
    b15 = 8 * b11 ** 3 / b12 ** 2
    b16 = 1 - chi2.cdf((b9 - b14) / b13, b15)
    b17 = -np.log10(b16)
    return b17, b9
if b18 = = "__main__":
    a1 = 100
    b1 = 10
    b19 = np.random.rand(a1, b1)
    b20 = np.random.rand(a1, a1)
    b21 = np.random.rand(a1, a1)
    b17, b9 = fonk1(b19, b20, b21)
    print("b17:", b17)
    print("b9:", b9)