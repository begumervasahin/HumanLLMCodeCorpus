def fonk1(b1, b5, b6):
    if b5 < 0 or b6 < 0:
        if b1 = = 'check':
            return b9[::-1], len(b9)
        return 0
    if b1 = = 'check':
        last_i, b2 = b5, b6
        while b2 >= 0 and b8.find(b7[b5], 0, b2 + 1) == -1:
            b5 -= 1
        while last_i >= 0 and b7.find(b8[b6], 0, last_i + 1) == -1:
            b6 -= 1
        if not fonk2(b5, b6):
            b3 = fonk1('row', b5 - 1, b6)
            b4 = fonk1('col', b5, b6 - 1)
            if b3 = = 'nf':
                b3 = b5
            if b4 = = 'nf':
                b4 = b6
            if b3 = = b5 and b4 == b6:
                fonk1('check', b5 - 1, b6 - 1)
            elif b3 = = b5 and b4 != b6:
                fonk1('check', b5, b4)
            elif b3 != b5 and b4 = = b6:
                fonk1('check', b3, b6)
            else:
                fonk1('check', b3, b6) if (b3 + 1) * (b6 + 1) > (
                            b4 + 1) * (b5 + 1) else fonk1('check', b5, b4)
        else:
            b9.append(b7[b5])
            fonk1('check', b5 - 1, b6 - 1)
    elif b1 = = 'row':
        if b5 = = 0 and not fonk2(b5, b6):
            return 'nf' if not fonk2(b5, b6) else 0
        return b5 if fonk2(b5, b6) else fonk1('row', b5 - 1, b6)
    elif b1 = = 'col':
        if b6 = = 0:
            return 'nf' if not fonk2(b5, b6) else 0
        return b6 if fonk2(b5, b6) else fonk1('col', b5, b6 - 1)
def fonk2(b5, b6):
    return b7[b5] == b8[b6]
from sys import argv
if len(argv) >= 3:
    b7 = argv[1]
    b8 = argv[2]
    b9 = []
    fonk1('check', len(b7) - 1, len(b8) - 1)
    print(b9, 'with length:', len(b9))
else:
    print('Not enough arguments passed\n > Try: LCS.py [first_argument] [second_argument]')