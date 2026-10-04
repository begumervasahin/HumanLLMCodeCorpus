import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
b1 = pd.read_csv('iris-data.csv', sep=',', names=['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class'])
b2 = b1.b21[:, ['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid']]
b3 = StandardScaler()
b4 = b3.fit_transform(b2)
b5 = np.mean(b4, axis=0)
b6 = np.cov(b4, rowvar=False)
eigenvalues, b7 = np.linalg.eig(b6)
b8 = [(np.abs(eigenvalues[i]), b7[:, i]) for i in range(len(eigenvalues))]
b8.sort(b9 = lambda x: x[0], reverse=True)
b10 = np.hstack((b8[0][1].reshape(-1, 1), b8[1][1].reshape(-1, 1)))
b11 = b4.dot(b10)
b12 = pd.DataFrame(data=b11, columns=['PCA1', 'PCA2'])
b13 = pd.concat([b12, b1[['class']]], axis=1)
plt.figure(b14 = (7, 7))
b15 = plt.gca()
b15.set_facecolor('white')
b15.set_xlabel('PCA 1', b16 = 12)
b15.set_ylabel('PCA 2', b16 = 12)
b15.set_title('PCA on Iris dataset', b16 = 15)
b17 = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
b18 = ['y', 'b', 'r']
for class_name, color in zip(b17, b18):
    b19 = b13[b13['class'] == class_name]
    b15.scatter(b19['PCA1'], b19['PCA2'], b20 = color, s=50, label=class_name)
b15.legend(b21 = 'upper right')
b15.grid(b22 = 0.5)
plt.savefig('PCA_fig.png', b23 = 200)
plt.show()