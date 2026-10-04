import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn import datasets
b1 = pd.read_csv("D:/Python_programs/ML/iris.csv")
b2 = ['sepal length', 'sepal width', 'petal length', 'petal width']
b3 = b1[b2].values
b4 = b1['target'].values
b5 = StandardScaler().fit_transform(b3)
b6 = PCA(n_components=4)
b7 = b6.fit_transform(b5)
b8 = b6.explained_variance_ratio_
plt.figure(b9 = (8, 6))
plt.bar(range(1, 5), b8 * 100, b10 = 'b', label='Principal Components')
plt.legend()
plt.xlabel('Principal Components')
plt.xticks(range(1, 5), ['PC-1', 'PC-2', 'PC-3', 'PC-4'], b11 = 8, rotation=30)
plt.ylabel('Variance Ratio (%)')
plt.title('Variance Ratio of IRIS Dataset')
plt.show()
b12 = PCA(n_components=2)
b13 = b12.fit_transform(b5)
b14 = pd.DataFrame(data=b13, columns=['PC-1', 'PC-2'])
b15 = pd.concat([b14, b1[['target']]], axis=1)
fig, b16 = plt.subplots(b9=(8, 8))
b16.set_xlabel('PC-1', b11 = 15)
b16.set_ylabel('PC-2', b11 = 15)
b16.set_title('PCA on IRIS Dataset', b11 = 20)
b17 = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
b18 = ['r', 'g', 'b']
for target, b10 in zip(b17, b18):
    b19 = b15['target'] == target
    b16.scatter(b15.loc[b19, 'PC-1'], b15.loc[b19, 'PC-2'], b20 = b10, s=50)
b16.legend(b17)
b16.grid()
plt.show()
b15.to_csv('iris_after_pca.csv', b21 = False)