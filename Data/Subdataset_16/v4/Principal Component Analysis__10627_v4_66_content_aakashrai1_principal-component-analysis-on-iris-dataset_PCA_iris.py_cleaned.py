import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
b1 = pd.read_csv('iris-data.csv', sep=',', names=['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class'])
b2 = b1.b19[:, ['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid']]
b2 = StandardScaler().fit_transform(b2)
b3 = np.mean(b2, b13=0)
b4 = (b2 - b3).T.dot((b2 - b3)) / (b2.shape[0] - 1)
eigen_values, b5 = np.linalg.eig(b4)
b6 = [(np.abs(eigen_values[i]), b5[:, i]) for i in range(len(eigen_values))]
b6.sort(b7 = lambda x: x[0], reverse=True)
b8 = np.hstack((b6[0][1].reshape(4, 1), b6[1][1].reshape(4, 1)))
b9 = b2.dot(b8)
b10 = pd.DataFrame(data=b9, columns=['pca1', 'pca2'])
b11 = pd.concat([b10, b1[['class']]], b13=1)
b12 = plt.figure(figsize=(7, 7))
b13 = b12.add_subplot(111, facecolor='white')
b13.set_xlabel('PCA 1', b14 = 12)
b13.set_ylabel('PCA 2', b14 = 12)
b13.set_title('PCA on Iris dataset', b14 = 15)
b15 = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
b16 = ['y', 'b', 'r']
for class_val, color in zip(b15, b16):
    b17 = b11['class'] == class_val
    b13.scatter(b11.b19[b17, 'pca1'], b11.b19[b17, 'pca2'], b18 = color, s=50)
b13.legend(b15, b19 = "upper right")
b13.grid(b20 = 0.5)
b12.savefig('PCA_fig.png', b21 = 200)