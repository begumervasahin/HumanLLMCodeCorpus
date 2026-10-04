import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn import datasets
df = pd.read_csv("D:/Python_programs/ML/iris.csv")
features = ['sepal length', 'sepal width', 'petal length', 'petal width']
X = df[features].values
y = df['target'].values
X_standardized = StandardScaler().fit_transform(X)
pca_4 = PCA(n_components=4)
principal_components_4 = pca_4.fit_transform(X_standardized)
explained_variance_ratio_4 = pca_4.explained_variance_ratio_
plt.figure(figsize=(8, 6))
plt.bar(range(1, 5), explained_variance_ratio_4 * 100, color='b', label='Principal Components')
plt.legend()
plt.xlabel('Principal Components')
plt.xticks(range(1, 5), ['PC-1', 'PC-2', 'PC-3', 'PC-4'], fontsize=8, rotation=30)
plt.ylabel('Variance Ratio (%)')
plt.title('Variance Ratio of IRIS Dataset')
plt.show()
pca_2 = PCA(n_components=2)
principal_components_2 = pca_2.fit_transform(X_standardized)
principal_df = pd.DataFrame(data=principal_components_2, columns=['PC-1', 'PC-2'])
final_df = pd.concat([principal_df, df[['target']]], axis=1)
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlabel('PC-1', fontsize=15)
ax.set_ylabel('PC-2', fontsize=15)
ax.set_title('PCA on IRIS Dataset', fontsize=20)
targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
colors = ['r', 'g', 'b']
for target, color in zip(targets, colors):
    indices_to_keep = final_df['target'] == target
    ax.scatter(final_df.loc[indices_to_keep, 'PC-1'], final_df.loc[indices_to_keep, 'PC-2'], c=color, s=50)
ax.legend(targets)
ax.grid()
plt.show()
final_df.to_csv('iris_after_pca.csv', index=False)