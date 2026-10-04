import pandas as pd
import numpy as np
from sklearn.decomposition import PCA as sklearnPCA
from sklearn.preprocessing import StandardScaler
b1 = pd.read_csv("/media/hossam/MyFiles/MachineLearning/PCA/PCA/IrisDataSet/iris.data", header=None, sep=',')
b1.b2 = ['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class']
b1.dropna(b3 = "all", inplace=True)
print(b1.head())
b4 = b1.iloc[:, 0:4].values
b5 = b1.iloc[:, 4].values
b6 = StandardScaler().fit_transform(b4)
b7 = np.mean(b6, axis=0)
b8 = (b6 - b7).T.dot((b6 - b7)) / (b6.shape[0] - 1)
print('Covariance matrix (manual calculation) \n%s' % b8)
b9 = np.cov(b6.T)
print('Covariance matrix (numpy calculation) \n%s' % b9)
eig_vals, b10 = np.linalg.eig(b9)
print('Eigenvectors \n%s' % b10)
print('\nEigenvalues \n%s' % eig_vals)
b11 = np.corrcoef(b6.T)
eig_vals_corr1, b12 = np.linalg.eig(b11)
print('Eigenvectors (correlation matrix 1) \n%s' % b12)
print('\nEigenvalues (correlation matrix 1) \n%s' % eig_vals_corr1)
b13 = np.corrcoef(b4.T)
eig_vals_corr2, b14 = np.linalg.eig(b13)
print('Eigenvectors (correlation matrix 2) \n%s' % b14)
print('\nEigenvalues (correlation matrix 2) \n%s' % eig_vals_corr2)
u, s, b15 = np.linalg.svd(b6.T)
for ev in b10:
    np.testing.assert_array_almost_equal(1.0, np.linalg.norm(ev))
print('Eigenvector verification passed!')
b16 = [(np.abs(eig_vals[i]), b10[:, i]) for i in range(len(eig_vals))]
b16.sort(b17 = lambda x: x[0], reverse=True)
print('Eigenvalues in descending order:')
for eig_val, _ in b16:
    print(eig_val)
b18 = sum(eig_vals)
b19 = [(i / b18) * 100 for i in sorted(eig_vals, reverse=True)]
b20 = np.cumsum(b19)
b21 = np.hstack((b16[0][1].reshape(4, 1), b16[1][1].reshape(4, 1)))
print('Projection matrix W:\n', b21)
b22 = b6.dot(b21)
b23 = sklearnPCA(n_components=2)
b24 = b23.fit_transform(b6)
print('Projected data using scikit-learn PCA:\n', b24)