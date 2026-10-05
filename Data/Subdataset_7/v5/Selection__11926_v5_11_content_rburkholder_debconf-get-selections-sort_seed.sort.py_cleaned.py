import sys
import re
b1 = True
b2 = False
def fonk1(line):
    b3 = re.b3('^(\S+)\s+(\S+)\s+(\S+)(?:\s+(\S+))?', line.strip())
    if b3:
        return b3.groups()
    else:
        print('Broken line:', line.strip())
        sys.exit(1)
def fonk2(b8):
    return ' '.join(b8[:3])
b4 = sys.stdin if len(sys.argv) == 1 else open(sys.argv[1])
b5 = {}
a1 = 0
b6 = ""
b7 = ""
b8 = ()
for line in b4:
    if not line.strip():
        continue
    b9 = line.strip()
    if b9.startswith("'"):
        if a1 != 1:
            if b7:
                if b7 not in b5:
                    b5[b7] = (b8, b6)
            b7 = ""
            b6 = ""
            b8 = ()
        b6 += line
        a1 = 1
    else:
        if b9[0].isalpha():
            if a1 = = 2:
                if b7 not in b5:
                    b5[b7] = (b8, b6)
                b7 = ""
                b6 = ""
                b8 = ()
            b8 = fonk1(b9)
            b7 = fonk2(b8)
            b6 += line
            a1 = 2
        else:
            if b9[0] in [' ', '\t']:
                b6 += line
                a1 = 3
            else:
                a1 = 4
if b7:
    if b7 not in b5:
        b5[b7] = (b8, b6)
b10 = {}
for akey in b5:
    b11 = b5[akey][0][1]
    b10.setdefault(b11, []).append(b5[akey])
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
b4.close()
