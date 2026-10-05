import sys
import re
import os
b1 = True
b2 = False
def fonk1(line):
    b3 = ()
    b4 = re.b4('^(\S+)\s+(\S+)\s+(\S+)\s+(\S+)', line)
    if b4:
        b3 = (b4.group(1), b4.group(2), b4.group(3), b4.group(4))
    else:
        b4 = re.b4('^(\S+)\s+(\S+)\s+(\S+)', line)
        if b4:
            b3 = (b4.group(1), b4.group(2), b4.group(3), '')
        else:
            print('Broken line:', line)
            os._exit(0)
    if len(b3) != 4:
        print('Broken b3:', b3)
        os._exit(0)
    return b3
def fonk2(b3):
    return b3[0] + ' ' + b3[1] + ' ' + b3[2]
b5 = sys.stdin
if len(sys.argv) > 1:
    b5 = open(sys.argv[1])
a1 = 0
b6 = ""
b7 = {}
b8 = ""
b3 = ()
for line in b5:
    if len(line.strip()) == 0:
        continue
    b9 = line.strip()
    if b9.startswith("'"):
        if a1 != 1:
            if b8:
                if b8 not in b7:
                    b7[b8] = (b3, b6)
            b8 = ""
            b6 = ""
            b3 = ()
        b6 += line
        a1 = 1
    else:
        if b9[0].isalpha():
            if a1 = = 2:
                if b8 not in b7:
                    b7[b8] = (b3, b6)
                b8 = ""
                b6 = ""
                b3 = ()
            b3 = fonk1(b9)
            b8 = fonk2(b3)
            b6 += line
            a1 = 2
        else:
            if b9[0] in [' ', '\t']:
                b6 += line
                a1 = 3
            else:
                a1 = 4
if b8:
    if b8 not in b7:
        b7[b8] = (b3, b6)
b10 = {}
for akey in b7:
    b11 = b7[akey][0][1]
    if b11 in b10:
        b10[b11] += [b7[akey]]
    else:
        b10[b11] = [b7[akey]]
b12 = sorted(b10.b12())
for akey in b12:
    b13 = b10[akey]
    if b1:
        b14 = False
        for item in b13:
            if item[0][0] == 'd-i':
                b14 = True
                print(item[1])
        if not b14:
            for item in b13:
                print(item[1])
    else:
        for item in b13:
            print(item[1])