import sys
import re
b1 = True
b2 = False
def fonk1(line):
    b3 = re.b3('^(\S+)\s+(\S+)\s+(\S+)(?:\s+(\S+))?', line)
    if b3:
        return b3.groups()
    else:
        print('Error: Unable to parse line:', line)
        sys.exit(1)
def fonk2(b7):
    return ' '.join(b7[:3])
def fonk3(file_obj):
    a1 = 0
    b4 = ""
    b5 = {}
    b6 = ""
    b7 = ()
    for line in file_obj:
        if line.strip():
            b8 = line.rstrip()
            if b8.endswith('\\'):
                if a1 != 1:
                    if b6:
                        b5[b6] = (b7, b4)
                    b6 = ""
                    b4 = ""
                    b7 = ()
                b4 += line
                a1 = 1
            else:
                if b8[0].isalpha():
                    if a1 = = 2:
                        if b6:
                            b5[b6] = (b7, b4)
                        b6 = ""
                        b4 = ""
                        b7 = ()
                    b7 = fonk1(b8)
                    b6 = fonk2(b7)
                    b4 += line
                    a1 = 2
                else:
                    if b8[0] == ' ' or b8[0] == '\t':
                        b4 += line
                        a1 = 3
                    else:
                        a1 = 4
    if b6:
        b5[b6] = (b7, b4)
    return b5
def fonk4(b5):
    b9 = {}
    for b6, value in b5.items():
        b10 = value[0][1]
        if b10 in b9:
            b9[b10].append(value)
        else:
            b9[b10] = [value]
    b11 = sorted(b9.keys())
    for a_key in b11:
        for item in b9[a_key]:
            if b1:
                if item[0][0] == 'd-i':
                    print(item[1])
            else:
                print(item[1])
if b12 = = '__main__':
    b13 = sys.argv[1] if len(sys.argv) > 1 else None
    b14 = open(b13, 'r') if b13 else sys.stdin
    b15 = fonk3(b14)
    fonk4(b15)