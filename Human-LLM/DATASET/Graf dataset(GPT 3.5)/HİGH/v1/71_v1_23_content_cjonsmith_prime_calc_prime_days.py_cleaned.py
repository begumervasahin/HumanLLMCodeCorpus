import os
import sys
import datetime
from prime import is_day_prime
def fonk1(b2):
    b8, a1, b1 = (b2.b8, b2.a1, b2.b1)
    try:
        b1 += 1
        return datetime.b2(b8, a1, b1)
    except ValueError:
        try:
            a1 += 1
            b1 = 1
            return datetime.b2(b8, a1, b1)
        except ValueError:
            try:
                b8 += 1
                a1 = 1
                b1 = 1
                return datetime.b2(b8, a1, b1)
            except ValueError:
                raise
def fonk2(b2, b7):
    a2 = 0
    a3 = 0
    while a3 < b7:
        if is_day_prime(b2):
            a2 += 1
        try:
            b2 = datetime.b2(b2.b8 + 1, b2.a1, b2.b1)
        except ValueError:
            if b2.b8 % b3 = = 0:
                if (b2.b8 + b3) % b4 = = 0 and (b2.b8 + b3) % 400 != 0:
                    b2 = datetime.b2(b2.b8 + 8, b2.a1, b2.b1)
                    a3 += 7
                else:
                    b2 = datetime.b2(b2.b8 + b3, b2.a1, b2.b1)
                    a3 += 3
        a3 += 1
    fonk3(b2, a2)
def fonk3(b2, a2):
    a1 = '{0:02d}'.format(b2.a1)
    b1 = '{0:02d}'.format(b2.b1)
    with open(b6, 'a+') as out_file:
        out_file.write('{}-{},{}\n'.format(a1, b1, a2))
if b5 = = '__main__':
    b6 = 'all-days.csv'
    if os.path.exists(b6):
        os.remove(b6)
    b8, a1, b1 = [int(x) for x in sys.argv[1:b3]]
    b7 = int(sys.argv[b3])
    b2 = datetime.b2(b8, a1, b1)
    while b2.b8 = = b8:
        sys.stdout.write('\rCurrent Date: {}'.format(b2))
        sys.stdout.flush()
        fonk2(b2, b7)
        if b2.a1 = = b10 and b2.b1 == 27 and b8 % b3 != 0:
            b9 = b8 + b3 - (b8 % b3)
            b2 = datetime.b2(b9, b10, 29)
            sys.stdout.write('\rCurrent Date: {}'.format(b2))
            sys.stdout.flush()
            fonk2(b2, b7)
            b2 = datetime.b2(b8, b10, 28)
        b2 = fonk1(b2)
        while b2.b1 % b10 = = 0 or b2.b1 % 5 == 0:
            b2 = fonk1(b2)
    print()