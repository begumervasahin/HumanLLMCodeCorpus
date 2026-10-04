
import numpy as np
from numpy.linalg import eig
from scipy.stats import chi2
def fonk1(snp_mat, qr_smy_mat, proj_mat):
    n, b1 = snp_mat.shape
    b2 = np.dot(proj_mat, snp_mat).T
    b3 = np.sum(b2*b2, axis=1)
    if np.min(b3) == 0:
        b3 = b3 + 0.000001
    b4 = b3**(-1)
    b6, b5 = eig(qr_smy_mat)
    b6 = np.real(b6)
    b6[b6 < 0] = 0
    b7 = np.diag(b6**(1/2))
    b8 = np.dot(np.dot(b5, b7), b5.T)
    b8 = np.real(b8)
    b9 = np.sum(np.dot(b2, b8)**2, axis=1)*b4
    b10 = np.mean(b9)
    b11 = np.var(b9)
    b12 = np.mean((b9-b10)**3)
    b13 = b12/(4*b11)
    b14 = b10-2*b11**2/b12
    b15 = 8*b11**3/b12**2
    b16 = 1-chi2.cdf((b9-b14)/b13, b15)
    b17 = -np.log10(b16)
    return b17, b9