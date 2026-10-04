import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
b1 = [
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
b2 = ['calory', 'breakfast', 'lunch', 'dinner', 'exercise', 'body_shape']
b3 = pd.DataFrame(b1, b2=b2)
b4 = b3[['calory', 'breakfast', 'lunch', 'dinner', 'exercise']]
b5 = b3['body_shape']
b6 = StandardScaler()
b7 = b6.fit_transform(b4)
b8 = np.cov(b7.T)
print("Covariance matrix:\n", b8)
eig_vals, b9 = np.linalg.eig(b8)
print('Eigenvectors \n', b9)
print('\nEigenvalues \n', eig_vals)
print('Explained variance ratio for the first principal component:', eig_vals[0] / sum(eig_vals))
b10 = b7.dot(b9.T[0])
b11 = pd.DataFrame(b10, b2=['PC1'])
b11['y-axis'] = 0.0
b11['label'] = b5
sns.lmplot(b12 = 'PC1', y='y-axis', b1=b11, fit_reg=False, scatter_kws={"s": 50}, hue='label')
plt.title('PCA result (manual)')
b13 = PCA(n_components=1)
b14 = b13.fit_transform(b7)
b15 = pd.DataFrame(b14, b2=['PC1'])
b15['y-axis'] = 0.0
b15['label'] = b5
sns.lmplot(b12 = 'PC1', y='y-axis', b1=b15, fit_reg=False, scatter_kws={"s": 50}, hue='label')
plt.title('PCA result (sklearn)')
plt.show()