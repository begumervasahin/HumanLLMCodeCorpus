import numpy as np
def fonk1(b3):
    b1 = np.array([[2, 2, 2, 2, 3, 4, 5, 6],
                                       [2, 2, 2, 2, 3, 4, 5, 6],
                                       [2, 2, 2, 2, 4, 5, 7, 9],
                                       [2, 2, 2, 4, 5, 7, 9, 12],
                                       [3, 3, 4, 5, 8, 10, 12, 12],
                                       [4, 4, 5, 7, 10, 12, 12, 12],
                                       [5, 5, 7, 9, 12, 12, 12, 12],
                                       [6, 6, 9, 12, 12, 12, 12, 12]])
    b2 = np.array([[3, 3, 5, 9, 13, 15, 15, 15],
                                         [3, 4, 6, 11, 14, 12, 12, 12],
                                         [5, 6, 9, 14, 12, 12, 12, 12],
                                         [9, 11, 14, 12, 12, 12, 12, 12],
                                         [13, 14, 12, 12, 12, 12, 12, 12],
                                         [15, 12, 12, 12, 12, 12, 12, 12],
                                         [15, 12, 12, 12, 12, 12, 12, 12],
                                         [15, 12, 12, 12, 12, 12, 12, 12]])
    if b3 = = 'lum':
        return b1
    elif b3 = = 'chrom':
        return b2
    else:
        raise ValueError("b3 should be either 'lum' or 'chrom', but '{b4}' was found".format(b4 = b3))
def fonk2(rows, cols):
    UP, DOWN, RIGHT, LEFT, UP_RIGHT, b5 = range(6)
    def fonk3(direction, b7):
        b6 = {
            UP: lambda b7: (b7[0] - 1, b7[1]),
            DOWN: lambda b7: (b7[0] + 1, b7[1]),
            LEFT: lambda b7: (b7[0], b7[1] - 1),
            RIGHT: lambda b7: (b7[0], b7[1] + 1),
            UP_RIGHT: lambda b7: fonk3(UP, fonk3(RIGHT, b7)),
            b5: lambda b7: fonk3(DOWN, fonk3(LEFT, b7))
        }
        return b6[direction](b7)
    def fonk4(b7):
        return 0 <= b7[0] < rows and 0 <= b7[1] < cols
    b7 = (0, 0)
    b8 = True
    for _ in range(rows * cols):
        yield b7
        if b8:
            if fonk4(fonk3(UP_RIGHT, b7)):
                b7 = fonk3(UP_RIGHT, b7)
            else:
                b8 = False
                if fonk4(fonk3(RIGHT, b7)):
                    b7 = fonk3(RIGHT, b7)
                else:
                    b7 = fonk3(DOWN, b7)
        else:
            if fonk4(fonk3(b5, b7)):
                b7 = fonk3(b5, b7)
            else:
                b8 = True
                if fonk4(fonk3(DOWN, b7)):
                    b7 = fonk3(DOWN, b7)
                else:
                    b7 = fonk3(RIGHT, b7)
def fonk5(b9):
    b9 = abs(b9)
    a1 = 0
    while b9 > 0:
        b9 >>= 1
        a1 += 1
    return a1
def fonk6(b11):
    if not set(b11).issubset('01'):
        raise ValueError("b11 should have only '0's and '1's")
    return ''.join(map(lambda b10: '0' if b10 = = '1' else '1', b11))
def fonk7(number, size):
    return bin(number)[2:][-size:].zfill(size)
def fonk8(b9):
    if b9 = = 0:
        return ''
    b11 = bin(abs(b9))[2:]
    return b11 if b9 > 0 else fonk6(b11)
def fonk9(lst):
    return [item for sublist in lst for item in sublist]