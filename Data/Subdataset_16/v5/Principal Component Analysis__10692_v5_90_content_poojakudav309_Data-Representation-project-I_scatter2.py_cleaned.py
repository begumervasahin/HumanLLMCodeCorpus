import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import sys
def fonk1():
    if len(sys.argv) != 5:
        print(f"{sys.argv[0]} takes 4 arguments. Not {len(sys.argv) - 1}")
        sys.exit()
    b1 = sys.argv[1]
    b2 = sys.argv[2]
    b3 = sys.argv[3]
    b4 = sys.argv[4]
    b5 = np.genfromtxt(b1, b24=',')
    b6 = np.genfromtxt(b2, autostrip=True)
    m, b7 = b5.shape
    b8 = set(b6)
    b9 = np.mean(b5, axis=0)
    b10 = np.zeros((b7, b7))
    for c in b8:
        b11 = [i for i, label in enumerate(b6) if label == c]
        b12 = b5[b11]
        b13 = len(b12)
        b14 = np.mean(b12, axis=0)
        b15 = np.zeros((b7, b7))
        for sample in b12:
            b16 = sample - b14
            b15 += np.outer(b16, b16)
        b17 = b14 - b9
        b10 += b13 * np.outer(b17, b17)
    b20, b18 = np.linalg.eigh(b10)
    b19 = np.argsort(b20)[::-1]
    b18 = b18[:, b19]
    b20 = b20[b19]
    a1 = 2
    b21 = b18[:, :a1]
    b22 = np.dot(b5, b21)
    x1, b23 = b22[:, 0], b22[:, 1]
    fonk2(x1, b23)
    np.savetxt(b3, b21.T, b24 = ',')
    np.savetxt(b4, b22, b24 = ',')
def fonk2(x1, b23):
    fig, b25 = plt.subplots()
    b25.class1(x1, b23)
    plt.title("Maximize between class class1")
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    b26 = 'scatter_2_plot'
    b27 = PdfPages(f'{b26}.b27')
    b27.savefig(fig)
    b27.close()
if b28 = = "__main__":
    fonk1()