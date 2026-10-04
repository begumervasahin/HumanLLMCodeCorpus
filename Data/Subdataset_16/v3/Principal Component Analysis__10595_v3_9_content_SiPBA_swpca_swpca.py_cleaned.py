import numpy as np
from scipy.linalg import svd
from scipy.stats import f_oneway
def fonk1(b25, b26, b1 = 0.05, b3=None):
    N, b2 = b25.shape
    if b3 is None:
        b3 = np.ones(N, dtype=bool)
        b4 = False
    else:
        b4 = True
    b5 = b25.mean(axis=1)
    b6 = (b25.T - b5).T
    b7 = b6[b3].mean(axis=0)
    b6 -= b7
    b8 = b6[b3].var(axis=0)
    b8 = np.maximum(b8, 1)
    b6 /= b8
    b9 = b6[b3]
    b10 = b6[~b3] if b4 else None
    U, s, b11 = svd(b9, full_matrices=False)
    b12 = b11.T
    b13 = np.argsort(s)[::-1]
    b12 = b12[:, b13]
    b14 = b9.dot(b12)
    b15 = b10.dot(b12) if b4 else None
    b16 = np.unique(b26)
    F, b17 = f_oneway(b14[b26[b3] == b16[0]],
                        b14[b26[b3] == b16[1]])
    b18 = 1 - np.exp(-b17 / b1)
    b19 = np.linalg.pinv(b12)
    b20 = np.diag(b18)
    if b4:
        b21 = b14.dot(b20).dot(b19)
        b22 = b15.dot(b20).dot(b19)
        b23 = np.zeros((N, b2))
        b23[b3] = b21
        b23[~b3] = b22
    else:
        b23 = b14.dot(b20).dot(b19)
    b23 = (b23 * b8) + b7
    b23 = (b23.T + b5).T
    return b23, b18, b19
if b24 = = "__main__":
    b25 = np.random.rand(100, 10)
    b26 = np.random.randint(0, 2, 100)
    Xhat, b18, b19 = fonk1(b25, b26)
    print("Reconstructed Dataset:\n", Xhat)
    print("Weights:\n", b18)
    print("Transformation Matrix:\n", b19)