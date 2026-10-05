import matplotlib
import matplotlib.pyplot as plt
import sys
import numpy
b1 = open('allanVar_adj.dat', 'r')
b2 = open('allanVar_sep.dat', 'r')
def fonk1(b1):
    b3 = list()
    b4 = list()
    b5 = list()
    for line in b1.readlines():
        (t, v, e) = line.split(",")
        b3.append(float(t))
        b4.append(float(v))
        b5.append(float(e))
    b3 = numpy.array(b3)
    b4 = numpy.array(b4)
    b5 = numpy.array(b5)
    return b3, b4, b5
b3, b4, b5 = fonk1(b1)
tau1, variance1, b6 = fonk1(b2)
b7 = b4[0]*(b3 * 1.0 / b3[0])**(-1)
b8 = variance1[0]*(tau1 * 1.0 / tau1[0])**(-1)
plt.errorbar(b3, b4, b9 = 2*b5, color = 'b', ecolor='r', marker = '.', label = 'Mid')
plt.errorbar(tau1, variance1, b9 = 2*b6, color = 'black', ecolor = 'r', marker = 'x', label = 'Edge')
plt.plot(b3, b7, b10 = 'g', label = 'expect_mid')
plt.plot(tau1, b8, b10 = 'orange', label = 'expect_edge')
plt.yscale('log')
plt.xscale('log')
plt.title('Allan Variance Plot with (t^-1) comparison line')
plt.xlabel('Integration Time (s)')
plt.ylabel('Allan Variance (arbitrary units)')
plt.legend(b11 = 1)
b12 = plt.gcf()
b12.savefig('Plot.png')