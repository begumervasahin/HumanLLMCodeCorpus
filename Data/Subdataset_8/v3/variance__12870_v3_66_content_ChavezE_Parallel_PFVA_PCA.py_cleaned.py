import numpy as np
import pandas as pd
def principal_component_analysis(X):
    X_centered = (X - np.mean(X)) / np.std(X)
    covariance_matrix = np.dot(X_centered.T, X_centered)
    transformation_matrix = np.identity(X.shape[1])
    for _ in range(40):
        Q, R = np.linalg.qr(covariance_matrix)
        covariance_matrix = np.dot(R, Q)
        transformation_matrix = np.dot(transformation_matrix, Q)
    print("Covariance matrix shape:", covariance_matrix.shape)
    print("Diagonal of the covariance matrix:", np.diag(covariance_matrix))
    print("Transformation matrix shape:", transformation_matrix.shape)
    print("Transformation matrix:")
    print(transformation_matrix)
    transformed_data = np.dot(X_centered, transformation_matrix)
    print("Transformed data shape:", transformed_data.shape)
    print("Transformed data:")
    print(transformed_data)
def singular_value_decomposition(X):
    X_centered = (X - np.mean(X)) / np.std(X)
    U, D, Vt = np.linalg.svd(X_centered, full_matrices=True)
    print('Left singular vectors (U):', U)
    print('Singular values (D):', D)
    print('Right singular vectors (Vt):', Vt)
def main():
    data = pd.read_excel("Clean Data.xlsx")
    X = data.values[:, 2:22]
    print("Principal Component Analysis:")
    principal_component_analysis(X)
    print("\nSingular Value Decomposition:")
    singular_value_decomposition(X)
if __name__ == "__main__":
    main()