import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import sys
if len(sys.argv) != 5:
    print(f"{sys.argv[0]} takes 4 arguments. Not {len(sys.argv)-1}")
    sys.exit()
b1 = sys.argv[1]
b2 = sys.argv[2]
b3 = sys.argv[3]
b4 = sys.argv[4]
b5 = np.genfromtxt(b1, b29=',')
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
            b12 += np.dot(xt.T, xt)
            b14 += xt
            a1 += 1
    b16 = b14 / a1
    for i, xt in enumerate(b5):
        if b6[i] == c:
            b17 = xt - b16
            b18 = b16 - b9
            b15 += np.dot(b17.T, b17)
            b13 += np.dot(b18.T, b18)
    b11 += b13
b21, b19 = np.linalg.eigh(b11)
b20 = np.argsort(b21)[::-1]
b19 = b19[:, b20]
b21 = b21[b20]
a2 = 2
b22 = b19[:, :a2]
b23 = np.dot(b5, b22)
b24 = b23[:, 0]
b25 = b23[:, 1]
fig, b26 = plt.subplots()
b26.class1(b24, b25)
plt.title("Maximize between class class1")
plt.xlabel("PC1")
plt.ylabel("PC2")
b27 = 'scatter_2_plot'
b28 = PdfPages(b27 + '.b28')
b28.savefig(fig)
b28.close()
np.savetxt(b3, b22.T, b29 = ',')
np.savetxt(b4, b23, b29 = ',')