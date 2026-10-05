import numpy as np
import pandas as pd
def PCA(X):
    X_centered = (X - np.mean(X)) / np.std(X)
    covariance_matrix = np.dot(X_centered.T, X_centered)
    S = np.identity(X.shape[1])
    for _ in range(40):
        Q, R = np.linalg.qr(covariance_matrix)
        covariance_matrix = np.dot(R, Q)
        S = np.dot(S, Q)
    print("Covariance matrix shape:", covariance_matrix.shape)
    print("Diagonal of the covariance matrix:", np.diag(covariance_matrix))
    print("Transformation matrix shape:", S.shape)
    print("Transformation matrix:")
    print(S)
    transformed_data = np.dot(X_centered, S)
    print("Transformed data shape:", transformed_data.shape)
    print("Transformed data:")
    print(transformed_data)
def SVC(X):
    X_centered = (X - np.mean(X)) / np.std(X)
    U, D, Vt = np.linalg.svd(X_centered, full_matrices=True)
    print('Left singular vectors (U):', U)
    print('Singular values (D):', D)
    print('Right singular vectors (Vt):', Vt)
def main():
    data = pd.read_excel("Clean Data.xlsx")
    X = data.values[:, 2:22]
    print("Principal Component Analysis:")
    PCA(X)
    print("\nSingular Value Decomposition:")
    SVC(X)
if __name__ == "__main__":
    main()