import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
df = pd.read_csv("D:\Python_programs\ML\iris.csv")
features = ['sepal length', 'sepal width', 'petal length', 'petal width']
x = df[features].values
y = df[['target']].values
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)
pca_4 = PCA(n_components=4)
principal_components_4 = pca_4.fit_transform(x_scaled)
explained_variance_ratio = pca_4.explained_variance_ratio_
plt.figure()
plt.bar([1, 2, 3, 4], explained_variance_ratio * 100, color='b', label='Principal Components')
plt.legend()
plt.xlabel('Principal Components')
plt.xticks([1, 2, 3, 4], ['PC-1', 'PC-2', 'PC-3', 'PC-4'], fontsize=8, rotation=30)
plt.ylabel('Variance Ratio (%)')
plt.title('Variance Ratio of IRIS Dataset')
plt.show()
pca_2 = PCA(n_components=2)
principal_components_2 = pca_2.fit_transform(x_scaled)
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