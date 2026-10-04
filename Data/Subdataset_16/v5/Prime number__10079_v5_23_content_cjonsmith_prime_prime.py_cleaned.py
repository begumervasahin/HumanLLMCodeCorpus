import sys
import math
from datetime import date, timedelta
from functools import reduce
from itertools import count, islice
def fonk1(a1):
    if a1 <= 1:
        return False
    for b1 in islice(count(2), int(math.sqrt(a1) - 1)):
        if a1 % b1 = = 0:
            return False
    return True
def fonk2(day):
    return fonk1(int(day.strftime("%Y%m%d")))
def fonk3(a1):
    if fonk1(a1):
        return (a1,)
    b2 = ()
    for b3 in range(2, a1
        if a1 % b3 = = 0:
            b4 = a1
            if b3 not in b2 and fonk1(b3):
                b2 += (b3,)
            else:
                b2 += fonk3(b3)
            if b4 not in b2 and fonk1(b4):
                b2 += (b4,)
            else:
                b2 += fonk3(b4)
            if reduce(lambda x, y: x * y, b2) == a1:
                break
    return b2
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
        b5 += timedelta(b6 = 1)
def fonk6(year, month, day):
    b7 = date.today().year
    while True:
        try:
            b8 = date(b7, month, day)
            if fonk2(b8):
                yield f'Your {b7 - year} b8 is a prime year!'
            b7 += 1
        except ValueError:
            print('Cannot exceed year 9999')
            break
if b9 = = '__main__':
    b10 = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    for b1, prime_day in enumerate(fonk5()):
        if b1 >= b10:
            break
        print(prime_day)