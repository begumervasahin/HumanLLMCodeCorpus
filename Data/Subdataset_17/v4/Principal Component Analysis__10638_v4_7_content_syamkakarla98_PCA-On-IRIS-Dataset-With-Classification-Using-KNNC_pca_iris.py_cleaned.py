import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn import datasets
df = pd.read_csv("D:/Python_programs/ML/iris.csv")
features = ['sepal length', 'sepal width', 'petal length', 'petal width']
x = df.loc[:, features].values
y = df.loc[:, ['target']].values
x = StandardScaler().fit_transform(x)
pca = PCA(n_components=4)
principalComponents = pca.fit_transform(x)
explained_variance_ratio = pca.explained_variance_ratio_
plt.figure(figsize=(8, 6))
plt.bar([1, 2, 3, 4], list(explained_variance_ratio * 100), color='b', label='Principal Components')
plt.legend()
plt.xlabel('Principal Components')
plt.xticks([1, 2, 3, 4], ['PC-1', 'PC-2', 'PC-3', 'PC-4'], fontsize=8, rotation=30)
plt.ylabel('Variance Ratio (%)')
plt.title('Variance Ratio of IRIS Dataset')
plt.show()
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data=principalComponents, columns=['PC-1', 'PC-2'])
finalDf = pd.concat([principalDf, df[['target']]], axis=1)
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlabel('PC-1', fontsize=15)
ax.set_ylabel('PC-2', fontsize=15)
ax.set_title('PCA on IRIS Dataset', fontsize=20)
targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
colors = ['r', 'g', 'b']
for target, color in zip(targets, colors):
    indicesToKeep = finalDf['target'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'PC-1'], finalDf.loc[indicesToKeep, 'PC-2'], c=color, s=50)
ax.legend(targets)
ax.grid()
plt.show()
finalDf.to_csv('iris_after_pca.csv', index=False)