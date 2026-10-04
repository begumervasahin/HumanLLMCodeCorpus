def fonk1(grid):
    b1 = []
    b2 = '123456789'
    for b3 in grid:
        if b3 in b2:
            b1.append(b3)
        elif b3 = = '.':
            b1.append(b2)
    assert len(b1) == 81
    return dict(zip(b15, b1))
def fonk2(b6):
    b4 = 1 + max(len(b6[b7]) for b7 in b15)
    b5 = '+'.join(['-' * (b4 * 3)] * 3)
    for r in b13:
        print(''.join(b6[r + b3].center(b4) + ('|' if b3 in '36' else '')
                      for b3 in b14))
        if r in 'CF': print(b5)
    print()
def fonk3(b6):
    b6 = fonk4(b6)
    if b6 is False:
        return False
    if all(len(b6[b7]) == 1 for b7 in b15):
        return b6
    n, b7 = min((len(b6[b7]), b7) for b7 in b15 if len(b6[b7]) > 1)
    for value in b6[b7]:
        b8 = b6.copy()
        b8[b7] = value
        b9 = fonk3(b8)
        if b9:
            return b9
def fonk4(b6):
    b10 = False
    while not b10:
        b11 = len([box for box in b6 if len(b6[box]) == 1])
        b6 = fonk5(b6)
        b6 = fonk6(b6)
        b6 = fonk7(b6)
        b12 = len([box for box in b6 if len(b6[box]) == 1])
        b10 = b11 == b12
        if len([box for box in b6 if len(b6[box]) == 0]):
            return False
    return b6
b13 = 'ABCDEFGHI'
b14 = '123456789'
b15 = [r + b3 for r in b13 for b3 in b14]
def fonk5(b6):
    return b6
def fonk6(b6):
    return b6
def fonk7(b6):
    return b6
if b16 = = "__main__":
    b17 = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
    b6 = fonk1(b17)
    b6 = fonk3(b6)
    fonk2(b6)