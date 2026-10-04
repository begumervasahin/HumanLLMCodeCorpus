import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn import decomposition
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
b1.head(10)
b2 = b1[['calory', 'breakfast', 'lunch', 'dinner', 'exercise']]
b2.head(9)
b3 = b1[['body_shape']]
b3.head(10)
from sklearn.preprocessing import StandardScaler
b4 = StandardScaler().fit_transform(b2)
b4
b5 = b4.T
b6 = np.cov(b5)
print(b6)
eig_vals, b7 = np.linalg.eig(b6)
print('Eigenvectors \n%s' %b7)
print('\nEigenvalues \n%s' %eig_vals)
eig_vals[0] / sum(eig_vals)
b8 = b4.dot(b7.T[0])
b8
b9 = pd.DataFrame(b8, columns=['PC1'])
b9['y-axis'] = 0.0
b9['label'] = b3
b9.head(10)
sns.lmplot('PC1', 'y-axis', b10 = b9, fit_reg=False,
           b11 = {"s": 50},
           b12 = "label")
plt.title('PCA b9')
b13 = decomposition.PCA(n_components=1)
b14 = b13.fit_transform(b4)
b15 = pd.DataFrame(b14, columns=['PC1'])
b15['y-axis'] = 0.0
b15['label'] = b3
sns.lmplot('PC1', 'y-axis', b10 = b15, fit_reg=False,
           b11 = {"s": 50},
           b12 = "label")