from sklearn.decomposition import PCA as sklearnPCA
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
b1 = pd.read_csv(
    b2 = "/media/hossam/MyFiles/MachineLearning/PCA/PCA/IrisDataSet/iris.data", header=None, sep=',')
b1.b3 = ['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class']
b1.dropna(b4 = "all", inplace=True)
print(b1.head())
b5 = b1.ix[:, 0:4].values
b6 = b1.ix[:, 4]
b7 = StandardScaler().fit_transform(b5)
b8 = np.mean(b7, axis=0)
b9 = (b7-b8).T.dot((b7-b8))/(b7.shape[0]-1)
print('Covariance matrix \n%s' % b9)
b9 = np.cov(b7.T)
eig_vals, b10 = np.linalg.eig(b9)
print('Eigenvectors \n%s' % b10)
print('\nEigenvalues \n%s' % eig_vals)
b11 = np.corrcoef(b7.T)
eig_vals, b10 = np.linalg.eig(b11)
print('Eigenvectors \n%s' % b10)
print('\nEigenvalues \n%s' % eig_vals)
b12 = np.corrcoef(b5.T)
eig_vals, b10 = np.linalg.eig(b12)
print('Eigenvectors \n%s' % b10)
print('\nEigenvalues \n%s' % eig_vals)
u, s, b13 = np.linalg.svd(b7.T)
for ev in b10:
    np.testing.assert_array_almost_equal(1.0, np.linalg.norm(ev))
print('Everything ok!')
b14 = [(np.abs(eig_vals[i]), b10[:, i])
             for i in range(len(eig_vals))]
b14.sort()
b14.reverse()
print('Eigenvalues in descending order:')
for i in b14:
    print(i[0])
b15 = sum(eig_vals)
b16 = [(i / b15)*100 for i in sorted(eig_vals, reverse=True)]
b17 = np.cumsum(b16)
b18 = np.hstack((b14[0][1].reshape(4, 1),
                      b14[1][1].reshape(4, 1)))
print('Matrix W:\n', b18)
b19 = b7.dot(b18)
b20 = sklearnPCA(n_components=2)
b21 = b20.fit_transform(b7)