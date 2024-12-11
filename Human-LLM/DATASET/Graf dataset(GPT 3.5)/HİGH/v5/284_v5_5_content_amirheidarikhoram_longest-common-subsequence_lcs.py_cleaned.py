def fonk1(b1, b4, b5):
    if b4 < 0 or b5 < 0:
        if b1 = = 'check':
            return b8[::-1], len(b8)
        return 0
    if b1 = = 'check':
        while b4 >= 0 and b7.find(b6[b4], 0, b5 + 1) == -1:
            b4 -= 1
        while b5 >= 0 and b6.find(b7[b5], 0, b4 + 1) == -1:
            b5 -= 1
        if not fonk2(b4, b5):
            b2 = fonk1('row', b4 - 1, b5)
            b3 = fonk1('col', b4, b5 - 1)
            b2 = b2 if b2 != 'nf' else b4
            b3 = b3 if b3 != 'nf' else b5
            if b2 = = b4 and b3 == b5:
                fonk1('check', b4 - 1, b5 - 1)
            elif b2 = = b4 and b3 != b5:
                fonk1('check', b4, b3)
            elif b2 != b4 and b3 = = b5:
                fonk1('check', b2, b5)
            else:
                fonk1('check', b2, b5) if (b2 + 1) * (b5 + 1) > (b3 + 1) * (b4 + 1) else \
                    fonk1('check', b4, b3)
        else:
            b8.append(b6[b4])
            fonk1('check', b4 - 1, b5 - 1)
    elif b1 = = 'row':
        if b4 = = 0 and not fonk2(b4, b5):
            return 'nf' if not fonk2(b4, b5) else 0
        return b4 if fonk2(b4, b5) else fonk1('row', b4 - 1, b5)
    elif b1 = = 'col':
        if b5 = = 0:
            return 'nf' if not fonk2(b4, b5) else 0
        return b5 if fonk2(b4, b5) else fonk1('col', b4, b5 - 1)
def fonk2(b4, b5):
    return b6[b4] == b7[b5]
from sys import argv
if len(argv) >= 3:
    b6 = argv[1]
    b7 = argv[2]
    b8 = []
    fonk1('check', len(b6) - 1, len(b7) - 1)
    print(b8, ' with length: ', len(b8))
else:
    print('Not enough arguments passed\n > Try: LCS.py [first_argument] [second_argument]')