import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import sys
def main():
    if len(sys.argv) != 5:
        print(f"{sys.argv[0]} takes 4 arguments. Not {len(sys.argv) - 1}")
        sys.exit()
    input_data_path = sys.argv[1]
    labels_path = sys.argv[2]
    output_matrix_path = sys.argv[3]
    output_projection_path = sys.argv[4]
    Xt = np.genfromtxt(input_data_path, delimiter=',')
    y = np.genfromtxt(labels_path, autostrip=True)
    m, n = Xt.shape
    unique_labels = set(y)
    mu_global = np.mean(Xt, axis=0)
    B_class = np.zeros((n, n))
    for c in unique_labels:
        class_indices = [i for i, label in enumerate(y) if label == c]
        class_samples = Xt[class_indices]
        m1 = len(class_samples)
        mu1 = np.mean(class_samples, axis=0)
        W_class = np.zeros((n, n))
        for sample in class_samples:
            ct = sample - mu1
            W_class += np.outer(ct, ct)
        bt = mu1 - mu_global
        B_class += m1 * np.outer(bt, bt)
    evals, evecs = np.linalg.eigh(B_class)
    idx = np.argsort(evals)[::-1]
    evecs = evecs[:, idx]
    evals = evals[idx]
    r = 2
    V_r = evecs[:, :r]
    result = np.dot(Xt, V_r)
    x1, x2 = result[:, 0], result[:, 1]
    plot_results(x1, x2)
    np.savetxt(output_matrix_path, V_r.T, delimiter=',')
    np.savetxt(output_projection_path, result, delimiter=',')
def plot_results(x1, x2):
    fig, ax = plt.subplots()
    ax.scatter(x1, x2)
    plt.title("Maximize between class scatter")
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plotname = 'scatter_2_plot'
    pdf = PdfPages(f'{plotname}.pdf')
    pdf.savefig(fig)
    pdf.close()
if __name__ == "__main__":
    main()