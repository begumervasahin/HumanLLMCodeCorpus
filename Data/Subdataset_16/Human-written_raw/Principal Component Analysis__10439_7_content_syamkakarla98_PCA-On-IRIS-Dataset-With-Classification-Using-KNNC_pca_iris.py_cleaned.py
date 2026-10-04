import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import decomposition
from sklearn import datasets
b1 = pd.read_csv("D:\Python_programs\ML\iris.csv")
from sklearn.preprocessing import StandardScaler
b2 = ['sepal length', 'sepal width', 'petal length', 'petal width']
b3 = b1.loc[:, b2].values
b4 = b1.loc[:,['target']].values
b3 = StandardScaler().fit_transform(b3)
from sklearn.decomposition import PCA
b5 = PCA(n_components=4)
b6 = b5.fit_transform(b3)
b7 = b5.explained_variance_ratio_
plt.bar([1,2,3,4],list(b7*100),b8 = 'Principal Components',color='b')
plt.legend()
plt.xlabel('Principal Components')
plt.xticks([1,2,3,4],['PC-1','PC-2','PC-3','PC-4'], b9 = 8, rotation=30)
plt.ylabel('Variance Ratio')
plt.title('Variance Ratio of IRIS Dataset')
plt.show()
b5 = PCA(n_components=2)
b6 = b5.fit_transform(b3)
b10 = pd.DataFrame(data = b6
             , b11 = ['PC-1', 'PC-2'])
b12 = pd.concat([b10, b1[['target']]], axis = 1)
b13 = plt.figure(figsize = (8,8))
b14 = b13.add_subplot(1,1,1)
b14.set_xlabel('PC-1', b9 = 15)
b14.set_ylabel('PC-2', b9 = 15)
b14.set_title('PCA on IRIS Dataset', b9 = 20)
b15 = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
b16 = ['r', 'g', 'b']
for target, color in zip(b15,b16):
    b17 = b12['target'] == target
    b14.scatter(b12.loc[b17, 'PC-1']
               , b12.loc[b17, 'PC-2']
               , b18 = color
               , b19 = 50)
b14.legend(b15)
b14.grid()
plt.show()
b12.to_csv('iris_after_pca.csv')