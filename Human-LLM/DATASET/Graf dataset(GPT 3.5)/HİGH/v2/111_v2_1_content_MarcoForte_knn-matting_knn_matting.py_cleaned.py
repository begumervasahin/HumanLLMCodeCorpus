import numpy as np
import sklearn.neighbors
import scipy.sparse
import warnings
import matplotlib.pyplot as plt
import scipy.misc
def fonk1(b2, b3, b1 = 100):
    b2 = b2 / 255.0
    b3 = b3 / 255.0
    b4 = (b3 > 0.99).astype(int)
    b5 = (b3 < 0.01).astype(int)
    b6 = b4 + b5
    print('Finding nearest neighbors')
    [m, n, b19] = b2.shape
    a, b7 = np.unravel_index(np.arange(m * n), (m, n))
    b8 = np.append(np.transpose(b2.reshape(m * n, b19)), [a, b7] / np.sqrt(m * m + n * n), axis=0).T
    b9 = sklearn.neighbors.NearestNeighbors(n_neighbors=10, n_jobs=4).fit(b8)
    b10 = b9.kneighbors(b8)[1]
    print('Computing sparse b14')
    b11 = np.repeat(np.arange(m * n), 10)
    b12 = b10.reshape(m * n * 10)
    b13 = 1 - np.linalg.norm(b8[b11] - b8[b12], axis=1) / (b19 + 2)
    b14 = scipy.sparse.coo_matrix((b13, (b11, b12)), shape=(m * n, m * n))
    b15 = scipy.sparse.diags(np.ravel(b14.sum(axis=1)))
    b16 = b15 - b14
    b17 = scipy.sparse.diags(np.ravel(b6[:, :, 0]))
    b18 = np.ravel(b4[:, :, 0])
    b19 = 2 * b1 * np.transpose(b18)
    b20 = 2 * (b16 + b1 * b17)
    print('Solving linear system for b21')
    warnings.filterwarnings('error')
    b21 = []
    try:
        b21 = np.minimum(np.maximum(scipy.sparse.linalg.spsolve(b20, b19), 0), 1).reshape(m, n)
    except Warning:
        b22 = scipy.sparse.linalg.lsqr(b20, b19)
        b21 = np.minimum(np.maximum(b22[0], 0), 1).reshape(m, n)
    return b21
def fonk2():
    b2 = scipy.misc.imread('donkey.png')[:, :, :3]
    b3 = scipy.misc.imread('donkeyTrimap.png')[:, :, :3]
    b21 = fonk1(b2, b3)
    scipy.misc.imsave('donkeyAlpha.png', b21)
    plt.title('Alpha Matte')
    plt.imshow(b21, b23 = 'gray')
    plt.show()
if b24 = = '__main__':
    fonk2()