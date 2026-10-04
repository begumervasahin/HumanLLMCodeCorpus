import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn import decomposition
from sklearn.preprocessing import StandardScaler
b1 = pd.DataFrame(columns=['calory', 'breakfast', 'lunch', 'dinner', 'exercise', 'body_shape'])
b1.loc[0] = [1200, 1, 0, 0, 2, 'Skinny']
b1.loc[1] = [2800, 1, 1, 1, 1, 'Normal']
b1.loc[2] = [3500, 2, 2, 1, 0, 'Fat']
b1.loc[3] = [1400, 0, 1, 0, 3, 'Skinny']
b1.loc[4] = [5000, 2, 2, 2, 0, 'Fat']
b1.loc[5] = [1300, 0, 0, 1, 2, 'Skinny']
b1.loc[6] = [3000, 1, 0, 1, 1, 'Normal']
b1.loc[7] = [4000, 2, 2, 2, 0, 'Fat']
b1.loc[8] = [2600, 0, 2, 0, 0, 'Normal']
b1.loc[9] = [3000, 1, 2, 1, 1, 'Fat']
b2 = b1[['calory', 'breakfast', 'lunch', 'dinner', 'exercise']]
b3 = b1[['body_shape']]
b4 = StandardScaler()
b5 = b4.fit_transform(b2)
b6 = b5.T
b7 = np.cov(b6)
print("Covariance Matrix:\n", b7)
eig_vals, b8 = np.linalg.eig(b7)
print('Eigenvectors \n', b8)
print('\nEigenvalues \n', eig_vals)
b9 = eig_vals[0] / sum(eig_vals)
print("Explained variance by the first principal component: ", b9)
b10 = b5.dot(b8.T[0])
b11 = pd.DataFrame(b10, columns=['PC1'])
b11['y-axis'] = 0.0
b11['label'] = b3
sns.lmplot(b12 = 'PC1', y='y-axis', data=b11, fit_reg=False, scatter_kws={"s": 50}, hue='label')
plt.title('PCA Result')
plt.show()
b13 = decomposition.PCA(n_components=1)
b14 = b13.fit_transform(b5)
b15 = pd.DataFrame(b14, columns=['PC1'])
b15['y-axis'] = 0.0
b15['label'] = b3
sns.lmplot(b12 = 'PC1', y='y-axis', data=b15, fit_reg=False, scatter_kws={"s": 50}, hue='label')
plt.title('PCA Result using sklearn')
plt.show()