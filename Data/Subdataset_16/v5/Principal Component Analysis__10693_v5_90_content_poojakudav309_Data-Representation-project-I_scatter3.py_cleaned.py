
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import sys
def fonk1():
    if len(sys.argv) != 5:
        print(f"{sys.argv[0]} takes 4 arguments. Not {len(sys.argv) - 1}")
        sys.exit()
    first, second, third, b1 = sys.argv[1:5]
    b2 = np.genfromtxt(first, b5=',')
    b3 = np.genfromtxt(second, autostrip=True)
    b14, b4 = fonk2(b2, b3)
    fonk4(b4)
    np.savetxt(third, b14.T, b5 = ',')
    np.savetxt(b1, b4, b5 = ',')
def fonk2(b2, b3):
    m, b6 = b2.shape
    b7 = set(b3)
    b8 = np.mean(b2, axis=0)
    b9 = np.zeros((b6, b6))
    b10 = np.zeros((b6, b6))
    for c in b7:
        b15, b16, b11 = fonk3(b2, b3, c, b8)
        b9 += b15
        b10 += b16
    b12 = np.dot(np.linalg.inv(b9), b10)
    evals, b13 = np.linalg.eig(b12)
    a1 = 2
    b14 = b13[:, :a1]
    b4 = np.dot(b2, b14)
    return b14, b4
def fonk3(b2, b3, label, b8):
    b6 = b2.shape[1]
    b15 = np.zeros((b6, b6))
    b16 = np.zeros((b6, b6))
    b17 = np.zeros((1, b6))
    a2 = 0
    for i, xt in enumerate(b2):
        if b3[i] == label:
            b17 += xt
            a2 += 1
    b11 = b17 / a2
    for i, xt in enumerate(b2):
        if b3[i] == label:
            b18 = xt - b11
            b19 = b11 - b8
            b15 += np.dot(b18.T, b18)
            b16 += np.dot(b19.T, b19)
    return b15, b16, b11
def fonk4(b4):
    b20 = b4[:, 0]
    b21 = b4[:, 1]
    fig, b22 = plt.subplots()
    b22.class2(b20, b21)
    plt.title("Maximize the ratio of between-class class1 and within-class class2")
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    b23 = 'scatter_3_plot'
    b24 = PdfPages(b23 + '.b24')
    b24.savefig(fig)
    b24.close()
if b25 = = "__main__":
    fonk1()