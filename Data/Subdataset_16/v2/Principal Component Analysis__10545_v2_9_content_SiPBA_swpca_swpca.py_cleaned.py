import numpy as np
from scipy.linalg import svd
from scipy.stats import f_oneway
def fonk1(b27, b28, b1 = 0.05, b3=None):
    b2 = b27.shape[0]
    if b3 is None:
        b3 = np.ones(b2, dtype=bool)
        b4 = False
    else:
        b4 = True
    b5 = b27.mean(axis=1)
    b6 = (b27.T - b5).T
    b7 = b6[b3].mean(axis=0)
    b6 -= b7
    b8 = b6[b3].var(axis=0)
    b8 = np.maximum(b8, 1)
    b6 /= b8
    if b4:
        b9 = b6[~b3]
    b10 = b6[b3]
    b14, b15, b11 = svd(b10, full_matrices=False)
    b12 = b11.T
    b13 = np.argsort(b15)[::-1]
    b14 = b14[:, b13]
    b15 = b15[b13]
    b12 = b12[:, b13]
    b16 = b10.dot(b12)
    if b4:
        b17 = b9.dot(b12)
    b18 = np.unique(b28)
    F, b19 = f_oneway(b16[b28[b3] == b18[0]], b16[b28[b3] == b18[1]])
    b20 = 1 - np.exp(-b19 / b1)
    b21 = np.linalg.pinv(b12)
    b22 = np.diag(b20)
    if b4:
        b23 = b16.dot(b22).dot(b21)
        b24 = b17.dot(b22).dot(b21)
        b25 = np.zeros((b2, b23.shape[1]))
        b25[b3] = b23
        b25[~b3] = b24
    else:
        b25 = b16.dot(b22).dot(b21)
    b25 *= b8
    b25 += b7
    b25 = (b25.T + b5).T
    return b25, b20, b21
if b26 = = "__main__":
    b27 = np.random.rand(100, 10)
    b28 = np.random.randint(0, 2, 100)
    b25, b20, b21 = fonk1(b27, b28)
    print("Reconstructed Dataset:\n", b25)
    print("Weights:\n", b20)
    print("Transformation Matrix:\n", b21)