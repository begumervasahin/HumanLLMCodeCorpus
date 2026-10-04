
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import sys
if len(sys.argv) != 5:
    print(f"{sys.argv[0]} takes 4 arguments. Not {len(sys.argv) - 1}")
    sys.exit()
first, second, third, four = sys.argv[1:5]
Xt = np.genfromtxt(first, delimiter=',')
y = np.genfromtxt(second, autostrip=True)
m, n = Xt.shape
unique_labels = set(y)
mu_global = np.mean(Xt, axis=0)
W_class = np.zeros((n, n))
B_class = np.zeros((n, n))
for c in unique_labels:
    B1 = np.zeros((n, n))
    BT1 = np.zeros((n, n))
    s1 = np.zeros((1, n))
    C1 = np.zeros((n, n))
    m1 = 0
    for i, xt in enumerate(Xt):
        if y[i] == c:
            B1 += np.dot(xt.T, xt)
            s1 += xt
            m1 += 1
    mu1 = s1 / m1
    for i, xt in enumerate(Xt):
        if y[i] == c:
            ct = xt - mu1
            bt = mu1 - mu_global
            C1 += np.dot(ct.T, ct)
            BT1 += np.dot(bt.T, bt)
    W_class += C1
    B_class += BT1
x = np.dot(np.linalg.inv(W_class), B_class)
evals, evecs = np.linalg.eig(x)
r = 2
V_r = evecs[:, :r]
result = np.dot(Xt, V_r)
x1 = result[:, 0]
x2 = result[:, 1]
fig, ax = plt.subplots()
ax.scatter(x1, x2)
plt.title("Maximize the ratio of between-class scatter and within-class scatter")
plt.xlabel("PC1")
plt.ylabel("PC2")
plotname = 'scatter_3_plot'
pdf = PdfPages(plotname + '.pdf')
pdf.savefig(fig)
pdf.close()
np.savetxt(third, V_r.T, delimiter=',')
np.savetxt(four, result, delimiter=',')