import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import sys
def main():
    if len(sys.argv) != 5:
        print(f"{sys.argv[0]} takes 4 arguments. Not {len(sys.argv) - 1}")
        sys.exit()
    first, second, third, fourth = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    Xt = np.genfromtxt(first, delimiter=',')
    y = np.genfromtxt(second, autostrip=True)
    m, n = Xt.shape
    unique_labels = set(y)
    mu_global = np.mean(Xt, axis=0)
    B_class = np.zeros((n, n))
    for c in unique_labels:
        class_data = Xt[y == c]
        class_mean = np.mean(class_data, axis=0)
        class_scatter = np.dot((class_mean - mu_global).reshape(-1, 1), (class_mean - mu_global).reshape(1, -1))
        B_class += len(class_data) * class_scatter
    evals, evecs = np.linalg.eigh(B_class)
    idx = np.argsort(evals)[::-1]
    evecs = evecs[:, idx]
    r = 2
    V_r = evecs[:, :r]
    result = np.dot(Xt, V_r)
    fig, ax = plt.subplots()
    scatter = ax.scatter(result[:, 0], result[:, 1], c=y)
    legend1 = ax.legend(*scatter.legend_elements(), title="Classes")
    ax.add_artist(legend1)
    plt.title("Maximize between class scatter")
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    with PdfPages('scatter_2_plot.pdf') as pdf:
        pdf.savefig(fig)
    np.savetxt(third, V_r.T, delimiter=',')
    np.savetxt(fourth, result, delimiter=',')
if __name__ == "__main__":
    main()