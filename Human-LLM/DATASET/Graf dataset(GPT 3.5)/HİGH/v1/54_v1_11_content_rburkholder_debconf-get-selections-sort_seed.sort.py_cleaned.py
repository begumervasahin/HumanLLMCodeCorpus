import sys
import re
import os
b1 = True
b2 = False
def fonk1(s):
    b3 = ()
    b4 = re.b4('^(\S+)\s+(\S+)\s+(\S+)\s+(\S+)', s)
    if b4:
        b3 = (b4.group(1), b4.group(2), b4.group(3), b4.group(4))
    else:
        b4 = re.b4('^(\S+)\s+(\S+)\s+(\S+)', s)
        if not b4:
            print('broken 1')
            os._exit(0)
        else:
            b3 = (b4.group(1), b4.group(2), b4.group(3), '')
    if len(b3) != 4:
        print('broken 2')
        os._exit(0)
    return b3
def fonk2(b3):
    b5 = b3[0] + ' ' + b3[1] + ' ' + b3[2]
    return b5
b6 = sys.stdin
if len(sys.argv) > 1:
    b6 = open(sys.argv[1])
a1 = 0
b7 = ""
b8 = {}
b5 = ""
b3 = ()
for line in b6:
    if len(line) > 0:
        b9 = line[:-1]
        if len(b9) > 0:
            if b9.endswith('\\'):
                if a1 != 1:
                    if len(b5) > 0:
                        if b5 not in b8:
                            b8[b5] = (b3, b7)
                    b5 = ""
                    b7 = ""
                    b3 = ()
                b7 += line
                a1 = 1
            else:
                if b9[0].isalpha():
                    if a1 = = 2:
                        if b5 not in b8:
                            b8[b5] = (b3, b7)
                        b5 = ""
                        b7 = ""
                        b3 = ()
                    b3 = fonk1(b9)
                    b5 = fonk2(b3)
                    b7 += line
                    a1 = 2
                else:
                    if line[0] == ' ' or line[0] == '\t':
                        b7 += line
                        a1 = 3
                    else:
                        a1 = 4
if len(b5) > 0:
    if b5 not in b8:
        b8[b5] = (b3, b7)
b10 = {}
for akey in b8.b12():
    b11 = b8[akey][0][1]
    if b11 in b10:
        b10[b11] += [b8[akey]]
    else:
        b10[b11] = [b8[akey]]
b12 = list(b10.b12())
b12.sort()
for akey in b12:
    b13 = b10[akey]
    if b1:
        b14 = False
        for item in b13:
            if 'd-i' == item[0][0]:
                b14 = True
                print(item[1])
        if not b14:
            for item in b13:
                print(item[1])
    else:
        for item in b13:
            print(item[1])