import matplotlib
import matplotlib.pyplot as plt
import sys
import numpy
f = open('allanVar_adj.dat', 'r')
f1 = open('allanVar_sep.dat', 'r')
def read_file(f):
    tau = list()
    variance = list()
    error = list()
    for line in f.readlines():
        (t, v, e) = line.split(",")
        tau.append(float(t))
        variance.append(float(v))
        error.append(float(e))
    tau = numpy.array(tau)
    variance = numpy.array(variance)
    error = numpy.array(error)
    return tau, variance, error
tau, variance, error = read_file(f)
tau1, variance1, error1 = read_file(f1)
expected = variance[0]*(tau * 1.0 / tau[0])**(-1)
expected1 = variance1[0]*(tau1 * 1.0 / tau1[0])**(-1)
plt.errorbar(tau, variance, yerr=2*error, color = 'b', ecolor='r', marker = '.', label = 'Mid')
plt.errorbar(tau1, variance1, yerr= 2*error1, color = 'black', ecolor = 'r', marker = 'x', label = 'Edge')
plt.plot(tau, expected, c='g', label = 'expect_mid')
plt.plot(tau1, expected1, c='orange', label = 'expect_edge')
plt.yscale('log')
plt.xscale('log')
plt.title('Allan Variance Plot with (t^-1) comparison line')
plt.xlabel('Integration Time (s)')
plt.ylabel('Allan Variance (arbitrary units)')
plt.legend(loc=1)
fig = plt.gcf()
fig.savefig('Plot.png')