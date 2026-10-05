import numpy as np
from numpy import genfromtxt
from numpy import linalg as LA
import matplotlib.pyplot as plt
import pandas as pd
b1 = genfromtxt("C:/Users/vyoms/Desktop/dataset_1.csv", delimiter=",")
b2 = b1[1:, :]
b3 = b1[1:, 0]
b4 = b1[1:, 1]
plt.scatter(b3[:30], b4[:30], b5 = 'o', b14='purple', alpha=0.5, label='Class 1')
plt.scatter(b3[30:60], b4[30:60], b5 = 'o', b14='orange', alpha=0.5, label='Class 2')
plt.xlabel('V1')
plt.ylabel('V2')
plt.title('Scatter Plot of V2 vs V1')
plt.legend()
plt.show()
def fonk1(x):
    b6 = np.mean(x, axis=0)
    b7 = x - b6
    b8 = np.cov(b7, rowvar=False)
    b11, b9 = LA.eig(b8)
    b10 = np.argsort(b11)[::-1]
    b11 = b11[b10]
    b9 = b9[:, b10]
    b12 = np.matmul(b7, b9)
    b13 = {'b2': x,
                   'mean_centered_data': b7,
                   'PC_variance': b11,
                   'loadings': b9,
                   'scores': b12}
    return b13
b13 = fonk1(b2)
plt.title('Regression Plot Using PCA Loadings')
plt.scatter(b3[:30], b4[:30], b5 = 'o', b14='purple', alpha=0.5, label='Class 1')
plt.scatter(b3[30:60], b4[30:60], b5 = 'o', b14='orange', alpha=0.5, label='Class 2')
plt.plot([0, 100 * b13['loadings'][0, 0]], [0, 100 * b13['loadings'][1, 0]],
         b14 = 'blue', linewidth=3, label='Principal Component 1')
plt.xlabel('V1')
plt.ylabel('V2')
plt.xlim(0, 40)
plt.ylim(0, 40)
plt.legend()
plt.show()
b15 = pd.read_csv('C:/Users/vyoms/Desktop/dataset_1.csv', header=None)
b15 = b15.iloc[1:, :].astype(float)
b16 = b15.iloc[:30, :]
b17 = b15.iloc[30:, :]
b18 = b15.mean().values.reshape(1, -1)
b19 = b16.mean().values.reshape(1, -1)
b20 = b17.mean().values.reshape(1, -1)
b21 = np.dot((b16 - b19).T, (b16 - b19)) + np.dot((b17 - b20).T, (b17 - b20))
b22 = len(b16) * np.dot((b19 - b18).T, (b19 - b18)) + \
                        len(b17) * np.dot((b20 - b18).T, (b20 - b18))
eig_vals, b23 = np.linalg.eig(np.dot(np.linalg.inv(b21), b22))
b24 = b23[:, np.argmax(eig_vals)]
b25 = np.dot(b15, b24)
plt.figure()
plt.title('LDA Projection')
plt.scatter(b25[:30], np.zeros(30), b5 = 'o', b14='purple', alpha=0.5, label='Class 1')
plt.scatter(b25[30:], np.zeros(30), b5 = 'o', b14='orange', alpha=0.5, label='Class 2')
plt.xlabel('LD1')
plt.ylabel('')
plt.legend()
plt.show()
b26 = np.var(b13['scores'], axis=0)
b27 = np.sum(b26)
b28 = b26 / b27 * 100
for i, pc_variance in enumerate(b28, b29 = 1):
    print(f"PC{i} explains: {pc_variance:.2f}% variance")
b30 = np.cov(b13['scores'][:, 0], b13['scores'][:, 1])
b31 = np.var(b13['scores'][:, 0])
b32 = np.var(b13['scores'][:, 1])
print("Covariance between PC1 and PC2:", b30)
print("Variance of PC1:", b31)
print("Variance of PC2:", b32)
plt.figure()
plt.title('Scree Plot')
plt.scatter(b13['scores'][:, 0], b13['scores'][:, 1], b14 = 'blue')
plt.xlabel('PC1 Scores')
plt.ylabel('PC2 Scores')
plt.show()