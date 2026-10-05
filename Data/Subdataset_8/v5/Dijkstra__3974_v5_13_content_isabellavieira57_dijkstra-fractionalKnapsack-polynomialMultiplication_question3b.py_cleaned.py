from __future__ import print_function
from CPUtimer import CPUTimer
from numpy.polynomial import polynomial as P
from data3 import instance_iterator, print_solution
def solve(instance_path):
    timer = CPUTimer()
    for instance in instance_iterator(instance_path):
        instance_name, degree, poly1, poly2 = instance
        timer.reset()
        timer.start()
        for _ in range(2):
            result = P.polymul(poly1, poly2)
            timer.lap()
        timer.stop()
        print_solution(result, instance_name, '3b', timer)
def multiply_arrays_elementwise(degree, array1, array2):
    product = []
    for i in range(degree):
        product.append(karatsuba(int(array1[i]), int(array2[i])))
    return product
def karatsuba(x, y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    else:
        n = max(len(str(x)), len(str(y)))
        nby2 = n
        a = x
        b = x % 10**nby2
        c = y
        d = y % 10**nby2
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_plus_bc = karatsuba(a + b, c + d) - ac - bd
        prod = ac * 10**(2 * nby2) + ad_plus_bc * 10**nby2 + bd
        return prod
solve('your_instance_path_here')