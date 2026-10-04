import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn import decomposition
df = pd.DataFrame(columns=['calory', 'breakfast', 'lunch', 'dinner', 'exercise', 'body_shape'])
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
for i, row in enumerate(data):
    df.loc[i] = row
X = df[['calory', 'breakfast', 'lunch', 'dinner', 'exercise']]
Y = df[['body_shape']]
x_std = StandardScaler().fit_transform(X)
features = x_std.T
covariance_matrix = np.cov(features)
print("Covariance matrix:\n", covariance_matrix)
eig_vals, eig_vecs = np.linalg.eig(covariance_matrix)
print('Eigenvectors \n%s' % eig_vecs)
print('\nEigenvalues \n%s' % eig_vals)
print('Explained variance ratio for the first principal component: ', eig_vals[0] / sum(eig_vals))
projected_X = x_std.dot(eig_vecs.T[0])
result = pd.DataFrame(projected_X, columns=['PC1'])
result['y-axis'] = 0.0
result['label'] = Y
sns.lmplot('PC1', 'y-axis', data=result, fit_reg=False, scatter_kws={"s": 50}, hue='label')
plt.title('PCA result (manual)')
pca = decomposition.PCA(n_components=1)
sklearn_pca_x = pca.fit_transform(x_std)
sklearn_result = pd.DataFrame(sklearn_pca_x, columns=['PC1'])
sklearn_result['y-axis'] = 0.0
sklearn_result['label'] = Y
sns.lmplot('PC1', 'y-axis', data=sklearn_result, fit_reg=False, scatter_kws={"s": 50}, hue='label')
plt.title('PCA result (sklearn)')
plt.show()