import sys
import math
from datetime import date
from functools import reduce
from math import sqrt
from itertools import count, islice
def fonk1(a1):
    return a1 > 1 and all(a1 % i for i in islice(count(2), int(sqrt(a1)) + 1))
def fonk2(day):
    return fonk1(int(day.strftime('%Y%m%d')))
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
        if fonk1(a1):
            yield a1
        a1 += 1
def fonk5(b5 = date.today()):
    while True:
        if fonk2(b5):
            yield b5
        try:
            b5 = b5.replace(day=b5.day + 1)
        except ValueError:
            try:
                b5 = b5.replace(month=b5.month + 1, day=1)
            except ValueError:
                b5 = b5.replace(year=b5.year + 1, month=1, day=1)
def fonk6(year, month, day):
    b6 = date.today().year
    while True:
        try:
            b7 = date(b6, month, day)
            if fonk2(b7):
                yield f'Your {b6 - year}th b7 is a prime year!'
            b6 += 1
        except ValueError:
            print('Cannot exceed year 9999')
            break
if b8 = = '__main__':
    b9 = 1 if len(sys.argv) < 2 else int(sys.argv[1])
    for i, prime_day in enumerate(fonk5()):
        if i >= b9:
            break
        print(prime_day)