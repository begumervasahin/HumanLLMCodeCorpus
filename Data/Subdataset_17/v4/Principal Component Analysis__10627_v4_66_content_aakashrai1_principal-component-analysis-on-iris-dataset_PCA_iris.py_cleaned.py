import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
df = pd.read_csv('iris-data.csv', sep=',', names=['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class'])
features_df = df.loc[:, ['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid']]
features_df = StandardScaler().fit_transform(features_df)
mean_vals = np.mean(features_df, axis=0)
covariance_matrix = (features_df - mean_vals).T.dot((features_df - mean_vals)) / (features_df.shape[0] - 1)
eigen_values, eigen_vectors = np.linalg.eig(covariance_matrix)
eigen_pairs = [(np.abs(eigen_values[i]), eigen_vectors[:, i]) for i in range(len(eigen_values))]
eigen_pairs.sort(key=lambda x: x[0], reverse=True)
top2_matrix = np.hstack((eigen_pairs[0][1].reshape(4, 1), eigen_pairs[1][1].reshape(4, 1)))
principal_components = features_df.dot(top2_matrix)
pca_df = pd.DataFrame(data=principal_components, columns=['pca1', 'pca2'])
new_df = pd.concat([pca_df, df[['class']]], axis=1)
fig = plt.figure(figsize=(7, 7))
axis = fig.add_subplot(111, facecolor='white')
axis.set_xlabel('PCA 1', fontsize=12)
axis.set_ylabel('PCA 2', fontsize=12)
axis.set_title('PCA on Iris dataset', fontsize=15)
classes = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
colors = ['y', 'b', 'r']
for class_val, color in zip(classes, colors):
    index_vals = new_df['class'] == class_val
    axis.scatter(new_df.loc[index_vals, 'pca1'], new_df.loc[index_vals, 'pca2'], c=color, s=50)
axis.legend(classes, loc="upper right")
axis.grid(linewidth=0.5)
fig.savefig('PCA_fig.png', dpi=200)