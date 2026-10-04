import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
data = [
    [1200, 1, 0, 0, 2, 'Skinny'],
    [2800, 1, 1, 1, 1, 'Normal'],
    [3500, 2, 2, 1, 0, 'Fat'],
    [1400, 0, 1, 0, 3, 'Skinny'],
    [5000, 2, 2, 2, 0, 'Fat'],
    [1300, 0, 0, 1, 2, 'Skinny'],
    [3000, 1, 0, 1, 1, 'Normal'],
    [4000, 2, 2, 2, 0, 'Fat'],
    [2600, 0, 2, 0, 0, 'Normal'],
    [3000, 1, 2, 1, 1, 'Fat']
]
columns = ['calory', 'breakfast', 'lunch', 'dinner', 'exercise', 'body_shape']
df = pd.DataFrame(data, columns=columns)
X = df[['calory', 'breakfast', 'lunch', 'dinner', 'exercise']]
Y = df['body_shape']
scaler = StandardScaler()
x_std = scaler.fit_transform(X)
covariance_matrix = np.cov(x_std.T)
print("Covariance matrix:\n", covariance_matrix)
eig_vals, eig_vecs = np.linalg.eig(covariance_matrix)
print('Eigenvectors:\n', eig_vecs)
print('\nEigenvalues:\n', eig_vals)
explained_variance_ratio = eig_vals[0] / sum(eig_vals)
print('Explained variance ratio for the first principal component:', explained_variance_ratio)
projected_X = x_std.dot(eig_vecs.T[0])
manual_pca_result = pd.DataFrame(projected_X, columns=['PC1'])
manual_pca_result['y-axis'] = 0.0
manual_pca_result['label'] = Y
sns.lmplot(x='PC1', y='y-axis', data=manual_pca_result, fit_reg=False, scatter_kws={"s": 50}, hue='label')
plt.title('PCA result (manual)')
plt.show()
pca = PCA(n_components=1)
sklearn_pca_x = pca.fit_transform(x_std)
sklearn_pca_result = pd.DataFrame(sklearn_pca_x, columns=['PC1'])
sklearn_pca_result['y-axis'] = 0.0
sklearn_pca_result['label'] = Y
sns.lmplot(x='PC1', y='y-axis', data=sklearn_pca_result, fit_reg=False, scatter_kws={"s": 50}, hue='label')
plt.title('PCA result (sklearn)')
plt.show()