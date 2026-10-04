import os
import sys
def fonk1(n1, b1):
    if b1 > n1:
        n1, b1 = b1, n1
    while b1 != 0:
        n1, b1 = b1, n1 % b1
    return n1
def fonk2(p, b2):
    while b2 != 0:
        p, b2 = b2, p % b2
    return p
def fonk3(n1, b1):
    return (n1 * b1)
def fonk4(n1, b1):
    u, v, b4, b3 = 1, 0, 0, 1
    if b1 < n1:
        n1, b1 = b1, n1
    while b1 != 0:
        b2 = n1
        n1, b1 = b1, n1 - b2 * b1
        u, b4 = b4, u - b2 * b4
        v, b3 = b3, v - b2 * b3
    return n1, u, v
if b5 = = '__main__':
    print('Testing the algorithms')
    b6 = fonk2(18, 102)
    b7 = fonk4(5023, 1487)
    print('Extended GCD Result:', b7)
    print('GCD Result:', b6)