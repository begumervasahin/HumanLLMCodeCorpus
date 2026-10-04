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
print('Covariance matrix \n%s' % b8)
b8 = np.cov(b6.T)
eig_vals, b9 = np.linalg.eig(b8)
print('Eigenvectors \n%s' % b9)
print('\nEigenvalues \n%s' % eig_vals)
b10 = np.corrcoef(b6.T)
eig_vals, b9 = np.linalg.eig(b10)
print('Eigenvectors \n%s' % b9)
print('\nEigenvalues \n%s' % eig_vals)
b11 = np.corrcoef(b4.T)
eig_vals, b9 = np.linalg.eig(b11)
print('Eigenvectors \n%s' % b9)
print('\nEigenvalues \n%s' % eig_vals)
u, s, b12 = np.linalg.svd(b6.T)
for ev in b9:
    np.testing.assert_array_almost_equal(1.0, np.linalg.norm(ev))
print('Everything ok!')
b13 = [(np.abs(eig_vals[i]), b9[:, i]) for i in range(len(eig_vals))]
b13.sort(b14 = lambda x: x[0], reverse=True)
print('Eigenvalues in descending order:')
for eig_val, _ in b13:
    print(eig_val)
b15 = sum(eig_vals)
b16 = [(i / b15) * 100 for i in sorted(eig_vals, reverse=True)]
b17 = np.cumsum(b16)
b18 = np.hstack((b13[0][1].reshape(4, 1), b13[1][1].reshape(4, 1)))
print('Matrix W:\n', b18)
b19 = b6.dot(b18)
b20 = sklearnPCA(n_components=2)
b21 = b20.fit_transform(b6)