import numpy as np
import pandas as pd
def standardize_data(X):
    mean_X = np.mean(X, axis=0)
    std_X = np.std(X, axis=0)
    return (X - mean_X) / std_X
def principal_component_analysis(X):
    X_centered = standardize_data(X)
    cov_matrix = np.dot(X_centered.T, X_centered)
    transformation_matrix = np.identity(X.shape[1])
    iterations = 40
    for _ in range(iterations):
        Q, R = np.linalg.qr(cov_matrix)
        cov_matrix = np.dot(R, Q)
        transformation_matrix = np.dot(transformation_matrix, Q)
    transformed_data = np.dot(X_centered, transformation_matrix)
    return transformed_data
def singular_value_decomposition(X):
    X_centered = standardize_data(X)
    U, D, V = np.linalg.svd(X_centered, full_matrices=True)
    return U, D, V
def main():
    data_input = pd.read_excel("Clean Data.xlsx")
    X = data_input.iloc[:, 2:22].values
    pca_result = principal_component_analysis(X)
    print("Principal Component Analysis Result:")
    print(pca_result)
    print("\nSingular Value Decomposition Result:")
    U, D, V = singular_value_decomposition(X)
    print("U:", U)
    print("D:", D)
    print("V:", V)
if __name__ == "__main__":
    main()