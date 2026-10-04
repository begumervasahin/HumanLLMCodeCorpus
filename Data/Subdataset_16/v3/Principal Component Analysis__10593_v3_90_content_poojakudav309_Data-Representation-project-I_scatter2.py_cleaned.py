import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import sys
def fonk1(features_path, labels_path):
    b1 = np.genfromtxt(features_path, b16=',')
    b2 = np.genfromtxt(labels_path, autostrip=True)
    return b1, b2
def fonk2(b1):
    return np.mean(b1, b3 = 0)
def fonk3(b1, b2, b18):
    b4 = b1.shape[1]
    b5 = set(b2)
    b6 = np.zeros((b4, b4))
    for label in b5:
        b7 = b1[b2 == label]
        b8 = np.mean(b7, b3=0)
        b9 = np.outer(b8 - b18, b8 - b18)
        b6 += len(b7) * b9
    return b6
def fonk4(matrix):
    evals, b10 = np.linalg.eigh(matrix)
    b11 = np.argsort(evals)[::-1]
    return evals[b11], b10[:, b11]
def fonk5(b1, eigenvectors, b12 = 2):
    return np.dot(b1, eigenvectors[:, :b12])
def fonk6(b19, b2, output_pdf):
    fig, b13 = plt.subplots()
    b14 = b13.b14(b19[:, 0], b19[:, 1], c=b2)
    b15 = b13.legend(*b14.legend_elements(), title="Classes")
    b13.add_artist(b15)
    plt.title("Maximize between class b14")
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    with PdfPages(output_pdf) as pdf:
        pdf.savefig(fig)
def fonk7(eigenvectors, b19, eigenvectors_file, b17):
    np.savetxt(eigenvectors_file, eigenvectors.T, b16 = ',')
    np.savetxt(b17, b19, b16 = ',')
def fonk8():
    if len(sys.argv) != 5:
        print(f"{sys.argv[0]} takes 4 arguments. Not {len(sys.argv) - 1}")
        sys.exit()
    features_file, labels_file, eigenvectors_file, b17 = sys.argv[1:5]
    b1, b2 = fonk1(features_file, labels_file)
    b18 = fonk2(b1)
    b6 = fonk3(b1, b2, b18)
    _, b10 = fonk4(b6)
    b19 = fonk5(b1, b10)
    fonk6(b19, b2, 'scatter_2_plot.pdf')
    fonk7(b10, b19, eigenvectors_file, b17)
if b20 = = "__main__":
    fonk8()