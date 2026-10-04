import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn import decomposition
b1 = pd.DataFrame(columns=['calory', 'breakfast', 'lunch', 'dinner', 'exercise', 'body_shape'])
b2 = [
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
for i, row in enumerate(b2):
    b1.loc[i] = row
b3 = b1[['calory', 'breakfast', 'lunch', 'dinner', 'exercise']]
b4 = b1[['body_shape']]
b5 = StandardScaler().fit_transform(b3)
b6 = b5.T
b7 = np.cov(b6)
print("Covariance matrix:\n", b7)
eig_vals, b8 = np.linalg.eig(b7)
print('Eigenvectors \n%s' % b8)
print('\nEigenvalues \n%s' % eig_vals)
print('Explained variance ratio for the first principal component: ', eig_vals[0] / sum(eig_vals))
b9 = b5.dot(b8.T[0])
b10 = pd.DataFrame(b9, columns=['PC1'])
b10['y-axis'] = 0.0
b10['label'] = b4
sns.lmplot('PC1', 'y-axis', b2 = b10, fit_reg=False, scatter_kws={"s": 50}, hue='label')
plt.title('PCA b10 (manual)')
b11 = decomposition.PCA(n_components=1)
b12 = b11.fit_transform(b5)
b13 = pd.DataFrame(b12, columns=['PC1'])
b13['y-axis'] = 0.0
b13['label'] = b4
sns.lmplot('PC1', 'y-axis', b2 = b13, fit_reg=False, scatter_kws={"s": 50}, hue='label')
plt.title('PCA b10 (sklearn)')
plt.show()