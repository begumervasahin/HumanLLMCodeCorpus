import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data_1 = np.genfromtxt("C:/Users/vyoms/Desktop/dataset_1.csv", delimiter=",")
data = data_1[1:, :]
data_V1 = data_1[1:, 0]
data_V2 = data_1[1:, 1]
plt.scatter(data_V1[:30], data_V2[:30], marker='o', color='purple', alpha=0.5, label='Class 1')
plt.scatter(data_V1[30:60], data_V2[30:60], marker='o', color='orange', alpha=0.5, label='Class 2')
plt.xlabel('V1')
plt.ylabel('V2')
plt.title('Scatter Plot of V2 vs V1')
plt.legend()
plt.show()
def perform_PCA(x):
    x_mean_centered = x - x.mean(axis=0)
    covariance_matrix = np.cov(x_mean_centered, rowvar=False)
    eigen_values, eigen_vectors = np.linalg.eig(covariance_matrix)
    sorted_indices = np.argsort(eigen_values)[::-1]
    eigen_values = eigen_values[sorted_indices]
    eigen_vectors = eigen_vectors[:, sorted_indices]
    pca_scores = np.matmul(x_mean_centered, eigen_vectors)
    pca_results = {'data': x,
                   'mean_centered_data': x_mean_centered,
                   'PC_variance': eigen_values,
                   'loadings': eigen_vectors,
                   'scores': pca_scores}
    return pca_results
pca_results = perform_PCA(data)
V1 = data_V1
V2 = data_V2
mean_V1, mean_V2 = np.mean(V1), np.mean(V2)
numerator = np.sum((V1 - mean_V1) * (V2 - mean_V2))
denominator = np.sum((V1 - mean_V1) ** 2)
b1 = numerator / denominator
b0 = mean_V2 - (b1 * mean_V1)
plt.scatter(V1[:30], V2[:30], marker='o', color='purple', alpha=0.5, label='Class 1')
plt.scatter(V1[30:60], V2[30:60], marker='o', color='orange', alpha=0.5, label='Class 2')
plt.plot(V1, b0 + b1 * V1, color='blue', linewidth=2, label='Regression Line')
plt.xlabel('V1')
plt.ylabel('V2')
plt.title('Regression Plot')
plt.legend()
plt.show()
df = pd.read_csv('C:/Users/vyoms/Desktop/dataset_1.csv', header=None)
df = df.drop(df.index[0])
df = df.drop(df.columns[2], axis=1)
df1, df2 = df.values[:30, :], df.values[30:, :]
m_1, m_2 = np.mean(df1, axis=0), np.mean(df2, axis=0)
mean_all = np.mean(df, axis=0)
within_class_scatter = np.cov((df1 - m_1).T) + np.cov((df2 - m_2).T)
between_class_scatter = len(df1) * np.outer((m_1 - mean_all), (m_1 - mean_all)) + \
                        len(df2) * np.outer((m_2 - mean_all), (m_2 - mean_all))
e_val, e_vector = np.linalg.eig(np.dot(np.linalg.inv(within_class_scatter), between_class_scatter))
sorted_indices = np.argsort(np.abs(e_val))[::-1]
e_val, e_vector = e_val[sorted_indices], e_vector[:, sorted_indices]
lda_project = df.values.dot(e_vector[:, 0])
plt.scatter(lda_project[:30], np.zeros(30), marker='o', color='purple', alpha=0.5, label='Class 1')
plt.scatter(lda_project[30:60], np.zeros(30), marker='o', color='orange', alpha=0.5, label='Class 2')
plt.title('LDA Projection')
plt.xlabel('LD1')
plt.legend()
plt.show()
sqr_PCAdata = pca_results['scores'] ** 2
variance = np.sum(sqr_PCAdata, axis=0) / (sqr_PCAdata.shape[0] - 1)
total_variance = np.sum(variance)
percent_variance_explained = 100 * pca_results['PC_variance'][0] / np.sum(pca_results['PC_variance'])
percent_variance_explained1 = 100 * pca_results['PC_variance'][1] / np.sum(pca_results['PC_variance'])
covariance_pc1pc2 = np.cov(pca_results['scores'][:, 0], pca_results['scores'][:, 1])
PC1_variance, PC2_variance = np.var(pca_results['scores'][:, 0]), np.var(pca_results['scores'][:, 1])
plt.scatter(pca_results['scores'][:, 0], pca_results['scores'][:, 1], color='blue', alpha=0.5)
plt.title('Scree Plot')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.show()
PC_axis = pca_results['data'].dot(pca_results['loadings'][:, 0])
plt.scatter(PC_axis[:30], PC_axis[:30], marker='o', color='purple', alpha=0.5, label='Class 1')
plt.scatter(PC_axis[30:60], PC_axis[30:60], marker='o', color='orange', alpha=0.5, label='Class 2')
plt.title('Regression Plot using PCA Axis')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.legend()
plt.show()