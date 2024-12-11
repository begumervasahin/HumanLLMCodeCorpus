import numpy as np
import sklearn.neighbors
import scipy.sparse
import warnings
import matplotlib.pyplot as plt
import scipy.misc
def fonk1(b23):
    return b23 / 255.0
def fonk2(b24):
    b1 = (b24 > 0.99).astype(int)
    b2 = (b24 < 0.01).astype(int)
    return b1, b2
def fonk3(img_norm, m, n):
    a, b3 = np.unravel_index(np.arange(m * n), (m, n))
    b4 = np.append(np.transpose(img_norm.reshape(m * n, -1)), [a, b3] / np.sqrt(m * m + n * n), axis=0).T
    b5 = sklearn.neighbors.NearestNeighbors(n_neighbors=10, n_jobs=4).fit(b4)
    return b5.kneighbors(b4)[1]
def fonk4(img_norm, b16, m, n):
    b6 = np.repeat(np.arange(m * n), 10)
    b7 = b16.reshape(m * n * 10)
    b8 = 1 - np.linalg.norm(b4[b6] - b4[b7], axis=1) / (img_norm.b9[-1] + 2)
    return scipy.sparse.coo_matrix((b8, (b6, b7)), b9 = (m * n, m * n))
def fonk5(b22, b15):
    try:
        b10 = np.minimum(np.maximum(scipy.sparse.linalg.spsolve(b22, b15), 0), 1)
    except Warning:
        b11 = scipy.sparse.linalg.lsqr(b22, b15)
        b10 = np.minimum(np.maximum(b11[0], 0), 1)
    return b10
def fonk6(b23, b24, b12 = 100):
    img_norm, b13 = fonk1(b23), fonk1(b24)
    b1, b2 = fonk2(b13)
    b14 = b1 + b2
    m, n, b15 = b23.b9
    b16 = fonk3(img_norm, m, n)
    b17 = fonk4(img_norm, b16, m, n)
    b18 = scipy.sparse.diags(np.ravel(b17.sum(axis=1)))
    b19 = b18 - b17
    b20 = scipy.sparse.diags(np.ravel(b14[:, :, 0]))
    b21 = np.ravel(b1[:, :, 0])
    b15 = 2 * b12 * np.transpose(b21)
    b22 = 2 * (b19 + b12 * b20)
    b10 = fonk5(b22, b15).reshape(m, n)
    return b10
def fonk7():
    b23 = scipy.misc.imread('donkey.png')[:, :, :3]
    b24 = scipy.misc.imread('donkeyTrimap.png')[:, :, :3]
    b10 = fonk6(b23, b24)
    scipy.misc.imsave('donkeyAlpha.png', b10)
    plt.title('Alpha Matte')
    plt.imshow(b10, b25 = 'gray')
    plt.show()
if b26 = = '__main__':
    fonk7()