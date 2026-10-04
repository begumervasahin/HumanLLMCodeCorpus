import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
def pca(df, n_components=150):
    df = df.transpose()
    label = df.iloc[:, -1].values
    matrix = StandardScaler().fit_transform(df.iloc[:, :-1])
    covariance = np.cov(matrix.T)
    eigen_val, eigen_vec = np.linalg.eig(covariance)
    eigens = [(np.abs(eigen_val[i]), eigen_vec[:, i]) for i in range(len(eigen_val))]
    eigens.sort(key=lambda x: x[0], reverse=True)
    eigen_total = sum(eigen_val)
    lam = [sum(eigen_val[:i+1]) / eigen_total for i in range(len(eigen_val))]
    plt.plot(lam, marker='o')
    plt.xlabel("Number of Components")
    plt.ylabel("Cumulative Sum of Eigenvalues / Total Eigenvalue")
    plt.show()
    top_eigenvectors = np.array([eigens[i][1] for i in range(n_components)]).T
    reduced_matrix = matrix.dot(top_eigenvectors)
    reduced_matrix = np.real(reduced_matrix)
    column_names = [f"PC{i+1}" for i in range(n_components)]
    df_out = pd.DataFrame(reduced_matrix, columns=column_names)
    df_out['label'] = label
    return df_out, top_eigenvectors, column_names
def pca_test(df, model, column_names):
    df = df.transpose()
    label = df.iloc[:, -1].values
    matrix = StandardScaler().fit_transform(df.iloc[:, :-1])
    reduced_matrix = matrix.dot(model)
    reduced_matrix = np.real(reduced_matrix)
    df_out = pd.DataFrame(reduced_matrix, columns=column_names)
    df_out['label'] = label
    return df_out
if __name__ == '__main__':
    train = pd.read_csv('train.csv')
    df_train, model, column_names = pca(train)
    df_train.to_csv("pca_out.csv", index=False)
    test = pd.read_csv('test.csv')
    df_test = pca_test(test, model, column_names)
    df_test.to_csv("pca_test_out.csv", index=False)