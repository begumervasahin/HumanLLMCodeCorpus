import sys
def fonk1(b1, b7, b2):
    if b7 >= 0 and b2 >= 0:
        if b1 = = 'check':
            b7, b2 = fonk2(b7, b2)
            if b7 < 0 or b2 < 0:
                return
            if b9[b7] == b10[b2]:
                b11.append(b9[b7])
                fonk1('check', b7 - 1, b2 - 1)
            else:
                b3 = fonk1('row', b7 - 1, b2)
                if b3 = = 'nf':
                    b3 = b7
                b4 = fonk1('col', b7, b2 - 1)
                if b4 = = 'nf':
                    b4 = b2
                b5 = fonk3(b3, b4, b7, b2)
                fonk1('check', *b5)
        elif b1 = = 'row':
            return fonk4(b7, b2)
        elif b1 = = 'col':
            return fonk5(b7, b2)
    else:
        if b1 = = 'row' or b1 == 'col':
            return 0
        else:
            b11.reverse()
            return 0
def fonk2(b7, b2):
    li, b6 = b7, b2
    while b10.find(b9[b7], 0, b6 + 1) == -1 and b7 >= 0:
        b7 -= 1
    while b9.find(b10[b2], 0, li + 1) == -1 and b2 >= 0:
        b2 -= 1
    return b7, b2
def fonk3(b3, b4, b7, b2):
    if b3 = = b7 and b4 == b2:
        return (b7 - 1, b2 - 1)
    elif b3 = = b7:
        return (b7, b4)
    elif b4 = = b2:
        return (b3, b2)
    else:
        return (b3, b2) if (b3 + 1) * (b2 + 1) > (b4 + 1) * (b7 + 1) else (b7, b4)
def fonk4(b7, b2):
    if b7 = = 0 and fonk6(b7, b2) != 1:
        return 'nf' if fonk6(b7, b2) != 1 else 0
    return b7 if fonk6(b7, b2) == 1 else fonk1('row', b7 - 1, b2)
def fonk5(b7, b2):
    if b2 = = 0:
        return 'nf' if fonk6(b7, b2) != 1 else 0
    return b2 if fonk6(b7, b2) == 1 else fonk1('col', b7, b2 - 1)
def fonk6(b7, b2):
    return 1 if b9[b7] == b10[b2] else 0
if b8 = = "__main__":
    if len(sys.argv) >= 3:
        b9 = sys.argv[1]
        b10 = sys.argv[2]
        b11 = []
        fonk1('check', len(b9) - 1, len(b10) - 1)
        print(b11, 'with length:', len(b11))
    else:
        print('Not enough arguments passed\n > Try: LCS.py [first_argument] [second_argument]')