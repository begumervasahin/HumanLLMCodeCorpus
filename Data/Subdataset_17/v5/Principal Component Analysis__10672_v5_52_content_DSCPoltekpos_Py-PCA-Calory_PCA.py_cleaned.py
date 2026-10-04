import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn import decomposition
from sklearn.preprocessing import StandardScaler
data = {
    'calory': [1200, 2800, 3500, 1400, 5000, 1300, 3000, 4000, 2600, 3000],
    'breakfast': [1, 1, 2, 0, 2, 0, 1, 2, 0, 1],
    'lunch': [0, 1, 2, 1, 2, 0, 0, 2, 2, 2],
    'dinner': [0, 1, 1, 0, 2, 1, 1, 2, 0, 1],
    'exercise': [2, 1, 0, 3, 0, 2, 1, 0, 0, 1],
    'body_shape': ['Skinny', 'Normal', 'Fat', 'Skinny', 'Fat', 'Skinny', 'Normal', 'Fat', 'Normal', 'Fat']
}
df = pd.DataFrame(data)
X = df[['calory', 'breakfast', 'lunch', 'dinner', 'exercise']]
Y = df['body_shape']
scaler = StandardScaler()
x_std = scaler.fit_transform(X)
covariance_matrix = np.cov(x_std.T)
print("Covariance Matrix:\n", covariance_matrix)
eig_vals, eig_vecs = np.linalg.eig(covariance_matrix)
print('Eigenvectors \n', eig_vecs)
print('\nEigenvalues \n', eig_vals)
explained_variance = eig_vals[0] / sum(eig_vals)
print("Explained variance by the first principal component: ", explained_variance)
projected_X = x_std.dot(eig_vecs[:, 0])
result = pd.DataFrame(projected_X, columns=['PC1'])
result['y-axis'] = 0.0
result['label'] = Y
sns.lmplot(x='PC1', y='y-axis', data=result, fit_reg=False, scatter_kws={"s": 50}, hue='label')
plt.title('PCA Result')
plt.show()
pca = decomposition.PCA(n_components=1)
sklearn_pca_x = pca.fit_transform(x_std)
sklearn_result = pd.DataFrame(sklearn_pca_x, columns=['PC1'])
sklearn_result['y-axis'] = 0.0
sklearn_result['label'] = Y
sns.lmplot(x='PC1', y='y-axis', data=sklearn_result, fit_reg=False, scatter_kws={"s": 50}, hue='label')
plt.title('PCA Result using sklearn')
plt.show()