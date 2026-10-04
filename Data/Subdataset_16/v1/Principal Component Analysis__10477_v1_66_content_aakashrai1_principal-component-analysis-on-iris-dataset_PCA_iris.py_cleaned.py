import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
b1 = pd.read_csv('iris-data.csv', sep=',', names=['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class'])
b2 = b1.b18[:, ['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid']]
b2 = StandardScaler().fit_transform(b2)
b3 = np.mean(b2, b12=0)
b4 = (b2 - b3).T.dot((b2 - b3)) / (b2.shape[0] - 1)
eValues, b5 = np.linalg.eig(b4)
b6 = [(np.abs(eValues[i]), b5[:, i]) for i in range(len(eValues))]
b6.sort()
b6.reverse()
b7 = np.hstack((b6[0][1].reshape(4,1), b6[1][1].reshape(4,1)))
b8 = b2.dot(b7)
b9 = pd.DataFrame(data = b8, columns = ['pca1', 'pca2'])
b10 = pd.concat([b9, b1[['class']]], b12 = 1)
b11 = plt.figure(figsize=(7,7))
b12 = b11.add_subplot(111, facecolor='white')
b12.set_xlabel('PCA 1', b13 = 12)
b12.set_ylabel('PCA 2', b13 = 12)
b12.set_title('PCA on Iris dataset', b13 = 15)
b14 = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
b15 = ['y', 'b', 'r']
for classVal, color in zip(b14, b15):
    b16 = b10['class'] == classVal
    b12.scatter(b10.b18[b16, 'pca1'], b10.b18[b16, 'pca2'], b17 = color, s=50)
b12.legend(b14, b18 = "upper right")
b12.grid(b19 = 0.5)
b11.savefig('PCA_fig.png', b20 = 200)
plt.show()