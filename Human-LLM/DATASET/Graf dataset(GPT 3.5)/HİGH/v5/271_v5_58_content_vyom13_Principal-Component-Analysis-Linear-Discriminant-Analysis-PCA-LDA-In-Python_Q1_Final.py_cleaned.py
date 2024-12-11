import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
b18 = np.genfromtxt("C:/Users/vyoms/Desktop/dataset_1.csv", delimiter=",")
b2 = b18[1:, :]
b3 = b18[1:, 0]
b4 = b18[1:, 1]
plt.scatter(b3[:30], b4[:30], b5 = 'o', b20='purple', alpha=0.5, label='Class 1')
plt.scatter(b3[30:60], b4[30:60], b5 = 'o', b20='orange', alpha=0.5, label='Class 2')
plt.xlabel('b13')
plt.ylabel('b14')
plt.title('Scatter Plot of b14 vs b13')
plt.legend()
plt.show()
def fonk1(x):
    b6 = x - x.mean(axis=0)
    b7 = np.cov(b6, rowvar=False)
    b10, b8 = np.linalg.eig(b7)
    b9 = np.argsort(b10)[::-1]
    b10 = b10[b9]
    b8 = b8[:, b9]
    b11 = np.matmul(b6, b8)
    b12 = {'b2': x,
                   'mean_centered_data': b6,
                   'PC_variance': b10,
                   'loadings': b8,
                   'scores': b11}
    return b12
b12 = fonk1(b2)
b13 = b3
b14 = b4
mean_V1, b15 = np.mean(b13), np.mean(b14)
b16 = np.sum((b13 - mean_V1) * (b14 - b15))
b17 = np.sum((b13 - mean_V1) ** 2)
b18 = b16 / b17
b19 = b15 - (b18 * mean_V1)
plt.scatter(b13[:30], b14[:30], b5 = 'o', b20='purple', alpha=0.5, label='Class 1')
plt.scatter(b13[30:60], b14[30:60], b5 = 'o', b20='orange', alpha=0.5, label='Class 2')
plt.plot(b13, b19 + b18 * b13, b20 = 'blue', linewidth=2, label='Regression Line')
plt.xlabel('b13')
plt.ylabel('b14')
plt.title('Regression Plot')
plt.legend()
plt.show()
b21 = pd.read_csv('C:/Users/vyoms/Desktop/dataset_1.csv', header=None)
b21 = b21.drop(b21.index[0])
b21 = b21.drop(b21.columns[2], axis=1)
df1, b22 = b21.values[:30, :], b21.values[30:, :]
m_1, b23 = np.mean(df1, axis=0), np.mean(b22, axis=0)
b24 = np.mean(b21, axis=0)
b25 = np.cov((df1 - m_1).T) + np.cov((b22 - b23).T)
b26 = len(df1) * np.outer((m_1 - b24), (m_1 - b24)) + \
                        len(b22) * np.outer((b23 - b24), (b23 - b24))
e_val, b27 = np.linalg.eig(np.dot(np.linalg.inv(b25), b26))
b9 = np.argsort(np.abs(e_val))[::-1]
e_val, b27 = e_val[b9], b27[:, b9]
b28 = b21.values.dot(b27[:, 0])
plt.scatter(b28[:30], np.zeros(30), b5 = 'o', b20='purple', alpha=0.5, label='Class 1')
plt.scatter(b28[30:60], np.zeros(30), b5 = 'o', b20='orange', alpha=0.5, label='Class 2')
plt.title('LDA Projection')
plt.xlabel('LD1')
plt.legend()
plt.show()
b29 = b12['scores'] ** 2
b30 = np.sum(b29, axis=0) / (b29.shape[0] - 1)
b31 = np.sum(b30)
b32 = 100 * b12['PC_variance'][0] / np.sum(b12['PC_variance'])
b33 = 100 * b12['PC_variance'][1] / np.sum(b12['PC_variance'])
b34 = np.cov(b12['scores'][:, 0], b12['scores'][:, 1])
PC1_variance, b35 = np.var(b12['scores'][:, 0]), np.var(b12['scores'][:, 1])
plt.scatter(b12['scores'][:, 0], b12['scores'][:, 1], b20 = 'blue', alpha=0.5)
plt.title('Scree Plot')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.show()
b36 = b12['b2'].dot(b12['loadings'][:, 0])
plt.scatter(b36[:30], b36[:30], b5 = 'o', b20='purple', alpha=0.5, label='Class 1')
plt.scatter(b36[30:60], b36[30:60], b5 = 'o', b20='orange', alpha=0.5, label='Class 2')
plt.title('Regression Plot using PCA Axis')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.legend()
plt.show()