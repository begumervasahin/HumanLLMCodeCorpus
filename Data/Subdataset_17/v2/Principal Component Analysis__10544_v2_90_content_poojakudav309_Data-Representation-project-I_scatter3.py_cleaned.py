import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import sys
def main():
    if len(sys.argv) != 5:
        print(f"Usage: {sys.argv[0]} <input_data_file> <input_labels_file> <output_transformation_matrix_file> <output_projected_data_file>")
        sys.exit(1)
    input_data_file = sys.argv[1]
    input_labels_file = sys.argv[2]
    output_transformation_matrix_file = sys.argv[3]
    output_projected_data_file = sys.argv[4]
    Xt = np.genfromtxt(input_data_file, delimiter=',')
    y = np.genfromtxt(input_labels_file, autostrip=True)
    m, n = Xt.shape
    unique_labels = set(y)
    mu_global = np.mean(Xt, axis=0)
    W_class = np.zeros((n, n))
    B_class = np.zeros((n, n))
    for c in unique_labels:
        class_data = Xt[y == c]
        class_mean = np.mean(class_data, axis=0)
        W_class += np.dot((class_data - class_mean).T, (class_data - class_mean))
        B_class += len(class_data) * np.outer(class_mean - mu_global, class_mean - mu_global)
    eigvals, eigvecs = np.linalg.eig(np.linalg.inv(W_class).dot(B_class))
    V_r = eigvecs[:, :2]
    projected_data = Xt.dot(V_r)
    plt.figure()
    for label in unique_labels:
        plt.scatter(projected_data[y == label, 0], projected_data[y == label, 1], label=f"Class {label}")
    plt.title("Maximize the ratio of between-class scatter to within-class scatter")
    plt.xlabel("LD1")
    plt.ylabel("LD2")
    plt.legend()
    plotname = 'scatter_3_plot.pdf'
    plt.savefig(plotname)
    plt.close()
    np.savetxt(output_transformation_matrix_file, V_r.T, delimiter=',')
    np.savetxt(output_projected_data_file, projected_data, delimiter=',')
if __name__ == "__main__":
    main()