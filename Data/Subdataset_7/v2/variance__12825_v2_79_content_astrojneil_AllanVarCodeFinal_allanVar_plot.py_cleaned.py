import matplotlib.pyplot as plt
import numpy as np
def fonk1(file_path):
    b1 = []
    b2 = []
    b3 = []
    with open(file_path, 'r') as file:
        for line in file:
            t, v, b4 = map(float, line.split(","))
            b1.append(t)
            b2.append(v)
            b3.append(b4)
    return np.array(b1), np.array(b2), np.array(b3)
tau_mid, variance_mid, b5 = fonk1('allanVar_adj.dat')
tau_edge, variance_edge, b6 = fonk1('allanVar_sep.dat')
b7 = variance_mid[0] * (tau_mid / tau_mid[0])**(-1)
b8 = variance_edge[0] * (tau_edge / tau_edge[0])**(-1)
plt.errorbar(tau_mid, variance_mid, b9 = 2*b5, color='b', ecolor='r', marker='.', label='Mid')
plt.errorbar(tau_edge, variance_edge, b9 = 2*b6, color='black', ecolor='r', marker='x', label='Edge')
plt.plot(tau_mid, b7, b10 = 'g', label='Expected Mid')
plt.plot(tau_edge, b8, b10 = 'orange', label='Expected Edge')
plt.yscale('log')
plt.xscale('log')
plt.title('Allan Variance Plot with $\\b1^{-1}$ Comparison Line')
plt.xlabel('Integration Time (s)')
plt.ylabel('Allan Variance (arbitrary units)')
plt.legend(b11 = 'best')
plt.grid(True, b12 = "both", ls="--")
plt.savefig('Plot.png')
plt.show()