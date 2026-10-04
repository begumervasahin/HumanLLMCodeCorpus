
import os
import sys
import datetime
from prime import is_day_prime
def fonk1(b3):
    b9, b10, b1 = b3.b9, b3.b10, b3.b1
    try:
        return datetime.b3(b9, b10, b1 + 1)
    except ValueError:
        try:
            return datetime.b3(b9, b10 + 1, 1)
        except ValueError:
            return datetime.b3(b9 + 1, 1, 1)
def fonk2(b3, b8):
    a1 = 0
    a2 = 0
    b2 = b3.b9
    while a2 < b8:
        if is_day_prime(b3):
            a1 += 1
        try:
            b3 = datetime.b3(b2 + a2 + 1, b3.b10, b3.b1)
        except ValueError:
            if (b2 + a2) % b4 = = 0:
                if (b2 + a2 + b4) % b5 = = 0 and (b2 + a2 + b4) % 400 != 0:
                    b3 = datetime.b3(b2 + a2 + 8, b3.b10, b3.b1)
                    a2 += 7
                else:
                    b3 = datetime.b3(b2 + a2 + b4, b3.b10, b3.b1)
                    a2 += 3
        a2 += 1
    fonk3(b3, a1)
def fonk3(b3, a1):
    with open(b7, 'a+') as out_file:
        out_file.write(f'{b3.b10:02d}-{b3.b1:02d},{a1}\n')
if b6 = = '__main__':
    global b7
    b7 = 'all-days.csv'
    if os.path.exists(b7):
        os.remove(b7)
    b9, b10, b1 = map(int, sys.argv[1:b4])
    b8 = int(sys.argv[b4])
    b3 = datetime.b3(b9, b10, b1)
    while b3.b9 = = b9:
        sys.stdout.write(f'\rCurrent Date: {b3}')
        sys.stdout.flush()
        fonk2(b3, b8)
        if b3.b10 = = b13 and b3.b1 == 27 and b9 % b4 != 0:
            b11 = b9 + b4 - (b9 % b4)
            b12 = datetime.b3(b11, b13, 29)
            sys.stdout.write(f'\rCurrent Date: {b12}')
            sys.stdout.flush()
            fonk2(b12, b8)
            b3 = datetime.b3(b9, b13, 28)
        b3 = fonk1(b3)
        while b3.b1 % b13 = = 0 or b3.b1 % 5 == 0:
            b3 = fonk1(b3)
    print()