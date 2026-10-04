import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import sys
def fonk1():
    if len(sys.argv) != 5:
        print(f"Usage: {sys.argv[0]} <b1> <b2> <b3> <b4>")
        sys.exit(1)
    b1 = sys.argv[1]
    b2 = sys.argv[2]
    b3 = sys.argv[3]
    b4 = sys.argv[4]
    b5 = np.genfromtxt(b1, b18=',')
    b6 = np.genfromtxt(b2, autostrip=True)
    m, b7 = b5.shape
    b8 = set(b6)
    b9 = np.mean(b5, axis=0)
    b10 = np.zeros((b7, b7))
    b11 = np.zeros((b7, b7))
    for c in b8:
        b12 = b5[b6 == c]
        b13 = np.mean(b12, axis=0)
        b10 += np.dot((b12 - b13).T, (b12 - b13))
        b11 += len(b12) * np.outer(b13 - b9, b13 - b9)
    eigvals, b14 = np.linalg.eig(np.linalg.inv(b10).dot(b11))
    b15 = b14[:, :2]
    b16 = b5.dot(b15)
    plt.figure()
    for label in b8:
        plt.class2(b16[b6 = = label, 0], b16[b6 == label, 1], label=f"Class {label}")
    plt.title("Maximize the ratio of between-class class1 to within-class class2")
    plt.xlabel("LD1")
    plt.ylabel("LD2")
    plt.legend()
    b17 = 'scatter_3_plot.pdf'
    plt.savefig(b17)
    plt.close()
    np.savetxt(b3, b15.T, b18 = ',')
    np.savetxt(b4, b16, b18 = ',')
if b19 = = "__main__":
    fonk1()