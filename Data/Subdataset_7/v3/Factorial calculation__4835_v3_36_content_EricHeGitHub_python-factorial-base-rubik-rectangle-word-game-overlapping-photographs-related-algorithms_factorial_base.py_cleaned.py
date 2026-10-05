import time
from sys import exit
def fonk1(n):
    a1 = 1
    for i in range(1, n + 1):
        a1 *= i
    return a1
def fonk2(lst):
    a1 = 0
    b1 = len(lst) - 1
    for digit in lst:
        if not str(digit).isdigit():
            return None
        a1 += digit * 10 ** b1
        b1 -= 1
    return a1
def fonk3():
    b2 = input('Input a nonnegative integer: ')
    if not b2.isdigit() or b2.startswith('0'):
        print('Incorrect input, giving up...')
        exit()
    return int(b2)
def fonk4(b2):
    a2 = 1
    while fonk1(a2) <= b2:
        a2 += 1
    return a2 - 1
def fonk5(b2, a2):
    a3 = 0
    b3 = []
    while b2:
        for i in range(a2, 0, -1):
            while a3 * fonk1(i) < b2:
                a3 += 1
            if a3 * fonk1(i) > b2:
                a3 -= 1
            b3.append(a3)
            b2 -= a3 * fonk1(i)
            a3 = 0
    return b3
def fonk6():
    b2 = fonk3()
    a2 = fonk4(b2)
    b3 = fonk5(b2, a2)
    print('Decimal {} reads as {} in factorial base.'.format(b2, fonk2(b3)))
if b4 = = "__main__":
    fonk6()