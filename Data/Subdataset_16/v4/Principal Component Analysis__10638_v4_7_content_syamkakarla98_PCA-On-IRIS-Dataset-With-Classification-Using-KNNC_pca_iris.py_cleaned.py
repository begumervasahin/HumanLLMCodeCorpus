import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn import datasets
b1 = pd.read_csv("D:/Python_programs/ML/iris.csv")
b2 = ['sepal length', 'sepal width', 'petal length', 'petal width']
b3 = b1.loc[:, b2].values
b4 = b1.loc[:, ['target']].values
b3 = StandardScaler().fit_transform(b3)
b5 = PCA(n_components=4)
b6 = b5.fit_transform(b3)
b7 = b5.explained_variance_ratio_
plt.figure(b8 = (8, 6))
plt.bar([1, 2, 3, 4], list(b7 * 100), b9 = 'b', label='Principal Components')
plt.legend()
plt.xlabel('Principal Components')
plt.xticks([1, 2, 3, 4], ['PC-1', 'PC-2', 'PC-3', 'PC-4'], b10 = 8, rotation=30)
plt.ylabel('Variance Ratio (%)')
plt.title('Variance Ratio of IRIS Dataset')
plt.show()
b5 = PCA(n_components=2)
b6 = b5.fit_transform(b3)
b11 = pd.DataFrame(data=b6, columns=['PC-1', 'PC-2'])
b12 = pd.concat([b11, b1[['target']]], axis=1)
fig, b13 = plt.subplots(b8=(8, 8))
b13.set_xlabel('PC-1', b10 = 15)
b13.set_ylabel('PC-2', b10 = 15)
b13.set_title('PCA on IRIS Dataset', b10 = 20)
b14 = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
b15 = ['r', 'g', 'b']
for target, b9 in zip(b14, b15):
    b16 = b12['target'] == target
    b13.scatter(b12.loc[b16, 'PC-1'], b12.loc[b16, 'PC-2'], b17 = b9, s=50)
b13.legend(b14)
b13.grid()
plt.show()
b12.to_csv('iris_after_pca.csv', b18 = False)