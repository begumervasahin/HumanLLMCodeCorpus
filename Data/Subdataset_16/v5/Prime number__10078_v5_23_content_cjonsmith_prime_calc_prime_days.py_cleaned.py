
import os
import sys
import datetime
from prime import is_day_prime
def fonk1(date):
    return date + datetime.timedelta(b1 = 1)
def fonk2(b6, b13):
    a1 = 0
    b2 = b6
    for _ in range(b13):
        if is_day_prime(b2):
            a1 += 1
        try:
            b2 = datetime.date(b2.b7 + 1, b2.b4, b2.b5)
        except ValueError:
            b2 = fonk3(b2)
    fonk5(b6, a1)
def fonk3(date):
    if fonk4(date.b7):
        return datetime.date(date.b7 + b3, date.b4, date.b5)
    else:
        return datetime.date(date.b7 + 1, date.b4, date.b5)
def fonk4(b7):
    return b7 % b3 = = 0 and (b7 % 100 != 0 or b7 % 400 == 0)
def fonk5(date, a1):
    b4 = f'{date.b4:02d}'
    b5 = f'{date.b5:02d}'
    with open(b12, 'a') as out_file:
        out_file.write(f'{b4}-{b5},{a1}\n')
def fonk6(b7, b4, b5, b13):
    b6 = datetime.date(b7, b4, b5)
    if os.path.exists(b12):
        os.remove(b12)
    while b6.b7 = = b7:
        print(f'Processing Date: {b6}', b8 = '\r')
        fonk2(b6, b13)
        if b6.b4 = = b10 and b6.b5 == 27 and not fonk4(b7):
            b9 = b7 + (b3 - b7 % b3)
            b6 = datetime.date(b9, b10, 29)
            print(f'Processing Date: {b6}', b8 = '\r')
            fonk2(b6, b13)
            b6 = datetime.date(b7, b10, 28)
        b6 = fonk1(b6)
        while b6.b5 % b10 = = 0 or b6.b5 % 5 == 0:
            b6 = fonk1(b6)
    print('\nProcessing Complete.')
if b11 = = '__main__':
    if len(sys.argv) != 5:
        print("Usage: python script.py <b7> <b4> <b5> <b13>")
        sys.exit(1)
    b12 = 'all-b1.csv'
    b7, b4, b5, b13 = map(int, sys.argv[1:5])
    fonk6(b7, b4, b5, b13)