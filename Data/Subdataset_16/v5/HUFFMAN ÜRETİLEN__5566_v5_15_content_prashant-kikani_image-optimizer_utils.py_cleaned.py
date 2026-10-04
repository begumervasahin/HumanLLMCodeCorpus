import numpy as np
def fonk1(b1):
    if b1 = = 'lum':
        return np.array([
            [2, 2, 2, 2, 3, 4, 5, 6],
            [2, 2, 2, 2, 3, 4, 5, 6],
            [2, 2, 2, 2, 4, 5, 7, 9],
            [2, 2, 2, 4, 5, 7, 9, 12],
            [3, 3, 4, 5, 8, 10, 12, 12],
            [4, 4, 5, 7, 10, 12, 12, 12],
            [5, 5, 7, 9, 12, 12, 12, 12],
            [6, 6, 9, 12, 12, 12, 12, 12]
        ])
    elif b1 = = 'chrom':
        return np.array([
            [3, 3, 5, 9, 13, 15, 15, 15],
            [3, 4, 6, 11, 14, 12, 12, 12],
            [5, 6, 9, 14, 12, 12, 12, 12],
            [9, 11, 14, 12, 12, 12, 12, 12],
            [13, 14, 12, 12, 12, 12, 12, 12],
            [15, 12, 12, 12, 12, 12, 12, 12],
            [15, 12, 12, 12, 12, 12, 12, 12],
            [15, 12, 12, 12, 12, 12, 12, 12]
        ])
    else:
        raise ValueError(f"Invalid b1 '{b1}'. Expected 'lum' or 'chrom'.")
def fonk2(rows, cols):
    b2 = {
        "UP": lambda p: (p[0] - 1, p[1]),
        "DOWN": lambda p: (p[0] + 1, p[1]),
        "LEFT": lambda p: (p[0], p[1] - 1),
        "RIGHT": lambda p: (p[0], p[1] + 1),
        "UP_RIGHT": lambda p: (p[0] - 1, p[1] + 1),
        "DOWN_LEFT": lambda p: (p[0] + 1, p[1] - 1)
    }
    def fonk3(b3):
        return 0 <= b3[0] < rows and 0 <= b3[1] < cols
    b3 = (0, 0)
    b4 = True
    for _ in range(rows * cols):
        yield b3
        if b4:
            if fonk3(b2["UP_RIGHT"](b3)):
                b3 = b2["UP_RIGHT"](b3)
            else:
                b4 = False
                b3 = b2["RIGHT"](b3) if fonk3(b2["RIGHT"](b3)) else b2["DOWN"](b3)
        else:
            if fonk3(b2["DOWN_LEFT"](b3)):
                b3 = b2["DOWN_LEFT"](b3)
            else:
                b4 = True
                b3 = b2["DOWN"](b3) if fonk3(b2["DOWN"](b3)) else b2["RIGHT"](b3)
def fonk4(b6):
    return b6.bit_length()
def fonk5(b7):
    if not set(b7).issubset('01'):
        raise ValueError("Input string should contain only '0's and '1's")
    return ''.join('0' if b5 = = '1' else '1' for b5 in b7)
def fonk6(number, size):
    return bin(number)[2:].zfill(size)[-size:]
def fonk7(b6):
    if b6 = = 0:
        return '0'
    b7 = bin(abs(b6))[2:]
    return b7 if b6 > 0 else fonk5(b7)
def fonk8(lst):
    return [item for sublist in lst for item in sublist]