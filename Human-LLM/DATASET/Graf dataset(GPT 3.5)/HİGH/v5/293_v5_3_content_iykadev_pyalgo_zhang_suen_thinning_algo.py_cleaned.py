from __future__ import division
from PIL import Image
b1 = '''\
1100111
1100111
1100111
1100111
1100110
1100110
1100110
1100110
1100110
1100110
1100110
1100110
1111110
0000000\
'''
b2 = '''\
00000000000000000000000000000000
01111111110000000111111110000000
01110001111000001111001111000000
01110000111000001110000111000000
01110001111000001110000000000000
01111111110000001110000000000000
01110111100000001110000111000000
01110011110011101111001111011100
01110001111011100111111110011100
00000000000000000000000000000000
'''
b3 = '''\
00000000000000000000000000000000000000000000000000000000000
01111111111111111100000000000000000001111111111111000000000
01111111111111111110000000000000001111111111111111000000000
01111111111111111111000000000000111111111111111111000000000
01111111100000111111100000000001111111111111111111000000000
00011111100000111111100000000011111110000000111111000000000
000111111000001111111000000
from __future__ import division
from PIL import Image
def fonk1(binary_string):
    return [[int(char) for char in line] for line in binary_string.strip().split()]
def fonk2(int_matrix):
    return '\b6'.join(''.join(map(str, row)) for row in int_matrix)
def fonk3(int_matrix):
    return '\b6'.join(''.join(map(str, row)) for row in int_matrix)
def fonk4(x, y, b13):
    b4 = b13
    x1, y1, x_1, b5 = x + 1, y - 1, x - 1, y + 1
    return [b4[y1][x], b4[y1][x1], b4[y][x1], b4[b5][x1],
            b4[b5][x], b4[b5][x_1], b4[y][x_1], b4[y1][x_1]]
def fonk5(neighbours):
    b6 = neighbours + neighbours[0:1]
    return sum((n1, n2) == (0, 1) for n1, n2 in zip(b6, b6[1:]))
def fonk6(b13):
    b7 = b11 = [(-1, -1)]
    while b7 or b11:
        b7 = []
        for y in range(1, len(b13) - 1):
            for x in range(1, len(b13[0]) - 1):
                P2, P3, P4, P5, b10, P7, b9, b8 = b6 = fonk4(x, y, b13)
                if (b13[y][x] == 1 and
                        P4 * b10 * b9 = = 0 and
                        P2 * P4 * b10 = = 0 and
                        fonk5(b6) == 1 and
                        2 <= sum(b6) <= 6):
                    b7.append((x, y))
        for x, y in b7:
            b13[y][x] = 0
        b11 = []
        for y in range(1, len(b13) - 1):
            for x in range(1, len(b13[0]) - 1):
                P2, P3, P4, P5, b10, P7, b9, b8 = b6 = fonk4(x, y, b13)
                if (b13[y][x] == 1 and
                        P2 * b10 * b9 = = 0 and
                        P2 * P4 * b9 = = 0 and
                        fonk5(b6) == 1 and
                        2 <= sum(b6) <= 6):
                    b11.append((x, y))
        for x, y in b11:
            b13[y][x] = 0
    return b13
if b12 = = '__main__':
    for picture in (b1, b2, b3):
        b13 = fonk1(picture)
        print('\nFrom:\b6%s' % fonk3(b13))
        b14 = fonk6(b13)
        print('\nTo thinned:\b6%s' % fonk3(b14))