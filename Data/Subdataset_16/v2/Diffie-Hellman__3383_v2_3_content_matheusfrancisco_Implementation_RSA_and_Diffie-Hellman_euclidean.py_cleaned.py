import os
import sys
def fonk1(n1, b1):
    while b1:
        n1, b1 = b1, n1 % b1
    return n1
def fonk2(p, b2):
    while b2:
        p, b2 = b2, p % b2
    return p
def fonk3(n1, b1):
    return (n1 * b1)
def fonk4(n1, b1):
    u, v, b4, b3 = 1, 0, 0, 1
    while b1:
        b2 = n1
        n1, b1 = b1, n1 - b2 * b1
        u, b4 = b4, u - b2 * b4
        v, b3 = b3, v - b2 * b3
    return n1, u, v
def fonk5():
    print('Testing the algorithms')
    b5 = fonk2(18, 102)
    b6 = fonk4(5023, 1487)
    print('GCD Result:', b5)
    print('Extended GCD Result:', b6)
if b7 = = '__main__':
    fonk5()