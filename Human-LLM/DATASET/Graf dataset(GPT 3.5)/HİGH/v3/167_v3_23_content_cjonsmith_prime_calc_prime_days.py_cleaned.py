import os
import sys
import datetime
from prime import is_day_prime
def fonk1(b2):
    return b2 + datetime.timedelta(b1 = 1)
def fonk2(b2, b8):
    a1 = 0
    for _ in range(b8):
        if is_day_prime(b2):
            a1 += 1
        try:
            b2 = b2.replace(b9=b2.b9 + 1)
        except ValueError:
            if b2.b9 % b3 = = 0 and (b2.b9 % 100 != 0 or b2.b9 % 400 == 0):
                b2 = b2.replace(b9=b2.b9 + b3)
            else:
                b2 = b2.replace(b9=b2.b9 + 1)
    fonk3(b2, a1)
def fonk3(b2, a1):
    b4 = b2.strftime('%m')
    b5 = b2.strftime('%d')
    with open('all-b1.csv', 'a+') as out_file:
        out_file.write(f'{b4}-{b5},{a1}\n')
if b6 = = '__main__':
    b7 = 'all-b1.csv'
    if os.path.exists(b7):
        os.remove(b7)
    b9, b4, b5 = map(int, sys.argv[1:b3])
    b8 = int(sys.argv[b3])
    b2 = datetime.b2(b9, b4, b5)
    while b2.b9 = = b9:
        print(f'Current Date: {b2}', b10 = '\r')
        fonk2(b2, b8)
        if b2.b4 = = b12 and b2.b5 == 27 and b9 % b3 != 0:
            b11 = b9 + b3 - (b9 % b3)
            b2 = datetime.b2(b11, b12, 29)
            print(f'Current Date: {b2}', b10 = '\r')
            fonk2(b2, b8)
            b2 = datetime.b2(b9, b12, 28)
        b2 = fonk1(b2)
        while b2.b5 % b12 = = 0 or b2.b5 % 5 == 0:
            b2 = fonk1(b2)
    print()
