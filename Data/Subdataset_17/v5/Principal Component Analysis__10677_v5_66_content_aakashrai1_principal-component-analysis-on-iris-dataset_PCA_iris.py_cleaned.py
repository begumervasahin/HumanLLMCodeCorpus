import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
df = pd.read_csv('iris-data.csv', sep=',', names=['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class'])
features = df[['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid']]
scaled_features = StandardScaler().fit_transform(features)
cov_matrix = np.cov(scaled_features, rowvar=False)
eigen_values, eigen_vectors = np.linalg.eig(cov_matrix)
eigen_pairs = sorted([(np.abs(eigen_values[i]), eigen_vectors[:, i]) for i in range(len(eigen_values))],
                     key=lambda x: x[0], reverse=True)
transformation_matrix = np.hstack((eigen_pairs[0][1].reshape(4, 1), eigen_pairs[1][1].reshape(4, 1)))
principal_components = scaled_features.dot(transformation_matrix)
pca_df = pd.DataFrame(data=principal_components, columns=['PCA1', 'PCA2'])
final_df = pd.concat([pca_df, df[['class']]], axis=1)
plt.figure(figsize=(7, 7))
plt.xlabel('PCA 1', fontsize=12)
plt.ylabel('PCA 2', fontsize=12)
plt.title('PCA on Iris Dataset', fontsize=15)
class_names = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
colors = ['y', 'b', 'r']
for class_name, color in zip(class_names, colors):
    subset = final_df[final_df['class'] == class_name]
    plt.scatter(subset['PCA1'], subset['PCA2'], c=color, s=50, label=class_name)
plt.legend(loc="upper right")
plt.grid(linewidth=0.5)
plt.savefig('PCA_fig.png', dpi=200)
plt.show()