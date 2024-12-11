from sys import exit
import time
b1 = time.time()
from itertools import product
def fonk1(n):
    a1 = 1
    for i in range(n):
        a1 *= i+1
    return a1
def fonk2(List):
    a1 = 0
    b2 = len(List) - 1
    for i in List:
        if not str(i).isdigit:
            return
        else:
            a1 += i * 10 ** b2
        b2 -= 1
    return a1
b3 = input('Input a nonnegative integer: ')
if not b3.isdigit() or b3[0] == '0':
    print('Incorrect input, giving up...')
    exit()
b3 = int(b3)
a2 = 1
while fonk1(a2) <= b3:
    a2 += 1
a2 -= 1
a3 = 0
b4 = []
b5 = b3
while b3:
    for i in range(a2, 0 , -1):
        while a3 * fonk1(i) < b3:
            a3 += 1
        if a3 * fonk1(i) > b3:
            a3 -= 1
        else:
            pass
        b4.append(a3)
        b3 -= a3 * fonk1(i)
        a3 = 0
print('Decimal {} reads as {} in factorial base.'.format(b5, fonk2(b4)))