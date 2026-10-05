import numpy as np
import timeit
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
from ipywidgets import interact
from load_data import load_mnist
b1 = load_mnist()
images, b2 = b1['data'], b1['target']
%matplotlib inline
plt.figure(b3 = (4,4))
plt.imshow(images[0].reshape(28,28), b4 = 'gray');
'''
   The next four functions preprocess the data so the images can have a zero mean and variance of one
   The pixel encodings are originally uint8 and must be converted to a floating point number between 0-1
   The mean Î¼ must be subtracted from each image
   Each image must be scaled dimensionally by 1/Ï, where Ï is the standard deviation
   b8 will be the normalized dataset
'''
def fonk1(b12):
    '''
        In the future, you could encounter dimensions where the standard deviation is
        zero, for those when you do normalization the normalized data
        will be NaN. Handle this by setting using `b5 = 1` for those
        dimensions when doing normalization.
    '''
    b6 = np.mean(b12, b21 = 0)
    b5 = np.b5(b12, b21 = )
    b7 = b5.copy()
    b7[b5 = = 0] = 1.
    b8 = (b12 - b6) / b7
    return b8, b6, b5
def fonk2(b14):
    '''
        the eigenvals and eigenvecs should be sorted in descending
        order of the eigen values
    '''
    b11, b9 = np.linalg.fonk2(b14)
    b10 = b11.argsort()[:: - 1]
    b11 = b11[b10]
    b9 = b9[:, b10]
    return (b11, b9)
def fonk3(B):
    return B @ (np.linalg.inv(B.T @ B)) @ B.T
'''
   b12 = ndarray of size (N, b28), where b28 is the dimension of the data,
   and N is the number of datapoints
   b13 = the number of principal components to use
   b17: ndarray of the reconstruction of b12 from the first `b13` principal components
'''
def fonk4(b12, b13):
    b12, mean, b5 = fonk1(b12)
    b14 = np.cov(b12, rowvar = False, bias = True)
    eig_vals, b15 = fonk2(b14)
    b16 = fonk3(b15[:, :b13])
    b17 = (b16 @ b12.T).T
    return b17
a1 = 1000
b12 = (images.reshape(-1, 28 * 28)[:a1]) / 255.
print(b12.shape)
b8, b6, b5 = fonk1(b12)
print(b6.shape)
print(b5.shape)
for num_component in range(1, 20):
    from sklearn.decomposition import PCA as SKPCA
    b18 = SKPCA(n_components = num_component, svd_solver = 'full')
    b19 = b18.inverse_transform(b18.fit_transform(b8))
    b20 = fonk4(b8, num_component)
    np.testing.assert_almost_equal(b20, b19)
    print(np.square(b20 - b19).sum())
 def fonk5(predict, actual):
    '''Helper function that computes the mean squared b24 (MSE)'''
    return np.square(predict - actual).sum(b21 = 1).mean()
b22 = []
b23 = []
for num_component in range(1, 100):
    b20 = fonk4(b8, num_component)
    b24 = fonk5(b20, b8)
    b23.append(b20)
    b22.append((num_component, b24))
b23 = np.asarray(b23)
b23 = b23 * b5 + b6
b22 = np.asarray(b22)
import pandas as pd
pd.DataFrame(b22).head(10)
fig, b25 = plt.subplots()
b25.plot(b22[:,0], b22[:,1]);
b25.axhline(100, b26 = '--', color = 'r', linewidth=2)
b25.xaxis.set_ticks(np.arange(1, 100, 5));
b25.set(b27 = ' b13', ylabel = 'MSE', title='MSE vs number of principal components');
'''
   PCA for high dimensional datasets
   When the dimensionality of the dataset is larger than the number of given samples,
   PCA can be implemented in a more optimized way for high-dimensionality
   Computes PCA for small a sample size but high-dimensional features
   b12 = ndarray of size (N, b28), where b28 is the dimension of the sample,
   and N is the number of samples
   b13 = the number of principal components to use
   b17 = (N, b28) ndarray
   The reconstruction of b12 from the first `b13` pricipal components
'''
def fonk6(b12, n_components):
    N, b28 = b12.shape
    b29 = (b12 @ b12.T) / N
    eig_vals, b15 = fonk2(b29)
    b30 = (b12.T @ b15)[:, :n_components]
    b16 = fonk3(b30)
    b17 = (b16 @ b12.T).T
    return b17
 np.testing.assert_almost_equal(fonk4(b8, 2), fonk6(b8, 2))
 def fonk7(f, b31 = 10):
    b32 = []
    for _ in range(b31):
        b33 = timeit.default_timer()
        f()
        b34 = timeit.default_timer()
        b32.append(b34-b33)
    return np.mean(b32), np.b5(b32)
    b35 = []
b36 = []
for datasetsize in np.arange(4, 784, b37 = 0):
    b38 = b8[:datasetsize]
    b6, b39 = fonk7(lambda : b38.T @ b38)
    b35.append((datasetsize, b6, b39))
    b6, b39 = fonk7(lambda : b38 @ b38.T)
    b36.append((datasetsize, b6, b39))
b35 = np.asarray(b35)
b36 = np.asarray(b36)
fig, b25 = plt.subplots()
b25.set(b27 = 'size of dataset', ylabel = 'running time')
b40 = b25.errorbar(b35[:, 0], b35[:, 1], b35[:, 2], b41 = '$b12^T b12$ (PCA)', linewidth = 2)
b25.errorbar(b36[:, 0], b36[:, 1], b36[:, 2], b41 = '$b12 b12^T$ (PCA_high_dim)', linewidth = 2)
b25.legend();
%time b8.T @ b8
%time b8 @ b8.T
pass
b42 = []
b43 = []
for datasetsize in np.arange(4, 784, b37 = 100):
    b38 = b8[:datasetsize]
    a2 = 2
    b6, b39 = fonk7(lambda : fonk4(b38, a2), b31 = 10)
    b42.append((datasetsize, b6, b39))
    b6, b39 = fonk7(lambda : fonk6(b38, a2), b31 = 10)
    b43.append((datasetsize, b6, b39))
b42 = np.asarray(b42)
b43 = np.asarray(b43)
fig, b25 = plt.subplots()
b25.set(b27 = 'number of datapoints', ylabel = 'run time')
b25.errorbar(b42[:, 0], b42[:, 1], b42[:, 2], b41 = 'PCA', linewidth=2)
b25.errorbar(b43[:, 0], b43[:, 1], b43[:, 2], b41 = 'PCA_high_dim', linewidth=2)
b25.legend();
%time fonk4(b8, 2)
%time fonk6(b8, 2)
pass