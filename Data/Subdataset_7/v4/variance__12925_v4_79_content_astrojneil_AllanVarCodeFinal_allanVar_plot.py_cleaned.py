import matplotlib.pyplot as plt
import numpy as np
with open('allanVar_adj.dat', 'r') as f:
    b4, b5, b1 = np.loadtxt(f, delimiter=',', unpack=True)
with open('allanVar_sep.dat', 'r') as f1:
    tau1, variance1, b2 = np.loadtxt(f1, delimiter=',', unpack=True)
def fonk1(file):
    b3 = np.loadtxt(file, delimiter=',')
    b4 = b3[:, 0]
    b5 = b3[:, 1]
    b1 = b3[:, 2]
    return b4, b5, b1
b4, b5, b1 = fonk1('allanVar_adj.dat')
tau1, variance1, b2 = fonk1('allanVar_sep.dat')
b6 = b5[0] * (b4 * 1.0 / b4[0]) ** (-1)
b7 = variance1[0] * (tau1 * 1.0 / tau1[0]) ** (-1)
plt.errorbar(b4, b5, b8 = 2 * b1, color='b', ecolor='r', marker='.', label='Mid')
plt.errorbar(tau1, variance1, b8 = 2 * b2, color='black', ecolor='r', marker='x', label='Edge')
plt.plot(b4, b6, b9 = 'g', label='expect_mid')
plt.plot(tau1, b7, b9 = 'orange', label='expect_edge')
plt.yscale('log')
plt.xscale('log')
plt.title('Allan Variance Plot with (t^-1) comparison line')
plt.xlabel('Integration Time (s)')
plt.ylabel('Allan Variance (arbitrary units)')
plt.legend(b10 = 1)
plt.savefig('Plot.png')
plt.show()