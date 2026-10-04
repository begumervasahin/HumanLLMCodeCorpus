import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
def load_and_prepare_data(filepath):
    data = pd.read_csv(filepath, header=1)
    data.columns = [
        "Alkohol", "Kwas jabÅkowy", "PopiÃ³Å", "ZasadowoÅÄ popioÅu",
        "Magnez", "CaÅkowita zawartoÅÄ fenoli", "Flawonoidy",
        "Fenole nieflawonoidowe", "Proantocyjaniny", "IntensywnoÅÄ koloru",
        "OdcieÅ", "Transmitacja", "Prolina", "Etykieta"
    ]
    return data
def split_data(data):
    X = data.iloc[:, :-1].values
    y = data.iloc[:, -1].values
    return train_test_split(X, y, test_size=0.3, random_state=42)
def standardize_data(X_train, X_test):
    scaler = StandardScaler()
    X_train_stand = scaler.fit_transform(X_train)
    X_test_stand = scaler.transform(X_test)
    return X_train_stand, X_test_stand
def compute_pca(X_train_stand):
    cov_matrix = np.cov(X_train_stand.T)
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
    eigen_pairs = [(np.abs(eigenvalues[i]), eigenvectors[:, i]) for i in range(len(eigenvalues))]
    eigen_pairs.sort(key=lambda x: x[0], reverse=True)
    projection_matrix = np.hstack((eigen_pairs[0][1][:, np.newaxis], eigen_pairs[1][1][:, np.newaxis]))
    PCA_transformed = X_train_stand.dot(projection_matrix)
    total_variance = sum(eigenvalues)
    variance_explained = [(i / total_variance) for i in sorted(eigenvalues, reverse=True)]
    cumulative_variance_explained = np.cumsum(variance_explained)
    return PCA_transformed, variance_explained, cumulative_variance_explained
def plot_pca_results(PCA_transformed, y_train):
    targets = np.unique(y_train)
    colors = ["r", "g", "b"]
    markers = ["s", "x", "o"]
    plt.figure(figsize=(10, 6))
    for target, color, marker in zip(targets, colors, markers):
        plt.scatter(
            PCA_transformed[y_train == target, 0],
            PCA_transformed[y_train == target, 1],
            color=color,
            label=target,
            marker=marker
        )
    plt.xlabel("Principal Component 1 (PC1)")
    plt.ylabel("Principal Component 2 (PC2)")
    plt.legend(loc="lower right")
    plt.title("PCA of Wine Dataset")
    plt.show()
def main():
    data = load_and_prepare_data("Wine.csv")
    print(data.head())
    X_train, X_test, y_train, y_test = split_data(data)
    X_train_stand, X_test_stand = standardize_data(X_train, X_test)
    PCA_transformed, variance_explained, cumulative_variance_explained = compute_pca(X_train_stand)
    plot_pca_results(PCA_transformed, y_train)
if __name__ == "__main__":
    main()