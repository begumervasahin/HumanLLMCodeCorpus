import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
def pca(df):
    df = df.transpose()
    labels = list(df.iloc[:, -1])
    matrix = StandardScaler().fit_transform(df.iloc[:, :-1])
    covariance = np.cov(matrix.T)
    eigen_values, eigen_vectors = np.linalg.eig(covariance)
    eigens = [(np.abs(eigen_values[i]), eigen_vectors[:, i]) for i in range(len(eigen_values))]
    eigens.sort(key=lambda x: x[0], reverse=True)
    eigen_total = sum(eigen_values)
    cumulative_sum = np.cumsum([eigen[0] for eigen in eigens]) / eigen_total
    plt.plot(cumulative_sum, marker='o')
    plt.xlabel("Number of components")
    plt.ylabel("Cumulative sum of eigenvalues / total eigenvalues")
    plt.show()
    reduced_eigen_vectors = np.array([eigen[1] for eigen in eigens[:150]]).T
    reduced_matrix = matrix.dot(reduced_eigen_vectors)
    reduced_matrix = np.real(reduced_matrix)
    df_out = pd.DataFrame(reduced_matrix)
    df_out['label'] = labels
    return df_out, reduced_eigen_vectors, [f"PC{i+1}" for i in range(150)] + ['label']
def pca_test(df, model, names):
    df = df.transpose()
    labels = list(df.iloc[:, -1])
    matrix = StandardScaler().fit_transform(df.iloc[:, :-1])
    final_matrix = matrix.dot(model)
    final_matrix = np.real(final_matrix)
    df_out = pd.DataFrame(final_matrix, columns=names[:-1])
    df_out['label'] = labels
    return df_out
if __name__ == '__main__':
    train_df = pd.read_csv('train.csv')
    pca_train_df, model, names = pca(train_df)
    pca_train_df.to_csv("pca_out.csv", index=False)
    test_df = pd.read_csv('test.csv')
    pca_test_df = pca_test(test_df, model, names)
    pca_test_df.to_csv("pca_test_out.csv", index=False)