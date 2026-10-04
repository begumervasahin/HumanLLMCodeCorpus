import numpy as np
from numpy.linalg import eig
from scipy.stats import chi2
def fonk1(snp_mat, qr_smy_mat, proj_mat):
    def fonk2(b14):
        b1 = np.sum(b14 * b14, b5=1)
        b1[b1 = = 0] += 1e-6
        return b1
    def fonk3(matrix):
        b3, b2 = eig(matrix)
        b3 = np.real(b3)
        b3[b3 < 0] = 0
        return b3, b2
    def fonk4(b3, b2):
        b4 = np.diag(np.sqrt(b3))
        return np.real(np.dot(np.dot(b2, b4), b2.T))
    def fonk5(b14, b16, b15):
        return np.sum(np.dot(b14, b16) ** 2, b5 = 1) * b15
    def fonk6(b17):
        b6 = np.mean(b17)
        b7 = np.var(b17)
        b8 = np.mean((b17 - b6) ** 3)
        return b6, b7, b8
    def fonk7(b6, b7, b8):
        b9 = b8 / (4 * b7)
        b10 = b6 - (2 * b7 ** 2) / b8
        b11 = 8 * (b7 ** 3) / (b8 ** 2)
        return b9, b10, b11
    def fonk8(b17, b9, b10, b11):
        b12 = 1 - chi2.cdf((b17 - b10) / b9, b11)
        return -np.log10(b12)
    n, b13 = snp_mat.shape
    b14 = np.dot(proj_mat, snp_mat).T
    b1 = fonk2(b14)
    b15 = b1 ** (-1)
    b3, b2 = fonk3(qr_smy_mat)
    b16 = fonk4(b3, b2)
    b17 = fonk5(b14, b16, b15)
    b6, b7, b8 = fonk6(b17)
    b9, b10, b11 = fonk7(b6, b7, b8)
    b18 = fonk8(b17, b9, b10, b11)
    return b18, b17