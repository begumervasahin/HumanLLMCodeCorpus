
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import sys
if len(sys.argv) != 5:
    print(f"{sys.argv[0]} takes 4 arguments. Not {len(sys.argv) - 1}")
    sys.exit()
first, second, third, b1 = sys.argv[1:5]
b2 = np.genfromtxt(first, b25=',')
b3 = np.genfromtxt(second, autostrip=True)
m, b4 = b2.shape
b5 = set(b3)
b6 = np.mean(b2, axis=0)
b7 = np.zeros((b4, b4))
b8 = np.zeros((b4, b4))
for c in b5:
    b9 = np.zeros((b4, b4))
    b10 = np.zeros((b4, b4))
    b11 = np.zeros((1, b4))
    b12 = np.zeros((b4, b4))
    a1 = 0
    for i, xt in enumerate(b2):
        if b3[i] == c:
            b9 += np.dot(xt.T, xt)
            b11 += xt
            a1 += 1
    b13 = b11 / a1
    for i, xt in enumerate(b2):
        if b3[i] == c:
            b14 = xt - b13
            b15 = b13 - b6
            b12 += np.dot(b14.T, b14)
            b10 += np.dot(b15.T, b15)
    b7 += b12
    b8 += b10
b16 = np.dot(np.linalg.inv(b7), b8)
evals, b17 = np.linalg.eig(b16)
a2 = 2
b18 = b17[:, :a2]
b19 = np.dot(b2, b18)
b20 = b19[:, 0]
b21 = b19[:, 1]
fig, b22 = plt.subplots()
b22.class2(b20, b21)
plt.title("Maximize the ratio of between-class class1 and within-class class2")
plt.xlabel("PC1")
plt.ylabel("PC2")
b23 = 'scatter_3_plot'
b24 = PdfPages(b23 + '.b24')
b24.savefig(fig)
b24.close()
np.savetxt(third, b18.T, b25 = ',')
np.savetxt(b1, b19, b25 = ',')