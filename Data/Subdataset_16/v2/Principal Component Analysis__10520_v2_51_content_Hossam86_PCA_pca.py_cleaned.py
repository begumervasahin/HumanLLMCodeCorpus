import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.decomposition import PCA as sklearnPCA
b1 = pd.read_csv('/media/hossam/MyFiles/MachineLearning/PCA/PCA/IrisDataSet/iris.data', header=None, sep=',')
b1.b2 = ['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class']
b1.dropna(b3 = "all", inplace=True)
print("First 5 rows of the dataset:\n", b1.head())
b4 = b1.iloc[:, 0:4].values
b5 = b1.iloc[:, 4].values
b6 = StandardScaler().fit_transform(b4)
b7 = np.cov(b6.T)
print('Covariance matrix:\n', b7)
eig_vals, b8 = np.linalg.eig(b7)
print('Eigenvectors:\n', b8)
print('Eigenvalues:\n', eig_vals)
u, s, b9 = np.linalg.svd(b6.T)
for ev in b8:
    np.testing.assert_array_almost_equal(1.0, np.linalg.norm(ev))
print('Eigenvector validation: Everything is ok!')
b10 = [(np.abs(eig_vals[i]), b8[:, i]) for i in range(len(eig_vals))]
b10.sort(b11 = lambda x: x[0], reverse=True)
print('Eigenvalues in descending order:')
for eig_val, eig_vec in b10:
    print(eig_val)
b12 = sum(eig_vals)
b13 = [(i / b12) * 100 for i in sorted(eig_vals, reverse=True)]
b14 = np.cumsum(b13)
b15 = np.hstack((b10[0][1].reshape(4, 1), b10[1][1].reshape(4, 1)))
print('Projection matrix W:\n', b15)
b16 = b6.dot(b15)
b17 = sklearnPCA(n_components=2)
b18 = b17.fit_transform(b6)
print("Projection by manual PCA:\n", b16[:5])
print("Projection by sklearn PCA:\n", b18[:5])