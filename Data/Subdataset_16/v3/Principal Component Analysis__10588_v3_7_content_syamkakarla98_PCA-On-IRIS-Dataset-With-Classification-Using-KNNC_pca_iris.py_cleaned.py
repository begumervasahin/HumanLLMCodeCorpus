import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
b1 = pd.read_csv("D:\Python_programs\ML\iris.csv")
b2 = ['sepal length', 'sepal width', 'petal length', 'petal width']
b3 = 'target'
b4 = b1[b2].values
b5 = b1[[b3]].values
b6 = StandardScaler()
b7 = b6.fit_transform(b4)
b8 = PCA(n_components=4)
b9 = b8.fit_transform(b7)
b10 = b8.explained_variance_ratio_
plt.figure(b11 = (8, 6))
plt.bar(range(1, 5), b10 * 100, b12 = 'b', label='Principal Components')
plt.xlabel('Principal Components')
plt.ylabel('Variance Ratio (%)')
plt.title('Variance Ratio of IRIS Dataset')
plt.xticks(range(1, 5), ['PC-1', 'PC-2', 'PC-3', 'PC-4'], b13 = 10, rotation=30)
plt.legend()
plt.grid(True)
plt.show()
b14 = PCA(n_components=2)
b15 = b14.fit_transform(b7)
b16 = pd.DataFrame(data=b15, columns=['PC-1', 'PC-2'])
b17 = pd.concat([b16, b1[[b3]]], axis=1)
fig, b18 = plt.subplots(b11=(8, 8))
b18.set_xlabel('PC-1', b13 = 15)
b18.set_ylabel('PC-2', b13 = 15)
b18.set_title('PCA on IRIS Dataset', b13 = 20)
b19 = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
b20 = ['r', 'g', 'b']
for target, b12 in zip(b19, b20):
    b21 = b17[b3] == target
    b18.scatter(b17.loc[b21, 'PC-1'], b17.loc[b21, 'PC-2'], b22 = b12, s=50, label=target)
b18.legend()
b18.grid(True)
plt.show()
b17.to_csv('iris_after_pca.csv', b23 = False)