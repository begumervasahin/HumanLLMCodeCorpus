import sys
import math
from datetime import date
from functools import reduce
from math import sqrt
from itertools import count, islice
def fonk1(a1):
    return a1 > 1 and all(a1 % i for i in islice(count(2), int(sqrt(a1)-1)))
def fonk2(b6):
    return fonk1(int(str(b6).replace('-', '')))
def fonk3(a1):
    b1 = ()
    if fonk1(a1):
        return (a1,)
    b2 = a1
    for b3 in range(2, b2 + 1):
        if a1 % b3 = = 0:
            b4 = a1
            if b4 in b1 or b3 in b1:
                continue
            if fonk1(b3):
                b1 += (b3,)
            else:
                b1 += fonk3(b3)
            if fonk1(b4):
                b1 += (b4,)
            else:
                b1 += fonk3(b4)
            if reduce(lambda x, y: x * y, b1) == a1:
                break
    return b1
def fonk4():
    a1 = 2
    while True:
        if fonk1(a1): yield a1
        a1 += 1
def fonk5(b5 = date.today()):
    b6 = b5.b6
    b7 = b5.b7
    b8 = b5.b8
    while True:
        if fonk2(b5):
            yield b5
        try:
            b6 += 1
            b5 = date(b8, b7, b6)
            continue
        except ValueError:
            try:
                b6 = 1
                b7 += 1
                b5 = date(b8, b7, b6)
                continue
            except ValueError:
                try:
                    b7 = 1
                    b8 += 1
                    b5 = date(b8, b7, b6)
                    continue
                except ValueError:
                    print('Exceeded b8 9999')
                    break
def fonk6(b8, b7, b6):
    b9 = date.today().b8
    while True:
        try:
            b10 = date(b9, b7, b6)
            if fonk2(b10):
                yield 'Your {} b10 is a prime b8!'.format(b9 - b8)
            b9 += 1
        except ValueError:
            print('Cannot exceed b8 9999')
            break
if b11 = = '__main__':
    b12 = 1 if len(sys.argv) < 2 else int(sys.argv[1])
    for i, prime_day in enumerate(fonk5()):
       if i >= b12: break
       print(prime_day)