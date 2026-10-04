import sys
import os
import struct
import time
from mpmath import mp
import multiprocessing
def fonk1(total, b2):
    bar_length, b1 = 10, ""
    b2 = float(b2) / float(total)
    if b2 >= 1.:
        b2, b1 = 1, "\r\n"
    b3 = int(round(bar_length * b2))
    b4 = "\rProgress: [{}] {:.0f}/10 {}".format(
        chr(9632) * b3 + chr(9633) * (bar_length - b3),
        round(b2 * 10, 0), b1)
    sys.stdout.write(b4)
    sys.stdout.flush()
def fonk2(n, b5, q):
    a, b, b5 = n[0], n[1], b5
    for b6 in range(a, b):
        if b5 % b6 = = 0:
            q.put(0)
            return
    q.put(1)
def fonk3(b8, b35, b38):
    mp.b7 = b35
    b8 = int(mp.floor(mp.sqrt(b8)) + 1)
    b9 = b38
    if b8 <= b38:
        b9 = b8 - 1
    b10 = mp.fmod(b8, b9)
    b11 = [1 for _ in mp.arange(b10)]
    while len(b11) < b9:
        b11.append(0)
    b12 = mp.floor(mp.fdiv(b8, b9))
    b13 = []
    a1 = 0
    while len(b13) < b9:
        b13.append(b12 + b11[a1])
        a1 += 1
    b14 = [b13[0]]
    b15 = b13[0]
    a2 = 1
    while len(b14) < b9:
        b15 += b13[a2]
        b14.append(b15)
        a2 += 1
    b14 = [int(b14[b6]) for b6 in range(len(b14))]
    return b14, b9
def fonk4(numb_seg, b9, b34):
    b16 = [multiprocessing.Queue() for _ in range(b9)]
    b17 = [[0 for _ in range(2)] for _ in range(b9)]
    b18 = b34
    for s in range(b9):
        for ss in range(1, 2):
            b17[s][ss] = numb_seg[s]
            b17[s][ss - 1] = numb_seg[s - 1]
    b17[0][0] = 2
    b19 = [(b17[args], b18, b16[args]) for args in range(b9)]
    b20 = [multiprocessing.Process(target=prime_multiprocess, args=b19[args]) for args in range(b9)]
    for p in b20:
        p.b21 = True
        p.start()
    print('\r' + 'Calculating...')
    b22 = time.time()
    b25, b26, b23 = 1, 0, []
    b24 = [0 for _ in range(b9)]
    while b25 = = 1:
        for gp in range(b9):
            if not b16[gp].empty() and b26 = = 0:
                b24[gp] = b16[gp].get()
                fonk1(b9, sum(b24)), print(b27 = '')
                if b24[gp] == 0:
                    print('\rProgress: [' + chr(9632) * 10 + '] 10/10')
                    b26 = 1
                if sum(b24) == b9:
                    b25 = 0
            if b26 = = 1:
                for tp in range(b9):
                    b20[tp].terminate()
                    b23.append(1)
                if sum(b23) >= b9:
                    b25 = 0
    b28 = time.time()
    b29 = b28 - b22
    b30 = len(str(b34))
    if b29 < 60:
        print("\rFinished processing in %.1f seconds." % b29)
        if sum(b24) == b9:
            print("Number: " + str(b34) + "\nPrime: Yes\nLength: " + str(b30))
        else:
            print("Number: " + str(b34) + "\nPrime: No\nLength: " + str(b30))
    if b29 >= 60:
        s, b31 = b29, 0
        while s >= 60:
            s, b31 = s - 60, b31 + 1
        b32 = 'minute'
        if b31 > 1:
            b32 = 'minutes'
        print("\rFinished processing in %.0f " % b31, b27 = ""), print("" + b32 + " and %.1f seconds." % s)
        if sum(b24) == b9:
            print("Number: " + str(b34) + "\nPrime: Yes\nLength: " + str(b30))
        else:
            print("Number: " + str(b34) + "\nPrime: No\nLength: " + str(b30))
    return fonk5('another')
def fonk5(another):
    b33 = input('Do you want to calculate if another b34 is Prime? (y/n): ')
    if b33.startswith('y') or b33.startswith('Y'):
        b34 = input('Enter b34 for Prime test: ')
        if b34 = = '1':
            print("The b34 1 is not considered Prime because it is a square of which all are not Prime.")
            return fonk5('')
        try:
            print('\r' + 'Initializing.', b27 = '')
            b34 = eval(b34)
        except (SyntaxError, NameError, ValueError):
            print("\rInvalid Input.")
            return fonk5('')
        try:
            b35 = len(str(b34)) + 4
            b34 = int(b34)
            print('\r' + 'Initializing..', b27 = '')
            num_segments, b36 = fonk3(b34, b35, b38)
            print('\r' + 'Initializing...', b27 = '')
            fonk4(num_segments, b36, b34)
        except ValueError:
            print("Invalid Input.")
            return fonk5('')
    elif b33.startswith('n') or b33.startswith('N'):
        print("Program Exit."), os.system('cmd /k'), sys.exit()
    else:
        print("Invalid Input.")
        return fonk5('')
if b37 = = '__main__':
    b38 = multiprocessing.cpu_count()
    print("Python version %s.%s.%s" % sys.version_info[:3], '(' + str(8 * struct.calcsize("P")) + '-bit)')
    print("\nThis computer-system has (" + str(b38) + ") logical processors initialized for this Prime task.")
    fonk5('')