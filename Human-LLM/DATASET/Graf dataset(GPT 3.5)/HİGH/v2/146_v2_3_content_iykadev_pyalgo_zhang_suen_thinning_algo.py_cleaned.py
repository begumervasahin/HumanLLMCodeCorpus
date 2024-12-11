def fonk1(binstring):
    return [[1 if b1 = = '1' else 0 for b1 in line] for line in binstring.strip().split()]
def fonk2(intmatrix):
    return '\b5'.join(''.join(str(b2) for b2 in row) for row in intmatrix)
def fonk3(intmatrix):
    return '\b5'.join(''.join(('1' if b2 = = 1 else '0') for b2 in row) for row in intmatrix)
def fonk4(x, y, b12):
    b3 = b12
    x1, y1, x_1, b4 = x+1, y-1, x-1, y+1
    return [b3[y1][x],  b3[y1][x1],   b3[y][x1],  b3[b4][x1],
            b3[b4][x], b3[b4][x_1], b3[y][x_1], b3[y1][x_1]]
def fonk5(neighbours):
    b5 = neighbours + neighbours[0:1]
    return sum((n1, n2) == (0, 1) for n1, n2 in zip(b5, b5[1:]))
def fonk6(b12):
    b6 = b10 = [(-1, -1)]
    while b6 or b10:
        b6 = []
        for y in range(1, len(b12) - 1):
            for x in range(1, len(b12[0]) - 1):
                P2, P3, P4, P5, b9, P7, b8, b7 = neighbours(x, y, b12)
                if (b12[y][x] == 1 and
                    P4 * b9 * b8 = = 0 and
                    P2 * P4 * b9 = = 0 and
                    fonk5(neighbours(x, y, b12)) == 1 and
                    2 <= sum(neighbours(x, y, b12)) <= 6):
                    b6.append((x, y))
        for x, y in b6:
            b12[y][x] = 0
        b10 = []
        for y in range(1, len(b12) - 1):
            for x in range(1, len(b12[0]) - 1):
                P2, P3, P4, P5, b9, P7, b8, b7 = neighbours(x, y, b12)
                if (b12[y][x] == 1 and
                    P2 * b9 * b8 = = 0 and
                    P2 * P4 * b8 = = 0 and
                    fonk5(neighbours(x, y, b12)) == 1 and
                    2 <= sum(neighbours(x, y, b12)) <= 6):
                    b10.append((x, y))
        for x, y in b10:
            b12[y][x] = 0
    return b12
if b11 = = '__main__':
    for picture in (beforeTxt, smallrc01, rc01):
        b12 = fonk1(picture)
        print('\nFrom:\b5%s' % fonk3(b12))
        b13 = fonk6(b12)
        print('\nTo thinned:\b5%s' % fonk3(b13))