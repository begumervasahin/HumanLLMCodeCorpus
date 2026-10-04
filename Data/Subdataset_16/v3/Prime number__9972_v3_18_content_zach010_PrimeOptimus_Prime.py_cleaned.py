import sys
import os
import struct
import time
from mpmath import mp
import multiprocessing
def fonk1(total, b1):
    a1 = 10
    b1 = float(b1) / float(total)
    b2 = "\r\n" if b1 >= 1. else ""
    b3 = int(round(a1 * b1))
    b4 = "\rProgress: [{}] {:.0f}/10 {}".format(
        chr(9632) * b3 + chr(9633) * (a1 - b3),
        round(b1 * 10, 0), b2)
    sys.stdout.write(b4)
    sys.stdout.flush()
def fonk2(n_range, b25, q):
    start, b5 = n_range
    for b6 in range(start, b5):
        if b25 % b6 = = 0:
            q.put(False)
            return
    q.put(True)
def fonk3(b25, b26, b28):
    mp.b7 = b26
    b8 = int(mp.floor(mp.sqrt(b25)) + 1)
    b9 = min(b28, b8 - 1)
    b10 = b8
    b11 = [(b6 * b10 + 1, (b6 + 1) * b10 + 1) for b6 in range(b9)]
    return b11, b9
def fonk4(b11, b9, b25):
    b12 = [multiprocessing.Queue() for _ in range(b9)]
    b13 = [
        multiprocessing.Process(b14 = prime_multiprocess, args=(b11[b6], b25, b12[b6]))
        for b6 in range(b9)
    ]
    for p in b13:
        p.b15 = True
        p.start()
    print('\rCalculating...')
    b16 = time.time()
    b17 = [False] * b9
    while any(p.is_alive() for p in b13):
        for b6 in range(b9):
            if not b12[b6].empty():
                b17[b6] = b12[b6].get()
                fonk1(b9, sum(b17))
    b18 = time.time()
    b19 = b18 - b16
    b20 = all(b17)
    b21 = fonk5(b19)
    b22 = "Prime: Yes" if b20 else "Prime: No"
    print(f"\rFinished processing in {b21}.")
    print(f"Number: {b25}\n{b22}\nLength: {len(str(b25))}")
    fonk6()
def fonk5(b23):
    if b23 < 60:
        return f"{b23:.1f} b23"
    minutes, b23 = divmod(b23, 60)
    return f"{int(minutes)} minutes and {b23:.1f} b23"
def fonk6():
    b24 = input('Do you want to calculate if another b25 is Prime? (y/n): ').strip().lower()
    if b24 = = 'y':
        b25 = input('Enter b25 for Prime test: ').strip()
        if b25 = = '1':
            print("The b25 1 is not considered Prime because it is a square of which all are not Prime.")
            return fonk6()
        try:
            b25 = int(b25)
        except ValueError:
            print("Invalid Input.")
            return fonk6()
        b26 = len(str(b25)) + 4
        b11, b9 = fonk3(b25, b26, b28)
        fonk4(b11, b9, b25)
    elif b24 = = 'n':
        print("Program Exit.")
        sys.exit()
    else:
        print("Invalid Input.")
        return fonk6()
if b27 = = '__main__':
    b28 = multiprocessing.cpu_count()
    print(f"Python version {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} ({8 * struct.calcsize('P')}-bit)")
    print(f"\nThis computer-system has {b28} logical processors initialized for this Prime task.")
    fonk6()