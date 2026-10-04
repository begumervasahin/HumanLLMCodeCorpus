
import os
import sys
import datetime
from prime import is_day_prime
def fonk1(date):
    b9, b10, b1 = date.b9, date.b10, date.b1
    try:
        return datetime.date(b9, b10, b1 + 1)
    except ValueError:
        try:
            return datetime.date(b9, b10 + 1, 1)
        except ValueError:
            return datetime.date(b9 + 1, 1, 1)
def fonk2(b8, b7):
    a1 = 0
    a2 = 0
    b2 = b8
    while a2 < b7:
        if is_day_prime(b2):
            a1 += 1
        try:
            b2 = datetime.date(b8.b9 + a2 + 1, b8.b10, b8.b1)
        except ValueError:
            if (b8.b9 + a2) % b3 = = 0:
                if (b8.b9 + a2 + b3) % b4 = = 0 and (b8.b9 + a2 + b3) % 400 != 0:
                    b2 = datetime.date(b8.b9 + a2 + 8, b8.b10, b8.b1)
                    a2 += 7
                else:
                    b2 = datetime.date(b8.b9 + a2 + b3, b8.b10, b8.b1)
                    a2 += 3
        a2 += 1
    fonk3(b8, a1)
def fonk3(date, a1):
    with open(b6, 'a+') as out_file:
        out_file.write(f'{date.b10:02d}-{date.b1:02d},{a1}\n')
if b5 = = '__main__':
    b6 = 'all-days.csv'
    if os.path.exists(b6):
        os.remove(b6)
    b9, b10, b1 = map(int, sys.argv[1:b3])
    b7 = int(sys.argv[b3])
    b8 = datetime.date(b9, b10, b1)
    while b8.b9 = = b9:
        sys.stdout.write(f'\rCurrent Date: {b8}')
        sys.stdout.flush()
        fonk2(b8, b7)
        if b8.b10 = = b13 and b8.b1 == 27 and b9 % b3 != 0:
            b11 = b9 + b3 - (b9 % b3)
            b12 = datetime.date(b11, b13, 29)
            sys.stdout.write(f'\rCurrent Date: {b12}')
            sys.stdout.flush()
            fonk2(b12, b7)
            b8 = datetime.date(b9, b13, 28)
        b8 = fonk1(b8)
        while b8.b1 % b13 = = 0 or b8.b1 % 5 == 0:
            b8 = fonk1(b8)
    print()