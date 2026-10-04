import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import sys
def load_data(features_path, labels_path):
    features = np.genfromtxt(features_path, delimiter=',')
    labels = np.genfromtxt(labels_path, autostrip=True)
    return features, labels
def calculate_global_mean(features):
    return np.mean(features, axis=0)
def calculate_between_class_scatter(features, labels, global_mean):
    n_features = features.shape[1]
    unique_labels = set(labels)
    B_class = np.zeros((n_features, n_features))
    for label in unique_labels:
        class_data = features[labels == label]
        class_mean = np.mean(class_data, axis=0)
        class_scatter = np.outer(class_mean - global_mean, class_mean - global_mean)
        B_class += len(class_data) * class_scatter
    return B_class
def perform_eigen_decomposition(matrix):
    evals, evecs = np.linalg.eigh(matrix)
    idx = np.argsort(evals)[::-1]
    return evals[idx], evecs[:, idx]
def project_data(features, eigenvectors, num_components=2):
    return np.dot(features, eigenvectors[:, :num_components])
def plot_results(projected_data, labels, output_pdf):
    fig, ax = plt.subplots()
    scatter = ax.scatter(projected_data[:, 0], projected_data[:, 1], c=labels)
    legend1 = ax.legend(*scatter.legend_elements(), title="Classes")
    ax.add_artist(legend1)
    plt.title("Maximize between class scatter")
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    with PdfPages(output_pdf) as pdf:
        pdf.savefig(fig)
def save_results(eigenvectors, projected_data, eigenvectors_file, projected_data_file):
    np.savetxt(eigenvectors_file, eigenvectors.T, delimiter=',')
    np.savetxt(projected_data_file, projected_data, delimiter=',')
def main():
    if len(sys.argv) != 5:
        print(f"{sys.argv[0]} takes 4 arguments. Not {len(sys.argv) - 1}")
        sys.exit()
    features_file, labels_file, eigenvectors_file, projected_data_file = sys.argv[1:5]
    features, labels = load_data(features_file, labels_file)
    global_mean = calculate_global_mean(features)
    B_class = calculate_between_class_scatter(features, labels, global_mean)
    _, evecs = perform_eigen_decomposition(B_class)
    projected_data = project_data(features, evecs)
    plot_results(projected_data, labels, 'scatter_2_plot.pdf')
    save_results(evecs, projected_data, eigenvectors_file, projected_data_file)
if __name__ == "__main__":
    main()