import matplotlib.pyplot as plt
import numpy as np
def read_data(file_path):
    tau, variance, error = [], [], []
    with open(file_path, 'r') as file:
        for line in file:
            t, v, e = map(float, line.split(","))
            tau.append(t)
            variance.append(v)
            error.append(e)
    return np.array(tau), np.array(variance), np.array(error)
tau_mid, variance_mid, error_mid = read_data('allanVar_adj.dat')
tau_edge, variance_edge, error_edge = read_data('allanVar_sep.dat')
expected_mid = variance_mid[0] * (tau_mid / tau_mid[0])**(-1)
expected_edge = variance_edge[0] * (tau_edge / tau_edge[0])**(-1)
plt.errorbar(tau_mid, variance_mid, yerr=2*error_mid, color='b', ecolor='r', marker='.', label='Mid')
plt.errorbar(tau_edge, variance_edge, yerr=2*error_edge, color='black', ecolor='r', marker='x', label='Edge')
plt.plot(tau_mid, expected_mid, c='g', label='Expected Mid')
plt.plot(tau_edge, expected_edge, c='orange', label='Expected Edge')
plt.yscale('log')
plt.xscale('log')
plt.title('Allan Variance Plot with $\\tau^{-1}$ Comparison Line')
plt.xlabel('Integration Time (s)')
plt.ylabel('Allan Variance (arbitrary units)')
plt.legend(loc='best')
plt.grid(True, which="both", ls="--")
plt.savefig('Plot.png')
plt.show()