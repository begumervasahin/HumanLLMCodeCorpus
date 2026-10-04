import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import sys
def fonk1():
    if len(sys.argv) != 5:
        print(f"{sys.argv[0]} takes 4 arguments. Not {len(sys.argv) - 1}")
        sys.exit()
    first, second, third, b1 = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    b2 = np.genfromtxt(first, b18=',')
    b3 = np.genfromtxt(second, autostrip=True)
    m, b4 = b2.shape
    b5 = set(b3)
    b6 = np.mean(b2, axis=0)
    b7 = np.zeros((b4, b4))
    for c in b5:
        b8 = b2[b3 == c]
        b9 = np.mean(b8, axis=0)
        b10 = np.dot((b9 - b6).reshape(-1, 1), (b9 - b6).reshape(1, -1))
        b7 += len(b8) * b10
    evals, b11 = np.linalg.eigh(b7)
    b12 = np.argsort(evals)[::-1]
    b11 = b11[:, b12]
    a1 = 2
    b13 = b11[:, :a1]
    b14 = np.dot(b2, b13)
    fig, b15 = plt.subplots()
    b16 = b15.b16(b14[:, 0], b14[:, 1], c=b3)
    b17 = b15.legend(*b16.legend_elements(), title="Classes")
    b15.add_artist(b17)
    plt.title("Maximize between class b16")
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    with PdfPages('scatter_2_plot.pdf') as pdf:
        pdf.savefig(fig)
    np.savetxt(third, b13.T, b18 = ',')
    np.savetxt(b1, b14, b18 = ',')
if b19 = = "__main__":
    fonk1()