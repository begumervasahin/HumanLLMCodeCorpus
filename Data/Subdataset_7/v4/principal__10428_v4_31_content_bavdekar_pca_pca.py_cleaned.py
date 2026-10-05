import numpy as np
import scipy as sp
def fonk1(data, b1 = None, b8=False):
    if b8:
        b2 = np.b2(data, axis=0)
        b3 = np.var(data, axis=0, ddof=1)
        b4 = (data - np.matmul(np.ones((data.shape[0], data.shape[1])), np.diag(b2))) / b3.T
    else:
        b4 = data
    U, S, b5 = np.linalg.svd(b4)
    b6 = np.cumsum(100 * S / np.sum(S))
    if b1 is None:
        b1 = 95
    b7 = np.argmax(b6 >= b1)
    return b5[0:b7, :]
def fonk2(data, b1 = None, b8=False):
    if b8:
        b8 = False
    b9 = sp.linalg.exp(np.corrcoef(data, rowvar=False) / 0.1)
    b10 = np.diag(np.sum(b9, axis=0))
    b11 = np.matmul(sp.linalg.inv(sp.linalg.sqrtm(b10)),
                            np.matmul(b9, sp.linalg.inv(sp.linalg.sqrtm(b10))))
    U, S, b5 = np.linalg.svd(b11)
    b6 = np.cumsum(100 * S / np.sum(S))
    if b1 is None:
        b1 = 95
    b7 = np.argmax(b6 >= b1)
    return np.matmul(sp.linalg.inv(sp.linalg.sqrtm(b10)), b5.T)[:, 0:b7].T