import numpy as np
import sklearn.neighbors
import scipy.sparse
import warnings
import matplotlib.pyplot as plt
from imageio import imread, imwrite
a1 = 10
a2 = 100
def fonk1(b22, b3, b1 = a2):
    m, n, b2 = b22.shape
    b22, b3 = b22 / 255.0, b3 / 255.0
    b4 = (b3 > 0.99).astype(int)
    b5 = (b3 < 0.01).astype(int)
    b6 = b4 + b5
    print('Finding nearest neighbors')
    a, b7 = np.unravel_index(np.arange(m * n), (m, n))
    b8 = np.append(np.transpose(b22.reshape(m * n, b2)), [a, b7] / np.sqrt(m * m + n * n), axis=0).T
    b9 = sklearn.neighbors.NearestNeighbors(n_neighbors=a1, n_jobs=4).fit(b8)
    b10 = b9.kneighbors(b8)[1]
    print('Computing sparse matrix b14')
    b11 = np.repeat(np.arange(m * n), a1)
    b12 = b10.reshape(m * n * a1)
    b13 = 1 - np.linalg.norm(b8[b11] - b8[b12], axis=1) / (b2 + 2)
    b14 = scipy.sparse.coo_matrix((b13, (b11, b12)), shape=(m * n, m * n))
    b15 = scipy.sparse.diags(np.ravel(b14.sum(axis=1)))
    b16 = b15 - b14
    b17 = scipy.sparse.diags(np.ravel(b6[:, :, 0]))
    b18 = np.ravel(b4[:, :, 0])
    b2 = 2 * b1 * np.transpose(b18)
    b19 = 2 * (b16 + b1 * b17)
    print('Solving linear system for b20')
    warnings.filterwarnings('error')
    try:
        b20 = np.clip(scipy.sparse.linalg.spsolve(b19, b2), 0, 1).reshape(m, n)
    except Warning:
        b21 = scipy.sparse.linalg.lsqr(b19, b2)
        b20 = np.clip(b21[0], 0, 1).reshape(m, n)
    return b20
def fonk2():
    b22 = imread('donkey.png')[:, :, :3]
    b3 = imread('donkeyTrimap.png')[:, :, :3]
    b20 = fonk1(b22, b3)
    imwrite('donkeyAlpha.png', (b20 * 255).astype(np.uint8))
    plt.title('Alpha Matte')
    plt.imshow(b20, b23 = 'gray')
    plt.show()
if b24 = = '__main__':
    fonk2()