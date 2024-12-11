import sys
from datetime import date
from math import sqrt
from itertools import count, islice
def fonk1(a1):
    return a1 > 1 and all(a1 % i for i in islice(count(2), int(sqrt(a1)-1)))
def fonk2(b5):
    return fonk1(int(b5.strftime('%Y%m%d')))
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
            if reduce(lambda x, y: x * y, b1) == a1:
                break
    return b1
def fonk4():
    a1 = 2
    while True:
        if fonk1(a1):
            yield a1
        a1 += 1
def fonk5(b4 = date.today()):
    while True:
        if fonk2(b4):
            yield b4
        b4 = b4.replace(b5=b4.b5 + 1)
        if b4.b5 = = 1:
            b4 = b4.replace(b6=b4.b6 + 1)
            if b4.b6 = = 1:
                b4 = b4.replace(year=b4.year + 1)
def fonk6(year, b6, b5):
    b7 = date.today().year
    while True:
        try:
            b8 = date(b7, b6, b5)
            if fonk2(b8):
                yield 'Your {} b8 is a prime b5!'.format(b7 - year)
            b7 += 1
        except ValueError:
            print('Cannot exceed year 9999')
            break
if b9 = = '__main__':
    b10 = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    for prime_day in islice(fonk5(), b10):
        print(prime_day)