import numpy as np
import scipy as sp
def fonk1(b13, b1 = None, b8=False):
    if b8:
        b2 = np.mean(b13, axis=0)
        b3 = np.var(b13, axis=0, ddof=1)
        b4 = (b13 - np.outer(np.ones(b13.shape[0]), b2)) / b3[:, np.newaxis]
    else:
        b4 = b13
    U, S, b5 = np.linalg.svd(b4)
    b6 = np.cumsum(100 * S / np.sum(S))
    if b1 is None:
        b1 = 95
    b7 = np.argmax(b6 >= b1)
    return b5[:b7, :]
def fonk2(b13, b1 = None, b8=False):
    if b8:
        b8 = False
    b9 = sp.linalg.expm(np.corrcoef(b13, rowvar=False) / 0.1)
    b10 = np.diag(np.sum(b9, axis=0))
    b11 = np.matmul(sp.linalg.inv(sp.linalg.sqrtm(b10)), np.matmul(b9, sp.linalg.inv(sp.linalg.sqrtm(b10))))
    U, S, b5 = np.linalg.svd(b11)
    b6 = np.cumsum(100 * S / np.sum(S))
    if b1 is None:
        b1 = 95
    b7 = np.argmax(b6 >= b1)
    return np.matmul(sp.linalg.inv(sp.linalg.sqrtm(b10)), b5.T)[:b7, :].T
if b12 = = "__main__":
    b13 = np.random.rand(100, 10)
    b14 = fonk1(b13)
    print("LPCA Result Shape:", b14.shape)
    b15 = fonk2(b13)
    print("SCPA Result Shape:", b15.shape)