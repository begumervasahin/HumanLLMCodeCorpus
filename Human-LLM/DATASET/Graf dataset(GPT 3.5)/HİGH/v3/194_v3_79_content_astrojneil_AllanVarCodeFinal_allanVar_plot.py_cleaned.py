import matplotlib.pyplot as plt
import numpy as np
def fonk1(file_path):
    tau, variance, b1 = [], [], []
    with open(file_path, 'r') as file:
        for line in file:
            t, v, b2 = map(float, line.split(","))
            tau.append(t)
            variance.append(v)
            b1.append(b2)
    return np.array(tau), np.array(variance), np.array(b1)
tau_mid, variance_mid, b3 = fonk1('allanVar_adj.dat')
tau_edge, variance_edge, b4 = fonk1('allanVar_sep.dat')
b5 = variance_mid[0] * (tau_mid / tau_mid[0])**(-1)
b6 = variance_edge[0] * (tau_edge / tau_edge[0])**(-1)
plt.errorbar(tau_mid, variance_mid, b7 = 2*b3, color='b', ecolor='r', marker='.', label='Mid')
plt.errorbar(tau_edge, variance_edge, b7 = 2*b4, color='black', ecolor='r', marker='x', label='Edge')
plt.plot(tau_mid, b5, b8 = 'g', label='Expected Mid')
plt.plot(tau_edge, b6, b8 = 'orange', label='Expected Edge')
plt.yscale('log')
plt.xscale('log')
plt.title('Allan Variance Plot with $\\tau^{-1}$ Comparison Line')
plt.xlabel('Integration Time (s)')
plt.ylabel('Allan Variance (arbitrary units)')
plt.legend(b9 = 'best')
plt.grid(True, b10 = "both", ls="--")
plt.savefig('Plot.png')
plt.show()