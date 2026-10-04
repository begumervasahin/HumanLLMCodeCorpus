import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
b1 = pd.read_csv('iris-data.csv', sep=',', names=['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class'])
b2 = b1[['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid']]
b3 = StandardScaler().fit_transform(b2)
b4 = np.cov(b3, rowvar=False)
eigen_values, b5 = np.linalg.eig(b4)
b6 = sorted([(np.abs(eigen_values[i]), b5[:, i]) for i in range(len(eigen_values))],
                     b7 = lambda x: x[0], reverse=True)
b8 = np.hstack((b6[0][1].reshape(4, 1), b6[1][1].reshape(4, 1)))
b9 = b3.dot(b8)
b10 = pd.DataFrame(data=b9, columns=['PCA1', 'PCA2'])
b11 = pd.concat([b10, b1[['class']]], axis=1)
plt.figure(b12 = (7, 7))
plt.xlabel('PCA 1', b13 = 12)
plt.ylabel('PCA 2', b13 = 12)
plt.title('PCA on Iris Dataset', b13 = 15)
b14 = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
b15 = ['y', 'b', 'r']
for class_name, color in zip(b14, b15):
    b16 = b11[b11['class'] == class_name]
    plt.scatter(b16['PCA1'], b16['PCA2'], b17 = color, s=50, label=class_name)
plt.legend(b18 = "upper right")
plt.grid(b19 = 0.5)
plt.savefig('PCA_fig.png', b20 = 200)
plt.show()