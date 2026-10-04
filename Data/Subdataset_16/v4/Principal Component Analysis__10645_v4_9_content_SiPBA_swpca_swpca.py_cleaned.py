import numpy as np
from scipy.linalg import svd
from scipy.stats import f_oneway
def fonk1(dataset, catvar, b1 = 0.05, b4=False):
    b2 = dataset.shape[0]
    b3 = False
    if not isinstance(b4, np.ndarray) or b4 is False:
        b4 = np.ones(b2, dtype=bool)
    else:
        b3 = True
    b5 = dataset.mean(axis=1)
    b6 = (dataset.T - b5).T
    b7 = b6[b4].mean(axis=0)
    b6 -= b7
    b8 = b6[b4].var(axis=0)
    b8 = np.maximum(b8, 1)
    b6 /= b8
    if b3:
        b9 = b6[~b4]
    b10 = b6[b4]
    U, s, b11 = svd(b10, full_matrices=False)
    b12 = b11.T
    b13 = np.argsort(s)[::-1]
    U, s, b12 = U[:, b13], s[b13], b12[:, b13]
    b14 = b10.dot(b12)
    if b3:
        b15 = b9.dot(b12)
    b16 = np.unique(catvar)
    F, b17 = f_oneway(b14[catvar[b4] == b16[0]], b14[catvar[b4] == b16[1]])
    b18 = 1 - np.exp(-b17 / b1)
    b19 = np.linalg.pinv(b12)
    b20 = np.diag(b18)
    if b3:
        b21 = b14.dot(b20).dot(b19)
        b22 = b15.dot(b20).dot(b19)
        b23 = np.zeros((b2, b21.shape[1]))
        b23[b4] = b21
        b23[~b4] = b22
    else:
        b23 = b14.dot(b20).dot(b19)
    b23 = b23 * b8 + b7
    b23 = (b23.T + b5).T
    return b23, b18, b19