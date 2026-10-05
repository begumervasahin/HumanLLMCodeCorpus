import numpy as np
import sklearn.neighbors
import scipy.sparse
import warnings
import matplotlib.pyplot as plt
import scipy.misc
def normalize_image(img):
    return img / 255.0
def create_foreground_background_masks(trimap):
    foreground = (trimap > 0.99).astype(int)
    background = (trimap < 0.01).astype(int)
    return foreground, background
def compute_feature_vectors(img):
    [m, n, c] = img.shape
    a, b = np.unravel_index(np.arange(m * n), (m, n))
    feature_vec = np.append(np.transpose(img.reshape(m * n, c)), [a, b] / np.sqrt(m * m + n * n), axis=0).T
    return feature_vec
def find_nearest_neighbors(feature_vec):
    nbrs = sklearn.neighbors.NearestNeighbors(n_neighbors=10, n_jobs=4).fit(feature_vec)
    knns = nbrs.kneighbors(feature_vec)[1]
    return knns
def compute_weight_matrix(feature_vec, knns):
    row_inds = np.repeat(np.arange(m * n), 10)
    col_inds = knns.reshape(m * n * 10)
    vals = 1 - np.linalg.norm(feature_vec[row_inds] - feature_vec[col_inds], axis=1) / (c + 2)
    A = scipy.sparse.coo_matrix((vals, (row_inds, col_inds)), shape=(m * n, m * n))
    return A
def compute_alpha(img, trimap, mylambda=100):
    img = normalize_image(img)
    trimap = normalize_image(trimap)
    foreground, background = create_foreground_background_masks(trimap)
    feature_vec = compute_feature_vectors(img)
    knns = find_nearest_neighbors(feature_vec)
    A = compute_weight_matrix(feature_vec, knns)
    D_script = scipy.sparse.diags(np.ravel(A.sum(axis=1)))
    L = D_script - A
    D = scipy.sparse.diags(np.ravel(all_constraints[:, :, 0]))
    v = np.ravel(foreground[:, :, 0])
    c = 2 * mylambda * np.transpose(v)
    H = 2 * (L + mylambda * D)
    warnings.filterwarnings('error')
    alpha = []
    try:
        alpha = np.minimum(np.maximum(scipy.sparse.linalg.spsolve(H, c), 0), 1).reshape(m, n)
    except Warning:
        x = scipy.sparse.linalg.lsqr(H, c)
        alpha = np.minimum(np.maximum(x[0], 0), 1).reshape(m, n)
    return alpha
def main():
    img = scipy.misc.imread('donkey.png')[:, :, :3]
    trimap = scipy.misc.imread('donkeyTrimap.png')[:, :, :3]
    alpha = compute_alpha(img, trimap)
    scipy.misc.imsave('donkeyAlpha.png', alpha)
    plt.title('Alpha Matte')
    plt.imshow(alpha, cmap='gray')
    plt.show()
if __name__ == '__main__':
    main()