import numpy as np
from scipy.linalg import svd
from scipy.stats import f_oneway
def fonk1(dataset, catvar, b1 = 0.05, b4=None):
    N, b2 = dataset.shape
    b3 = b4 is not None
    if not b3:
        b4 = np.ones(N, dtype=bool)
    b5 = dataset.mean(axis=1)
    b6 = dataset - b5[:, np.newaxis]
    b7 = b6[b4].mean(axis=0)
    b6 -= b7
    b8 = np.maximum(b6[b4].var(axis=0), 1)
    b6 /= b8
    if b3:
        b9 = b6[~b4]
    b10 = b6[b4]
    b14, b15, b11 = svd(b10, full_matrices=False)
    b12 = b11.T
    b13 = np.argsort(b15)[::-1]
    b14 = b14[:, b13]
    b15 = b15[b13]
    b12 = b12[:, b13]
    b16 = b10.dot(b12)
    if b3:
        b17 = b9.dot(b12)
    b18 = np.unique(catvar)
    F, b19 = f_oneway(b16[catvar[b4] == b18[0]],
                        b16[catvar[b4] == b18[1]])
    b20 = 1 - np.exp(-b19 / b1)
    b21 = np.linalg.pinv(b12)
    b22 = np.diag(b20)
    if b3:
        b23 = b16.dot(b22).dot(b21)
        b24 = b17.dot(b22).dot(b21)
        b25 = np.zeros((N, b23.shape[1]))
        b25[b4] = b23
        b25[~b4] = b24
    else:
        b25 = b16.dot(b22).dot(b21)
    b25 = b25 * b8
    b25 += b7
    b25 += b5[:, np.newaxis]
    return b25, b20, b21