import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn import decomposition
from sklearn.preprocessing import StandardScaler
b1 = {
    'calory': [1200, 2800, 3500, 1400, 5000, 1300, 3000, 4000, 2600, 3000],
    'breakfast': [1, 1, 2, 0, 2, 0, 1, 2, 0, 1],
    'lunch': [0, 1, 2, 1, 2, 0, 0, 2, 2, 2],
    'dinner': [0, 1, 1, 0, 2, 1, 1, 2, 0, 1],
    'exercise': [2, 1, 0, 3, 0, 2, 1, 0, 0, 1],
    'body_shape': ['Skinny', 'Normal', 'Fat', 'Skinny', 'Fat', 'Skinny', 'Normal', 'Fat', 'Normal', 'Fat']
}
b2 = pd.DataFrame(b1)
b3 = b2[['calory', 'breakfast', 'lunch', 'dinner', 'exercise']]
b4 = b2['body_shape']
b5 = StandardScaler()
b6 = b5.fit_transform(b3)
b7 = np.cov(b6.T)
print("Covariance Matrix:\n", b7)
eig_vals, b8 = np.linalg.eig(b7)
print('Eigenvectors \n', b8)
print('\nEigenvalues \n', eig_vals)
b9 = eig_vals[0] / sum(eig_vals)
print("Explained variance by the first principal component: ", b9)
b10 = b6.dot(b8[:, 0])
b11 = pd.DataFrame(b10, columns=['PC1'])
b11['y-axis'] = 0.0
b11['label'] = b4
sns.lmplot(b12 = 'PC1', y='y-axis', b1=b11, fit_reg=False, scatter_kws={"s": 50}, hue='label')
plt.title('PCA Result')
plt.show()
b13 = decomposition.PCA(n_components=1)
b14 = b13.fit_transform(b6)
b15 = pd.DataFrame(b14, columns=['PC1'])
b15['y-axis'] = 0.0
b15['label'] = b4
sns.lmplot(b12 = 'PC1', y='y-axis', b1=b15, fit_reg=False, scatter_kws={"s": 50}, hue='label')
plt.title('PCA Result using sklearn')
plt.show()