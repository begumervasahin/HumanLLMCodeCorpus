import numpy as np
import scipy as sp
def fonk1(data, b1 = None, b8=False):
    if b8:
        b2 = np.b2(data, axis=0)
        b3 = np.var(data, axis=0, ddof=1)
        b4 = (data - np.ones((data.shape[0], 1)) * b2) / b3
    else:
        b4 = data
    _, _, b5 = np.linalg.svd(b4)
    b6 = np.cumsum(100 * np.square(b5) / np.sum(np.square(b5)))
    if b1 is None:
        b1 = 95
    b7 = np.argmax(b6 >= b1)
    return b5[:b7, :]
def fonk2(data, b1 = None, b8=False):
    if b8:
        b8 = False
    b9 = sp.linalg.expm(np.corrcoef(data, rowvar=False) / 0.1)
    b10 = np.diag(np.sum(b9, axis=0))
    b11 = np.matmul(np.linalg.inv(sp.linalg.sqrtm(b10)),
                            np.matmul(b9, np.linalg.inv(sp.linalg.sqrtm(b10))))
    _, _, b5 = np.linalg.svd(b11)
    b6 = np.cumsum(100 * np.square(b5) / np.sum(np.square(b5)))
    if b1 is None:
        b1 = 95
    b7 = np.argmax(b6 >= b1)
    return np.matmul(np.linalg.inv(sp.linalg.sqrtm(b10)), b5.T)[:b7, :].T