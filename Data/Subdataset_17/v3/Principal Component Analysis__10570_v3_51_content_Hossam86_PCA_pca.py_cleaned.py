import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.decomposition import PCA as sklearnPCA
def load_dataset(filepath):
    df = pd.read_csv(filepath, header=None, sep=',')
    df.columns = ['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class']
    df.dropna(how="all", inplace=True)
    return df
def standardize_features(X):
    scaler = StandardScaler()
    X_std = scaler.fit_transform(X)
    return X_std
def compute_covariance_matrix(X_std):
    return np.cov(X_std.T)
def compute_eigen_decomposition(matrix):
    eig_vals, eig_vecs = np.linalg.eig(matrix)
    return eig_vals, eig_vecs
def validate_eigenvectors(eig_vecs):
    for ev in eig_vecs:
        np.testing.assert_array_almost_equal(1.0, np.linalg.norm(ev))
    print('Eigenvector validation: Everything is ok!')
def sort_eigen_pairs(eig_vals, eig_vecs):
    eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:, i]) for i in range(len(eig_vals))]
    eig_pairs.sort(key=lambda x: x[0], reverse=True)
    return eig_pairs
def calculate_explained_variance(eig_vals):
    total = sum(eig_vals)
    var_exp = [(i / total) * 100 for i in sorted(eig_vals, reverse=True)]
    cum_var_exp = np.cumsum(var_exp)
    return var_exp, cum_var_exp
def create_projection_matrix(eig_pairs, n_components=2):
    matrix_w = np.hstack([eig_pairs[i][1].reshape(4, 1) for i in range(n_components)])
    return matrix_w
def project_data(X_std, matrix_w):
    return X_std.dot(matrix_w)
def sklearn_pca_transform(X_std, n_components=2):
    pca = sklearnPCA(n_components=n_components)
    return pca.fit_transform(X_std)
def main():
    filepath = '/media/hossam/MyFiles/MachineLearning/PCA/PCA/IrisDataSet/iris.data'
    df = load_dataset(filepath)
    print("First 5 rows of the dataset:\n", df.head())
    X = df.iloc[:, 0:4].values
    y = df.iloc[:, 4].values
    X_std = standardize_features(X)
    cov_mat = compute_covariance_matrix(X_std)
    print('Covariance matrix:\n', cov_mat)
    eig_vals, eig_vecs = compute_eigen_decomposition(cov_mat)
    print('Eigenvectors:\n', eig_vecs)
    print('Eigenvalues:\n', eig_vals)
    validate_eigenvectors(eig_vecs)
    eig_pairs = sort_eigen_pairs(eig_vals, eig_vecs)
    print('Eigenvalues in descending order:')
    for eig_val, eig_vec in eig_pairs:
        print(eig_val)
    var_exp, cum_var_exp = calculate_explained_variance(eig_vals)
    matrix_w = create_projection_matrix(eig_pairs)
    print('Projection matrix W:\n', matrix_w)
    Y_manual = project_data(X_std, matrix_w)
    print("Projection by manual PCA:\n", Y_manual[:5])
    Y_sklearn = sklearn_pca_transform(X_std)
    print("Projection by sklearn PCA:\n", Y_sklearn[:5])
if __name__ == "__main__":
    main()