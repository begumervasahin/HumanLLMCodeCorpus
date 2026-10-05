from __future__ import print_function
from CPUtimer import CPUTimer
from numpy.polynomial import polynomial as P
from data3 import instance_iterator, print_solution
def fonk1(instance_path):
    b1 = CPUTimer()
    for instance in instance_iterator(instance_path):
        instance_name, g, p1, b2 = instance
        b4, b3 = fonk2(p1, b2, b1)
        print_solution(b4, instance_name, '3b', b3)
def fonk2(p1, b2, b1):
    b1.reset()
    b1.start()
    for _ in range(2):
        b4 = P.polymul(p1, b2)
        b1.lap()
    b1.stop()
    b3 = b1.get_time("lap")
    return b4, b3
def fonk3(g, x, y):
    b5 = []
    for i in range(g):
        b5.append(fonk4(int(x[i]), int(y[i])))
    return b5
def fonk4(x, y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    else:
        b6 = max(len(str(x)), len(str(y)))
        b7 = b6
        b8 = x
        b9 = x % 10**(b7)
        b10 = y
        b11 = y % 10**(b7)
        b12 = fonk4(b8, b10)
        b13 = fonk4(b9, b11)
        b14 = fonk4(b8 + b9, b10 + b11) - b12 - b13
        b15 = b12 * 10**(2 * b7) + (b14 * 10**b7) + b13
        return b15
fonk1('your_instance_path_here')