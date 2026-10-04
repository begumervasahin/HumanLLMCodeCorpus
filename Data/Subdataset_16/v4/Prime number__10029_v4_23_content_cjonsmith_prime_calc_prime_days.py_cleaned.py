
import os
import sys
import datetime
from prime import is_day_prime
def fonk1(date):
    try:
        return date + datetime.timedelta(b1 = 1)
    except ValueError:
        raise
def fonk2(b9, b8):
    a1 = 0
    b2 = b9
    for _ in range(b8):
        if is_day_prime(b2):
            a1 += 1
        try:
            b2 = datetime.date(b2.b10 + 1, b2.b4, b2.b5)
        except ValueError:
            if fonk3(b2.b10):
                b2 = datetime.date(b2.b10 + b3, b2.b4, b2.b5)
            else:
                b2 = datetime.date(b2.b10 + 1, b2.b4, b2.b5)
    fonk4(b9, a1)
def fonk3(b10):
    return b10 % b3 = = 0 and (b10 % 100 != 0 or b10 % 400 == 0)
def fonk4(date, a1):
    b4 = f'{date.b4:02d}'
    b5 = f'{date.b5:02d}'
    with open(b7, 'a') as out_file:
        out_file.write(f'{b4}-{b5},{a1}\n')
if b6 = = '__main__':
    b7 = 'all-b1.csv'
    if os.path.exists(b7):
        os.remove(b7)
    b10, b4, b5, b8 = map(int, sys.argv[1:5])
    b9 = datetime.date(b10, b4, b5)
    while b9.b10 = = b10:
        print(f'\rCurrent Date: {b9}', b11 = '')
        fonk2(b9, b8)
        if b9.b4 = = b13 and b9.b5 == 27 and not fonk3(b10):
            b12 = b10 + (b3 - b10 % b3)
            b9 = datetime.date(b12, b13, 29)
            print(f'\rCurrent Date: {b9}', b11 = '')
            fonk2(b9, b8)
            b9 = datetime.date(b10, b13, 28)
        b9 = fonk1(b9)
        while b9.b5 % b13 = = 0 or b9.b5 % 5 == 0:
            b9 = fonk1(b9)
    print()