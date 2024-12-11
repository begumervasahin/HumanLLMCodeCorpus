import numpy as np
def fonk1(b1):
    if b1 = = 'lum':
        b2 = np.array([[2, 2, 2, 2, 3, 4, 5, 6],
                      [2, 2, 2, 2, 3, 4, 5, 6],
                      [2, 2, 2, 2, 4, 5, 7, 9],
                      [2, 2, 2, 4, 5, 7, 9, 12],
                      [3, 3, 4, 5, 8, 10, 12, 12],
                      [4, 4, 5, 7, 10, 12, 12, 12],
                      [5, 5, 7, 9, 12, 12, 12, 12],
                      [6, 6, 9, 12, 12, 12, 12, 12]])
    elif b1 = = 'chrom':
        b2 = np.array([[3, 3, 5, 9, 13, 15, 15, 15],
                      [3, 4, 6, 11, 14, 12, 12, 12],
                      [5, 6, 9, 14, 12, 12, 12, 12],
                      [9, 11, 14, 12, 12, 12, 12, 12],
                      [13, 14, 12, 12, 12, 12, 12, 12],
                      [15, 12, 12, 12, 12, 12, 12, 12],
                      [15, 12, 12, 12, 12, 12, 12, 12],
                      [15, 12, 12, 12, 12, 12, 12, 12]])
    else:
        raise ValueError("b1 should be either 'lum' or 'chrom', but '{b3}' was found".format(b3 = b1))
    return b2
def fonk2(rows, cols):
    UP, DOWN, RIGHT, LEFT, UP_RIGHT, b4 = range(6)
    def fonk3(direction, b5):
        return {
            UP: lambda b5: (b5[0] - 1, b5[1]),
            DOWN: lambda b5: (b5[0] + 1, b5[1]),
            LEFT: lambda b5: (b5[0], b5[1] - 1),
            RIGHT: lambda b5: (b5[0], b5[1] + 1),
            UP_RIGHT: lambda b5: fonk3(UP, fonk3(RIGHT, b5)),
            b4: lambda b5: fonk3(DOWN, fonk3(LEFT, b5))
        }[direction](b5)
    def fonk4(b5):
        return 0 <= b5[0] < rows and 0 <= b5[1] < cols
    b5 = (0, 0)
    b6 = True
    for i in range(rows * cols):
        yield b5
        if b6:
            if fonk4(fonk3(UP_RIGHT, b5)):
                b5 = fonk3(UP_RIGHT, b5)
            else:
                b6 = False
                if fonk4(fonk3(RIGHT, b5)):
                    b5 = fonk3(RIGHT, b5)
                else:
                    b5 = fonk3(DOWN, b5)
        else:
            if fonk4(fonk3(b4, b5)):
                b5 = fonk3(b4, b5)
            else:
                b6 = True
                if fonk4(fonk3(DOWN, b5)):
                    b5 = fonk3(DOWN, b5)
                else:
                    b5 = fonk3(RIGHT, b5)
def fonk5(b7):
    b7 = abs(b7)
    a1 = 0
    while b7 > 0:
        b7 >>= 1
        a1 += 1
    return a1
def fonk6(b9):
    if not set(b9).issubset('01'):
        raise ValueError("b9 should have only '0's and '1's")
    return ''.join(map(lambda b8: '0' if b8 = = '1' else '1', b9))
def fonk7(number, size):
    return bin(number)[2:][-size:].zfill(size)
def fonk8(b7):
    if b7 = = 0:
        return ''
    b9 = bin(abs(b7))[2:]
    return b9 if b7 > 0 else fonk6(b9)
def fonk9(lst):
    return [item for sublist in lst for item in sublist]