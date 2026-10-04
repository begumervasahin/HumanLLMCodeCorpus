import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import sys
def load_data(data_file, labels_file):
    data = np.genfromtxt(data_file, delimiter=',')
    labels = np.genfromtxt(labels_file, autostrip=True)
    return data, labels
def calculate_scatter_matrices(X, y):
    n_features = X.shape[1]
    unique_labels = set(y)
    mu_global = np.mean(X, axis=0)
    W_class = np.zeros((n_features, n_features))
    B_class = np.zeros((n_features, n_features))
    for label in unique_labels:
        class_data = X[y == label]
        class_mean = np.mean(class_data, axis=0)
        W_class += np.dot((class_data - class_mean).T, (class_data - class_mean))
        B_class += len(class_data) * np.outer(class_mean - mu_global, class_mean - mu_global)
    return W_class, B_class
def lda_transform(X, W_class, B_class, n_components=2):
    eigvals, eigvecs = np.linalg.eig(np.linalg.inv(W_class).dot(B_class))
    top_eigvecs = eigvecs[:, :n_components]
    X_lda = X.dot(top_eigvecs)
    return X_lda, top_eigvecs
def plot_results(X_lda, y, unique_labels, plot_file):
    plt.figure()
    for label in unique_labels:
        plt.scatter(X_lda[y == label, 0], X_lda[y == label, 1], label=f"Class {label}")
    plt.title("Maximize the ratio of between-class scatter to within-class scatter")
    plt.xlabel("LD1")
    plt.ylabel("LD2")
    plt.legend()
    with PdfPages(plot_file) as pdf:
        pdf.savefig()
    plt.close()
def save_results(transformation_matrix, projected_data, transformation_file, projected_file):
    np.savetxt(transformation_file, transformation_matrix.T, delimiter=',')
    np.savetxt(projected_file, projected_data, delimiter=',')
def main():
    if len(sys.argv) != 5:
        print(f"Usage: {sys.argv[0]} <input_data_file> <input_labels_file> <output_transformation_matrix_file> <output_projected_data_file>")
        sys.exit(1)
    input_data_file = sys.argv[1]
    input_labels_file = sys.argv[2]
    output_transformation_matrix_file = sys.argv[3]
    output_projected_data_file = sys.argv[4]
    X, y = load_data(input_data_file, input_labels_file)
    unique_labels = set(y)
    W_class, B_class = calculate_scatter_matrices(X, y)
    X_lda, transformation_matrix = lda_transform(X, W_class, B_class)
    plot_results(X_lda, y, unique_labels, 'scatter_3_plot.pdf')
    save_results(transformation_matrix, X_lda, output_transformation_matrix_file, output_projected_data_file)
if __name__ == "__main__":
    main()