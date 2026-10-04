import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
def perform_pca(df, n_components=150):
    df = df.transpose()
    labels = df.iloc[:, -1].values
    features = StandardScaler().fit_transform(df.iloc[:, :-1])
    covariance_matrix = np.cov(features.T)
    eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
    eigen_pairs = [(np.abs(eigenvalues[i]), eigenvectors[:, i]) for i in range(len(eigenvalues))]
    eigen_pairs.sort(key=lambda x: x[0], reverse=True)
    eigen_total = sum(eigenvalues)
    cumulative_sum = np.cumsum([pair[0] for pair in eigen_pairs]) / eigen_total
    plt.plot(cumulative_sum, marker='o')
    plt.xlabel("Number of components")
    plt.ylabel("Cumulative sum of eigenvalues / total eigenvalues")
    plt.title("Cumulative Sum of Eigenvalues")
    plt.grid(True)
    plt.show()
    top_eigenvectors = np.array([pair[1] for pair in eigen_pairs[:n_components]]).T
    transformed_data = features.dot(top_eigenvectors)
    transformed_data = np.real(transformed_data)
    column_names = [f"PC{i+1}" for i in range(n_components)] + ['label']
    transformed_df = pd.DataFrame(transformed_data, columns=column_names[:-1])
    transformed_df['label'] = labels
    return transformed_df, top_eigenvectors, column_names
def transform_test_data(df, model, column_names):
    df = df.transpose()
    labels = df.iloc[:, -1].values
    features = StandardScaler().fit_transform(df.iloc[:, :-1])
    transformed_data = features.dot(model)
    transformed_data = np.real(transformed_data)
    transformed_df = pd.DataFrame(transformed_data, columns=column_names[:-1])
    transformed_df['label'] = labels
    return transformed_df
if __name__ == '__main__':
    train_df = pd.read_csv('train.csv')
    pca_train_df, pca_model, column_names = perform_pca(train_df)
    pca_train_df.to_csv("pca_out.csv", index=False)
    test_df = pd.read_csv('test.csv')
    pca_test_df = transform_test_data(test_df, pca_model, column_names)
    pca_test_df.to_csv("pca_test_out.csv", index=False)