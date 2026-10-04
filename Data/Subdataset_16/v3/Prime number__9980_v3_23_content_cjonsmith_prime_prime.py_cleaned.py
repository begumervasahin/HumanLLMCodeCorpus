import sys
import math
from datetime import date
from functools import reduce
from itertools import count, islice
def fonk1(a1):
    if a1 < 2:
        return False
    for b1 in islice(count(2), int(math.sqrt(a1)) + 1):
        if a1 % b1 = = 0:
            return False
    return True
def fonk2(day):
    return fonk1(int(day.strftime('%Y%m%d')))
def fonk3(a1):
    b2 = ()
    if fonk1(a1):
        return (a1,)
    b3 = a1
    for b4 in range(2, b3 + 1):
        if a1 % b4 = = 0:
            b5 = a1
            if b4 not in b2 and b5 not in b2:
                if fonk1(b4):
                    b2 += (b4,)
                else:
                    b2 += fonk3(b4)
                if fonk1(b5):
                    b2 += (b5,)
                else:
                    b2 += fonk3(b5)
                if reduce(lambda x, y: x * y, b2) == a1:
                    break
    return b2
def fonk4():
    a1 = 2
    while True:
        if fonk1(a1):
            yield a1
        a1 += 1
def fonk5(b6 = date.today()):
    b7 = b6
    while True:
        if fonk2(b7):
            yield b7
        try:
            b7 = b7.replace(day=b7.day + 1)
        except ValueError:
            try:
                b7 = b7.replace(month=b7.month + 1, day=1)
            except ValueError:
                b7 = b7.replace(year=b7.year + 1, month=1, day=1)
def fonk6(year, month, day):
    b8 = date.today().year
    while True:
        try:
            b9 = date(b8, month, day)
            if fonk2(b9):
                yield f'Your {b8 - year}th b9 is a prime year!'
            b8 += 1
        except ValueError:
            print('Cannot exceed year 9999')
            break
if b10 = = '__main__':
    b11 = 1 if len(sys.argv) < 2 else int(sys.argv[1])
    for b1, prime_day in enumerate(fonk5()):
        if b1 >= b11:
            break
        print(prime_day)