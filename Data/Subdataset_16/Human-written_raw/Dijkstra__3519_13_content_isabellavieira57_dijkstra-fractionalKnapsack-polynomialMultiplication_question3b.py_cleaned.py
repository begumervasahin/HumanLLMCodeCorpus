from __future__ import print_function
import CPUtimer
from numpy.polynomial import polynomial as P
from data3 import instance_iterator, print_solution
b1 = []
def fonk1(instance_path):
    b2 = CPUtimer.CPUTimer()
    for instance in instance_iterator(instance_path):
        instance_name, g, p1, b3 = instance
        b2.reset()
        b2.start()
        for i in range(0, 2):
            b4 = P.polymul(p1, b3)
            b2.lap()
        b2.stop()
        print_solution(b4, instance_name, '3b', b2)
def fonk2(g, x, y):
    b5 = []
    for i in range(0, g):
        b5.append(fonk3(int(x[i]),int(y[i])))
    return b5
def fonk3(x,y):
	if len(str(x)) == 1 or len(str(y)) == 1:
		return x*y
	else:
		b6 = max(len(str(x)),len(str(y)))
		b7 = b6 / 2
		b8 = x / 10**(b7)
		b9 = x % 10**(b7)
		b10 = y / 10**(b7)
		b11 = y % 10**(b7)
		b12 = fonk3(b8,b10)
		b13 = fonk3(b9,b11)
		b14 = fonk3(b8+b9,b10+b11) - b12 - b13
		b1 = b12 * 10**(2*b7) + (b14 * 10**b7) + b13
		return b1