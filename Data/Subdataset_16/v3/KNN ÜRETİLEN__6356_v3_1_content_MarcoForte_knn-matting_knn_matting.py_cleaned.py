import numpy as np
import sklearn.neighbors
import scipy.sparse
import warnings
import matplotlib.pyplot as plt
from imageio import imread, imsave
def fonk1(b22, b2, b1 = 100):
    b22, b2 = b22 / 255.0, b2 / 255.0
    m, n, b3 = b22.shape
    b4 = (b2 > 0.99).astype(int)
    b5 = (b2 < 0.01).astype(int)
    b6 = b4 + b5
    print('Finding nearest neighbors')
    a, b7 = np.unravel_index(np.arange(m * n), (m, n))
    b8 = np.hstack((b22.reshape(m * n, b3), np.c_[a, b7] / np.sqrt(m * m + n * n)))
    b9 = sklearn.neighbors.NearestNeighbors(n_neighbors=10, n_jobs=4).fit(b8)
    b10 = b9.kneighbors(b8)[1]
    print('Computing sparse matrix b14')
    b11 = np.repeat(np.arange(m * n), 10)
    b12 = b10.flatten()
    b13 = 1 - np.linalg.norm(b8[b11] - b8[b12], axis=1) / (b3 + 2)
    b14 = scipy.sparse.coo_matrix((b13, (b11, b12)), shape=(m * n, m * n))
    b15 = scipy.sparse.diags(b14.sum(axis=1).A1)
    b16 = b15 - b14
    b17 = scipy.sparse.diags(b6.ravel())
    b18 = b4.ravel()
    b3 = 2 * b1 * b18
    b19 = 2 * (b16 + b1 * b17)
    print('Solving linear system for b20')
    warnings.filterwarnings('error')
    try:
        b20 = np.clip(scipy.sparse.linalg.spsolve(b19, b3), 0, 1).reshape(m, n)
    except Warning:
        b21 = scipy.sparse.linalg.lsqr(b19, b3)
        b20 = np.clip(b21[0], 0, 1).reshape(m, n)
    return b20
def fonk2():
    b22 = imread('donkey.png')[:, :, :3]
    b2 = imread('donkeyTrimap.png')[:, :, :3]
    b20 = fonk1(b22, b2)
    imsave('donkeyAlpha.png', b20)
    plt.title('Alpha Matte')
    plt.imshow(b20, b23 = 'gray')
    plt.show()
if b24 = = '__main__':
    fonk2()