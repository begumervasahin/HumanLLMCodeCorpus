import numpy as np
import sklearn.neighbors
import scipy.sparse
import warnings
import matplotlib.pyplot as plt
import scipy.misc
def normalize(img):
    return img / 255.0
def create_masks(trimap):
    foreground = (trimap > 0.99).astype(int)
    background = (trimap < 0.01).astype(int)
    return foreground, background
def find_nearest_neighbors(img_norm, m, n):
    a, b = np.unravel_index(np.arange(m * n), (m, n))
    feature_vec = np.append(np.transpose(img_norm.reshape(m * n, -1)), [a, b] / np.sqrt(m * m + n * n), axis=0).T
    nbrs = sklearn.neighbors.NearestNeighbors(n_neighbors=10, n_jobs=4).fit(feature_vec)
    return nbrs.kneighbors(feature_vec)[1]
def compute_sparse_A(img_norm, knns, m, n):
    row_inds = np.repeat(np.arange(m * n), 10)
    col_inds = knns.reshape(m * n * 10)
    vals = 1 - np.linalg.norm(feature_vec[row_inds] - feature_vec[col_inds], axis=1) / (img_norm.shape[-1] + 2)
    return scipy.sparse.coo_matrix((vals, (row_inds, col_inds)), shape=(m * n, m * n))
def solve_linear_system(H, c):
    try:
        alpha = np.minimum(np.maximum(scipy.sparse.linalg.spsolve(H, c), 0), 1)
    except Warning:
        x = scipy.sparse.linalg.lsqr(H, c)
        alpha = np.minimum(np.maximum(x[0], 0), 1)
    return alpha
def knn_matte(img, trimap, mylambda=100):
    img_norm, trimap_norm = normalize(img), normalize(trimap)
    foreground, background = create_masks(trimap_norm)
    all_constraints = foreground + background
    m, n, c = img.shape
    knns = find_nearest_neighbors(img_norm, m, n)
    A = compute_sparse_A(img_norm, knns, m, n)
    D_script = scipy.sparse.diags(np.ravel(A.sum(axis=1)))
    L = D_script - A
    D = scipy.sparse.diags(np.ravel(all_constraints[:, :, 0]))
    v = np.ravel(foreground[:, :, 0])
    c = 2 * mylambda * np.transpose(v)
    H = 2 * (L + mylambda * D)
    alpha = solve_linear_system(H, c).reshape(m, n)
    return alpha
def main():
    img = scipy.misc.imread('donkey.png')[:, :, :3]
    trimap = scipy.misc.imread('donkeyTrimap.png')[:, :, :3]
    alpha = knn_matte(img, trimap)
    scipy.misc.imsave('donkeyAlpha.png', alpha)
    plt.title('Alpha Matte')
    plt.imshow(alpha, cmap='gray')
    plt.show()
if __name__ == '__main__':
    main()