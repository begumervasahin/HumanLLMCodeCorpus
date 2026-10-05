from __future__ import print_function
from CPUtimer import CPUTimer
from numpy.polynomial import polynomial as P
from data3 import instance_iterator, print_solution
def fonk1(instance_path):
    b1 = CPUTimer()
    for instance in instance_iterator(instance_path):
        instance_name, g, p1, b2 = instance
        b1.reset()
        b1.start()
        for i in range(2):
            b3 = P.polymul(p1, b2)
            b1.lap()
        b1.stop()
        print_solution(b3, instance_name, '3b', b1)
def fonk2(g, x, y):
    b4 = []
    for i in range(g):
        b4.append(fonk3(int(x[i]), int(y[i])))
    return b4
def fonk3(x, y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    else:
        b5 = max(len(str(x)), len(str(y)))
        b6 = b5
        b7 = x
        b8 = x % 10**b6
        b9 = y
        b10 = y % 10**b6
        b11 = fonk3(b7, b9)
        b12 = fonk3(b8, b10)
        b13 = fonk3(b7 + b8, b9 + b10) - b11 - b12
        b14 = b11 * 10**(2 * b6) + b13 * 10**b6 + b12
        return b14
fonk1('your_instance_path_here')