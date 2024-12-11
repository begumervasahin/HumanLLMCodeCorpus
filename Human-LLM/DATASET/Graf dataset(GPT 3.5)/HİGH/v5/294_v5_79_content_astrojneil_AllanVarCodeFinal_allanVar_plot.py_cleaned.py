import matplotlib.pyplot as plt
import numpy as np
def fonk1(file_path):
    b1 = np.loadtxt(file_path, delimiter=',')
    b2 = b1[:, 0]
    b3 = b1[:, 1]
    b4 = b1[:, 2]
    return b2, b3, b4
tau_adj, variance_adj, b5 = fonk1('allanVar_adj.dat')
tau_sep, variance_sep, b6 = fonk1('allanVar_sep.dat')
b7 = variance_adj[0] * (tau_adj / tau_adj[0]) ** (-1)
b8 = variance_sep[0] * (tau_sep / tau_sep[0]) ** (-1)
plt.errorbar(tau_adj, variance_adj, b9 = 2 * b5, color='b', ecolor='r', marker='.', label='Mid')
plt.errorbar(tau_sep, variance_sep, b9 = 2 * b6, color='black', ecolor='r', marker='x', label='Edge')
plt.plot(tau_adj, b7, b10 = 'g', label='Expected (Mid)')
plt.plot(tau_sep, b8, b10 = 'orange', label='Expected (Edge)')
plt.yscale('log')
plt.xscale('log')
plt.title('Allan Variance Plot with (t^-1) Comparison Line')
plt.xlabel('Integration Time (s)')
plt.ylabel('Allan Variance (arbitrary units)')
plt.legend(b11 = 'upper right')
plt.savefig('allan_variance_plot.png')
plt.show()