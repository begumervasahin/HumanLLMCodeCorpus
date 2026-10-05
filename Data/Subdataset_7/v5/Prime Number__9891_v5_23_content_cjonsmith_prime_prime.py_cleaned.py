import sys
from datetime import date
from math import sqrt
from itertools import count
def fonk1(a1):
    return a1 > 1 and all(a1 % b3 for b3 in range(2, int(sqrt(a1)) + 1))
def fonk2(day):
    b1 = int(day.strftime('%Y%m%d'))
    return fonk1(b1)
def fonk3(a1):
    b2 = set()
    for b3 in range(2, int(sqrt(a1)) + 1):
        while a1 % b3 = = 0:
            b2.add(b3)
            a1
    if a1 > 1:
        b2.add(a1)
    return b2
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
        b4 = b4.replace(day=b4.day + 1)
        if b4.b5 = = 1 and b4.day == 1:
            b4 = b4.replace(year=b4.year + 1)
def fonk6(year, b5, day):
    b6 = date.today().year
    while True:
        try:
            b7 = date(b6, b5, day)
            if fonk2(b7):
                yield f'Your {b6 - year} b7 is a prime year!'
            b6 += 1
        except ValueError:
            print('Year cannot exceed 9999')
            break
if b8 = = '__main__':
    b9 = 1 if len(sys.argv) < 2 else int(sys.argv[1])
    b10 = fonk5()
    for _ in range(b9):
        print(next(b10))