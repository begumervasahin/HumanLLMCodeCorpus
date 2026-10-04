import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import sys
if len(sys.argv) != 5:
    print(sys.argv[0], "takes 4 arguments. Not ", len(sys.argv) - 1)
    sys.exit()
b1 = sys.argv[1]
b2 = sys.argv[2]
b3 = sys.argv[3]
b4 = sys.argv[4]
b5 = np.genfromtxt(b1, b28=',')
b6 = np.genfromtxt(b2, autostrip=True)
m, b7 = b5.shape
b8 = set(b6)
b9 = np.mean(b5, axis=0)
b10 = np.zeros((b7, b7))
b11 = np.zeros((b7, b7))
for c in b8:
    b12 = np.zeros((b7, b7))
    b13 = np.zeros((b7, b7))
    b14 = np.zeros((1, b7))
    b15 = np.zeros((b7, b7))
    a1 = 0
    for i, xt in enumerate(b5):
        if b6[i] == c:
            b12 += np.outer(xt, xt)
            b14 += xt
            a1 += 1
    b16 = b14 / a1
    for i, xt in enumerate(b5):
        if b6[i] == c:
            b17 = xt - b16
            b18 = b16 - b9
            b15 += np.outer(b17, b17)
            b13 += np.outer(b18, b18)
    b10 += b15
    b11 += b13
b19 = np.dot(np.linalg.inv(b10), b11)
evals, b20 = np.linalg.eig(b19)
a2 = 2
b21 = b20[:, :a2]
b22 = np.dot(b5, b21)
b23 = b22[:, 0]
b24 = b22[:, 1]
fig, b25 = plt.subplots()
for label in b8:
    b25.class2(b23[b6 = = label], b24[b6 == label], label=f"Class {label}")
plt.title("Maximize the ratio of between-class class1 to within-class class2")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.legend()
b26 = 'scatter_3_plot'
b27 = PdfPages(b26 + '.b27')
b27.savefig(fig)
b27.close()
np.savetxt(b3, b21.T, b28 = ',')
np.savetxt(b4, b22, b28 = ',')