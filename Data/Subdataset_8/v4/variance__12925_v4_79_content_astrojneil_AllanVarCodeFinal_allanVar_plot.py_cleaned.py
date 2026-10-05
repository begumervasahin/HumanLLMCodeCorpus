import matplotlib.pyplot as plt
import numpy as np
with open('allanVar_adj.dat', 'r') as f:
    tau, variance, error = np.loadtxt(f, delimiter=',', unpack=True)
with open('allanVar_sep.dat', 'r') as f1:
    tau1, variance1, error1 = np.loadtxt(f1, delimiter=',', unpack=True)
def read_file(file):
    data = np.loadtxt(file, delimiter=',')
    tau = data[:, 0]
    variance = data[:, 1]
    error = data[:, 2]
    return tau, variance, error
tau, variance, error = read_file('allanVar_adj.dat')
tau1, variance1, error1 = read_file('allanVar_sep.dat')
expected = variance[0] * (tau * 1.0 / tau[0]) ** (-1)
expected1 = variance1[0] * (tau1 * 1.0 / tau1[0]) ** (-1)
plt.errorbar(tau, variance, yerr=2 * error, color='b', ecolor='r', marker='.', label='Mid')
plt.errorbar(tau1, variance1, yerr=2 * error1, color='black', ecolor='r', marker='x', label='Edge')
plt.plot(tau, expected, c='g', label='expect_mid')
plt.plot(tau1, expected1, c='orange', label='expect_edge')
plt.yscale('log')
plt.xscale('log')
plt.title('Allan Variance Plot with (t^-1) comparison line')
plt.xlabel('Integration Time (s)')
plt.ylabel('Allan Variance (arbitrary units)')
plt.legend(loc=1)
plt.savefig('Plot.png')
plt.show()