import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
def pca(df, n_components=150):
    df = df.transpose()
    labels = df.iloc[:, -1].values
    data_matrix = StandardScaler().fit_transform(df.iloc[:, :-1])
    covariance_matrix = np.cov(data_matrix.T)
    eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
    eigens = sorted([(np.abs(eigenvalues[i]), eigenvectors[:, i]) for i in range(len(eigenvalues))], key=lambda x: x[0], reverse=True)
    eigen_total = sum(eigenvalues)
    cumulative_sum = np.cumsum([eigen[0] for eigen in eigens]) / eigen_total
    plt.plot(cumulative_sum, marker='o')
    plt.xlabel("Number of Components")
    plt.ylabel("Cumulative Sum of Eigenvalues / Total Eigenvalue")
    plt.title("PCA Cumulative Sum of Eigenvalues")
    plt.show()
    top_eigenvectors = np.array([eigens[i][1] for i in range(n_components)]).T
    reduced_data = data_matrix.dot(top_eigenvectors)
    reduced_data = np.real(reduced_data)
    column_names = [f"PC{i+1}" for i in range(n_components)]
    df_out = pd.DataFrame(reduced_data, columns=column_names)
    df_out['label'] = labels
    return df_out, top_eigenvectors, column_names
def pca_test(df, model, column_names):
    df = df.transpose()
    labels = df.iloc[:, -1].values
    data_matrix = StandardScaler().fit_transform(df.iloc[:, :-1])
    reduced_data = data_matrix.dot(model)
    reduced_data = np.real(reduced_data)
    df_out = pd.DataFrame(reduced_data, columns=column_names)
    df_out['label'] = labels
    return df_out
if __name__ == '__main__':
    train_df = pd.read_csv('train.csv')
    pca_train_df, pca_model, pca_column_names = pca(train_df)
    pca_train_df.to_csv("pca_out.csv", index=False)
    test_df = pd.read_csv('test.csv')
    pca_test_df = pca_test(test_df, pca_model, pca_column_names)
    pca_test_df.to_csv("pca_test_out.csv", index=False)