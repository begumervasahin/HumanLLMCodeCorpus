from __future__ import division
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
00000000000000000000000000000000\
'''
b3 = '''\
00000000000000000000000000000000000000000000000000000000000
01111111111111111100000000000000000001111111111111000000000
01111111111111111110000000000000001111111111111111000000000
01111111111111111111000000000000111111111111111111000000000
01111111100000111111100000000001111111111111111111000000000
00011111100000111111100000000011111110000000111111000000000
000111111000001111111000000
from PIL import Image
def fonk1(binary_string):
    return [[1 if b4 = = '1' else 0 for b4 in line] for line in binary_string.strip().split()]
def fonk2(int_matrix):
    return '\b7'.join(''.join(str(pixel) for pixel in row) for row in int_matrix)
def fonk3(int_matrix):
    return '\b7'.join(''.join(str(pixel) for pixel in row) for row in int_matrix)
def fonk4(x, y, b14):
    b5 = b14
    x1, y1, x_1, b6 = x + 1, y - 1, x - 1, y + 1
    return [b5[y1][x], b5[y1][x1], b5[y][x1], b5[b6][x1],
            b5[b6][x], b5[b6][x_1], b5[y][x_1], b5[y1][x_1]]
def fonk5(neighbours):
    b7 = neighbours + neighbours[0:1]
    return sum((n1, n2) == (0, 1) for n1, n2 in zip(b7, b7[1:]))
def fonk6(b14):
    b8 = b12 = [(-1, -1)]
    while b8 or b12:
        b8 = []
        for y in range(1, len(b14) - 1):
            for x in range(1, len(b14[0]) - 1):
                P2, P3, P4, P5, b11, P7, b10, b9 = b7 = fonk4(x, y, b14)
                if (b14[y][x] == 1 and
                        P4 * b11 * b10 = = 0 and
                        P2 * P4 * b11 = = 0 and
                        fonk5(b7) == 1 and
                        2 <= sum(b7) <= 6):
                    b8.append((x, y))
        for x, y in b8:
            b14[y][x] = 0
        b12 = []
        for y in range(1, len(b14) - 1):
            for x in range(1, len(b14[0]) - 1):
                P2, P3, P4, P5, b11, P7, b10, b9 = b7 = fonk4(x, y, b14)
                if (b14[y][x] == 1 and
                        P2 * b11 * b10 = = 0 and
                        P2 * P4 * b10 = = 0 and
                        fonk5(b7) == 1 and
                        2 <= sum(b7) <= 6):
                    b12.append((x, y))
        for x, y in b12:
            b14[y][x] = 0
    return b14
if b13 = = '__main__':
    for picture in (b1, b2, b3):
        b14 = fonk1(picture)
        print('\nFrom:\b7%s' % fonk3(b14))
        b15 = fonk6(b14)
        print('\nTo thinned:\b7%s' % fonk3(b15))