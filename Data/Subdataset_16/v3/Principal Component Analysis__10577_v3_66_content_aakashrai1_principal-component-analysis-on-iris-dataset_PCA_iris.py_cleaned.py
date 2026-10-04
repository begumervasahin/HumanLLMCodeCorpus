import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
b1 = pd.read_csv('iris-data.csv', sep=',', names=['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class'])
b2 = b1[['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid']]
b3 = StandardScaler()
b4 = b3.fit_transform(b2)
b5 = np.cov(b4, rowvar=False)
eigenvalues, b6 = np.linalg.eig(b5)
b7 = [(np.abs(eigenvalues[i]), b6[:, i]) for i in range(len(eigenvalues))]
b7.sort(b8 = lambda x: x[0], reverse=True)
b9 = np.hstack((b7[0][1].reshape(-1, 1), b7[1][1].reshape(-1, 1)))
b10 = b4.dot(b9)
b11 = pd.DataFrame(data=b10, columns=['PCA1', 'PCA2'])
b12 = pd.concat([b11, b1[['class']]], axis=1)
plt.figure(b13 = (7, 7))
b14 = plt.gca()
b14.set_facecolor('white')
b14.set_xlabel('PCA 1', b15 = 12)
b14.set_ylabel('PCA 2', b15 = 12)
b14.set_title('PCA on Iris dataset', b15 = 15)
b16 = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
b17 = ['y', 'b', 'r']
for class_name, color in zip(b16, b17):
    b18 = b12[b12['class'] == class_name]
    b14.scatter(b18['PCA1'], b18['PCA2'], b19 = color, s=50, label=class_name)
b14.legend(b20 = 'upper right')
b14.grid(b21 = 0.5)
plt.savefig('PCA_fig.png', b22 = 200)
plt.show()