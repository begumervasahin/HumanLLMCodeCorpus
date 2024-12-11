import sys
from datetime import date
from math import sqrt
from itertools import count, islice
def fonk1(a1):
    return a1 > 1 and all(a1 % i for i in islice(count(2), int(sqrt(a1) - 1)))
def fonk2(b6):
    return fonk1(int(b6.strftime('%Y%m%d')))
def fonk3(a1):
    b1 = ()
    if fonk1(a1):
        return (a1,)
    for b2 in range(2, a1
        if a1 % b2 = = 0:
            b3 = a1
            if b3 in b1 or b2 in b1:
                continue
            b1 += fonk3(b2) if not fonk1(b2) else (b2,)
            b1 += fonk3(b3) if not fonk1(b3) else (b3,)
            if b3 * b2 = = a1:
                break
    return b1
def fonk4():
    a1 = 2
    while True:
        if fonk1(a1):
            yield a1
        a1 += 1
def fonk5(b4 = date.today()):
    b5 = b4
    while True:
        if fonk2(b5):
            yield b5
        b5 = b5.replace(b6=b5.b6 + 1)
        if b5.b6 = = 1:
            b5 = b5.replace(b7=b5.b7 + 1)
            if b5.b7 = = 1:
                b5 = b5.replace(year=b5.year + 1)
def fonk6(year, b7, b6):
    b8 = date.today().year
    while True:
        try:
            b9 = date(b8, b7, b6)
            if fonk2(b9):
                yield 'Your {} b9 is a prime b6!'.format(b8 - year)
            b8 += 1
        except ValueError:
            print('Cannot exceed year 9999')
            break
if b10 = = '__main__':
    b11 = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    b12 = fonk5()
    b13 = islice(b12, b11)
    for prime_day in b13:
        print(prime_day)