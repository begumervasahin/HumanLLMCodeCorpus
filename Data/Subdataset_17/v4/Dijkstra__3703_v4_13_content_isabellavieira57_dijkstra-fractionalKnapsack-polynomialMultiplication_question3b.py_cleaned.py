from __future__ import print_function
import CPUtimer
from numpy.polynomial import polynomial as P
from data3 import instance_iterator, print_solution
def solve(instance_path):
    timer = CPUtimer.CPUTimer()
    for instance in instance_iterator(instance_path):
        instance_name, degree, p1, p2 = instance
        timer.reset()
        timer.start()
        for _ in range(2):
            result = P.polymul(p1, p2)
            timer.lap()
        timer.stop()
        print_solution(result, instance_name, '3b', timer)
def mult(degree, x, y):
    product = []
    for i in range(degree):
        product.append(karatsuba(int(x[i]), int(y[i])))
    return product
def karatsuba(x, y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    n = max(len(str(x)), len(str(y)))
    nby2 = n
    a = x
    b = x % 10**nby2
    c = y
    d = y % 10**nby2
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd
    return ac * 10**(2 * nby2) + ad_plus_bc * 10**nby2 + bd
if __name__ == "__main__":
    instance_path = 'path_to_instance_file'
    solve(instance_path)