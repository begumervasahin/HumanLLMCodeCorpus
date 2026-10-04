import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
df = pd.read_csv('iris-data.csv', sep=',', names=['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class'])
features = df.loc[:, ['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid']]
scaler = StandardScaler()
standardized_features = scaler.fit_transform(features)
mean_vals = np.mean(standardized_features, axis=0)
cov_matrix = np.cov(standardized_features, rowvar=False)
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
eigenpairs = [(np.abs(eigenvalues[i]), eigenvectors[:, i]) for i in range(len(eigenvalues))]
eigenpairs.sort(key=lambda x: x[0], reverse=True)
projection_matrix = np.hstack((eigenpairs[0][1].reshape(-1, 1), eigenpairs[1][1].reshape(-1, 1)))
principal_components = standardized_features.dot(projection_matrix)
pca_df = pd.DataFrame(data=principal_components, columns=['PCA1', 'PCA2'])
final_df = pd.concat([pca_df, df[['class']]], axis=1)
plt.figure(figsize=(7, 7))
ax = plt.gca()
ax.set_facecolor('white')
ax.set_xlabel('PCA 1', fontsize=12)
ax.set_ylabel('PCA 2', fontsize=12)
ax.set_title('PCA on Iris dataset', fontsize=15)
class_names = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
colors = ['y', 'b', 'r']
for class_name, color in zip(class_names, colors):
    class_data = final_df[final_df['class'] == class_name]
    ax.scatter(class_data['PCA1'], class_data['PCA2'], c=color, s=50, label=class_name)
ax.legend(loc='upper right')
ax.grid(linewidth=0.5)
plt.savefig('PCA_fig.png', dpi=200)
plt.show()