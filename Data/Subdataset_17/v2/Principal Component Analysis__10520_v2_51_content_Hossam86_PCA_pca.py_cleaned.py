import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.decomposition import PCA as sklearnPCA
df = pd.read_csv('/media/hossam/MyFiles/MachineLearning/PCA/PCA/IrisDataSet/iris.data', header=None, sep=',')
df.columns = ['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class']
df.dropna(how="all", inplace=True)
print("First 5 rows of the dataset:\n", df.head())
X = df.iloc[:, 0:4].values
y = df.iloc[:, 4].values
X_std = StandardScaler().fit_transform(X)
cov_mat = np.cov(X_std.T)
print('Covariance matrix:\n', cov_mat)
eig_vals, eig_vecs = np.linalg.eig(cov_mat)
print('Eigenvectors:\n', eig_vecs)
print('Eigenvalues:\n', eig_vals)
u, s, v = np.linalg.svd(X_std.T)
for ev in eig_vecs:
    np.testing.assert_array_almost_equal(1.0, np.linalg.norm(ev))
print('Eigenvector validation: Everything is ok!')
eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:, i]) for i in range(len(eig_vals))]
eig_pairs.sort(key=lambda x: x[0], reverse=True)
print('Eigenvalues in descending order:')
for eig_val, eig_vec in eig_pairs:
    print(eig_val)
total_eig_val = sum(eig_vals)
var_exp = [(i / total_eig_val) * 100 for i in sorted(eig_vals, reverse=True)]
cum_var_exp = np.cumsum(var_exp)
matrix_w = np.hstack((eig_pairs[0][1].reshape(4, 1), eig_pairs[1][1].reshape(4, 1)))
print('Projection matrix W:\n', matrix_w)
Y = X_std.dot(matrix_w)
sklearn_pca = sklearnPCA(n_components=2)
Y_sklearn = sklearn_pca.fit_transform(X_std)
print("Projection by manual PCA:\n", Y[:5])
print("Projection by sklearn PCA:\n", Y_sklearn[:5])