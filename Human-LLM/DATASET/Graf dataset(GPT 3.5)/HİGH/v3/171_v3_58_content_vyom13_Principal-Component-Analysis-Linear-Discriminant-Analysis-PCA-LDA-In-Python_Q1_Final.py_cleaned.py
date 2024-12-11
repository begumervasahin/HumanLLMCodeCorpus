import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
b1 = np.genfromtxt("C:/Users/vyoms/Desktop/dataset_1.csv", delimiter=",")[1:]
b2 = b1[:, 0]
b3 = b1[:, 1]
plt.scatter(b2[:30], b3[:30], b4 = 'o', b13='purple', alpha=0.5, label='Class 1')
plt.scatter(b2[30:60], b3[30:60], b4 = 'o', b13='orange', alpha=0.5, label='Class 2')
plt.xlabel('V1')
plt.ylabel('V2')
plt.title('Scatter Plot of V2 vs V1')
plt.legend()
plt.show()
def fonk1(x):
    b5 = np.mean(x, axis=0)
    b6 = x - b5
    b7 = np.cov(b6, rowvar=False)
    b10, b8 = np.linalg.eig(b7)
    b9 = np.argsort(b10)[::-1]
    b10 = b10[b9]
    b8 = b8[:, b9]
    b11 = np.dot(b6, b8)
    return {'PC_variance': b10, 'loadings': b8, 'scores': b11}
b12 = fonk1(b1)
plt.title('Regression Plot Using PCA Loadings')
plt.scatter(b2[:30], b3[:30], b4 = 'o', b13='purple', alpha=0.5, label='Class 1')
plt.scatter(b2[30:60], b3[30:60], b4 = 'o', b13='orange', alpha=0.5, label='Class 2')
plt.plot([0, 100 * b12['loadings'][0, 0]], [0, 100 * b12['loadings'][1, 0]],
         b13 = 'blue', linewidth=3, label='Principal Component 1')
plt.xlabel('V1')
plt.ylabel('V2')
plt.xlim(0, 40)
plt.ylim(0, 40)
plt.legend()
plt.show()
b14 = pd.read_csv("C:/Users/vyoms/Desktop/dataset_1.csv", header=None).iloc[1:, :].astype(float)
df1, b15 = b14.iloc[:30], b14.iloc[30:]
mean_all, mean_1, b16 = b14.mean(), df1.mean(), b15.mean()
b17 = ((df1 - mean_1).T @ (df1 - mean_1)) + ((b15 - b16).T @ (b15 - b16))
b18 = (len(df1) * (mean_1 - mean_all).reshape(-1, 1) @ (mean_1 - mean_all).reshape(1, -1)) + \
                        (len(b15) * (b16 - mean_all).reshape(-1, 1) @ (b16 - mean_all).reshape(1, -1))
eig_vals, b19 = np.linalg.eig(np.linalg.inv(b17) @ b18)
b20 = b19[:, np.argmax(eig_vals)]
b21 = b14 @ b20
plt.figure()
plt.title('LDA Projection')
plt.scatter(b21[:30], np.zeros(30), b4 = 'o', b13='purple', alpha=0.5, label='Class 1')
plt.scatter(b21[30:], np.zeros(30), b4 = 'o', b13='orange', alpha=0.5, label='Class 2')
plt.xlabel('LD1')
plt.ylabel('')
plt.legend()
plt.show()
b22 = np.var(b12['scores'], axis=0)
b23 = np.sum(b22)
b24 = (b22 / b23) * 100
for i, pc_variance in enumerate(b24, b25 = 1):
    print(f"PC{i} explains: {pc_variance:.2f}% variance")
b26 = np.cov(b12['scores'][:, 0], b12['scores'][:, 1])
PC1_variance, b27 = np.var(b12['scores'][:, 0]), np.var(b12['scores'][:, 1])
print("Covariance between PC1 and PC2:", b26)
print("Variance of PC1:", PC1_variance)
print("Variance of PC2:", b27)
plt.figure()
plt.title('Scree Plot')
plt.scatter(b12['scores'][:, 0], b12['scores'][:, 1], b13 = 'blue')
plt.xlabel('PC1 Scores')
plt.ylabel('PC2 Scores')
plt.show()