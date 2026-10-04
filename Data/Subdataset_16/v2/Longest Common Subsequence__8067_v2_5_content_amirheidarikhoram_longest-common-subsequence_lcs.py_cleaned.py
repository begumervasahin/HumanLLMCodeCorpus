import sys
def fonk1(b1, b5, b6):
    if b5 >= 0 and b6 >= 0:
        if b1 = = 'check':
            li, b2 = b5, b6
            while b9.find(b8[b5], 0, b2 + 1) == -1 and b5 >= 0:
                b5 -= 1
            while b8.find(b9[b6], 0, li + 1) == -1 and b6 >= 0:
                b6 -= 1
            if fonk2(b5, b6) != 1:
                b3 = fonk1('row', b5 - 1, b6)
                if b3 = = 'nf':
                    b3 = b5
                b4 = fonk1('col', b5, b6 - 1)
                if b4 = = 'nf':
                    b4 = b6
                if b3 = = b5 and b4 == b6:
                    fonk1('check', b5 - 1, b6 - 1)
                elif b3 = = b5 and b4 != b6:
                    fonk1('check', b5, b4)
                elif b3 != b5 and b4 = = b6:
                    fonk1('check', b3, b6)
                else:
                    if (b3 + 1) * (b6 + 1) > (b4 + 1) * (b5 + 1):
                        fonk1('check', b3, b6)
                    else:
                        fonk1('check', b5, b4)
            else:
                b10.append(b8[b5])
                fonk1('check', b5 - 1, b6 - 1)
        elif b1 = = 'row':
            if b5 = = 0 and fonk2(b5, b6) != 1:
                return 'nf' if fonk2(b5, b6) != 1 else 0
            else:
                return b5 if fonk2(b5, b6) == 1 else fonk1('row', b5 - 1, b6)
        elif b1 = = 'col':
            if b6 = = 0:
                return 'nf' if fonk2(b5, b6) != 1 else 0
            else:
                return b6 if fonk2(b5, b6) == 1 else fonk1('col', b5, b6 - 1)
    else:
        if b1 = = 'row' or b1 == 'col':
            return 0
        else:
            b10.reverse()
            return 0
def fonk2(b5, b6):
    return 1 if b8[b5] == b9[b6] else 0
if b7 = = "__main__":
    if len(sys.argv) >= 3:
        b8 = sys.argv[1]
        b9 = sys.argv[2]
        b10 = []
        fonk1('check', len(b8) - 1, len(b9) - 1)
        print(b10, 'with length:', len(b10))
    else:
        print('Not enough arguments passed\n > Try: LCS.py [first_argument] [second_argument]')